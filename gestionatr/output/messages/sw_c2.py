# -*- coding: utf-8 -*-
from gestionatr.output.messages.sw_c1 import *
from gestionatr.output.messages.base import rep_cut


# Paso 01
class MensajeCambiodeComercializadorConCambios(XmlModel):
    _sort_order = ('mensaje', 'cabecera', 'cambiode_comercializador_con_cambios')

    def __init__(self):
        self.doc_root = None
        self.mensaje = XmlField(
            'MensajeCambiodeComercializadorConCambios',
            attributes={'xmlns': 'http://localhost/elegibilidad'}
        )
        self.cabecera = Cabecera()
        self.cambiode_comercializador_con_cambios = CambiodeComercializadorConCambios()
        super(MensajeCambiodeComercializadorConCambios, self).__init__(
            'MensajeCambiodeComercializadorConCambios', 'mensaje'
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

    _sort_order = ('datos_solicitud', 'tipo_modificacion', 'tipo_solicitud_administrativa', 'cnae', 'ind_activacion', 'fecha_prevista_accion', 'contratacion_incondicional_ps', 'contratacion_incondicional_bs', 'bono_social', 'solicitud_tension', 'tension_solicitada')

    def __init__(self):
        super(DatosSolicitud, self).__init__()
        self.tipo_modificacion = XmlField('TipoModificacion')
        self.tipo_solicitud_administrativa = XmlField('TipoSolicitudAdministrativa')
        self.cnae = XmlField('CNAE')
        self.tension_solicitada = XmlField('TensionSolicitada')


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

    _sort_order = ('contacto', 'persona_de_contacto', 'telefonos', 'correo_electronico')

    def __init__(self):
        self.contacto = XmlField('Contacto')
        self.persona_de_contacto = XmlField('PersonaDeContacto')
        self.telefonos = []
        self.correo_electronico = XmlField('CorreoElectronico')
        super(Contacto, self).__init__('Contacto', 'contacto')


class Cliente(Cliente):

    _sort_order = ('cliente', 'id_cliente', 'nombre', 'telefonos', 'correo_electronico', 'indicador_tipo_direccion', 'direccion')

    def __init__(self):
        super(Cliente, self).__init__()
        self.indicador_tipo_direccion = XmlField('IndicadorTipoDireccion')
        self.direccion = Direccion()


class Direccion(XmlModel):

    _sort_order = ('direccion', 'pais', 'provincia', 'municipio', 'poblacion', 'cod_postal', 'via', 'apartado_de_correos')

    def __init__(self, name='Direccion'):
        self.direccion = XmlField(name)
        self.pais = XmlField('Pais')
        self.provincia = XmlField('Provincia')
        self.municipio = XmlField('Municipio')
        self.poblacion = XmlField('Poblacion')
        self.cod_postal = XmlField('CodPostal')
        self.via = Via()
        self.apartado_de_correos = XmlField('ApartadoDeCorreos')
        super(Direccion, self).__init__(name, 'direccion')


class Via(XmlModel):

    _sort_order = ('via', 'tipo_via', 'calle', 'numero_finca', 'duplicador_finca', 'escalera', 'piso', 'puerta', 'tipo_aclarador_finca', 'aclarador_finca')

    def __init__(self, name='Via'):
        self.via = XmlField(name)
        self.tipo_via = XmlField('TipoVia')
        self.calle = XmlField('Calle', rep=rep_cut(30))
        self.numero_finca = XmlField('NumeroFinca', rep=rep_cut(5))
        self.duplicador_finca = XmlField('DuplicadorFinca', rep=rep_cut(3))
        self.escalera = XmlField('Escalera', rep=rep_cut(3))
        self.piso = XmlField('Piso', rep=rep_cut(3))
        self.puerta = XmlField('Puerta', rep=rep_cut(3))
        self.tipo_aclarador_finca = XmlField(
            'TipoAclaradorFinca', rep=rep_cut(2)
        )
        self.aclarador_finca = XmlField('AclaradorFinca', rep=rep_cut(40))
        super(Via, self).__init__(name, 'via')


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


# Paso 03
class MensajeIncidenciasATRDistribuidor(XmlModel):

    _sort_order = ('mensaje', 'cabecera', 'incidencias_atr_distribuidor')

    def __init__(self):
        self.mensaje = XmlField('MensajeIncidenciasATRDistribuidor',
                                attributes={'xmlns': 'http://localhost/elegibilidad'})
        self.cabecera = Cabecera()
        self.incidencias_atr_distribuidor = IncidenciasATRDistribuidor()
        super(MensajeIncidenciasATRDistribuidor, self).__init__('MensajeIncidenciasATRDistribuidor', 'mensaje')


class IncidenciasATRDistribuidor(XmlModel):

    _sort_order = ('incidencias_atr_distribuidor', 'fecha_incidencia', 'fecha_prevista_accion', 'incidencia_list')

    def __init__(self):
        self.incidencias_atr_distribuidor = XmlField('IncidenciasATRDistribuidor')
        self.fecha_incidencia = XmlField('FechaIncidencia')
        self.fecha_prevista_accion = XmlField('FechaPrevistaAccion')
        self.incidencia_list = []
        super(IncidenciasATRDistribuidor, self).__init__('IncidenciasATRDistribuidor', 'incidencias_atr_distribuidor')


class Incidencia(XmlModel):

    _sort_order = ('incidencia', 'secuencial', 'codigo_motivo', 'comentarios')

    def __init__(self):
        self.incidencia = XmlField('Incidencia')
        self.secuencial = XmlField('Secuencial')
        self.codigo_motivo = XmlField('CodigoMotivo')
        self.comentarios = XmlField('Comentarios')
        super(Incidencia, self).__init__('Incidencia', 'incidencia')


# Paso 04 -> C1
# Paso 05
class MensajeActivacionCambiodeComercializadorConCambios(XmlModel):

    _sort_order = ('mensaje', 'cabecera', 'activacion_cambiode_comercializador_con_cambios')

    def __init__(self):
        self.mensaje = XmlField('MensajeActivacionCambiodeComercializadorConCambios',
                                attributes={'xmlns': 'http://localhost/elegibilidad'})
        self.cabecera = Cabecera()
        self.activacion_cambiode_comercializador_con_cambios = ActivacionCambiodeComercializadorConCambios()
        super(MensajeActivacionCambiodeComercializadorConCambios, self).__init__('MensajeActivacionCambiodeComercializadorConCambios', 'mensaje')


class ActivacionCambiodeComercializadorConCambios(XmlModel):

    _sort_order = ('activacion_cambiode_comercializador_con_cambios', 'datos_activacion', 'contrato', 'puntos_de_medida')

    def __init__(self):
        self.activacion_cambiode_comercializador_con_cambios = XmlField('ActivacionCambiodeComercializadorConCambios')
        self.datos_activacion = DatosActivacion()
        self.contrato = Contrato()
        self.puntos_de_medida = PuntosDeMedida()
        super(ActivacionCambiodeComercializadorConCambios, self).__init__('ActivacionCambiodeComercializadorConCambios', 'activacion_cambiode_comercializador_con_cambios')


# Paso 06
class MensajeActivacionComercializadorSaliente(XmlModel):

    _sort_order = ('mensaje', 'cabecera', 'notificacion_comercializador_saliente')

    def __init__(self):
        self.mensaje = XmlField('MensajeActivacionComercializadorSaliente',
                                attributes={'xmlns': 'http://localhost/elegibilidad'})
        self.cabecera = Cabecera()
        self.notificacion_comercializador_saliente = NotificacionComercializadorSaliente()
        super(MensajeActivacionComercializadorSaliente, self).__init__('MensajeActivacionComercializadorSaliente', 'mensaje')


class NotificacionComercializadorSaliente(XmlModel):

    _sort_order = ('notificacion_comercializador_saliente', 'datos_notificacion', 'contrato', 'puntos_de_medida')

    def __init__(self):
        self.notificacion_comercializador_saliente = XmlField('NotificacionComercializadorSaliente')
        self.datos_notificacion = DatosNotificacion()
        self.contrato = Contrato()
        self.puntos_de_medida = PuntosDeMedida()
        super(NotificacionComercializadorSaliente, self).__init__('NotificacionComercializadorSaliente', 'notificacion_comercializador_saliente')

# Paso 08 -> C1 MensajeAnulacionSolicitud
# Paso 09 -> C1 MensajeAceptacionAnulacion
# Paso 10 -> C1 MensajeAceptacionAnulacion
# Paso 11 -> C1 MensajeAceptacionCambiodeComercializadorSaliente
# Paso 12 -> C1 MensajeRechazoCambiodeComercializadorSaliente


# Paso 13
class MensajeContestacionIncidencia(XmlModel):

    _sort_order = ('mensaje', 'cabecera', 'contestacion_incidencia')

    def __init__(self):
        self.mensaje = XmlField('MensajeContestacionIncidencia',
                                attributes={'xmlns': 'http://localhost/elegibilidad'})
        self.cabecera = Cabecera()
        self.contestacion_incidencia = ContestacionIncidencia()
        super(MensajeContestacionIncidencia, self).__init__('MensajeContestacionIncidencia', 'mensaje')


class ContestacionIncidencia(XmlModel):

    _sort_order = ('contestacion_incidencia_node', 'contestacion_incidencia', 'contacto')

    def __init__(self):
        self.contestacion_incidencia_node = XmlField('ContestacionIncidencia')
        self.contestacion_incidencia = XmlField('ContestacionIncidencia')
        self.contacto = Contacto()
        super(ContestacionIncidencia, self).__init__('ContestacionIncidencia', 'contestacion_incidencia_node')
