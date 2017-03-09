# -*- coding: utf-8 -*-

from libcomxml.core import XmlModel, XmlField
from gestionatr.output.messages.base import Cabecera


# Paso 01
class MensajeCambiodeComercializadorSinCambios(XmlModel):
    _sort_order = ('mensage', 'cabecera', 'cambiode_comercializador_sin_cambios')

    def __init__(self):
        self.doc_root = None
        self.mensage = XmlField(
            'MensajeCambiodeComercializadorSinCambios',
            attributes={'xmlns': 'http://localhost/elegibilidad'}
        )
        self.cabecera = Cabecera()
        self.cambiode_comercializador_sin_cambios = CambiodeComercializadorSinCambios()
        super(MensajeCambiodeComercializadorSinCambios, self).__init__(
            'MensajeCambiodeComercializadorSinCambios', 'mensage'
        )


class CambiodeComercializadorSinCambios(XmlModel):

    _sort_order = ('cambiode_comercializador_sin_cambios', 'datos_solicitud',
                   'cliente', 'comentarios', 'registros_documento')

    def __init__(self):
        self.cambiode_comercializador_sin_cambios = XmlField('CambiodeComercializadorSinCambios')
        self.datos_solicitud = DatosSolicitud()
        self.cliente = Cliente()
        self.comentarios = XmlField('Comentarios')
        self.registros_documento = RegistrosDocumento()
        super(CambiodeComercializadorSinCambios, self).__init__('CambiodeComercializadorSinCambios', 'cambiode_comercializador_sin_cambios')


class DatosSolicitud(XmlModel):

    _sort_order = ('datos_solicitud', 'ind_activacion', 'fecha_prevista_accion', 'contratacion_incondicional_ps')

    def __init__(self):
        self.datos_solicitud = XmlField('DatosSolicitud')
        self.ind_activacion = XmlField('IndActivacion')
        self.fecha_prevista_accion = XmlField('FechaPrevistaAccion')
        self.contratacion_incondicional_ps = XmlField('ContratacionIncondicionalPS')
        super(DatosSolicitud, self).__init__('DatosSolicitud', 'datos_solicitud')


class Cliente(XmlModel):

    _sort_order = ('cliente', 'id_cliente', 'nombre', 'telefono', 'correo_electronico')

    def __init__(self):
        self.cliente = XmlField('Cliente')
        self.id_cliente = IdCliente()
        self.nombre = Nombre()
        self.telefono = Telefono()
        self.correo_electronico = XmlField('CorreoElectronico')
        super(Cliente, self).__init__('Cliente', 'cliente')


class IdCliente(XmlModel):

    _sort_order = ('id_cliente', 'tipo_identificador', 'identificador', 'tipo_persona')

    def __init__(self):
        self.id_cliente = XmlField('IdCliente')
        self.tipo_identificador = XmlField('TipoIdentificador')
        self.identificador = XmlField('Identificador')
        self.tipo_persona = XmlField('TipoPersona')
        super(IdCliente, self).__init__('IdCliente', 'id_cliente')


class Nombre(XmlModel):

    _sort_order = ('nombre', 'nombre_de_pila', 'primer_apellido', 'segundo_apellido', 'razon_social')

    def __init__(self):
        self.nombre = XmlField('Nombre')
        self.nombre_de_pila = XmlField('NombreDePila')
        self.primer_apellido = XmlField('PrimerApellido')
        self.segundo_apellido = XmlField('SegundoApellido')
        self.razon_social = XmlField('RazonSocial')
        super(Nombre, self).__init__('Nombre', 'nombre')


class Telefono(XmlModel):

    _sort_order = ('telefono', 'prefijo_pais', 'numero')

    def __init__(self):
        self.telefono = XmlField('Telefono')
        self.prefijo_pais = XmlField('PrefijoPais')
        self.numero = XmlField('Numero')
        super(Telefono, self).__init__('Telefono', 'telefono')


class RegistrosDocumento(XmlModel):

    _sort_order = ('registros_documento', 'registro_doc_list')

    def __init__(self):
        self.registros_documento = XmlField('RegistrosDocumento')
        self.registro_doc_list = []
        super(RegistrosDocumento, self).__init__('RegistrosDocumento', 'registros_documento')


class RegistroDoc(XmlModel):

    _sort_order = ('registro_doc', 'tipo_doc_aportado', 'direccion_url')

    def __init__(self):
        self.registro_doc = XmlField('RegistroDoc')
        self.tipo_doc_aportado = XmlField('TipoDocAportado')
        self.direccion_url = XmlField('DireccionUrl')
        super(RegistroDoc, self).__init__('RegistroDoc', 'registro_doc')


# Paso 02 accept
class MensajeAceptacionCambiodeComercializadorSinCambios(XmlModel):

    _sort_order = ('mensage', 'cabecera', 'aceptacion_cambiode_comercializador_sin_cambios')

    def __init__(self):
        self.mensage = XmlField('MensajeAceptacionCambiodeComercializadorSinCambios',
                                attributes={'xmlns': 'http://localhost/elegibilidad'})
        self.cabecera = Cabecera()
        self.aceptacion_cambiode_comercializador_sin_cambios = AceptacionCambiodeComercializadorSinCambios()
        super(MensajeAceptacionCambiodeComercializadorSinCambios, self).__init__('MensajeAceptacionCambiodeComercializadorSinCambios', 'mensage')


