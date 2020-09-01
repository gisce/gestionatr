# -*- coding: utf-8 -*-
from gestionatr.input.messages.C1 import Rechazo
from message import Message
from Deadlines import ProcessDeadline
from gestionatr.utils import get_rec_attr


class P0(Message, ProcessDeadline):
    """Clase que implementa P0."""

    # Datos paso 01
    @property
    def tipo_identificador(self):
        tree = '{0}.TipoIdentificador'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data:
            return data.text
        else:
            return False

    @property
    def identificador(self):
        tree = '{0}.Identificador'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data:
            return data.text
        else:
            return False

    # Datos paso 02 aceptacion
    @property
    def resultado_validacion_cliente(self):
        tree = '{0}.ResultadoValidacionCliente'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data:
            return data.text
        else:
            return False

    @property
    def en_vigor(self):
        tree = '{0}.EnVigor'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data:
            return data.text
        else:
            return False

    @property
    def estado_contratable(self):
        tree = '{0}.EstadoContratable'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data not in [None, False]:
            return EstadoContratable(data)
        else:
            return False

    @property
    def existe_solicitud_en_curso(self):
        tree = '{0}.ExisteSolicitudEnCurso'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data:
            return data.text
        else:
            return False

    @property
    def tipo_solicitud_en_curso(self):
        tree = '{0}.TipoSolicitudEnCurso'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data:
            return data.text
        else:
            return False

    @property
    def contrato(self):
        tree = '{0}.Contrato'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data not in [None, False]:
            return Contrato(data)
        else:
            return False

    @property
    def potencia_maxima_autorizada(self):
        tree = '{0}.PotenciaMaxAutorizada'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data:
            return data.text
        else:
            return False

    @property
    def tension_del_suministro(self):
        tree = '{0}.TensionDelSuministro'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data:
            return data.text
        else:
            return False

    @property
    def derechos_reconocidos(self):
        tree = '{0}.DerechosReconocidos'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data not in [None, False]:
            return DerechosReconocidos(data)
        else:
            return False

    @property
    def caracteristicas_pm(self):
        tree = '{0}.CaracteristicasPM'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data not in [None, False]:
            return CaracteristicasPM(data)
        else:
            return False

    @property
    def historia(self):
        tree = '{0}.Historia'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data not in [None, False]:
            return Historia(data)
        else:
            return False

    @property
    def equipo(self):
        data = []
        tree = get_rec_attr(self.obj, self._header, False)
        if hasattr(tree, 'Equipo'):
            for datos in tree.Equipo:
                data.append(Equipo(datos))
            return data
        else:
            return False

    @property
    def doc_tecnica(self):
        tree = '{0}.DocTecnica'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data not in [None, False]:
            return DocTecnica(data)
        else:
            return False

    @property
    def expediente_anomalia_fraude(self):
        tree = '{0}.ExpedienteAnomaliaFraude'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data not in [None, False]:
            return ExpedienteAnomaliaFraude(data)
        else:
            return False

    @property
    def expediente_acometida(self):
        tree = '{0}.ExpedienteAcometida'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data not in [None, False]:
            return ExpedienteAcometida(data)
        else:
            return False

    # Datos paso 02 rechazo
    @property
    def fecha_rechazo(self):
        tree = '{0}.FechaRechazo'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data:
            return data.text
        else:
            return False

    @property
    def rechazo(self):
        data = []
        tree = get_rec_attr(self.obj, self._header, False)
        if hasattr(tree, 'Rechazo'):
            for datos in tree.Rechazo:
                data.append(Rechazo(datos))
            return data
        else:
            return False


class EstadoContratable(object):

    def __init__(self, data):
        self.estado_contratable = data

    @property
    def contratable(self):
        data = ''
        try:
            data = self.estado_contratable.Contratable.text
        except AttributeError:
            pass
        return data

    @property
    def motivo(self):
        data = ''
        try:
            data = self.estado_contratable.Motivo.text
        except AttributeError:
            pass
        return data


