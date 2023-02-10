# -*- coding: utf-8 -*-
from gestionatr.input.messages import C1
from gestionatr.input.messages.C1 import DatosSuministro, DatosInstGen
from gestionatr.utils import get_rec_attr


class D1(C1):
    """Clase que implementa D1."""

    @property
    def motivo_cambio_atr_desde_distribuidora(self):
        tree = '{0}.MotivoCambioATRDesdeDistribuidora'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data:
            return data.text
        else:
            return False

    @property
    def fecha_prevista_aplicacion_cambio_atr(self):
        tree = '{0}.FechaPrevistaAplicacionCambioATR'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data:
            return data.text
        else:
            return False

    @property
    def periodicidad_facturacion(self):
        tree = '{0}.PeriodicidadFacturacion'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data:
            return data.text
        else:
            return False

    @property
    def info_registro_autocons(self):
        tree = '{0}.InfoRegistroAutocons'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data not in [None, False]:
            return InfoRegistroAutocons(data)
        else:
            tree = '{0}.InfoRegistroAutocons'.format(self._header)
            data = get_rec_attr(self.obj, tree, False)
            if data not in [None, False]:
                return InfoRegistroAutocons(data)
            return False

    @property
    def info_retardo_activ_autocons(self):
        tree = '{0}.InfoRetardoActivAutocons'.format(self._header)
        obj = get_rec_attr(self.obj, tree, False)
        data = []
        if obj not in [None, False]:
            for i in obj:
                data.append(InfoRetardoActivAutocons(i))
        return data


class InfoRetardoActivAutocons(object):

    def __init__(self, data):
        self.info_retardo_activ_atuocons = data

    @property
    def codigo_fiscal_factura(self):
        data = ''
        try:
            data = self.info_retardo_activ_atuocons.CodigoFiscalFactura.text
        except AttributeError:
            pass
        return data

    @property
    def fecha_inicio_conteo_activ_autocons(self):
        data = ''
        try:
            data = self.info_retardo_activ_atuocons.FechaInicioConteoActivAutocons.text
        except AttributeError:
            pass
        return data

    @property
    def fecha_desde(self):
        data = ''
        try:
            data = self.info_retardo_activ_atuocons.FechaDesde.text
        except AttributeError:
            pass
        return data

    @property
    def fecha_hasta(self):
        data = ''
        try:
            data = self.info_retardo_activ_atuocons.FechaHasta.text
        except AttributeError:
            pass
        return data

    @property
    def dias_retardo_activ_autocons(self):
        data = ''
        try:
            data = self.info_retardo_activ_atuocons.DiasRetardoActivAutocons.text
        except AttributeError:
            pass
        return data

    @property
    def valor_energia_anual_calculado(self):
        data = ''
        try:
            data = self.info_retardo_activ_atuocons.ValorEnergiaAnualCalculada.text
        except AttributeError:
            pass
        return data

    @property
    def valor_energia_horaria_calculada(self):
        data = ''
        try:
            data = self.info_retardo_activ_atuocons.ValorEnergiaHorariaCalculada.text
        except AttributeError:
            pass
        return data

    @property
    def pot_instalada_gen(self):
        data = ''
        try:
            data = self.info_retardo_activ_atuocons.PotInstaladaGen.text
        except AttributeError:
            pass
        return data


class InfoRegistroAutocons(object):

    def __init__(self, data):
        self.info_registro_autocons = data

    @property
    def autoconsumo(self):
        data = ''
        try:
            data = Autoconsumo(self.info_registro_autocons.Autoconsumo)
        except AttributeError:
            pass
        return data

    @property
    def datos_suministro(self):
        data = ''
        try:
            data = DatosSuministro(self.info_registro_autocons.DatosSuministro)
        except AttributeError:
            pass
        return data

    @property
    def datos_inst_gen(self):
        data = []
        try:
            for datos in self.info_registro_autocons.DatosInstGen:
                data.append(DatosInstGen(datos))
        except AttributeError:
            pass
        return data

    @property
    def comentarios(self):
        data = ''
        try:
            data = self.info_registro_autocons.Comentarios.text
        except AttributeError:
            pass
        return data


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
    def seccion_registro(self):
        data = ''
        try:
            data = self.autoconsumo.SeccionRegistro.text
        except AttributeError:
            pass
        return data

    @property
    def sub_seccion(self):
        data = ''
        try:
            data = self.autoconsumo.SubSeccion.text
        except AttributeError:
            pass
        return data

    @property
    def colectivo(self):
        data = ''
        try:
            data = self.autoconsumo.Colectivo.text
        except AttributeError:
            pass
        return data
