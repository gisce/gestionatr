# -*- coding: utf-8 -*-
from C2 import C2, Cliente, Contacto
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
            return Cliente(cli)
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


class Cliente(Cliente):

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