class Contrato(object):

    def __init__(self, data):
        self.contrato = data

    @property
    def tipo_contrato_atr(self):
        data = ''
        try:
            data = self.contrato.TipoContratoATR.text
        except AttributeError:
            pass
        return data

    @property
    def fecha_finalizacion(self):
        data = ''
        try:
            data = self.contrato.FechaFinalizacion.text
        except AttributeError:
            pass
        return data

    @property
    def tipo_autoconsumo(self):
        data = ''
        try:
            data = self.contrato.TipoAutoconsumo.text
        except AttributeError:
            pass
        return data

    @property
    def fecha_ultimo_movimiento_tipo_autocons(self):
        data = ''
        try:
            data = self.contrato.FechaUltimoMovimientoTipoAutocons.text
        except AttributeError:
            pass
        return data

    @property
    def ind_bono_social(self):
        data = ''
        try:
            data = self.contrato.IndBonoSocial.text
        except AttributeError:
            pass
        return data

    @property
    def ind_esencial(self):
        data = ''
        try:
            data = self.contrato.IndEsencial.text
        except AttributeError:
            pass
        return data

    @property
    def vivienda_habitual(self):
        data = ''
        try:
            data = self.contrato.ViviendaHabitual.text
        except AttributeError:
            pass
        return data

    @property
    def cnae(self):
        data = ''
        try:
            data = self.contrato.CNAE.text
        except AttributeError:
            pass
        return data

    @property
    def condiciones_contractuales(self):
        data = ''
        try:
            data = CondicionesContractuales(self.contrato.CondicionesContractuales)
        except AttributeError:
            pass
        return data

    @property
    def modo_facturacion_potencia(self):
        data = ''
        try:
            data = self.contrato.ModoFacturacionPotencia.text
        except AttributeError:
            pass
        return data

    @property
    def no_interrumpible(self):
        data = ''
        try:
            data = self.contrato.NoInterrumpible.text
        except AttributeError:
            pass
        return data

    @property
    def potencia_no_interrumpible(self):
        data = ''
        try:
            data = self.contrato.PotenciaNoInterrumpible.text
        except AttributeError:
            pass
        return data

    @property
    def potencia_max_sin_expediente(self):
        data = ''
        try:
            data = self.contrato.PotenciaMaxSinExpediente.text
        except AttributeError:
            pass
        return data

    @property
    def vas_trafo(self):
        data = ''
        try:
            data = self.contrato.VAsTrafo.text
        except AttributeError:
            pass
        return data

    @property
    def periodicidad_facturacion(self):
        data = ''
        try:
            data = self.contrato.PeriodicidadFacturacion.text
        except AttributeError:
            pass
        return data

    @property
    def tipo_de_telegestion(self):
        data = ''
        try:
            data = self.contrato.TipodeTelegestion.text
        except AttributeError:
            pass
        return data

    @property
    def icp_activado_telegestion(self):
        data = ''
        try:
            data = self.contrato.ICPActivadoTelegestion.text
        except AttributeError:
            pass
        return data

    @property
    def peaje_directo(self):
        data = ''
        try:
            data = self.contrato.PeajeDirecto.text
        except AttributeError:
            pass
        return data

    @property
    def deposito_garantia(self):
        data = ''
        try:
            data = self.contrato.DepositoGarantia.text
        except AttributeError:
            pass
        return data


class CondicionesContractuales(object):

    def __init__(self, data):
        self.condiciones_contractuales = data

    @property
    def tarifa_atr(self):
        data = ''
        try:
            data = self.condiciones_contractuales.TarifaATR.text
        except AttributeError:
            pass
        return data

    @property
    def potencias_contratadas(self):
        data = []
        obj = self.condiciones_contractuales
        if (hasattr(obj, 'PotenciasContratadas') and
                hasattr(obj.PotenciasContratadas, 'Potencia')):
            for d in obj.PotenciasContratadas.Potencia:
                data.append((int(d.get('Periodo')), int(d.text)))
        return data

    @property
    def modo_control_potencia(self):
        data = ''
        try:
            data = self.condiciones_contractuales.ModoControlPotencia.text
        except AttributeError:
            pass
        return data


