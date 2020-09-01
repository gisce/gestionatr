# -*- coding: utf-8 -*-
from libcomxml.core import XmlModel, XmlField
from gestionatr.output.messages.base import Cabecera


# Paso 01
class MensajeSolicitudInformacionAlRegistroDePS(XmlModel):

    _sort_order = ('mensaje', 'cabecera', 'validacion_cliente')

    def __init__(self):
        self.mensaje = XmlField('MensajeSolicitudInformacionAlRegistroDePS',
                                attributes={'xmlns': 'http://localhost/elegibilidad'})
        self.cabecera = Cabecera()
        self.validacion_cliente = ValidacionCliente()
        super(MensajeSolicitudInformacionAlRegistroDePS, self) \
            .__init__('MensajeSolicitudInformacionAlRegistroDePS', 'mensaje')


class ValidacionCliente(XmlModel):

    _sort_order = ('validacion_cliente', 'tipo_identificador', 'identificador')

    def __init__(self):
        self.validacion_cliente = XmlField('ValidacionCliente')
        self.tipo_identificador = XmlField('TipoIdentificador')
        self.identificador = XmlField('Identificador')
        super(ValidacionCliente, self).__init__('ValidacionCliente', 'validacion_cliente')


# Paso 02 accept
class MensajeEnvioInformacionPS(XmlModel):

    _sort_order = ('mensaje', 'cabecera', 'envio_informacion_ps')

    def __init__(self):
        self.mensaje = XmlField('MensajeEnvioInformacionPS', attributes={'xmlns': 'http://localhost/elegibilidad'})
        self.cabecera = Cabecera()
        self.envio_informacion_ps = EnvioInformacionPS()
        super(MensajeEnvioInformacionPS, self).__init__('MensajeEnvioInformacionPS', 'mensaje')


class EnvioInformacionPS(XmlModel):

    _sort_order = ('envio_informacion_ps', 'resultado_validacion_cliente', 'en_vigor', 'estado_contratable',
                   'existe_solicitud_en_curso', 'tipo_solicitud_en_curso', 'contrato', 'potencia_maxima_autorizada',
                   'tension_del_suministro', 'derechos_reconocidos', 'caracteristicas_pm', 'historia', 'equipo_list',
                   'doc_tecnica', 'expediente_anomalia_fraude', 'expediente_acometida')

    def __init__(self):
        self.envio_informacion_ps = XmlField('EnvioInformacionPS')
        self.resultado_validacion_cliente = XmlField('ResultadoValidacionCliente')
        self.en_vigor = XmlField('EnVigor')
        self.estado_contratable = EstadoContratable()
        self.existe_solicitud_en_curso = XmlField('ExisteSolicitudEnCurso')
        self.tipo_solicitud_en_curso = XmlField('TipoSolicitudEnCurso')
        self.contrato = Contrato()
        self.potencia_maxima_autorizada = XmlField('PotenciaMaxAutorizada')
        self.tension_del_suministro = XmlField('TensionDelSuministro')
        self.derechos_reconocidos = DerechosReconocidos()
        self.caracteristicas_pm = CaracteristicasPM()
        self.historia = Historia()
        self.equipo_list = []
        self.doc_tecnica = DocTecnica()
        self.expediente_anomalia_fraude = ExpedienteAnomaliaFraude()
        self.expediente_acometida = ExpedienteAcometida()

        super(EnvioInformacionPS, self).__init__('EnvioInformacionPS', 'envio_informacion_ps')


class EstadoContratable(XmlModel):

    _sort_order = ('estado_contratable', 'contratable', 'motivo')

    def __init__(self):
        self.estado_contratable = XmlField('EstadoContratable')
        self.contratable = XmlField('Contratable')
        self.motivo = XmlField('Motivo')
        super(EstadoContratable, self).__init__('EstadoContratable', 'estado_contratable')


