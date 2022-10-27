# -*- coding: utf-8 -*-
import sys
import click
import requests
import base64
from lxml import etree

from gestionatr.input.messages import message
from gestionatr.input.messages import message_gas
from gestionatr.input.messages.message import except_f1
from gestionatr.output.messages.sw_p0 import ENVELOP_BY_DISTR
from gestionatr.exceptions import *

from gestionatr import __version__


VERSION_TEXT = u'ATR library version (gestionatr) : {0}'.format(__version__)


P0_TEMPLATE = """
        <MensajeSolicitudInformacionAlRegistroDePS xmlns="http://localhost/elegibilidad">
          <Cabecera>
            <CodigoREEEmpresaEmisora>{emisora}</CodigoREEEmpresaEmisora>
            <CodigoREEEmpresaDestino>{destino}</CodigoREEEmpresaDestino>
            <CodigoDelProceso>P0</CodigoDelProceso>
            <CodigoDePaso>01</CodigoDePaso>
            <CodigoDeSolicitud>{solicitud}</CodigoDeSolicitud>
            <SecuencialDeSolicitud>01</SecuencialDeSolicitud>
            <FechaSolicitud>{fecha_solicitud}</FechaSolicitud>
            <CUPS>{cups}</CUPS>
          </Cabecera>
        </MensajeSolicitudInformacionAlRegistroDePS>
"""


def get_gestionatr_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo(VERSION_TEXT)
    ctx.exit()


@click.group()
@click.option("--version", "-v", is_flag=True, callback=get_gestionatr_version,
              expose_value=False, is_eager=True, help="ATR library version")
def atr():
    pass


@atr.command(name='test')
@click.option("--filename", "-f", help="path to XML filename", required=True)
@click.option("--sector", "-s", help="e (power) or g (gas)", default="e")
def test(filename, sector):
    with open(filename, 'r') as xml_file:
        try:
            data = xml_file.read()
            if sector == u'e':
                m = message.Message(data)
            elif sector == u'g':
                m = message_gas.MessageGas(data)
            m.parse_xml()
            sys.stdout.write(u'Correct File\n')
        except except_f1 as e:
            error_txt = unicode(e.value).encode(errors='ignore')
            sys.stdout.write(
                u'WARNING: Invalid File: {0}\n'.format(error_txt)
            )
        except Exception as e:
            error_txt = unicode(e).encode(errors='ignore')
            sys.stdout.write(
                u'WARNING: Invalid File: {0}\n'.format(error_txt)
            )
        finally:
            sys.stdout.flush()


def request_p0(url, user, password, xml_str=None, params=None):
    import random
    import re
    from datetime import datetime
    if xml_str is None and params is None:
        raise ValueError("XML or params must be passed to request_p0")
    if xml_str is None and params:
        codi_receptor = params['destino']
        params['fecha_solicitud'] = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        params['solicitud'] = 10**11 + int((random.random() * 10**11))
        xml_str = re.sub(r'\s+<', '<', P0_TEMPLATE)
        xml_str = re.sub(r'\s+$', '', xml_str)
        xml_str = re.sub(r'\n', '', xml_str).format(**params)
    else:
        codi_receptor = xml_str.split("<CodigoREEEmpresaDestino>")[1].split("</CodigoREEEmpresaDestino>")[0]

    base64string = base64.encodestring('%s:%s' % (user, password)).replace('\n', '')
    headers = {
        "Authorization": "Basic %s" % base64string,
        "content-type": 'text/xml; charset=utf-8',
    }

    # Clean XML
    xml_str = xml_str.strip()
    xml_str = xml_str.replace("'utf-8'", "'UTF-8'")
    xml_str = xml_str.replace("<?xml version='1.0' encoding='UTF-8'?>", "")

    # Fem sempre 2 intents: amb el que esta definit per aquella distri i si va malament amb una plantilla base que
    # sol funcionar en la majoria. Aixi si una distri no la tenim documentada es fa el intent amb les 2 plantilles
    # principals que tenim. La "altres" i la "reintent"
    distri_envelop = ENVELOP_BY_DISTR.get(codi_receptor, ENVELOP_BY_DISTR.get("altres"))
    retry_envelop = ENVELOP_BY_DISTR.get("reintent")
    error = None
    for envelop in [distri_envelop, retry_envelop]:
        xml_str_to_use = xml_str
        soap_content = envelop['template'].format(xml_str=xml_str_to_use)

        # Send request
        h = headers.copy()
        h.update(envelop['extra_headers'])
        res = requests.post(url, data=soap_content, headers=h, auth=(user, password))
        res = res.content
        try:
            def find_child(element, child_name):
                res = None
                if child_name in element.tag:
                    return element
                for child in element:
                    res = find_child(child, child_name)
                    if res is not None:
                        break
                return res

            aux = etree.fromstring(res)
            aux_res = find_child(aux, "MensajeEnvioInformacionPS")
            if aux_res is None:
                aux_res = find_child(aux, "MensajeRechazoP0")
            if aux_res is None:
                aux_res = find_child(aux, "faultstring")
                if aux_res is not None:
                    error_mssg = {
                        'request': res,
                        'response': etree.tostring(aux_res)
                    }
                    raise P0FaultError(error_mssg)

            res = etree.tostring(aux_res)
            return res
        except P0FaultError as p0efe:
            raise
        except Exception as e:
            if not error:
                error = e

    if error:
        print error

    return res


@atr.command(name='p0')
@click.option('-u', '--url', default='http://localhost', help=u'URL del webservice', show_default=True)
@click.option('-s', '--user', default='admin', help=u'User del webservice', show_default=True)
@click.option('-p', '--password', default='admin', help=u'Password del webservice', show_default=True)
@click.option('-f', '--file', help=u'Fitxer P0 pas 01 per enviar', show_default=True)
@click.option('--emisora', help='Código REE empresa emisora')
@click.option('--destino', help='Código REE empresa destino')
@click.option('--cups', help='CUPS')
def sollicitar_p0(url, user, password, file=None, emisora=None, destino=None, cups=None):
    params = None
    from lxml import etree
    if emisora and destino and cups:
        params = {
            'emisora': emisora,
            'destino': destino,
            'cups': cups
        }

    res = request_p0(url, user, password, file, params)
    res = etree.fromstring(res)
    print(etree.tostring(res, pretty_print=True))