class DerechosReconocidos(object):

    def __init__(self, data):
        self.derechos_reconocidos = data

    @property
    def derecho_acceso(self):
        data = ''
        try:
            data = self.derechos_reconocidos.DerechoAcceso.text
        except AttributeError:
            pass
        return data

    @property
    def derecho_extension(self):
        data = ''
        try:
            data = self.derechos_reconocidos.DerechosExtension.text
        except AttributeError:
            pass
        return data

    @property
    def fecha_limite_derechos_extension(self):
        data = ''
        try:
            data = self.derechos_reconocidos.FechaLimiteDerechosExtension.text
        except AttributeError:
            pass
        return data


class CaracteristicasPM(object):

    def __init__(self, data):
        self.caracteristicas_pm = data

    @property
    def tipo_pm(self):
        data = ''
        try:
            data = self.caracteristicas_pm.TipoPM.text
        except AttributeError:
            pass
        return data

    @property
    def tension_pm(self):
        data = ''
        try:
            data = self.caracteristicas_pm.TensionPM.text
        except AttributeError:
            pass
        return data

    @property
    def relacion_transformacion_intensidad(self):
        data = ''
        try:
            data = self.caracteristicas_pm.RelacionTransformacionIntensidad.text
        except AttributeError:
            pass
        return data


class Historia(object):

    def __init__(self, data):
        self.historia = data

    @property
    def fecha_ultimo_movimiento_contratacion(self):
        data = ''
        try:
            data = self.historia.FechaUltimoMovimientoContratacion.text
        except AttributeError:
            pass
        return data

    @property
    def fecha_cambio_comercializador(self):
        data = ''
        try:
            data = self.historia.FechaCambioComercializador.text
        except AttributeError:
            pass
        return data

    @property
    def fecha_ultima_lectura(self):
        data = ''
        try:
            data = self.historia.FechaUltimaLectura.text
        except AttributeError:
            pass
        return data

    @property
    def fecha_ultima_verificacion(self):
        data = ''
        try:
            data = self.historia.FechaUltimaVerificacion.text
        except AttributeError:
            pass
        return data

    @property
    def resultado_ultima_lectura(self):
        data = ''
        try:
            data = self.historia.ResultadoUltimaVerificacion.text
        except AttributeError:
            pass
        return data


class Equipo(object):

    def __init__(self, data):
        self.equipo = data

    @property
    def tipo_aparato(self):
        data = ''
        try:
            data = self.equipo.TipoAparato.text
        except AttributeError:
            pass
        return data

    @property
    def tipo_equipo(self):
        data = ''
        try:
            data = self.equipo.TipoEquipo.text
        except AttributeError:
            pass
        return data

    @property
    def tipo_propiedad(self):
        data = ''
        try:
            data = self.equipo.TipoPropiedad.text
        except AttributeError:
            pass
        return data

    @property
    def codigo_fases_equipo_medida(self):
        data = ''
        try:
            data = self.equipo.CodigoFasesEquipoMedida.text
        except AttributeError:
            pass
        return data

    @property
    def tipo_dh_edm(self):
        data = ''
        try:
            data = self.equipo.TipoDHEdM.text
        except AttributeError:
            pass
        return data


class DocTecnica(object):

    def __init__(self, data):
        self.doc_tecnica = data

    @property
    def datos_cie(self):
        data = ''
        try:
            data = DatosCie(self.doc_tecnica.DatosCie)
        except AttributeError:
            pass
        return data

    @property
    def datos_apm(self):
        data = ''
        try:
            data = DatosAPM(self.doc_tecnica.DatosAPM)
        except AttributeError:
            pass
        return data


class DatosCie(object):

    def __init__(self, data):
        self.datos_cie = data

    @property
    def cie_papel(self):
        data = ''
        try:
            data = CIEPapel(self.datos_cie.CIEPapel)
        except AttributeError:
            pass
        return data

    @property
    def cie_electronico(self):
        data = ''
        try:
            data = CIEElectronico(self.datos_cie.CIEElectronico)
        except AttributeError:
            pass
        return data

    @property
    def validez_cie(self):
        data = ''
        try:
            data = self.datos_cie.ValidezCIE.text
        except AttributeError:
            pass
        return data


