# -*- coding: utf-8 -*-
from C2 import C2, Cliente, Contacto
from C1 import DatosAceptacion
from W1 import LecturaAportada
from Deadlines import DeadLine, Workdays, Naturaldays
from gestionatr.utils import get_rec_attr
from gestionatr.defs import SUBTYPES_R101

class R1(C2):
    """Clase que implementa R1."""

    steps = [
        DeadLine('01', Workdays(5), '02'),
        DeadLine('03', Naturaldays(20), '04'),
    ]

    # Datos paso 01
    @property
    def datos_solicitud(self):
        tree = '{0}.DatosSolicitud'.format(self._header)
        sol = get_rec_attr(self.obj, tree, False)
        if sol not in [None, False]:
            return DatosSolicitud(sol)
        else:
            return False

    @property
    def variables_detalle_reclamacion(self):
        tree = '{0}.VariablesDetalleReclamacion'.format(self._header)
        obj = get_rec_attr(self.obj, tree, False)
        data = []
        if obj not in [None, False]:
            for i in obj.VariableDetalleReclamacion:
                data.append(VariableDetalleReclamacion(i))
            return data
        return data

    @property
    def tipo_reclamante(self):
        tree = '{0}.TipoReclamante'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data:
            return data.text
        else:
            return False

    @property
    def reclamante(self):
        tree = '{0}.Reclamante'.format(self._header)
        cli = get_rec_attr(self.obj, tree, False)
        if cli not in [None, False]:
            return Reclamante(cli)
        else:
            return False

    # Datos paso 02 aceptacion
    @property
    def datos_aceptacion(self):
        tree = '{0}.DatosAceptacion'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data not in [None, False]:
            return DatosAceptacion(data)
        else:
            return False

    # Datos paso 03
    @property
    def datos_informacion(self):
        tree = '{0}.DatosInformacion'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data not in [None, False]:
            return DatosInformacion(data)
        else:
            return False

    @property
    def informacion_intermedia(self):
        tree = '{0}.InformacionIntermedia'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data not in [None, False]:
            return InformacionIntermedia(data)
        else:
            return False

    @property
    def retipificacion(self):
        tree = '{0}.Retipificacion'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data not in [None, False]:
            return Retipificacion(data)
        else:
            return False

    @property
    def solicitudes_informacion_adicional(self):
        data = []
        tree = '{0}.SolicitudesInformacionAdicional'.format(self._header)
        obj = get_rec_attr(self.obj, tree, False)
        if obj is not None:
            for d in obj.SolicitudInformacionAdicional:
                data.append(SolicitudInformacionAdicional(d))
        return data

    @property
    def solicitud_informacion_adicional_para_retipificacion(self):
        tree = '{0}.SolicitudesInformacionAdicional.SolicitudInformacionAdicionalparaRetipificacion'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data not in [None, False]:
            return SolicitudInformacionAdicionalparaRetipificacion(data)
        else:
            return False

    # Datos paso 04
    @property
    def datos_envio_informacion(self):
        tree = '{0}.DatosEnvioInformacion'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data not in [None, False]:
            return DatosEnvioInformacion(data)
        else:
            return False

    @property
    def variables_aportacion_informacion(self):
        data = []
        tree = '{0}.VariablesAportacionInformacion'.format(self._header)
        obj = get_rec_attr(self.obj, tree, False)
        if obj is not None:
            for d in obj.VariableAportacionInformacion:
                data.append(VariableAportacionInformacion(d))
        return data

    @property
    def variables_aportacion_informacion_para_retipificacion(self):
        data = []
        tree = '{0}.VariablesAportacionInformacionparaRetipificacion'.format(self._header)
        obj = get_rec_attr(self.obj, tree, False)
        if obj is not None:
            for d in obj.VariableAportacionInformacionparaRetipificacion:
                data.append(VariableDetalleReclamacion(d))
        return data

    # Datos paso 5
    @property
    def datos_cierre(self):
        tree = '{0}.DatosCierre'.format(self._header)
        sol = get_rec_attr(self.obj, tree, False)
        if sol not in [None, False]:
            return DatosCierre(sol)
        else:
            return False

    @property
    def cod_contrato(self):
        tree = '{0}.CodContrato'.format(self._header)
        sol = get_rec_attr(self.obj, tree, False)
        if sol:
            return sol.text
        else:
            return False

    # Campos Minimos
    def get_subtypes(self):
        r1_type = self.datos_solicitud.tipo
        return [x['code'] for x in SUBTYPES_R101 if x['type'] == r1_type]

    def get_type_from_subtype(self):
        r1_subtype = self.datos_solicitud.subtipo
        for x in SUBTYPES_R101:
            if x['code'] == r1_subtype:
                return x['type']
        return []

    def get_minimum_fields(self):
        subtype = self.datos_solicitud.subtipo
        for x in SUBTYPES_R101:
            if x['code'] == subtype:
                return x['min_fields']
        return []

    def check_minimum_fields(self):
        checker = MinimumFieldsChecker(self)
        return checker.check()