class Contrato(XmlModel):

    _sort_order = ('contrato', 'tipo_contrato_atr', 'fecha_finalizacion', 'tipo_autoconsumo',
                   'fecha_ultimo_movimiento_tipo_autocons', 'ind_bono_social', 'ind_esencial', 'vivienda_habitual',
                   'cnae', 'condiciones_contractuales', 'modo_facturacion_potencia', 'no_interrumpible',
                   'potencia_no_interrumpible', 'potencia_max_sin_expediente', 'vas_trafo', 'periodicidad_facturacion',
                   'tipo_de_telegestion', 'icp_activado_telegestion', 'peaje_directo', 'deposito_garantia')

    def __init__(self):
        self.contrato = XmlField('Contrato')
        self.tipo_contrato_atr = XmlField('TipoContratoATR')
        self.fecha_finalizacion = XmlField('FechaFinalizacion')
        self.tipo_autoconsumo = XmlField('TipoAutoconsumo')
        self.fecha_ultimo_movimiento_tipo_autocons = XmlField('FechaUltimoMovimientoTipoAutocons')
        self.ind_bono_social = XmlField('IndBonoSocial')
        self.ind_esencial = XmlField('IndEsencial')
        self.vivienda_habitual = XmlField('ViviendaHabitual')
        self.cnae = XmlField('CNAE')
        self.condiciones_contractuales = CondicionesContractuales()
        self.modo_facturacion_potencia = XmlField('ModoFacturacionPotencia')
        self.no_interrumpible = XmlField('NoInterrumpible')
        self.potencia_no_interrumpible = XmlField('PotenciaNoInterrumpible')
        self.potencia_max_sin_expediente = XmlField('PotenciaMaxSinExpediente')
        self.vas_trafo = XmlField('VAsTrafo')
        self.periodicidad_facturacion = XmlField('PeriodicidadFacturacion')
        self.tipo_de_telegestion = XmlField('TipodeTelegestion')
        self.icp_activado_telegestion = XmlField('ICPActivadoTelegestion')
        self.peaje_directo = XmlField('PeajeDirecto')
        self.deposito_garantia = XmlField('DepositoGarantia')
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
    _sort_order = ('potencies', 'p1', 'p2', 'p3', 'p4', 'p5', 'p6')

    def __init__(self):
        self.potencies = XmlField('PotenciasContratadas')
        self.p1 = XmlField('Potencia', attributes={'Periodo': '1'}, rep=lambda x: '%d' % x)
        self.p2 = XmlField('Potencia', attributes={'Periodo': '2'})
        self.p3 = XmlField('Potencia', attributes={'Periodo': '3'})
        self.p4 = XmlField('Potencia', attributes={'Periodo': '4'})
        self.p5 = XmlField('Potencia', attributes={'Periodo': '5'})
        self.p6 = XmlField('Potencia', attributes={'Periodo': '6'})
        super(PotenciasContratadas, self).__init__('PotenciasContratadas', 'potencies')


class DerechosReconocidos(XmlModel):

    _sort_order = ('derechos_reconocidos', 'derecho_acceso', 'derechos_extension', 'fecha_limite_derechos_extension')

    def __init__(self):
        self.derechos_reconocidos = XmlField('DerechosReconocidos')
        self.derecho_acceso = XmlField('DerechoAcceso')
        self.derechos_extension = XmlField('DerechosExtension')
        self.fecha_limite_derechos_extension = XmlField('FechaLimiteDerechosExtension')
        super(DerechosReconocidos, self).__init__('DerechosReconocidos', 'derechos_reconocidos')


class CaracteristicasPM(XmlModel):

    _sort_order = ('caracteristicas_pm', 'tipo_pm', 'tension_pm', 'relacion_transformacion_intensidad')

    def __init__(self):
        self.caracteristicas_pm = XmlField('CaracteristicasPM')
        self.tipo_pm = XmlField('TipoPM')
        self.tension_pm = XmlField('TensionPM')
        self.relacion_transformacion_intensidad = XmlField('RelacionTransformacionIntensidad')
        super(CaracteristicasPM, self).__init__('CaracteristicasPM', 'caracteristicas_pm')


class Historia(XmlModel):

    _sort_order = ('historia', 'fecha_ultimo_movimiento_contratacion', 'fecha_cambio_comercializador',
                   'fecha_ultima_lectura', 'fecha_ultima_verificacion', 'resultado_ultima_lectura')

    def __init__(self):
        self.historia = XmlField('Historia')
        self.fecha_ultimo_movimiento_contratacion = XmlField('FechaUltimoMovimientoContratacion')
        self.fecha_cambio_comercializador = XmlField('FechaCambioComercializador')
        self.fecha_ultima_lectura = XmlField('FechaUltimaLectura')
        self.fecha_ultima_verificacion = XmlField('FechaUltimaVerificacion')
        self.resultado_ultima_lectura = XmlField('ResultadoUltimaVerificacion')
        super(Historia, self).__init__('Historia', 'historia')


