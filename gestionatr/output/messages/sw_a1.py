# -*- coding: utf-8 -*-
from libcomxml.core import XmlModel, XmlField

from gestionatr.output.messages.sw_d1 import InfoRegistroAutocons
from gestionatr.output.messages.base import rep_solicitud, rep_fecha


# Paso 01
class A101(XmlModel):

    _sort_order = ('mensaje', 'cabecera', 'info_registro_autocons')

    def __init__(self):
        self.mensaje = XmlField('A101',
                                attributes={'xmlns': 'http://localhost/elegibilidad'})
        self.cabecera = CabeceraA101()
        self.info_registro_autocons = InfoRegistroAutoconsA1()
        super(A101, self).__init__('A101', 'mensaje')


class CabeceraA101(XmlModel):

    _sort_order = ('cabecera', 'codigo_empresa_emisora',
                   'codigo_ree_empresa_destino', 'codigo_del_proceso',
                   'codigo_del_paso', 'codigo_de_solicitud',
                   'secuencial_de_solicitud', 'fecha')

    def __init__(self):
        self.cabecera = XmlField('Cabecera')
        self.codigo_empresa_emisora = XmlField('CodigoEmpresaEmisora')
        self.codigo_ree_empresa_destino = XmlField('CodigoREEEmpresaDestino')
        self.codigo_del_proceso = XmlField('CodigoDelProceso')
        self.codigo_del_paso = XmlField('CodigoDePaso')
        self.codigo_de_solicitud = XmlField('CodigoDeSolicitud', rep=rep_solicitud)
        self.secuencial_de_solicitud = XmlField('SecuencialDeSolicitud')
        self.fecha = XmlField('FechaSolicitud', rep=rep_fecha)
        super(CabeceraA101, self).__init__('Cabecera', 'cabecera')


class InfoRegistroAutoconsA1(InfoRegistroAutocons):

    _sort_order = ('info_registro_autocons', 'movimiento', 'autoconsumo', 'datos_suministro', 'datos_inst_gen',
                   'comentarios')

    def __init__(self):
        self.movimiento = XmlField('Movimiento')
        super(InfoRegistroAutoconsA1, self).__init__()


# Paso 02
class MensajeActualizacionRegistroAutoconsumo(XmlModel):

    _sort_order = ('mensaje', 'cabecera', 'actualizacion_registro_autoconsumo')

    def __init__(self):
        self.mensaje = XmlField('MensajeActualizacionRegistroAutoconsumo',
                                attributes={'xmlns': 'http://localhost/elegibilidad'})
        self.cabecera = CabeceraA102()
        self.actualizacion_registro_autoconsumo = ActualizacionRegistroAutoconsumo()
        super(MensajeActualizacionRegistroAutoconsumo, self).__init__('MensajeActualizacionRegistroAutoconsumo', 'mensaje')


class CabeceraA102(XmlModel):

    _sort_order = ('cabecera', 'codigo_ree_empresa_emisora',
                   'codigo_empresa_destino', 'codigo_del_proceso',
                   'codigo_del_paso', 'codigo_de_solicitud',
                   'secuencial_de_solicitud', 'fecha')

    def __init__(self):
        self.cabecera = XmlField('Cabecera')
        self.codigo_ree_empresa_emisora = XmlField('CodigoREEEmpresaEmisora')
        self.codigo_empresa_destino = XmlField('CodigoEmpresaDestino')
        self.codigo_del_proceso = XmlField('CodigoDelProceso')
        self.codigo_del_paso = XmlField('CodigoDePaso')
        self.codigo_de_solicitud = XmlField('CodigoDeSolicitud', rep=rep_solicitud)
        self.secuencial_de_solicitud = XmlField('SecuencialDeSolicitud')
        self.fecha = XmlField('FechaSolicitud', rep=rep_fecha)
        super(CabeceraA102, self).__init__('Cabecera', 'cabecera')


class ActualizacionRegistroAutoconsumo(XmlModel):

    _sort_order = ('actualizacion_registro_autoconsumo', 'cau', 'actualizacion_datos_registro',
                   'rechazos', 'comentarios')

    def __init__(self):
        self.actualizacion_registro_autoconsumo = XmlField('ActualizacionRegistroAutoconsumo')
        self.cau = XmlField('CAU')
        self.actualizacion_datos_registro = ActualizacionDatosRegistro()
        self.rechazos = Rechazos()
        self.comentarios = XmlField('Comentarios')
        super(ActualizacionRegistroAutoconsumo, self).__init__('ActualizacionRegistroAutoconsumo',
                                                               'actualizacion_registro_autoconsumo')


class ActualizacionDatosRegistro(XmlModel):

    _sort_order = ('actualizacion_datos_registro', 'sub_seccion')

    def __init__(self):
        self.actualizacion_datos_registro = XmlField('ActualizacionDatosRegistro')
        self.sub_seccion = XmlField('SubSeccion')
        super(ActualizacionDatosRegistro, self).__init__('ActualizacionDatosRegistro', 'actualizacion_datos_registro')


class Rechazos(XmlModel):

    _sort_order = ('rechazos', 'rechazo')

    def __init__(self):
        self.rechazos = XmlField('Rechazos')
        self.rechazo = Rechazo()
        super(Rechazos, self).__init__('Rechazos', 'rechazos')


class Rechazo(XmlModel):

    _sort_order = ('rechazo', 'fecha_rechazo', 'secuencial', 'codigo_motivo', 'cups', 'comentarios')

    def __init__(self):
        self.rechazo = XmlField('Rechazo')
        self.fecha_rechazo = XmlField('FechaRechazo')
        self.secuencial = XmlField('Secuencial')
        self.codigo_motivo = XmlField('CodigoMotivo')
        self.cups = XmlField('CUPS')
        self.comentarios = XmlField('Comentarios')
        super(Rechazo, self).__init__('Rechazo', 'rechazo')
