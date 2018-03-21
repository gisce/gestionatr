# -*- coding: utf-8 -*-
from gestionatr.output.messages.sw_c2 import *
from gestionatr.output.messages.base import CabeceraReclamacion


# Paso 01 
class MensajeReclamacionPeticion(XmlModel):

    _sort_order = ('mensaje', 'cabecera_reclamacion', 'solicitud_reclamacion')

    def __init__(self):
        self.mensaje = XmlField('MensajeReclamacionPeticion',
                                attributes={'xmlns': 'http://localhost/elegibilidad'})
        self.cabecera_reclamacion = CabeceraReclamacion()
        self.solicitud_reclamacion = SolicitudReclamacion()
        super(MensajeReclamacionPeticion, self).__init__('MensajeReclamacionPeticion', 'mensaje')


class SolicitudReclamacion(XmlModel):

    _sort_order = ('solicitud_reclamacion', 'datos_solicitud', 'variables_detalle_reclamacion', 'cliente', 'tipo_reclamante', 'reclamante', 'comentarios', 'registros_documento')

    def __init__(self):
        self.solicitud_reclamacion = XmlField('SolicitudReclamacion')
        self.datos_solicitud = DatosSolicitud()
        self.variables_detalle_reclamacion = VariablesDetalleReclamacion()
        self.cliente = Cliente()
        self.tipo_reclamante = XmlField('TipoReclamante')
        self.reclamante = Reclamante()
        self.comentarios = XmlField('Comentarios')
        self.registros_documento = RegistrosDocumento()
        super(SolicitudReclamacion, self).__init__('SolicitudReclamacion', 'solicitud_reclamacion')


class DatosSolicitud(XmlModel):

    _sort_order = ('datos_solicitud', 'tipo', 'subtipo', 'referencia_origen', 'fecha_limite', 'prioritario')

    def __init__(self):
        self.datos_solicitud = XmlField('DatosSolicitud')
        self.tipo = XmlField('Tipo')
        self.subtipo = XmlField('Subtipo')
        self.referencia_origen = XmlField('ReferenciaOrigen')
        self.fecha_limite = XmlField('FechaLimite')
        self.prioritario = XmlField('Prioritario')
        super(DatosSolicitud, self).__init__('DatosSolicitud', 'datos_solicitud')


class VariablesDetalleReclamacion(XmlModel):

    _sort_order = ('variables_detalle_reclamacion', 'variable_detalle_reclamacion_list')

    def __init__(self):
        self.variables_detalle_reclamacion = XmlField('VariablesDetalleReclamacion')
        self.variable_detalle_reclamacion_list = []
        super(VariablesDetalleReclamacion, self).__init__('VariablesDetalleReclamacion', 'variables_detalle_reclamacion')


class VariableDetalleReclamacion(XmlModel):

    _sort_order = ('variable_detalle_reclamacion', 'num_expediente_acometida', 'num_expediente_fraude', 'fecha_incidente', 'num_factura_atr', 'tipo_concepto_facturado', 'fecha_lectura', 'tipo_dhedm', 'lecturas_aportadas', 'codigo_incidencia', 'codigo_solicitud', 'parametro_contratacion', 'concepto_disconformidad', 'tipo_de_atencion_incorrecta', 'iban', 'contacto', 'codigo_solicitud_reclamacion', 'fecha_desde', 'fecha_hasta', 'importe_reclamado', 'ubicacion_incidencia')

    def __init__(self):
        self.variable_detalle_reclamacion = XmlField('VariableDetalleReclamacion')
        self.num_expediente_acometida = XmlField('NumExpedienteAcometida')
        self.num_expediente_fraude = XmlField('NumExpedienteFraude')
        self.fecha_incidente = XmlField('FechaIncidente')
        self.num_factura_atr = XmlField('NumFacturaATR')
        self.tipo_concepto_facturado = XmlField('TipoConceptoFacturado')
        self.fecha_lectura = XmlField('FechaLectura')
        self.tipo_dhedm = XmlField('TipoDHEdM')
        self.lecturas_aportadas = LecturasAportadas()
        self.codigo_incidencia = XmlField('CodigoIncidencia')
        self.codigo_solicitud = XmlField('CodigoSolicitud')
        self.parametro_contratacion = XmlField('ParametroContratacion')
        self.concepto_disconformidad = XmlField('ConceptoDisconformidad')
        self.tipo_de_atencion_incorrecta = XmlField('TipoDeAtencionIncorrecta')
        self.iban = XmlField('IBAN')
        self.contacto = Contacto()
        self.codigo_solicitud_reclamacion = XmlField('CodigoSolicitudReclamacion')
        self.fecha_desde = XmlField('FechaDesde')
        self.fecha_hasta = XmlField('FechaHasta')
        self.importe_reclamado = XmlField('ImporteReclamado')
        self.ubicacion_incidencia = UbicacionIncidencia()
        super(VariableDetalleReclamacion, self).__init__('VariableDetalleReclamacion', 'variable_detalle_reclamacion')


