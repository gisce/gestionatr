# -*- coding: utf-8 -*-
from gestionatr.input.messages.C1 import Autoconsumo
from gestionatr.input.messages.F1 import EnergiaActiva, InstalacionGenAutoconsumo, EnergiaExcedentaria, \
    InformacionAlConsumidor, DatosCAU
from message import Message
from gestionatr.utils import get_rec_attr
from Deadlines import ProcessDeadline


class Q1(Message, ProcessDeadline):
    """Clase que implementa Q1."""

    @property
    def datos(self):
        if hasattr(self.obj, 'Datos'):
            return Datos(self.obj.Datos)
        return None

    @property
    def energia_activa(self):
        if hasattr(self.obj, 'EnergiaActiva'):
            return EnergiaActiva(self.obj.EnergiaActiva)
        return None

    @property
    def autoconsumo(self):
        data = []
        if hasattr(self.obj, 'Autoconsumo'):
            for auto in self.obj.Autoconsumo:
                data.append(Autoconsumo(auto))
        return data

    @property
    def cod_pm(self):
        tree = '{0}.CodPM'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data:
            return data.text
        else:
            return False

    @property
    def modelos_aparato(self):
        data = []
        obj = get_rec_attr(self.obj, self._header, False)
        for i in obj.ModeloAparato:
            data.append(ModeloAparato(i))
        return data

    @property
    def informacion_al_consumidor(self):
        if hasattr(self.obj, 'InformacionAlConsumidor'):
            return InformacionAlConsumidor(self.obj.InformacionAlConsumidor)
        return None

class Datos(object):

    def __init__(self, data):
        self.datos = data

    @property
    def tipo_autoconsumo(self):
        data = ''
        try:
            data = self.datos.TipoAutoconsumo.text
        except AttributeError:
            pass
        return data

    @property
    def tipo_subseccion(self):
        data = ''
        try:
            data = self.datos.TipoSubseccion.text
        except AttributeError:
            pass
        return data

    @property
    def datos_cau(self):
        data = []
        for d in self.datos.DatosCAU:
            data.append(DatosCAU(d))
        return data

    @property
    def marca_medida_con_perdidas(self):
        data = ''
        try:
            data = self.datos.MarcaMedidaConPerdidas.text
        except AttributeError:
            pass
        return data

    @property
    def vas_trafo(self):
        data = ''
        try:
            data = self.datos.VAsTrafo.text
        except AttributeError:
            pass
        return data

    @property
    def porcentaje_perdidas(self):
        data = ''
        try:
            data = self.datos.PorcentajePerdidas.text
        except AttributeError:
            pass
        return data

    @property
    def indicativo_curva_carga(self):
        data = ''
        try:
            data = self.datos.IndicativoCurvaCarga.text
        except AttributeError:
            pass
        return data

    @property
    def _periodo_cch(self):
        if hasattr(self.datos, 'PeriodoCCH'):
            return self.datos.PeriodoCCH
        return None

    @property
    def fecha_desde_cch(self):
        if hasattr(self._periodo_cch, 'FechaDesdeCCH'):
            return self._periodo_cch.FechaDesdeCCH.text.strip()
        return None

    @property
    def fecha_hasta_cch(self):
        if hasattr(self._periodo_cch, 'FechaHastaCCH'):
            return self._periodo_cch.FechaHastaCCH.text.strip()
        return None

    @property
    def _periodo(self):
        if hasattr(self.datos, 'Periodo'):
            return self.datos.Periodo
        return None

    @property
    def fecha_desde_factura(self):
        if hasattr(self._periodo, 'FechaDesdeFactura'):
            return self._periodo.FechaDesdeFactura.text.strip()
        return None

    @property
    def fecha_hasta_factura(self):
        if hasattr(self._periodo, 'FechaHastaFactura'):
            return self._periodo.FechaHastaFactura.text.strip()
        return None

    @property
    def numero_dias(self):
        if hasattr(self._periodo, 'NumeroDias'):
            return int(self._periodo.NumeroDias.text.strip())
        return None

    @property
    def tipo_pm(self):
        if hasattr(self.datos, 'TipoPM'):
            return int(self.datos.TipoPM.text.strip())
        return None


class Autoconsumo(object):

    def __init__(self, data):
        self.autoconsumo = data

    @property
    def cau(self):
        data = ''
        try:
            data = self.autoconsumo.CAU.text
        except AttributeError:
            pass
        return data

    @property
    def instalacion_gen_autoconsumo(self):
        data = []
        for i in self.autoconsumo.InstalacionGenAutoconsumo:
            data.append(InstalacionGenAutoconsumo(i))
        return data

    @property
    def energia_excedentaria(self):
        if hasattr(self.autoconsumo, 'EnergiaExcedentaria'):
            return EnergiaExcedentaria(self.autoconsumo.EnergiaExcedentaria)
        return None