class DatosSolicitud(object):

    def __init__(self, data):
        self.datos_solicitud = data

    @property
    def tipo(self):
        data = ''
        try:
            data = self.datos_solicitud.Tipo.text
        except AttributeError:
            pass
        return data

    @property
    def subtipo(self):
        data = ''
        try:
            data = self.datos_solicitud.Subtipo.text
        except AttributeError:
            pass
        return data

    @property
    def referencia_origen(self):
        data = ''
        try:
            data = self.datos_solicitud.ReferenciaOrigen.text
        except AttributeError:
            pass
        return data

    @property
    def fecha_limite(self):
        data = False
        try:
            data = self.datos_solicitud.FechaLimite.text
        except AttributeError:
            pass
        return data

    @property
    def prioritario(self):
        data = ''
        try:
            data = self.datos_solicitud.Prioritario.text
        except AttributeError:
            pass
        return data


class Reclamante(Cliente):

    @property
    def tipo_identificador(self):
        data = ''
        try:
            data = self.cliente.IdReclamante.TipoIdentificador.text
        except AttributeError:
            pass
        return data

    @property
    def identificador(self):
        data = ''
        try:
            data = self.cliente.IdReclamante.Identificador.text
        except AttributeError:
            pass
        return data


class VariableDetalleReclamacion(object):

    def __init__(self, data):
        self.variable = data

    @property
    def num_expediente_acometida(self):
        data = ''
        try:
            data = self.variable.NumExpedienteAcometida.text
        except AttributeError:
            pass
        return data

    @property
    def num_expediente_fraude(self):
        data = ''
        try:
            data = self.variable.NumExpedienteFraude.text
        except AttributeError:
            pass
        return data

    @property
    def fecha_incidente(self):
        data = False
        try:
            data = self.variable.FechaIncidente.text
        except AttributeError:
            pass
        return data

    @property
    def num_factura_atr(self):
        data = ''
        try:
            data = self.variable.NumFacturaATR.text
        except AttributeError:
            pass
        return data

    @property
    def tipo_concepto_facturado(self):
        data = ''
        try:
            data = self.variable.TipoConceptoFacturado.text
        except AttributeError:
            pass
        return data

    @property
    def fecha_lectura(self):
        data = False
        try:
            data = self.variable.FechaLectura.text
        except AttributeError:
            pass
        return data

    @property
    def tipo_dhedm(self):
        data = ''
        try:
            data = self.variable.TipoDHEdM.text
        except AttributeError:
            pass
        return data

    @property
    def codigo_incidencia(self):
        data = ''
        try:
            data = self.variable.CodigoIncidencia.text
        except AttributeError:
            pass
        return data

    @property
    def codigo_solicitud(self):
        data = ''
        try:
            data = self.variable.CodigoSolicitud.text
        except AttributeError:
            pass
        return data

    @property
    def parametro_contratacion(self):
        data = ''
        try:
            data = self.variable.ParametroContratacion.text
        except AttributeError:
            pass
        return data

    @property
    def concepto_disconformidad(self):
        data = ''
        try:
            data = self.variable.ConceptoDisconformidad.text
        except AttributeError:
            pass
        return data

    @property
    def tipo_de_atencion_incorrecta(self):
        data = ''
        try:
            data = self.variable.TipoDeAtencionIncorrecta.text
        except AttributeError:
            pass
        return data

    @property
    def iban(self):
        data = ''
        try:
            data = self.variable.IBAN.text
        except AttributeError:
            pass
        return data

    @property
    def codigo_solicitud_reclamacion(self):
        data = ''
        try:
            data = self.variable.CodigoSolicitudReclamacion.text
        except AttributeError:
            pass
        return data

    @property
    def fecha_desde(self):
        data = False
        try:
            data = self.variable.FechaDesde.text
        except AttributeError:
            pass
        return data

    @property
    def fecha_hasta(self):
        data = False
        try:
            data = self.variable.FechaHasta.text
        except AttributeError:
            pass
        return data

    @property
    def importe_reclamado(self):
        data = ''
        try:
            data = self.variable.ImporteReclamado.text
        except AttributeError:
            pass
        return data

    @property
    def lecturas_aportadas(self):
        data = []
        obj = self.variable
        if (hasattr(obj, 'LecturasAportadas') and
                hasattr(obj.LecturasAportadas, 'LecturaAportada')):
            for d in obj.LecturasAportadas.LecturaAportada:
                data.append(LecturaAportada(d))
        return data

    @property
    def contacto(self):
        data = ''
        try:
            data = Contacto(self.variable.Contacto)
        except AttributeError:
            pass
        return data

    @property
    def ubicacion_incidencia(self):
        data = ''
        try:
            data = UbicacionIncidencia(self.variable.UbicacionIncidencia)
        except AttributeError:
            pass
        return data