class LecturasAportadas(XmlModel):

    _sort_order = ('lecturas_aportadas', 'lectura_aportada_list')

    def __init__(self):
        self.lecturas_aportadas = XmlField('LecturasAportadas')
        self.lectura_aportada_list = []
        super(LecturasAportadas, self).__init__('LecturasAportadas', 'lecturas_aportadas')


class LecturaAportada(XmlModel):

    _sort_order = ('lectura_aportada', 'integrador', 'codigo_periodo_dh', 'lectura_propuesta')

    def __init__(self):
        self.lectura_aportada = XmlField('LecturaAportada')
        self.integrador = XmlField('Integrador')
        self.codigo_periodo_dh = XmlField('CodigoPeriodoDH')
        self.lectura_propuesta = XmlField('LecturaPropuesta')
        super(LecturaAportada, self).__init__('LecturaAportada', 'lectura_aportada')


class UbicacionIncidencia(XmlModel):

    _sort_order = ('ubicacion_incidencia', 'des_ubicacion_incidencia', 'provincia', 'municipio', 'poblacion', 'cod_postal')

    def __init__(self):
        self.ubicacion_incidencia = XmlField('UbicacionIncidencia')
        self.des_ubicacion_incidencia = XmlField('DesUbicacionIncidencia')
        self.provincia = XmlField('Provincia')
        self.municipio = XmlField('Municipio')
        self.poblacion = XmlField('Poblacion')
        self.cod_postal = XmlField('CodPostal')
        super(UbicacionIncidencia, self).__init__('UbicacionIncidencia', 'ubicacion_incidencia')


class Reclamante(XmlModel):

    _sort_order = ('reclamante', 'id_reclamante', 'nombre', 'telefonos', 'correo_electronico')

    def __init__(self):
        self.reclamante = XmlField('Reclamante')
        self.id_reclamante = IdReclamante()
        self.nombre = Nombre()
        self.telefonos = []
        self.correo_electronico = XmlField('CorreoElectronico')
        super(Reclamante, self).__init__('Reclamante', 'reclamante')


class IdReclamante(XmlModel):

    _sort_order = ('id_reclamante', 'tipo_identificador', 'identificador')

    def __init__(self):
        self.id_reclamante = XmlField('IdReclamante')
        self.tipo_identificador = XmlField('TipoIdentificador')
        self.identificador = XmlField('Identificador')
        super(IdReclamante, self).__init__('IdReclamante', 'id_reclamante')


# Paso 02
class MensajeAceptacionReclamacion(XmlModel):

    _sort_order = ('mensaje', 'cabecera_reclamacion', 'aceptacion_reclamacion')

    def __init__(self):
        self.mensaje = XmlField('MensajeAceptacionReclamacion',
                                attributes={'xmlns': 'http://localhost/elegibilidad'})
        self.cabecera_reclamacion = CabeceraReclamacion()
        self.aceptacion_reclamacion = AceptacionReclamacion()
        super(MensajeAceptacionReclamacion, self).__init__('MensajeAceptacionReclamacion', 'mensaje')


