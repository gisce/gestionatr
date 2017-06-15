# -*- coding: utf-8 -*-

from libcomxml.core import XmlModel, XmlField
from gestionatr.output.messages.base import Cabecera


# Paso 01
class MensajeCambiodeComercializadorSinCambios(XmlModel):
    _sort_order = ('mensaje', 'cabecera', 'cambiode_comercializador_sin_cambios')

    def __init__(self):
        self.doc_root = None
        self.mensaje = XmlField(
            'MensajeCambiodeComercializadorSinCambios',
            attributes={'xmlns': 'http://localhost/elegibilidad'}
        )
        self.cabecera = Cabecera()
        self.cambiode_comercializador_sin_cambios = CambiodeComercializadorSinCambios()
        super(MensajeCambiodeComercializadorSinCambios, self).__init__(
            'MensajeCambiodeComercializadorSinCambios', 'mensaje'
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

    def __init__(self, name='IdCliente'):
        self.id_cliente = XmlField(name)
        self.tipo_identificador = XmlField('TipoIdentificador')
        self.identificador = XmlField('Identificador')
        self.tipo_persona = XmlField('TipoPersona')
        super(IdCliente, self).__init__(name, 'id_cliente')


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

    _sort_order = ('mensaje', 'cabecera', 'aceptacion_cambiode_comercializador_sin_cambios')

    def __init__(self):
        self.mensaje = XmlField('MensajeAceptacionCambiodeComercializadorSinCambios',
                                attributes={'xmlns': 'http://localhost/elegibilidad'})
        self.cabecera = Cabecera()
        self.aceptacion_cambiode_comercializador_sin_cambios = AceptacionCambiodeComercializadorSinCambios()
        super(MensajeAceptacionCambiodeComercializadorSinCambios, self).__init__('MensajeAceptacionCambiodeComercializadorSinCambios', 'mensaje')


class AceptacionCambiodeComercializadorSinCambios(XmlModel):

    _sort_order = ('aceptacion_cambiode_comercializador_sin_cambios', 'datos_aceptacion', 'contrato')

    def __init__(self):
        self.aceptacion_cambiode_comercializador_sin_cambios = XmlField('AceptacionCambiodeComercializadorSinCambios')
        self.datos_aceptacion = DatosAceptacion()
        self.contrato = Contrato()
        super(AceptacionCambiodeComercializadorSinCambios, self).__init__('AceptacionCambiodeComercializadorSinCambios', 'aceptacion_cambiode_comercializador_sin_cambios')


class DatosAceptacion(XmlModel):

    _sort_order = ('datos_aceptacion', 'fecha_aceptacion', 'potencia_actual', 'actuacion_campo', 'fecha_ultima_lectura_firme')

    def __init__(self):
        self.datos_aceptacion = XmlField('DatosAceptacion')
        self.fecha_aceptacion = XmlField('FechaAceptacion')
        self.potencia_actual = XmlField('PotenciaActual')
        self.actuacion_campo = XmlField('ActuacionCampo')
        self.fecha_ultima_lectura_firme = XmlField('FechaUltimaLecturaFirme')
        super(DatosAceptacion, self).__init__('DatosAceptacion', 'datos_aceptacion')


class Contrato(XmlModel):

    _sort_order = ('contrato', 'id_contrato', 'tipo_autoconsumo', 'tipo_contrato_atr', 'condiciones_contractuales', 'tipo_activacion_prevista', 'fecha_activacion_prevista')

    def __init__(self):
        self.contrato = XmlField('Contrato')
        self.id_contrato = IdContrato()
        self.tipo_autoconsumo = XmlField('TipoAutoconsumo')
        self.tipo_contrato_atr = XmlField('TipoContratoATR')
        self.condiciones_contractuales = CondicionesContractuales()
        self.tipo_activacion_prevista = XmlField('TipoActivacionPrevista')
        self.fecha_activacion_prevista = XmlField('FechaActivacionPrevista')
        super(Contrato, self).__init__('Contrato', 'contrato')


class IdContrato(XmlModel):

    _sort_order = ('id_contrato', 'cod_contrato')

    def __init__(self):
        self.id_contrato = XmlField('IdContrato')
        self.cod_contrato = XmlField('CodContrato')
        super(IdContrato, self).__init__('IdContrato', 'id_contrato')


class CondicionesContractuales(XmlModel):

    _sort_order = ('condiciones_contractuales', 'tarifa_atr', 'periodicidad_facturacion', 'tipode_telegestion', 'potencias_contratadas', 'modo_control_potencia', 'marca_medida_con_perdidas', 'tension_del_suministro', 'vas_trafo', 'porcentaje_perdidas')

    def __init__(self):
        self.condiciones_contractuales = XmlField('CondicionesContractuales')
        self.tarifa_atr = XmlField('TarifaATR')
        self.periodicidad_facturacion = XmlField('PeriodicidadFacturacion')
        self.tipode_telegestion = XmlField('TipodeTelegestion')
        self.potencias_contratadas = PotenciasContratadas()
        self.modo_control_potencia = XmlField('ModoControlPotencia')
        self.marca_medida_con_perdidas = XmlField('MarcaMedidaConPerdidas')
        self.tension_del_suministro = XmlField('TensionDelSuministro')
        self.vas_trafo = XmlField('VAsTrafo')
        self.porcentaje_perdidas = XmlField('PorcentajePerdidas')
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


# Paso 04 (Rechazo)
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


# Paso 05
class MensajeActivacionCambiodeComercializadorSinCambios(XmlModel):

    _sort_order = ('mensaje', 'cabecera', 'activacion_cambiode_comercializador_sin_cambios')

    def __init__(self):
        self.mensaje = XmlField('MensajeActivacionCambiodeComercializadorSinCambios',
                                attributes={'xmlns': 'http://localhost/elegibilidad'})
        self.cabecera = Cabecera()
        self.activacion_cambiode_comercializador_sin_cambios = ActivacionCambiodeComercializadorSinCambios()
        super(MensajeActivacionCambiodeComercializadorSinCambios, self).__init__('MensajeActivacionCambiodeComercializadorSinCambios', 'mensaje')


class ActivacionCambiodeComercializadorSinCambios(XmlModel):

    _sort_order = ('activacion_cambiode_comercializador_sin_cambios', 'datos_activacion', 'contrato', 'puntos_de_medida')

    def __init__(self):
        self.activacion_cambiode_comercializador_sin_cambios = XmlField('ActivacionCambiodeComercializadorSinCambios')
        self.datos_activacion = DatosActivacion()
        self.contrato = Contrato()
        self.puntos_de_medida = PuntosDeMedida()
        super(ActivacionCambiodeComercializadorSinCambios, self).__init__('ActivacionCambiodeComercializadorSinCambios', 'activacion_cambiode_comercializador_sin_cambios')


class DatosActivacion(XmlModel):

    _sort_order = ('datos_activacion', 'fecha')

    def __init__(self):
        self.datos_activacion = XmlField('DatosActivacion')
        self.fecha = XmlField('Fecha')
        super(DatosActivacion, self).__init__('DatosActivacion', 'datos_activacion')


class PuntosDeMedida(XmlModel):

    _sort_order = ('puntos_de_medida', 'punto_de_medida_list')

    def __init__(self):
        self.puntos_de_medida = XmlField('PuntosDeMedida')
        self.punto_de_medida_list = []
        super(PuntosDeMedida, self).__init__('PuntosDeMedida', 'puntos_de_medida')


class PuntoDeMedida(XmlModel):

    _sort_order = ('punto_de_medida', 'cod_pm', 'tipo_movimiento', 'tipo_pm', 'cod_pm_principal', 'modo_lectura', 'funcion', 'direccion_enlace', 'direccion_punto_medida', 'num_linea', 'telefono_telemedida', 'estado_telefono', 'clave_acceso', 'tension_pm', 'fecha_vigor', 'fecha_alta', 'fecha_baja', 'aparatos', 'comentarios')

    def __init__(self):
        self.punto_de_medida = XmlField('PuntoDeMedida')
        self.cod_pm = XmlField('CodPM')
        self.tipo_movimiento = XmlField('TipoMovimiento')
        self.tipo_pm = XmlField('TipoPM')
        self.cod_pm_principal = XmlField('CodPMPrincipal')
        self.modo_lectura = XmlField('ModoLectura')
        self.funcion = XmlField('Funcion')
        self.direccion_enlace = XmlField('DireccionEnlace')
        self.direccion_punto_medida = XmlField('DireccionPuntoMedida')
        self.num_linea = XmlField('NumLinea')
        self.telefono_telemedida = XmlField('TelefonoTelemedida')
        self.estado_telefono = XmlField('EstadoTelefono')
        self.clave_acceso = XmlField('ClaveAcceso')
        self.tension_pm = XmlField('TensionPM')
        self.fecha_vigor = XmlField('FechaVigor')
        self.fecha_alta = XmlField('FechaAlta')
        self.fecha_baja = XmlField('FechaBaja')
        self.aparatos = Aparatos()
        self.comentarios = XmlField('Comentarios')
        super(PuntoDeMedida, self).__init__('PuntoDeMedida', 'punto_de_medida')


class Aparatos(XmlModel):

    _sort_order = ('aparatos', 'aparato_list')

    def __init__(self):
        self.aparatos = XmlField('Aparatos')
        self.aparato_list = []
        super(Aparatos, self).__init__('Aparatos', 'aparatos')


class Aparato(XmlModel):

    _sort_order = ('aparato', 'modelo_aparato', 'tipo_movimiento', 'tipo_equipo_medida', 'tipo_propiedad_aparato', 'propietario', 'tipo_dhedm', 'modo_medida_potencia', 'lectura_directa', 'cod_precinto', 'datos_aparato', 'medidas')

    def __init__(self):
        self.aparato = XmlField('Aparato')
        self.modelo_aparato = ModeloAparato()
        self.tipo_movimiento = XmlField('TipoMovimiento')
        self.tipo_equipo_medida = XmlField('TipoEquipoMedida')
        self.tipo_propiedad_aparato = XmlField('TipoPropiedadAparato')
        self.propietario = XmlField('Propietario')
        self.tipo_dhedm = XmlField('TipoDHEdM')
        self.modo_medida_potencia = XmlField('ModoMedidaPotencia')
        self.lectura_directa = XmlField('LecturaDirecta')
        self.cod_precinto = XmlField('CodPrecinto')
        self.datos_aparato = DatosAparato()
        self.medidas = Medidas()
        super(Aparato, self).__init__('Aparato', 'aparato')


class ModeloAparato(XmlModel):

    _sort_order = ('modelo_aparato', 'tipo_aparato', 'marca_aparato', 'modelo_marca')

    def __init__(self):
        self.modelo_aparato = XmlField('ModeloAparato')
        self.tipo_aparato = XmlField('TipoAparato')
        self.marca_aparato = XmlField('MarcaAparato')
        self.modelo_marca = XmlField('ModeloMarca')
        super(ModeloAparato, self).__init__('ModeloAparato', 'modelo_aparato')


class DatosAparato(XmlModel):

    _sort_order = ('datos_aparato', 'periodo_fabricacion', 'numero_serie', 'funcion_aparato', 'num_integradores', 'constante_energia', 'constante_maximetro', 'ruedas_enteras', 'ruedas_decimales')

    def __init__(self):
        self.datos_aparato = XmlField('DatosAparato')
        self.periodo_fabricacion = XmlField('PeriodoFabricacion')
        self.numero_serie = XmlField('NumeroSerie')
        self.funcion_aparato = XmlField('FuncionAparato')
        self.num_integradores = XmlField('NumIntegradores')
        self.constante_energia = XmlField('ConstanteEnergia')
        self.constante_maximetro = XmlField('ConstanteMaximetro')
        self.ruedas_enteras = XmlField('RuedasEnteras')
        self.ruedas_decimales = XmlField('RuedasDecimales')
        super(DatosAparato, self).__init__('DatosAparato', 'datos_aparato')


class Medidas(XmlModel):

    _sort_order = ('medidas', 'medida_list')

    def __init__(self):
        self.medidas = XmlField('Medidas')
        self.medida_list = []
        super(Medidas, self).__init__('Medidas', 'medidas')


class Medida(XmlModel):

    _sort_order = ('medida', 'tipo_dhedm', 'periodo', 'magnitud_medida', 'procedencia', 'ultima_lectura_firme', 'fecha_lectura_firme', 'anomalia', 'comentarios')

    def __init__(self):
        self.medida = XmlField('Medida')
        self.tipo_dhedm = XmlField('TipoDHEdM')
        self.periodo = XmlField('Periodo')
        self.magnitud_medida = XmlField('MagnitudMedida')
        self.procedencia = XmlField('Procedencia')
        self.ultima_lectura_firme = XmlField('UltimaLecturaFirme')
        self.fecha_lectura_firme = XmlField('FechaLecturaFirme')
        self.anomalia = XmlField('Anomalia')
        self.comentarios = XmlField('Comentarios')
        super(Medida, self).__init__('Medida', 'medida')


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


class DatosNotificacion(XmlModel):

    _sort_order = ('datos_notificacion', 'fecha_activacion')

    def __init__(self):
        self.datos_notificacion = XmlField('DatosNotificacion')
        self.fecha_activacion = XmlField('FechaActivacion')
        super(DatosNotificacion, self).__init__('DatosNotificacion', 'datos_notificacion')


# Paso 08
class MensajeAnulacionSolicitud(XmlModel):

    _sort_order = ('mensaje', 'cabecera')

    def __init__(self):
        self.mensaje = XmlField('MensajeAnulacionSolicitud',
                                attributes={'xmlns': 'http://localhost/elegibilidad'})
        self.cabecera = Cabecera()
        super(MensajeAnulacionSolicitud, self).__init__('MensajeAnulacionSolicitud', 'mensaje')


# Paso 09, 10
class MensajeAceptacionAnulacion(XmlModel):

    _sort_order = ('mensaje', 'cabecera', 'aceptacion_anulacion')

    def __init__(self):
        self.mensaje = XmlField('MensajeAceptacionAnulacion',
                                attributes={'xmlns': 'http://localhost/elegibilidad'})
        self.cabecera = Cabecera()
        self.aceptacion_anulacion = AceptacionAnulacion()
        super(MensajeAceptacionAnulacion, self).__init__('MensajeAceptacionAnulacion', 'mensaje')


class AceptacionAnulacion(XmlModel):

    _sort_order = ('aceptacion_anulacion', 'fecha_aceptacion')

    def __init__(self):
        self.aceptacion_anulacion = XmlField('AceptacionAnulacion')
        self.fecha_aceptacion = XmlField('FechaAceptacion')
        super(AceptacionAnulacion, self).__init__('AceptacionAnulacion', 'aceptacion_anulacion')


# Paso 11
class MensajeAceptacionCambiodeComercializadorSaliente(XmlModel):

    _sort_order = ('mensaje', 'cabecera', 'aceptacion_cambio_comercializador_saliente')

    def __init__(self):
        self.mensaje = XmlField('MensajeAceptacionCambiodeComercializadorSaliente',
                                attributes={'xmlns': 'http://localhost/elegibilidad'})
        self.cabecera = Cabecera()
        self.aceptacion_cambio_comercializador_saliente = AceptacionCambioComercializadorSaliente()
        super(MensajeAceptacionCambiodeComercializadorSaliente, self).__init__('MensajeAceptacionCambiodeComercializadorSaliente', 'mensaje')


class AceptacionCambioComercializadorSaliente(XmlModel):

    _sort_order = ('aceptacion_cambio_comercializador_saliente', 'fecha_activacion_prevista')

    def __init__(self):
        self.aceptacion_cambio_comercializador_saliente = XmlField('AceptacionCambioComercializadorSaliente')
        self.fecha_activacion_prevista = XmlField('FechaActivacionPrevista')
        super(AceptacionCambioComercializadorSaliente, self).__init__('AceptacionCambioComercializadorSaliente', 'aceptacion_cambio_comercializador_saliente')


# Paso 12
class MensajeRechazoCambiodeComercializadorSaliente(XmlModel):

    _sort_order = ('mensaje', 'cabecera', 'rechazo_cambio_comercializador_saliente')

    def __init__(self):
        self.mensaje = XmlField('MensajeRechazoCambiodeComercializadorSaliente',
                                attributes={'xmlns': 'http://localhost/elegibilidad'})
        self.cabecera = Cabecera()
        self.rechazo_cambio_comercializador_saliente = RechazoCambioComercializadorSaliente()
        super(MensajeRechazoCambiodeComercializadorSaliente, self).__init__('MensajeRechazoCambiodeComercializadorSaliente', 'mensaje')


class RechazoCambioComercializadorSaliente(XmlModel):

    _sort_order = ('rechazo_cambio_comercializador_saliente', 'fecha_rechazo')

    def __init__(self):
        self.rechazo_cambio_comercializador_saliente = XmlField('RechazoCambioComercializadorSaliente')
        self.fecha_rechazo = XmlField('FechaRechazo')
        super(RechazoCambioComercializadorSaliente, self).__init__('RechazoCambioComercializadorSaliente', 'rechazo_cambio_comercializador_saliente')