class CIEPapel(object):

    def __init__(self, data):
        self.cie_papel = data

    @property
    def codigo_cie(self):
        data = ''
        try:
            data = self.cie_papel.CodigoCie.text
        except AttributeError:
            pass
        return data

    @property
    def fecha_emision_cie(self):
        data = ''
        try:
            data = self.cie_papel.FechaEmisionCie.text
        except AttributeError:
            pass
        return data

    @property
    def fecha_caducidad_cie(self):
        data = ''
        try:
            data = self.cie_papel.FechaCaducidadCie.text
        except AttributeError:
            pass
        return data

    @property
    def tension_suministro_cie(self):
        data = ''
        try:
            data = self.cie_papel.TensionSuministroCIE.text
        except AttributeError:
            pass
        return data

    @property
    def tipo_suministro(self):
        data = ''
        try:
            data = self.cie_papel.TipoSuministro.text
        except AttributeError:
            pass
        return data


class CIEElectronico(object):

    def __init__(self, data):
        self.cie_electronico = data

    @property
    def codigo_cie(self):
        data = ''
        try:
            data = self.cie_electronico.CodigoCie.text
        except AttributeError:
            pass
        return data

    @property
    def sello_electronico(self):
        data = ''
        try:
            data = self.cie_electronico.SelloElectronico.text
        except AttributeError:
            pass
        return data


class DatosAPM(object):

    def __init__(self, data):
        self.datos_apm = data

    @property
    def codigo_apm(self):
        data = ''
        try:
            data = self.datos_apm.CodigoApm.text
        except AttributeError:
            pass
        return data

    @property
    def potencia_inst_at(self):
        data = ''
        try:
            data = self.datos_apm.PotenciaInstAT.text
        except AttributeError:
            pass
        return data

    @property
    def fecha_emision_apm(self):
        data = ''
        try:
            data = self.datos_apm.FechaEmisionApm.text
        except AttributeError:
            pass
        return data

    @property
    def fecha_caducidad_apm(self):
        data = ''
        try:
            data = self.datos_apm.FechaCaducidadApm.text
        except AttributeError:
            pass
        return data


class ExpedienteAnomaliaFraude(object):

    def __init__(self, data):
        self.expediente_anomalia_fraude = data

    @property
    def expediente_abierto(self):
        data = ''
        try:
            data = self.expediente_anomalia_fraude.ExpedienteAbierto.text
        except AttributeError:
            pass
        return data

    @property
    def codigo_motivo_expediente(self):
        data = ''
        try:
            data = self.expediente_anomalia_fraude.CdigoMotivoExpediente.text
        except AttributeError:
            pass
        return data


class ExpedienteAcometida(object):

    def __init__(self, data):
        self.expediente_acometida = data

    @property
    def expediente_abierto(self):
        data = ''
        try:
            data = self.expediente_acometida.ExpedienteAbierto.text
        except AttributeError:
            pass
        return data

    @property
    def codigo_motivo_expediente(self):
        data = ''
        try:
            data = self.expediente_acometida.CdigoMotivoExpediente.text
        except AttributeError:
            pass
        return data


