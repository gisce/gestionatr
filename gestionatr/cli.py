# -*- encoding: utf-8 -*-
import sys
import click

from gestionatr.input.messages import message
from gestionatr.input.messages import message_gas
from gestionatr import __version__


VERSION_TEXT = u'ATR library version (gestionatr) : {0}'.format(__version__)


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
def test(filename):
    with open(filename, 'r') as xml_file:
        try:
            data = xml_file.read()
            m = message.Message(data)
            m.parse_xml()
            sys.stdout.write(u'Correct File\n')
        except Exception, e:
            try:
                m = message_gas.MessageGas(data)
                m.parse_xml()
                sys.stdout.write(u'Correct File\n')
            except Exception, e:
                sys.stdout.write(
                    u'WARNING: Invalid File: {0}\n'.format(str(e.value))
                )