class AceptacionReclamacion(XmlModel):

    _sort_order = ('aceptacion_reclamacion', 'datos_aceptacion')

    def __init__(self):
        self.aceptacion_reclamacion = XmlField('AceptacionReclamacion')
        self.datos_aceptacion = DatosAceptacion()
        super(AceptacionReclamacion, self).__init__('AceptacionReclamacion', 'aceptacion_reclamacion')


class DatosAceptacion(XmlModel):

    _sort_order = ('datos_aceptacion', 'fecha_aceptacion', 'codigo_reclamacion_distribuidora')

    def __init__(self):
        self.datos_aceptacion = XmlField('DatosAceptacion')
        self.fecha_aceptacion = XmlField('FechaAceptacion')
        self.codigo_reclamacion_distribuidora = XmlField('CodigoReclamacionDistribuidora')
        super(DatosAceptacion, self).__init__('DatosAceptacion', 'datos_aceptacion')


# Rechazo Reclamacion
class MensajeRechazoReclamacion(XmlModel):

    _sort_order = ('mensaje_rechazo_reclamacion', 'cabecera_reclamacion', 'rechazos')

    def __init__(self):
        self.mensaje_rechazo_reclamacion = XmlField('MensajeRechazoReclamacion',
                                        attributes={'xmlns': 'http://localhost/elegibilidad'})
        self.cabecera_reclamacion = CabeceraReclamacion()
        self.rechazos = Rechazos()
        super(MensajeRechazoReclamacion, self).__init__('MensajeRechazoReclamacion', 'mensaje_rechazo_reclamacion')


# Paso 03
class MensajePeticionInformacionAdicionalReclamacion(XmlModel):

    _sort_order = ('mensaje', 'cabecera_reclamacion', 'informacion_adicional')

    def __init__(self):
        self.mensaje = XmlField('MensajePeticionInformacionAdicionalReclamacion',
                                attributes={'xmlns': 'http://localhost/elegibilidad'})
        self.cabecera_reclamacion = CabeceraReclamacion()
        self.informacion_adicional = InformacionAdicional()
        super(MensajePeticionInformacionAdicionalReclamacion, self).__init__('MensajePeticionInformacionAdicionalReclamacion', 'mensaje')


class InformacionAdicional(XmlModel):

    _sort_order = ('informacion_adicional', 'datos_informacion', 'informacion_intermedia', 'retipificacion', 'solicitudes_informacion_adicional', 'comentarios', 'registros_documento')

    def __init__(self):
        self.informacion_adicional = XmlField('InformacionAdicional')
        self.datos_informacion = DatosInformacion()
        self.informacion_intermedia = InformacionIntermedia()
        self.retipificacion = Retipificacion()
        self.solicitudes_informacion_adicional = SolicitudesInformacionAdicional()
        self.comentarios = XmlField('Comentarios')
        self.registros_documento = RegistrosDocumento()
        super(InformacionAdicional, self).__init__('InformacionAdicional', 'informacion_adicional')


class DatosInformacion(XmlModel):

    _sort_order = ('datos_informacion', 'num_expediente_acometida', 'tipo_comunicacion', 'codigo_reclamacion_distribuidora')

    def __init__(self):
        self.datos_informacion = XmlField('DatosInformacion')
        self.num_expediente_acometida = XmlField('NumExpedienteAcometida')
        self.tipo_comunicacion = XmlField('TipoComunicacion')
        self.codigo_reclamacion_distribuidora = XmlField('CodigoReclamacionDistribuidora')
        super(DatosInformacion, self).__init__('DatosInformacion', 'datos_informacion')


class InformacionIntermedia(XmlModel):

    _sort_order = ('informacion_intermedia', 'desc_informacion_intermedia', 'intervenciones')

    def __init__(self):
        self.informacion_intermedia = XmlField('InformacionIntermedia')
        self.desc_informacion_intermedia = XmlField('DescInformacionIntermedia')
        self.intervenciones = Intervenciones()
        super(InformacionIntermedia, self).__init__('InformacionIntermedia', 'informacion_intermedia')


