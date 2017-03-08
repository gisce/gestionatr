# -*- coding: utf-8 -*-
from C2 import C2, Cliente, Contacto
from C1 import DatosAceptacion
from W1 import LecturaAportada
from Deadlines import DeadLine, Workdays, Naturaldays
from gestionatr.utils import get_rec_attr


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
        if sol:
            return DatosSolicitud(sol)
        else:
            return False

    @property
    def variables_detalle_reclamacion(self):
        tree = '{0}.VariablesDetalleReclamacion'.format(self._header)
        obj = get_rec_attr(self.obj, tree, False)
        data = []
        if obj:
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
        if cli:
            return Reclamante(cli)
        else:
            return False

    # Datos paso 02 aceptacion
    @property
    def datos_aceptacion(self):
        tree = '{0}.DatosAceptacion'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data:
            return DatosAceptacion(data)
        else:
            return False

    # Datos paso 03
    @property
    def datos_informacion(self):
        tree = '{0}.DatosInformacion'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data:
            return DatosInformacion(data)
        else:
            return False

    @property
    def informacion_intermedia(self):
        tree = '{0}.InformacionIntermedia'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data:
            return InformacionIntermedia(data)
        else:
            return False

    @property
    def retipificacion(self):
        tree = '{0}.Retipificacion'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data:
            return Retipificacion(data)
        else:
            return False

    @property
    def solicitudes_informacion_adicional(self):
        data = []
        tree = '{0}.SolicitudesInformacionAdicional'.format(self._header)
        obj = get_rec_attr(self.obj, tree, False)
        for d in obj.SolicitudInformacionAdicional:
            data.append(SolicitudInformacionAdicional(d))
        return data

    @property
    def solicitud_informacion_adicional_para_retipificacion(self):
        tree = '{0}.SolicitudesInformacionAdicional.SolicitudInformacionAdicionalparaRetipificacion'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data:
            return SolicitudInformacionAdicionalparaRetipificacion(data)
        else:
            return False

    # Datos paso 04
    @property
    def datos_envio_informacion(self):
        tree = '{0}.DatosEnvioInformacion'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data:
            return DatosEnvioInformacion(data)
        else:
            return False

    @property
    def variables_aportacion_informacion(self):
        data = []
        tree = '{0}.VariablesAportacionInformacion'.format(self._header)
        obj = get_rec_attr(self.obj, tree, False)
        for d in obj.VariableAportacionInformacion:
            data.append(VariableAportacionInformacion(d))
        return data

    @property
    def variables_aportacion_informacion_para_retipificacion(self):
        data = []
        tree = '{0}.VariablesAportacionInformacionparaRetipificacion'.format(self._header)
        obj = get_rec_attr(self.obj, tree, False)
        for d in obj.VariableAportacionInformacionparaRetipificacion:
            data.append(VariableDetalleReclamacion(d))
        return data

    # Datos paso 5
    @property
    def datos_cierre(self):
        tree = '{0}.DatosCierre'.format(self._header)
        sol = get_rec_attr(self.obj, tree, False)
        if sol:
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
        data = ''
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
        data = ''
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
        data = ''
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
        data = ''
        try:
            data = self.variable.FechaDesde.text
        except AttributeError:
            pass
        return data

    @property
    def fecha_hasta(self):
        data = ''
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
        data = ''
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
        data = ''
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
        data = ''
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
        data = ''
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
        data = ''
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
        data = ''
        try:
            data = self.datos.FechaMovimiento.text
        except AttributeError:
            pass
        return data