class Equipo(XmlModel):

    _sort_order = ('equipo', 'tipo_aparato', 'tipo_equipo', 'tipo_propiedad',
                   'codigo_fases_equipo_medida', 'tipo_dh_edm')

    def __init__(self):
        self.equipo = XmlField('Equipo')
        self.tipo_aparato = XmlField('TipoAparato')
        self.tipo_equipo = XmlField('TipoEquipo')
        self.tipo_propiedad = XmlField('TipoPropiedad')
        self.codigo_fases_equipo_medida = XmlField('CodigoFasesEquipoMedida')
        self.tipo_dh_edm = XmlField('TipoDHEdM')
        super(Equipo, self).__init__('Equipo', 'equipo')


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

    _sort_order = ('cie_papel', 'codigo_cie', 'fecha_emision_cie', 'fecha_caducidad_cie',
                   'tension_suministro_cie', 'tipo_suministro')

    def __init__(self):
        self.cie_papel = XmlField('CIEPapel')
        self.codigo_cie = XmlField('CodigoCie')
        self.fecha_emision_cie = XmlField('FechaEmisionCie')
        self.fecha_caducidad_cie = XmlField('FechaCaducidadCie')
        self.tension_suministro_cie = XmlField('TensionSuministroCIE')
        self.tipo_suministro = XmlField('TipoSuministro')
        super(CIEPapel, self).__init__('CIEPapel', 'cie_papel')


class CIEElectronico(XmlModel):
    _sort_order = ('cie_electronico', 'cie_papel', 'cie_electronico', 'validez_cie')

    def __init__(self):
        self.cie_electronico = XmlField('CIEElectronico')
        self.codigo_cie = XmlField('CodigoCie')
        self.sello_electronico = XmlField('SelloElectronico')
        super(CIEElectronico, self).__init__('CIEElectronico', 'cie_electronico')


class DatosAPM(XmlModel):

    _sort_order = ('datos_apm', 'codigo_apm', 'potencia_inst_at', 'fecha_emision_apm', 'fecha_caducidad_apm')

    def __init__(self):
        self.datos_apm = XmlField('DatosAPM')
        self.codigo_apm = XmlField('CodigoApm')
        self.potencia_inst_at = XmlField('PotenciaInstAT')
        self.fecha_emision_apm = XmlField('FechaEmisionApm')
        self.fecha_caducidad_apm = XmlField('FechaCaducidadApm')
        super(DatosAPM, self).__init__('DatosAPM', 'datos_apm')


class ExpedienteAnomaliaFraude(XmlModel):

    _sort_order = ('expediente_anomalia_fraude', 'expediente_abierto', 'codigo_motivo_expediente')

    def __init__(self):
        self.expediente_anomalia_fraude = XmlField('ExpedienteAnomaliaFraude')
        self.expediente_abierto = XmlField('ExpedienteAbierto')
        self.codigo_motivo_expediente = XmlField('CdigoMotivoExpediente')
        super(ExpedienteAnomaliaFraude, self).__init__('ExpedienteAnomaliaFraude', 'expediente_anomalia_fraude')


class ExpedienteAcometida(XmlModel):

    _sort_order = ('expediente_acometida', 'expediente_abierto', 'codigo_motivo_expediente')

    def __init__(self):
        self.expediente_acometida = XmlField('ExpedienteAcometida')
        self.expediente_abierto = XmlField('ExpedienteAbierto')
        self.codigo_motivo_expediente = XmlField('CdigoMotivoExpediente')
        super(ExpedienteAcometida, self).__init__('ExpedienteAcometida', 'expediente_acometida')


# Paso 02 (Rechazo)
class MensajeRechazo(XmlModel):

    _sort_order = ('mensaje_rechazo', 'cabecera', 'rechazos_peticion')

    def __init__(self):
        self.mensaje_rechazo = XmlField('MensajeRechazoP0',
                                        attributes={'xmlns': 'http://localhost/elegibilidad'})
        self.cabecera = Cabecera()
        self.rechazos_peticion = RechazosPeticion()
        super(MensajeRechazo, self).__init__('MensajeRechazoP0', 'mensaje_rechazo')


class RechazosPeticion(XmlModel):

    _sort_order = ('rechazos_peticion', 'fecha_rechazo', 'rechazo')

    def __init__(self):
        self.rechazos_peticion = XmlField('RechazosPeticion')
        self.fecha_rechazo = XmlField('FechaRechazo')
        self.rechazo = Rechazo()
        super(RechazosPeticion, self).__init__('RechazosPeticion', 'rechazos_peticion')


class Rechazo(XmlModel):

    _sort_order = ('rechazo', 'secuencial', 'codigo_motivo', 'comentarios')

    def __init__(self):
        self.rechazo = XmlField('Rechazo')
        self.secuencial = XmlField('Secuencial')
        self.codigo_motivo = XmlField('CodigoMotivo')
        self.comentarios = XmlField('Comentarios')
        super(Rechazo, self).__init__('Rechazo', 'rechazo')