class UbicacionIncidencia(object):

    def __init__(self, data):
        self.ubicacion = data

    @property
    def des_ubicacion_incidencia(self):
        data = ''
        try:
            data = self.ubicacion.DesUbicacionIncidencia.text
        except AttributeError:
            pass
        return data

    @property
    def provincia(self):
        data = ''
        try:
            data = self.ubicacion.Provincia.text
        except AttributeError:
            pass
        return data

    @property
    def municipio(self):
        data = ''
        try:
            data = self.ubicacion.Municipio.text
        except AttributeError:
            pass
        return data

    @property
    def poblacion(self):
        data = ''
        try:
            data = self.ubicacion.Poblacion.text
        except AttributeError:
            pass
        return data

    @property
    def cod_postal(self):
        data = ''
        try:
            data = self.ubicacion.CodPostal.text
        except AttributeError:
            pass
        return data


class LecturaAportada(LecturaAportada):

    @property
    def codigo_periodo_dh(self):
        data = ''
        try:
            data = self.lectura.CodigoPeriodoDH.text
        except AttributeError:
            pass
        return data


class DatosAceptacion(DatosAceptacion):

    @property
    def codigo_reclamacion_distribuidora(self):
        data = ''
        try:
            data = self.datos_aceptacion.CodigoReclamacionDistribuidora.text
        except AttributeError:
            pass
        return data


class DatosInformacion(object):

    def __init__(self, data):
        self.datos_informacion = data

    @property
    def num_expediente_acometida(self):
        data = ''
        try:
            data = self.datos_informacion.NumExpedienteAcometida.text
        except AttributeError:
            pass
        return data

    @property
    def tipo_comunicacion(self):
        data = ''
        try:
            data = self.datos_informacion.TipoComunicacion.text
        except AttributeError:
            pass
        return data

    @property
    def codigo_reclamacion_distribuidora(self):
        data = ''
        try:
            data = self.datos_informacion.CodigoReclamacionDistribuidora.text
        except AttributeError:
            pass
        return data


