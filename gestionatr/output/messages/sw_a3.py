# -*- coding: utf-8 -*-
from gestionatr.output.messages.sw_c2 import *


# Paso 01
class MensajeAlta(XmlModel):

    _sort_order = ('mensaje', 'cabecera', 'alta')

    def __init__(self):
        self.mensaje = XmlField('MensajeAlta',
                                attributes={'xmlns': 'http://localhost/elegibilidad'})
        self.cabecera = Cabecera()
        self.alta = Alta()
        super(MensajeAlta, self).__init__('MensajeAlta', 'mensaje')


class Alta(XmlModel):

    _sort_order = ('alta', 'datos_solicitud', 'contrato', 'cliente', 'medida', 'doc_tecnica', 'comentarios', 'registros_documento')

    def __init__(self):
        self.alta = XmlField('Alta')
        self.datos_solicitud = DatosSolicitud()
        self.contrato = Contrato()
        self.cliente = Cliente()
        self.medida = Medida()
        self.doc_tecnica = DocTecnica()
        self.comentarios = XmlField('Comentarios')
        self.registros_documento = RegistrosDocumento()
        super(Alta, self).__init__('Alta', 'alta')


# Paso 02
class MensajeAceptacionAlta(XmlModel):

    _sort_order = ('mensaje', 'cabecera', 'aceptacion_alta')

    def __init__(self):
        self.mensaje = XmlField('MensajeAceptacionAlta',
                                attributes={'xmlns': 'http://localhost/elegibilidad'})
        self.cabecera = Cabecera()
        self.aceptacion_alta = AceptacionAlta()
        super(MensajeAceptacionAlta, self).__init__('MensajeAceptacionAlta', 'mensaje')


class AceptacionAlta(XmlModel):

    _sort_order = ('aceptacion_alta', 'datos_aceptacion', 'contrato')

    def __init__(self):
        self.aceptacion_alta = XmlField('AceptacionAlta')
        self.datos_aceptacion = DatosAceptacion()
        self.contrato = Contrato()
        super(AceptacionAlta, self).__init__('AceptacionAlta', 'aceptacion_alta')


# Paso 03 -> C2 MensajeIncidenciasATRDistribuidor
# Paso 04 -> C1 MensajeRechazo

# Paso 05
class MensajeActivacionAlta(XmlModel):

    _sort_order = ('mensaje', 'cabecera', 'activacion_alta')

    def __init__(self):
        self.mensaje = XmlField('MensajeActivacionAlta',
                                attributes={'xmlns': 'http://localhost/elegibilidad'})
        self.cabecera = Cabecera()
        self.activacion_alta = ActivacionAlta()
        super(MensajeActivacionAlta, self).__init__('MensajeActivacionAlta', 'mensaje')


class ActivacionAlta(XmlModel):
    _sort_order = ('activacion_alta', 'datos_activacion', 'contrato', 'puntos_de_medida')

    def __init__(self):
        self.activacion_alta = XmlField('ActivacionAlta')
        self.datos_activacion = DatosActivacion()
        self.contrato = Contrato()
        self.puntos_de_medida = PuntosDeMedida()
        super(ActivacionAlta, self).__init__('ActivacionAlta', 'activacion_alta')

# Paso 06 -> C1 MensajeAnulacionSolicitud
# Paso 07 -> C1 MensajeAceptacionAnulacion
# Paso 13 -> C1 MesajeContestacionIncidencia