class AceptacionCambiodeComercializadorSinCambios(XmlModel):

    _sort_order = ('aceptacion_cambiode_comercializador_sin_cambios', 'datos_aceptacion', 'contrato')

    def __init__(self):
        self.aceptacion_cambiode_comercializador_sin_cambios = XmlField('AceptacionCambiodeComercializadorSinCambios')
        self.datos_aceptacion = DatosAceptacion()
        self.contrato = Contrato()
        super(AceptacionCambiodeComercializadorSinCambios, self).__init__('AceptacionCambiodeComercializadorSinCambios', 'aceptacion_cambiode_comercializador_sin_cambios')


class DatosAceptacion(XmlModel):

    _sort_order = ('datos_aceptacion', 'fecha_aceptacion', 'actuacion_campo', 'fecha_ultima_lectura_firme')

    def __init__(self):
        self.datos_aceptacion = XmlField('DatosAceptacion')
        self.fecha_aceptacion = XmlField('FechaAceptacion')
        self.actuacion_campo = XmlField('ActuacionCampo')
        self.fecha_ultima_lectura_firme = XmlField('FechaUltimaLecturaFirme')
        super(DatosAceptacion, self).__init__('DatosAceptacion', 'datos_aceptacion')


class Contrato(XmlModel):

    _sort_order = ('contrato', 'tipo_contrato_atr', 'condiciones_contractuales', 'tipo_activacion_prevista', 'fecha_activacion_prevista')

    def __init__(self):
        self.contrato = XmlField('Contrato')
        self.tipo_contrato_atr = XmlField('TipoContratoATR')
        self.condiciones_contractuales = CondicionesContractuales()
        self.tipo_activacion_prevista = XmlField('TipoActivacionPrevista')
        self.fecha_activacion_prevista = XmlField('FechaActivacionPrevista')
        super(Contrato, self).__init__('Contrato', 'contrato')


class CondicionesContractuales(XmlModel):

    _sort_order = ('condiciones_contractuales', 'tarifa_atr', 'potencias_contratadas', 'modo_control_potencia')

    def __init__(self):
        self.condiciones_contractuales = XmlField('CondicionesContractuales')
        self.tarifa_atr = XmlField('TarifaATR')
        self.potencias_contratadas = PotenciasContratadas()
        self.modo_control_potencia = XmlField('ModoControlPotencia')
        super(CondicionesContractuales, self).__init__('CondicionesContractuales', 'condiciones_contractuales')


class PotenciasContratadas(XmlModel):
    _sort_order = ('potencies', 'p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8',
                   'p9', 'p10')

    def __init__(self):
        self.potencies = XmlField('PotenciasContratadas')
        self.p1 = XmlField('Potencia', attributes={'Periodo': '1'}, rep=lambda x: '%d' % x)
        self.p2 = XmlField('Potencia', attributes={'Periodo': '2'})
        self.p3 = XmlField('Potencia', attributes={'Periodo': '3'})
        self.p4 = XmlField('Potencia', attributes={'Periodo': '4'})
        self.p5 = XmlField('Potencia', attributes={'Periodo': '5'})
        self.p6 = XmlField('Potencia', attributes={'Periodo': '6'})
        self.p7 = XmlField('Potencia', attributes={'Periodo': '7'})
        self.p8 = XmlField('Potencia', attributes={'Periodo': '8'})
        self.p9 = XmlField('Potencia', attributes={'Periodo': '9'})
        self.p10 = XmlField('Potencia', attributes={'Periodo': '10'})
        super(PotenciasContratadas, self).__init__('PotenciasContratadas', 'potencies')


# Paso 02 reject
class MensajeRechazo(XmlModel):

    _sort_order = ('mensaje_rechazo', 'cabecera', 'rechazos')

    def __init__(self):
        self.mensaje_rechazo = XmlField('MensajeRechazo',
                                        attributes={'xmlns': 'http://localhost/elegibilidad'})
        self.cabecera = Cabecera()
        self.rechazos = Rechazos()
        super(MensajeRechazo, self).__init__('MensajeRechazo', 'mensaje_rechazo')


class Rechazos(XmlModel):

    _sort_order = ('rechazos', 'fecha_rechazo', 'rechazo_list', 'registros_documento')

    def __init__(self):
        self.rechazos = XmlField('Rechazos')
        self.fecha_rechazo = XmlField('FechaRechazo')
        self.rechazo_list = []
        self.registros_documento = RegistrosDocumento()
        super(Rechazos, self).__init__('Rechazos', 'rechazos')


class Rechazo(XmlModel):

    _sort_order = ('rechazo', 'secuencial', 'codigo_motivo', 'comentarios')

    def __init__(self):
        self.rechazo = XmlField('Rechazo')
        self.secuencial = XmlField('Secuencial')
        self.codigo_motivo = XmlField('CodigoMotivo')
        self.comentarios = XmlField('Comentarios')
        super(Rechazo, self).__init__('Rechazo', 'rechazo')