class InformacionIntermedia(object):

    def __init__(self, data):
        self.info_intermedia = data

    @property
    def desc_informacion_intermedia(self):
        data = ''
        try:
            data = self.info_intermedia.DescInformacionIntermedia.text
        except AttributeError:
            pass
        return data

    @property
    def intervenciones(self):
        data = ''
        try:
            data = self.info_intermedia.Intervenciones.text
        except AttributeError:
            pass
        return data

    @property
    def intervenciones(self):
        data = []
        obj = self.info_intermedia
        if (hasattr(obj, 'Intervenciones') and
                hasattr(obj.Intervenciones, 'Intervencion')):
            for d in obj.Intervenciones.Intervencion:
                data.append(Intervencion(d))
        return data


class Intervencion(object):

    def __init__(self, data):
        self.intervencion = data

    @property
    def tipo_intervencion(self):
        data = ''
        try:
            data = self.intervencion.TipoIntervencion.text
        except AttributeError:
            pass
        return data

    @property
    def fecha(self):
        data = False
        try:
            data = self.intervencion.Fecha.text
        except AttributeError:
            pass
        return data

    @property
    def hora_desde(self):
        data = ''
        try:
            data = self.intervencion.HoraDesde.text
        except AttributeError:
            pass
        return data

    @property
    def hora_hasta(self):
        data = ''
        try:
            data = self.intervencion.HoraHasta.text
        except AttributeError:
            pass
        return data

    @property
    def numero_visita(self):
        data = ''
        try:
            data = self.intervencion.NumeroVisita.text
        except AttributeError:
            pass
        return data

    @property
    def resultado(self):
        data = ''
        try:
            data = self.intervencion.Resultado.text
        except AttributeError:
            pass
        return data

    @property
    def detalle_resultado(self):
        data = ''
        try:
            data = self.intervencion.DetalleResultado.text
        except AttributeError:
            pass
        return data


class Retipificacion(object):

    def __init__(self, data):
        self.retipificacion = data

    @property
    def tipo(self):
        data = ''
        try:
            data = self.retipificacion.Tipo.text
        except AttributeError:
            pass
        return data

    @property
    def subtipo(self):
        data = ''
        try:
            data = self.retipificacion.Subtipo.text
        except AttributeError:
            pass
        return data

    @property
    def desc_retipificacion(self):
        data = ''
        try:
            data = self.retipificacion.DescRetipificacion.text
        except AttributeError:
            pass
        return data


class SolicitudInformacionAdicional(object):

    def __init__(self, data):
        self.sol = data

    @property
    def tipo_informacion_adicional(self):
        data = ''
        try:
            data = self.sol.TipoInformacionAdicional.text
        except AttributeError:
            pass
        return data

    @property
    def desc_peticion_informacion(self):
        data = ''
        try:
            data = self.sol.DescPeticionInformacion.text
        except AttributeError:
            pass
        return data

    @property
    def fecha_limite_envio(self):
        data = False
        try:
            data = self.sol.FechaLimiteEnvio.text
        except AttributeError:
            pass
        return data


class SolicitudInformacionAdicionalparaRetipificacion(object):

    def __init__(self, data):
        self.sol = data

    @property
    def tipo(self):
        data = ''
        try:
            data = self.sol.Tipo.text
        except AttributeError:
            pass
        return data

    @property
    def subtipo(self):
        data = ''
        try:
            data = self.sol.Subtipo.text
        except AttributeError:
            pass
        return data

    @property
    def fecha_limite_envio(self):
        data = False
        try:
            data = self.sol.FechaLimiteEnvio.text
        except AttributeError:
            pass
        return data


class DatosEnvioInformacion(object):

    def __init__(self, data):
        self.datos = data

    @property
    def num_expediente_acometida(self):
        data = ''
        try:
            data = self.datos.NumExpedienteAcometida.text
        except AttributeError:
            pass
        return data

    @property
    def fecha_informacion(self):
        data = False
        try:
            data = self.datos.FechaInformacion.text
        except AttributeError:
            pass
        return data