# class MinimumFieldsChecker(object):
#
#     def __init__(self, p0):
#         self.p0 = p0
#
#     def check(self):
#         errors = []
#
#         for field in self.get_minimum_fields(pas=self.p0.pas):
#             valid = getattr(self, 'check_{0}'.format(field), None)
#             if not valid():
#                 errors.append(field)
#         return errors
#
#     def get_minimum_fields(self, pas='01'):
#         if pas == '01':
#             return [
#                 'moviment', 'cau', 'seccio_registre', 'collectiu', 'cups', 'tec_generador',
#                 'pot_installada_gen', 'tipus_installacio', 'ssaa', 'nom_titular', 'tipus_identificador',
#                 'identificador', 'telefon', 'pais', 'provincia', 'municipi', 'codi_postal', 'via_or_apartat_correus'
#             ]
#         elif pas == '02':
#             return ['cau']
#         else:
#             return False
#
#     def check_moviment(self):
#         return get_rec_attr(self.a1, "movimiento", False)
#
#     def check_cau(self):
#         return get_rec_attr(self.a1, "autoconsumo.cau", False)
#
#     def check_seccio_registre(self):
#         return get_rec_attr(self.a1, "autoconsumo.seccion_registro", False)
#
#     def check_collectiu(self):
#         return get_rec_attr(self.a1, "autoconsumo.colectivo", False)
#
#     def check_cups(self):
#         valid = True
#         for datos in self.a1.datos_suministro:
#             valid = valid and get_rec_attr(datos, "cups", False)
#         return valid
#
#     def check_tec_generador(self):
#         valid = True
#         for datos in self.a1.datos_inst_gen:
#             valid = valid and get_rec_attr(datos, "tec_generador", False)
#         return valid
#
#     def check_pot_installada_gen(self):
#         valid = True
#         for datos in self.a1.datos_inst_gen:
#             valid = valid and get_rec_attr(datos, "pot_instalada_gen", False)
#         return valid
#
#     def check_tipus_installacio(self):
#         valid = True
#         for datos in self.a1.datos_inst_gen:
#             valid = valid and get_rec_attr(datos, "tipo_instalacion", False)
#         return valid
#
#     def check_ssaa(self):
#         valid = True
#         for datos in self.a1.datos_inst_gen:
#             valid = valid and get_rec_attr(datos, "ssaa", False)
#         return valid
#
#     def check_nom_titular(self):
#         valid = True
#         if self.a1.autoconsumo.seccion_registro == '2':
#             for datos in self.a1.datos_inst_gen:
#                 nom = datos.titular_representante_gen.nombre
#                 check = get_rec_attr(nom, "nombre_de_pila", False) and \
#                         get_rec_attr(nom, "primer_apellido", False) or \
#                         get_rec_attr(nom, "razon_social", False)
#                 valid = valid and check
#         return valid
#
#     def check_tipus_identificador(self):
#         valid = True
#         if self.a1.autoconsumo.seccion_registro == '2':
#             for datos in self.a1.datos_inst_gen:
#                 valid = valid and get_rec_attr(datos.titular_representante_gen.id_titular, "tipo_identificador", False)
#         return valid
#
#     def check_identificador(self):
#         valid = True
#         if self.a1.autoconsumo.seccion_registro == '2':
#             for datos in self.a1.datos_inst_gen:
#                 valid = valid and get_rec_attr(datos.titular_representante_gen.id_titular, "identificador", False)
#         return valid
#
#     def check_telefon(self):
#         valid = True
#         if self.a1.autoconsumo.seccion_registro == '2':
#             for datos in self.a1.datos_inst_gen:
#                 telefon = get_rec_attr(datos.titular_representante_gen, "telefono", False)
#                 if not telefon:
#                     return False
#                 valid = valid and len(telefon) > 0
#         return valid
#
#     def check_pais(self):
#         valid = True
#         if self.a1.autoconsumo.seccion_registro == '2':
#             for datos in self.a1.datos_inst_gen:
#                 direccio = datos.titular_representante_gen.direccion
#                 valid = valid and get_rec_attr(direccio, "pais", False)
#         return valid
#
#     def check_provincia(self):
#         valid = True
#         if self.a1.autoconsumo.seccion_registro == '2':
#             for datos in self.a1.datos_inst_gen:
#                 direccio = datos.titular_representante_gen.direccion
#                 valid = valid and get_rec_attr(direccio, "provincia", False)
#         return valid
#
#     def check_municipi(self):
#         valid = True
#         if self.a1.autoconsumo.seccion_registro == '2':
#             for datos in self.a1.datos_inst_gen:
#                 direccio = datos.titular_representante_gen.direccion
#                 valid = valid and get_rec_attr(direccio, "municipio", False)
#         return valid
#
#     def check_codi_postal(self):
#         valid = True
#         if self.a1.autoconsumo.seccion_registro == '2':
#             for datos in self.a1.datos_inst_gen:
#                 direccio = datos.titular_representante_gen.direccion
#                 valid = valid and get_rec_attr(direccio, "cod_postal", False)
#         return valid
#
#     def check_via_or_apartat_correus(self):
#         valid = True
#         if self.a1.autoconsumo.seccion_registro == '2':
#             for datos in self.a1.datos_inst_gen:
#                 direccio = datos.titular_representante_gen.direccion
#                 has_apartado_correos = get_rec_attr(direccio, "apartado_de_correos", False)
#                 has_via = get_rec_attr(direccio, "tipo_via", False) and \
#                           get_rec_attr(direccio, "calle", False) and \
#                           get_rec_attr(direccio, "numero_finca", False)
#                 valid = valid and (has_apartado_correos or has_via)
#         return valid