class Intervenciones(XmlModel):

    _sort_order = ('intervenciones', 'intervencion_list')

    def __init__(self):
        self.intervenciones = XmlField('Intervenciones')
        self.intervencion_list = []
        super(Intervenciones, self).__init__('Intervenciones', 'intervenciones')


class Intervencion(XmlModel):

    _sort_order = ('intervencion', 'tipo_intervencion', 'fecha', 'hora_desde', 'hora_hasta', 'numero_visita', 'resultado', 'detalle_resultado')

    def __init__(self):
        self.intervencion = XmlField('Intervencion')
        self.tipo_intervencion = XmlField('TipoIntervencion')
        self.fecha = XmlField('Fecha')
        self.hora_desde = XmlField('HoraDesde')
        self.hora_hasta = XmlField('HoraHasta')
        self.numero_visita = XmlField('NumeroVisita')
        self.resultado = XmlField('Resultado')
        self.detalle_resultado = XmlField('DetalleResultado')
        super(Intervencion, self).__init__('Intervencion', 'intervencion')


class Retipificacion(XmlModel):

    _sort_order = ('retipificacion', 'tipo', 'subtipo', 'desc_retipificacion')

    def __init__(self):
        self.retipificacion = XmlField('Retipificacion')
        self.tipo = XmlField('Tipo')
        self.subtipo = XmlField('Subtipo')
        self.desc_retipificacion = XmlField('DescRetipificacion')
        super(Retipificacion, self).__init__('Retipificacion', 'retipificacion')


class SolicitudesInformacionAdicional(XmlModel):

    _sort_order = ('solicitudes_informacion_adicional', 'solicitud_informacion_adicional_list', 'solicitud_informacion_adicional_para_retipificacion')

    def __init__(self):
        self.solicitudes_informacion_adicional = XmlField('SolicitudesInformacionAdicional')
        self.solicitud_informacion_adicional_list = []
        self.solicitud_informacion_adicional_para_retipificacion = SolicitudInformacionAdicionalParaRetipificacion()
        super(SolicitudesInformacionAdicional, self).__init__('SolicitudesInformacionAdicional', 'solicitudes_informacion_adicional')


class SolicitudInformacionAdicional(XmlModel):

    _sort_order = ('solicitud_informacion_adicional', 'tipo_informacion_adicional', 'desc_peticion_informacion', 'fecha_limite_envio')

    def __init__(self):
        self.solicitud_informacion_adicional = XmlField('SolicitudInformacionAdicional')
        self.tipo_informacion_adicional = XmlField('TipoInformacionAdicional')
        self.desc_peticion_informacion = XmlField('DescPeticionInformacion')
        self.fecha_limite_envio = XmlField('FechaLimiteEnvio')
        super(SolicitudInformacionAdicional, self).__init__('SolicitudInformacionAdicional', 'solicitud_informacion_adicional')


class SolicitudInformacionAdicionalParaRetipificacion(XmlModel):

    _sort_order = ('solicitud_informacion_adicional_para_retipificacion', 'tipo', 'subtipo', 'fecha_limite_envio')

    def __init__(self):
        self.solicitud_informacion_adicional_para_retipificacion = XmlField('SolicitudInformacionAdicionalParaRetipificacion')
        self.tipo = XmlField('Tipo')
        self.subtipo = XmlField('Subtipo')
        self.fecha_limite_envio = XmlField('FechaLimiteEnvio')
        super(SolicitudInformacionAdicionalParaRetipificacion, self).__init__('SolicitudInformacionAdicionalParaRetipificacion', 'solicitud_informacion_adicional_para_retipificacion')


# Paso 04
class MensajeEnvioInformacionReclamacion(XmlModel):

    _sort_order = ('mensaje', 'cabecera_reclamacion', 'envio_informacion_reclamacion')

    def __init__(self):
        self.mensaje = XmlField('MensajeEnvioInformacionReclamacion',
                                attributes={'xmlns': 'http://localhost/elegibilidad'})
        self.cabecera_reclamacion = CabeceraReclamacion()
        self.envio_informacion_reclamacion = EnvioInformacionReclamacion()
        super(MensajeEnvioInformacionReclamacion, self).__init__('MensajeEnvioInformacionReclamacion', 'mensaje')


