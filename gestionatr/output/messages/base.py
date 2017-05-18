# -*- coding: utf-8 -*-

# pylint: disable=E1002
# pylint: disable=E1101
# pylint: disable=C0111

from libcomxml.core import XmlModel, XmlField


class Cabecera(XmlModel):
    _sort_order = ('cabecera', 'codigo_ree_empresa_emisora',
                   'codigo_ree_empresa_destino', 'codigo_del_proceso',
                   'codigo_del_paso', 'codigo_de_solicitud',
                   'secuencial_de_solicitud', 'fecha', 'cups')

    def __init__(self):
        self.cabecera = XmlField('Cabecera')
        self.codigo_ree_empresa_emisora = XmlField('CodigoREEEmpresaEmisora')
        self.codigo_ree_empresa_destino = XmlField('CodigoREEEmpresaDestino')
        self.codigo_del_proceso = XmlField('CodigoDelProceso')
        self.codigo_del_paso = XmlField('CodigoDePaso')
        self.codigo_de_solicitud = XmlField('CodigoDeSolicitud',
                                            rep=rep_solicitud)
        self.secuencial_de_solicitud = XmlField('SecuencialDeSolicitud')
        self.fecha = XmlField('FechaSolicitud', rep=rep_fecha)
        self.cups = XmlField('CUPS')
        super(Cabecera, self).__init__('Cabecera', 'cabecera')


class CabeceraReclamacion(XmlModel):

    _sort_order = ('cabecera', 'codigo_ree_empresa_emisora',
                   'codigo_ree_empresa_destino', 'codigo_del_proceso',
                   'codigo_del_paso', 'codigo_de_solicitud',
                   'secuencial_de_solicitud', 'fecha', 'cups')

    def __init__(self):
        self.cabecera = XmlField('CabeceraReclamacion')
        self.codigo_ree_empresa_emisora = XmlField('CodigoREEEmpresaEmisora')
        self.codigo_ree_empresa_destino = XmlField('CodigoREEEmpresaDestino')
        self.codigo_del_proceso = XmlField('CodigoDelProceso')
        self.codigo_del_paso = XmlField('CodigoDePaso')
        self.codigo_de_solicitud = XmlField('CodigoDeSolicitud',
                                            rep=rep_solicitud)
        self.secuencial_de_solicitud = XmlField('SecuencialDeSolicitud')
        self.fecha = XmlField('FechaSolicitud', rep=rep_fecha)
        self.cups = XmlField('CUPS')
        super(CabeceraReclamacion, self).__init__('CabeceraReclamacion',
                                                  'cabecera')


def rep_solicitud(codsol):
    codsol = ''.join([x for x in codsol if x.isalnum()])
    return codsol.ljust(12, '0')[:12]


def rep_fecha(fecha):
    if len(fecha.strip()) == 10:
        # We do not have time so add it
        fecha += ' 00:00:00'
    return 'T'.join(fecha.split(' '))


def rep_fecha_sin_hora(fecha):
    if len(fecha) > 10:
        return fecha[:10]
    else:
        return fecha


def rep_decimal(n_decimal):
    dec_format = '{0:.' + str(n_decimal) + 'f}'
    return lambda decimal: dec_format.format(decimal)


def rep_entera(decimal):
    return int(decimal)


def rep_ruedas(n_rodes):
    return '{:d}'.format(n_rodes)
