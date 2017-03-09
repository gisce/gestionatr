# -*- coding: utf-8 -*-

from libcomxml.core import XmlModel, XmlField
from gestionatr.output.messages.base import Cabecera


class MensajeCambiodeComercializadorSinCambios(XmlModel):
    _sort_order = ('missatge', 'cabecera', 'cambiode_comercializador_sin_cambios')

    def __init__(self):
        self.doc_root = None
        self.missatge = XmlField(
            'MensajeCambiodeComercializadorSinCambios',
            attributes={'xmlns': 'http://localhost/elegibilidad'}
        )
        self.cabecera = Cabecera()
        self.cambiode_comercializador_sin_cambios = CambiodeComercializadorSinCambios()
        super(MensajeCambiodeComercializadorSinCambios, self).__init__(
            'MensajeCambiodeComercializadorSinCambios', 'missatge'
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