class VariableAportacionInformacion(object):

    def __init__(self, data):
        self.var = data

    @property
    def tipo_informacion(self):
        data = ''
        try:
            data = self.var.TipoInformacion.text
        except AttributeError:
            pass
        return data

    @property
    def desc_peticion_informacion(self):
        data = ''
        try:
            data = self.var.DescPeticionInformacion.text
        except AttributeError:
            pass
        return data

    @property
    def variable(self):
        data = ''
        try:
            data = self.var.Variable.text
        except AttributeError:
            pass
        return data

    @property
    def valor(self):
        data = ''
        try:
            data = self.var.Valor.text
        except AttributeError:
            pass
        return data


class DatosCierre(object):

    def __init__(self, data):
        self.datos = data

    @property
    def num_expediente_acometida(self):
        data = ''
        try:
            data = self.datos.NumExpedienteAcometida.text
        except AttributeError:
            pass
        return data

    @property
    def fecha(self):
        data = False
        try:
            data = self.datos.Fecha.text
        except AttributeError:
            pass
        return data

    @property
    def hora(self):
        data = ''
        try:
            data = self.datos.Hora.text
        except AttributeError:
            pass
        return data

    @property
    def tipo(self):
        data = ''
        try:
            data = self.datos.Tipo.text
        except AttributeError:
            pass
        return data

    @property
    def subtipo(self):
        data = ''
        try:
            data = self.datos.Subtipo.text
        except AttributeError:
            pass
        return data

    @property
    def codigo_reclamacion_distribuidora(self):
        data = ''
        try:
            data = self.datos.CodigoReclamacionDistribuidora.text
        except AttributeError:
            pass
        return data

    @property
    def resultado_reclamacion(self):
        data = ''
        try:
            data = self.datos.ResultadoReclamacion.text
        except AttributeError:
            pass
        return data

    @property
    def detalle_resultado(self):
        data = ''
        try:
            data = self.datos.DetalleResultado.text
        except AttributeError:
            pass
        return data

    @property
    def observaciones(self):
        data = ''
        try:
            data = self.datos.Observaciones.text
        except AttributeError:
            pass
        return data

    @property
    def indemnizacion_abonada(self):
        data = ''
        try:
            data = self.datos.IndemnizacionAbonada.text
        except AttributeError:
            pass
        return data

    @property
    def num_expediente_anomalia_fraude(self):
        data = ''
        try:
            data = self.datos.NumExpedienteAnomaliaFraude.text
        except AttributeError:
            pass
        return data

    @property
    def fecha_movimiento(self):
        data = False
        try:
            data = self.datos.FechaMovimiento.text
        except AttributeError:
            pass
        return data