class EnvioInformacionReclamacion(XmlModel):

    _sort_order = ('envio_informacion_reclamacion', 'datos_envio_informacion', 'variables_aportacion_informacion', 'variables_aportacion_informacion_para_retipificacion', 'cliente', 'comentarios', 'registros_documento')

    def __init__(self):
        self.envio_informacion_reclamacion = XmlField('EnvioInformacionReclamacion')
        self.datos_envio_informacion = DatosEnvioInformacion()
        self.variables_aportacion_informacion = VariablesAportacionInformacion()
        self.variables_aportacion_informacion_para_retipificacion = VariablesAportacionInformacionParaRetipificacion()
        self.cliente = Cliente()
        self.comentarios = XmlField('Comentarios')
        self.registros_documento = RegistrosDocumento()
        super(EnvioInformacionReclamacion, self).__init__('EnvioInformacionReclamacion', 'envio_informacion_reclamacion')


class DatosEnvioInformacion(XmlModel):

    _sort_order = ('datos_envio_informacion', 'num_expediente_acometida', 'fecha_informacion')

    def __init__(self):
        self.datos_envio_informacion = XmlField('DatosEnvioInformacion')
        self.num_expediente_acometida = XmlField('NumExpedienteAcometida')
        self.fecha_informacion = XmlField('FechaInformacion')
        super(DatosEnvioInformacion, self).__init__('DatosEnvioInformacion', 'datos_envio_informacion')


class VariablesAportacionInformacion(XmlModel):

    _sort_order = ('variables_aportacion_informacion', 'variable_aportacion_informacion_list')

    def __init__(self):
        self.variables_aportacion_informacion = XmlField('VariablesAportacionInformacion')
        self.variable_aportacion_informacion_list = []
        super(VariablesAportacionInformacion, self).__init__('VariablesAportacionInformacion', 'variables_aportacion_informacion')


class VariableAportacionInformacion(XmlModel):

    _sort_order = ('variable_aportacion_informacion', 'tipo_informacion', 'desc_peticion_informacion', 'variable', 'valor')

    def __init__(self):
        self.variable_aportacion_informacion = XmlField('VariableAportacionInformacion')
        self.tipo_informacion = XmlField('TipoInformacion')
        self.desc_peticion_informacion = XmlField('DescPeticionInformacion')
        self.variable = XmlField('Variable')
        self.valor = XmlField('Valor')
        super(VariableAportacionInformacion, self).__init__('VariableAportacionInformacion', 'variable_aportacion_informacion')


class VariablesAportacionInformacionParaRetipificacion(XmlModel):

    _sort_order = ('variables_aportacion_informacion_para_retipificacion', 'variable_aportacion_informacion_para_retipificacion_list')

    def __init__(self):
        self.variables_aportacion_informacion_para_retipificacion = XmlField('VariablesAportacionInformacionParaRetipificacion')
        self.variable_aportacion_informacion_para_retipificacion_list = []
        super(VariablesAportacionInformacionParaRetipificacion, self).__init__('VariablesAportacionInformacionParaRetipificacion', 'variables_aportacion_informacion_para_retipificacion')


