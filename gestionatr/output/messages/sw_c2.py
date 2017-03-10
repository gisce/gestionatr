# -*- coding: utf-8 -*-

from gestionatr.output.messages.sw_c1 import *


# Paso 01
class MensajeCambiodeComercializadorConCambios(XmlModel):
    _sort_order = ('mensage', 'cabecera', 'cambiode_comercializador_con_cambios')

    def __init__(self):
        self.doc_root = None
        self.mensage = XmlField(
            'MensajeCambiodeComercializadorConCambios',
            attributes={'xmlns': 'http://localhost/elegibilidad'}
        )
        self.cabecera = Cabecera()
        self.cambiode_comercializador_con_cambios = CambiodeComercializadorConCambios()
        super(MensajeCambiodeComercializadorConCambios, self).__init__(
            'MensajeCambiodeComercializadorConCambios', 'mensage'
        )


class CambiodeComercializadorConCambios(XmlModel):

    _sort_order = ('cambiode_comercializador_con_cambios', 'datos_solicitud', 'contrato', 'cliente', 'medida', 'doc_tecnica', 'comentarios', 'registros_documento')

    def __init__(self):
        self.cambiode_comercializador_con_cambios = XmlField('CambiodeComercializadorConCambios')
        self.datos_solicitud = DatosSolicitud()
        self.contrato = Contrato()
        self.cliente = Cliente()
        self.medida = Medida()
        self.doc_tecnica = DocTecnica()
        self.comentarios = XmlField('Comentarios')
        self.registros_documento = RegistrosDocumento()
        super(CambiodeComercializadorConCambios, self).__init__('CambiodeComercializadorConCambios', 'cambiode_comercializador_con_cambios')


class DatosSolicitud(DatosSolicitud):

    _sort_order = ('datos_solicitud', 'tipo_modificacion', 'tipo_solicitud_administrativa', 'cnae', 'ind_activacion', 'fecha_prevista_accion', 'contratacion_incondicional_ps')

    def __init__(self):
        super(DatosSolicitud, self).__init__()
        self.tipo_modificacion = XmlField('TipoModificacion')
        self.tipo_solicitud_administrativa = XmlField('TipoSolicitudAdministrativa')
        self.cnae = XmlField('CNAE')


class Contrato(Contrato):

    _sort_order = ('contrato', 'id_contrato', 'fecha_finalizacion', 'tipo_autoconsumo', 'tipo_contrato_atr', 'condiciones_contractuales', 'periodicidad_facturacion', 'consumo_anual_estimado', 'contacto', 'tipo_activacion_prevista', 'fecha_activacion_prevista')

    def __init__(self):
        super(Contrato, self).__init__()
        self.fecha_finalizacion = XmlField('FechaFinalizacion')
        self.tipo_contrato_atr = XmlField('TipoContratoATR')
        self.periodicidad_facturacion = XmlField('PeriodicidadFacturacion')
        self.consumo_anual_estimado = XmlField('ConsumoAnualEstimado')
        self.contacto = Contacto()


class Contacto(XmlModel):

    _sort_order = ('contacto', 'persona_de_contacto', 'telefono', 'correo_electronico')

    def __init__(self):
        self.contacto = XmlField('Contacto')
        self.persona_de_contacto = XmlField('PersonaDeContacto')
        self.telefono = Telefono()
        self.correo_electronico = XmlField('CorreoElectronico')
        super(Contacto, self).__init__('Contacto', 'contacto')


class Cliente(Cliente):

    _sort_order = ('cliente', 'id_cliente', 'nombre', 'telefono', 'correo_electronico', 'indicador_tipo_direccion', 'direccion')

    def __init__(self):
        super(Cliente, self).__init__()
        self.indicador_tipo_direccion = XmlField('IndicadorTipoDireccion')
        self.direccion = Direccion()


class Direccion(XmlModel):

    _sort_order = ('direccion', 'pais', 'provincia', 'municipio', 'poblacion', 'tipo_via', 'cod_postal', 'calle', 'numero_finca', 'duplicador_finca', 'escalera', 'piso', 'puerta', 'tipo_aclarador_finca', 'aclarador_finca')

    def __init__(self):
        self.direccion = XmlField('Direccion')
        self.pais = XmlField('Pais')
        self.provincia = XmlField('Provincia')
        self.municipio = XmlField('Municipio')
        self.poblacion = XmlField('Poblacion')
        self.tipo_via = XmlField('TipoVia')
        self.cod_postal = XmlField('CodPostal')
        self.calle = XmlField('Calle')
        self.numero_finca = XmlField('NumeroFinca')
        self.duplicador_finca = XmlField('DuplicadorFinca')
        self.escalera = XmlField('Escalera')
        self.piso = XmlField('Piso')
        self.puerta = XmlField('Puerta')
        self.tipo_aclarador_finca = XmlField('TipoAclaradorFinca')
        self.aclarador_finca = XmlField('AclaradorFinca')
        super(Direccion, self).__init__('Direccion', 'direccion')


class Medida(XmlModel):

    _sort_order = ('medida', 'propiedad_equipo', 'tipo_equipo_medida', 'modelos_aparato')

    def __init__(self):
        self.medida = XmlField('Medida')
        self.propiedad_equipo = XmlField('PropiedadEquipo')
        self.tipo_equipo_medida = XmlField('TipoEquipoMedida')
        self.modelos_aparato = ModelosAparato()
        super(Medida, self).__init__('Medida', 'medida')