class MinimumFieldsChecker(object):

    def __init__(self, r1):
        self.r1 = r1

    def check(self):
        errors = []
        for field in self.r1.get_minimum_fields():
            valid = getattr(self, 'check_{0}'.format(field), None)
            if not valid():
                errors.append(field)
        return errors

    def check_nif_cliente(self):
        return get_rec_attr(self.r1, "cliente.identificador", False)

    def check_nombre_cliente(self):
        return (get_rec_attr(self.r1, "cliente.nombre_de_pila", False) and
                get_rec_attr(self.r1, "cliente.primer_apellido", False)) \
               or get_rec_attr(self.r1, "cliente.razon_social", False)

    def check_telefono_contacto(self):
        for var in self.r1.variables_detalle_reclamacion:
            if not get_rec_attr(var, "contacto.telfono_numero", False):
                return False
        return len(self.r1.variables_detalle_reclamacion) > 0

    def check_cups(self):
        return self.r1.cups

    def check_fecha_incidente(self):
        for var in self.r1.variables_detalle_reclamacion:
            if not var.fecha_incidente:
                return False
        return len(self.r1.variables_detalle_reclamacion) > 0

    def check_comentarios(self):
        return self.r1.comentarios

    def check_codigo_incidencia(self):
        for var in self.r1.variables_detalle_reclamacion:
            if not var.codigo_incidencia:
                return False
        return len(self.r1.variables_detalle_reclamacion) > 0

    def check_persona_de_contacto(self):
        for var in self.r1.variables_detalle_reclamacion:
            if not var.contacto:
                return False
        return len(self.r1.variables_detalle_reclamacion) > 0

    def check_num_fact(self):
        for var in self.r1.variables_detalle_reclamacion:
            if not var.num_factura_atr:
                return False
        return len(self.r1.variables_detalle_reclamacion) > 0

    def check_tipo_concepto_facturado(self):
        for var in self.r1.variables_detalle_reclamacion:
            if not var.tipo_concepto_facturado:
                return False
        return len(self.r1.variables_detalle_reclamacion) > 0

    def check_lectura(self):
        for var in self.r1.variables_detalle_reclamacion:
            if len(var.lecturas_aportadas) == 0:
                return False
        return len(self.r1.variables_detalle_reclamacion) > 0

    def check_fecha_de_lectura(self):
        for var in self.r1.variables_detalle_reclamacion:
            if not var.fecha_lectura:
                return False
        return len(self.r1.variables_detalle_reclamacion) > 0

    def check_fecha_desde(self):
        for var in self.r1.variables_detalle_reclamacion:
            if not var.fecha_desde:
                return False
        return len(self.r1.variables_detalle_reclamacion) > 0

    def check_fecha_hasta(self):
        for var in self.r1.variables_detalle_reclamacion:
            if not var.fecha_hasta:
                return False
        return len(self.r1.variables_detalle_reclamacion) > 0

    def check_ubicacion_incidencia(self):
        for var in self.r1.variables_detalle_reclamacion:
            if not var.ubicacion_incidencia:
                return False
        return len(self.r1.variables_detalle_reclamacion) > 0

    def check_codigo_de_solicitud(self):
        for var in self.r1.variables_detalle_reclamacion:
            if not var.codigo_solicitud_reclamacion:
                return False
        return len(self.r1.variables_detalle_reclamacion) > 0

    def check_concepto_contratacion(self):
        for var in self.r1.variables_detalle_reclamacion:
            if not var.parametro_contratacion:
                return False
        return len(self.r1.variables_detalle_reclamacion) > 0

    def check_cta_banco(self):
        for var in self.r1.variables_detalle_reclamacion:
            if not var.iban:
                return False
        return len(self.r1.variables_detalle_reclamacion) > 0

    def check_sol_nuevos_suministro(self):
        for var in self.r1.variables_detalle_reclamacion:
            if not var.num_expediente_acometida:
                return False
        return len(self.r1.variables_detalle_reclamacion) > 0

    def check_numero_expediente_fraude(self):
        for var in self.r1.variables_detalle_reclamacion:
            if not var.num_expediente_fraude:
                return False
        return len(self.r1.variables_detalle_reclamacion) > 0

    def check_cod_reclam_anterior(self):
        for var in self.r1.variables_detalle_reclamacion:
            if not var.codigo_solicitud_reclamacion:
                return False
        return len(self.r1.variables_detalle_reclamacion) > 0

    def check_importe_reclamado(self):
        for var in self.r1.variables_detalle_reclamacion:
            if not var.importe_reclamado:
                return False
        return len(self.r1.variables_detalle_reclamacion) > 0

    def check_tipo_atencion_incorrecta(self):
        for var in self.r1.variables_detalle_reclamacion:
            if not var.tipo_de_atencion_incorrecta:
                return False
        return len(self.r1.variables_detalle_reclamacion) > 0


# Module Functions

def get_minimum_fields(r1_subtype):
    for x in SUBTYPES_R101:
        if x['code'] == r1_subtype:
            return x['min_fields']
    return []


def get_subtypes(r1_type):
    return [x['code'] for x in SUBTYPES_R101 if x['type'] == r1_type]


def get_type_from_subtype(r1_subtype):
    for x in SUBTYPES_R101:
        if x['code'] == r1_subtype:
            return x['type']
    return []