class VariableAportacionInformacionParaRetipificacion(XmlModel):

    _sort_order = ('variable_aportacion_informacion_para_retipificacion', 'num_expediente_acometida', 'num_expediente_fraude', 'fecha_incidente', 'num_factura_atr', 'tipo_concepto_facturado', 'fecha_lectura', 'tipo_dhedm', 'lecturas_aportadas', 'codigo_incidencia', 'codigo_solicitud', 'parametro_contratacion', 'concepto_disconformidad', 'tipo_de_atencion_incorrecta', 'iban', 'contacto', 'codigo_solicitud_reclamacion', 'fecha_desde', 'fecha_hasta', 'importe_reclamado', 'ubicacion_incidencia')

    def __init__(self):
        self.variable_aportacion_informacion_para_retipificacion = XmlField('VariableAportacionInformacionParaRetipificacion')
        self.num_expediente_acometida = XmlField('NumExpedienteAcometida')
        self.num_expediente_fraude = XmlField('NumExpedienteFraude')
        self.fecha_incidente = XmlField('FechaIncidente')
        self.num_factura_atr = XmlField('NumFacturaATR')
        self.tipo_concepto_facturado = XmlField('TipoConceptoFacturado')
        self.fecha_lectura = XmlField('FechaLectura')
        self.tipo_dhedm = XmlField('TipoDHEdM')
        self.lecturas_aportadas = LecturasAportadas()
        self.codigo_incidencia = XmlField('CodigoIncidencia')
        self.codigo_solicitud = XmlField('CodigoSolicitud')
        self.parametro_contratacion = XmlField('ParametroContratacion')
        self.concepto_disconformidad = XmlField('ConceptoDisconformidad')
        self.tipo_de_atencion_incorrecta = XmlField('TipoDeAtencionIncorrecta')
        self.iban = XmlField('IBAN')
        self.contacto = Contacto()
        self.codigo_solicitud_reclamacion = XmlField('CodigoSolicitudReclamacion')
        self.fecha_desde = XmlField('FechaDesde')
        self.fecha_hasta = XmlField('FechaHasta')
        self.importe_reclamado = XmlField('ImporteReclamado')
        self.ubicacion_incidencia = UbicacionIncidencia()
        super(VariableAportacionInformacionParaRetipificacion, self).__init__('VariableAportacionInformacionParaRetipificacion', 'variable_aportacion_informacion_para_retipificacion')


# Paso 05
class MensajeCierreReclamacion(XmlModel):

    _sort_order = ('mensaje_cierre_reclamacion', 'cabecera_reclamacion', 'cierre_reclamacion')

    def __init__(self):
        self.mensaje = XmlField('MensajeCierreReclamacion',
                                attributes={'xmlns': 'http://localhost/elegibilidad'})
        self.cabecera_reclamacion = CabeceraReclamacion()
        self.cierre_reclamacion = CierreReclamacion()
        super(MensajeCierreReclamacion, self).__init__('MensajeCierreReclamacion', 'mensaje')


class CierreReclamacion(XmlModel):

    _sort_order = ('cierre_reclamacion', 'datos_cierre', 'cod_contrato', 'comentarios', 'registros_documento')

    def __init__(self):
        self.cierre_reclamacion = XmlField('CierreReclamacion')
        self.datos_cierre = DatosCierre()
        self.cod_contrato = XmlField('CodContrato')
        self.comentarios = XmlField('Comentarios')
        self.registros_documento = RegistrosDocumento()
        super(CierreReclamacion, self).__init__('CierreReclamacion', 'cierre_reclamacion')


class DatosCierre(XmlModel):

    _sort_order = ('datos_cierre', 'num_expediente_acometida', 'fecha', 'hora', 'tipo', 'subtipo', 'codigo_reclamacion_distribuidora', 'resultado_reclamacion', 'detalle_resultado', 'observaciones', 'indemnizacion_abonada', 'num_expediente_anomalia_fraude', 'fecha_movimiento')

    def __init__(self):
        self.datos_cierre = XmlField('DatosCierre')
        self.num_expediente_acometida = XmlField('NumExpedienteAcometida')
        self.fecha = XmlField('Fecha')
        self.hora = XmlField('Hora')
        self.tipo = XmlField('Tipo')
        self.subtipo = XmlField('Subtipo')
        self.codigo_reclamacion_distribuidora = XmlField('CodigoReclamacionDistribuidora')
        self.resultado_reclamacion = XmlField('ResultadoReclamacion')
        self.detalle_resultado = XmlField('DetalleResultado')
        self.observaciones = XmlField('Observaciones')
        self.indemnizacion_abonada = XmlField('IndemnizacionAbonada')
        self.num_expediente_anomalia_fraude = XmlField('NumExpedienteAnomaliaFraude')
        self.fecha_movimiento = XmlField('FechaMovimiento')
        super(DatosCierre, self).__init__('DatosCierre', 'datos_cierre')