class ModeloAparato(object):

    def __init__(self, data):
        self.modelo_aparato = data

    @property
    def tipo_aparato(self):
        data = ''
        try:
            data = self.modelo_aparato.TipoAparato.text
        except AttributeError:
            pass
        return data

    @property
    def marca_aparato(self):
        data = ''
        try:
            data = self.modelo_aparato.MarcaAparato.text
        except AttributeError:
            pass
        return data

    @property
    def numero_serie(self):
        data = ''
        try:
            data = self.modelo_aparato.NumeroSerie.text
        except AttributeError:
            pass
        return data

    @property
    def tipo_dhedm(self):
        data = ''
        try:
            data = self.modelo_aparato.TipoDHEdM.text
        except AttributeError:
            pass
        return data

    @property
    def integradores(self):
        data = []
        for i in self.modelo_aparato.Integrador:
            data.append(Integrador(i))
        return data


class Integrador(object):

    def __init__(self, data):
        self.integrador = data

    @property
    def magnitud(self):
        data = ''
        try:
            data = self.integrador.Magnitud.text
        except AttributeError:
            pass
        return data

    @property
    def codigo_periodo(self):
        data = ''
        try:
            data = self.integrador.CodigoPeriodo.text
        except AttributeError:
            pass
        return data

    @property
    def constante_multiplicadora(self):
        data = ''
        try:
            data = self.integrador.ConstanteMultiplicadora.text
        except AttributeError:
            pass
        return data

    @property
    def numero_ruedas_enteras(self):
        data = ''
        try:
            data = self.integrador.NumeroRuedasEnteras.text
        except AttributeError:
            pass
        return data

    @property
    def numero_ruedas_decimales(self):
        data = ''
        try:
            data = self.integrador.NumeroRuedasDecimales.text
        except AttributeError:
            pass
        return data

    @property
    def consumo_calculado(self):
        data = ''
        try:
            data = self.integrador.ConsumoCalculado.text
        except AttributeError:
            pass
        return data

    @property
    def lectura_desde(self):
        data = ''
        try:
            data = LecturaInfo(self.integrador.LecturaDesde)
        except AttributeError:
            pass
        return data

    @property
    def lectura_hasta(self):
        data = ''
        try:
            data = LecturaInfo(self.integrador.LecturaHasta)
        except AttributeError:
            pass
        return data

    @property
    def ajuste(self):
        data = ''
        try:
            data = Ajuste(self.integrador.Ajuste)
        except AttributeError:
            pass
        return data

    @property
    def anomalia(self):
        data = ''
        try:
            data = Anomalia(self.integrador.Anomalia)
        except AttributeError:
            pass
        return data

    @property
    def fecha_hora_maximetro(self):
        data = False
        try:
            data = self.integrador.FechaHoraMaximetro.text
        except AttributeError:
            pass
        return data


class LecturaInfo(object):

    def __init__(self, data):
        self.lect = data

    @property
    def fecha(self):
        data = False
        try:
            data = self.lect.Fecha.text
        except AttributeError:
            pass
        return data

    @property
    def procedencia(self):
        data = ''
        try:
            data = self.lect.Procedencia.text
        except AttributeError:
            pass
        return data

    @property
    def lectura(self):
        data = ''
        try:
            data = self.lect.Lectura.text
        except AttributeError:
            pass
        return data


class Ajuste(object):

    def __init__(self, data):
        self.ajuste = data

    @property
    def codigo_motivo_ajuste(self):
        data = ''
        try:
            data = self.ajuste.CodigoMotivoAjuste.text
        except AttributeError:
            pass
        return data

    @property
    def ajuste_por_integrador(self):
        data = ''
        try:
            data = self.ajuste.AjustePorIntegrador.text
        except AttributeError:
            pass
        return data

    @property
    def comentarios(self):
        data = ''
        try:
            data = self.ajuste.Comentarios.text
        except AttributeError:
            pass
        return data


class Anomalia(object):

    def __init__(self, data):
        self.anomalia = data

    @property
    def tipo_anomalia(self):
        data = ''
        try:
            data = self.anomalia.TipoAnomalia.text
        except AttributeError:
            pass
        return data

    @property
    def comentarios(self):
        data = ''
        try:
            data = self.anomalia.Comentarios.text
        except AttributeError:
            pass
        return data