class ModelosAparato(XmlModel):

    _sort_order = ('modelos_aparato', 'modelo_aparato_list')

    def __init__(self):
        self.modelos_aparato = XmlField('ModelosAparato')
        self.modelo_aparato_list = []
        super(ModelosAparato, self).__init__('ModelosAparato', 'modelos_aparato')


class ModeloAparato(XmlModel):

    _sort_order = ('modelo_aparato', 'tipo_aparato', 'marca_aparato', 'modelo_marca')

    def __init__(self):
        self.modelo_aparato = XmlField('ModeloAparato')
        self.tipo_aparato = XmlField('TipoAparato')
        self.marca_aparato = XmlField('MarcaAparato')
        self.modelo_marca = XmlField('ModeloMarca')
        super(ModeloAparato, self).__init__('ModeloAparato', 'modelo_aparato')


class DocTecnica(XmlModel):

    _sort_order = ('doc_tecnica', 'datos_cie', 'datos_apm')

    def __init__(self):
        self.doc_tecnica = XmlField('DocTecnica')
        self.datos_cie = DatosCie()
        self.datos_apm = DatosAPM()
        super(DocTecnica, self).__init__('DocTecnica', 'doc_tecnica')


class DatosCie(XmlModel):

    _sort_order = ('datos_cie', 'cie_papel', 'cie_electronico', 'validez_cie')

    def __init__(self):
        self.datos_cie = XmlField('DatosCie')
        self.cie_papel = CIEPapel()
        self.cie_electronico = CIEElectronico()
        self.validez_cie = XmlField('ValidezCIE')
        super(DatosCie, self).__init__('DatosCie', 'datos_cie')


class CIEPapel(XmlModel):

    _sort_order = ('cie_papel', 'codigo_cie', 'potencia_inst_bt', 'potencia_no_interrumpible', 'fecha_emision_cie', 'fecha_caducidad_cie', 'nif_instalador', 'codigo_instalador', 'tension_suministro_cie', 'tipo_suministro')

    def __init__(self):
        self.cie_papel = XmlField('CIEPapel')
        self.codigo_cie = XmlField('CodigoCie')
        self.potencia_inst_bt = XmlField('PotenciaInstBT')
        self.potencia_no_interrumpible = XmlField('PotenciaNoInterrumpible')
        self.fecha_emision_cie = XmlField('FechaEmisionCie')
        self.fecha_caducidad_cie = XmlField('FechaCaducidadCie')
        self.nif_instalador = XmlField('NifInstalador')
        self.codigo_instalador = XmlField('CodigoInstalador')
        self.tension_suministro_cie = XmlField('TensionSuministroCIE')
        self.tipo_suministro = XmlField('TipoSuministro')
        super(CIEPapel, self).__init__('CIEPapel', 'cie_papel')


class CIEElectronico(XmlModel):

    _sort_order = ('cie_electronico', 'codigo_cie', 'sello_electronico')

    def __init__(self):
        self.cie_electronico = XmlField('CIEElectronico')
        self.codigo_cie = XmlField('CodigoCie')
        self.sello_electronico = XmlField('SelloElectronico')
        super(CIEElectronico, self).__init__('CIEElectronico', 'cie_electronico')


class DatosAPM(XmlModel):

    _sort_order = ('datos_apm', 'codigo_apm', 'potencia_inst_at', 'fecha_emision_apm', 'fecha_caducidad_apm', 'tension_suministro_apm', 'nif_instalador', 'codigo_instalador')

    def __init__(self):
        self.datos_apm = XmlField('DatosAPM')
        self.codigo_apm = XmlField('CodigoApm')
        self.potencia_inst_at = XmlField('PotenciaInstAT')
        self.fecha_emision_apm = XmlField('FechaEmisionApm')
        self.fecha_caducidad_apm = XmlField('FechaCaducidadApm')
        self.tension_suministro_apm = XmlField('TensionSuministroAPM')
        self.nif_instalador = XmlField('NifInstalador')
        self.codigo_instalador = XmlField('CodigoInstalador')
        super(DatosAPM, self).__init__('DatosAPM', 'datos_apm')


# Paso 02
class MensajeAceptacionCambiodeComercializadorConCambios(XmlModel):

    _sort_order = ('mensaje', 'cabecera', 'aceptacion_cambiode_comercializador_con_cambios')

    def __init__(self):
        self.mensaje = XmlField('MensajeAceptacionCambiodeComercializadorConCambios',
                                attributes={'xmlns': 'http://localhost/elegibilidad'})
        self.cabecera = Cabecera()
        self.aceptacion_cambiode_comercializador_con_cambios = AceptacionCambiodeComercializadorConCambios()
        super(MensajeAceptacionCambiodeComercializadorConCambios, self).__init__('MensajeAceptacionCambiodeComercializadorConCambios', 'mensaje')


class AceptacionCambiodeComercializadorConCambios(XmlModel):

    _sort_order = ('aceptacion_cambiode_comercializador_con_cambios', 'datos_aceptacion', 'contrato')

    def __init__(self):
        self.aceptacion_cambiode_comercializador_con_cambios = XmlField('AceptacionCambiodeComercializadorConCambios')
        self.datos_aceptacion = DatosAceptacion()
        self.contrato = Contrato()
        super(AceptacionCambiodeComercializadorConCambios, self).__init__('AceptacionCambiodeComercializadorConCambios', 'aceptacion_cambiode_comercializador_con_cambios')
