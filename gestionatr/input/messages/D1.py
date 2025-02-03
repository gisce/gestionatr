# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gestionatr.input.messages import C1
from gestionatr.input.messages.C1 import Autoconsumo
from gestionatr.utils import get_rec_attr


class D1(C1):
    """Clase que implementa D1."""

    @property
    def notificacion_cambios_atr_desde_distribuidor(self):
        tree = 'NotificacionCambiosATRDesdeDistribuidor'
        data = []
        for d in get_rec_attr(self.obj, tree, False):
            data.append(NotificacionCambiosATRDesdeDistribuidor(d))
        return data

    @property
    def anulacion_notificacion_cambios_atr_desde_distribuidor(self):
        tree = 'AnulacionNotificacionCambiosATRDesdeDistribuidor'
        data = get_rec_attr(self.obj, tree, False)
        if data not in [None, False]:
            return AnulacionNotificacionCambiosATRDesdeDistribuidor(data)
        else:
            return False


class NotificacionCambiosATRDesdeDistribuidor(object):

    def __init__(self, data):
        self.notificacion_cambios_atr_desde_distribuidor = data

    @property
    def motivo_cambio_atr_desde_distribuidora(self):
        data = ''
        try:
            data = self.notificacion_cambios_atr_desde_distribuidor.MotivoCambioATRDesdeDistribuidora.text
        except AttributeError:
            pass
        return data

    @property
    def fecha_prevista_aplicacion_cambio_atr(self):
        data = ''
        try:
            data = self.notificacion_cambios_atr_desde_distribuidor.FechaPrevistaAplicacionCambioATR.text
        except AttributeError:
            pass
        return data

    @property
    def fecha_maxima_rechazo(self):
        data = ''
        try:
            data = self.notificacion_cambios_atr_desde_distribuidor.FechaMaximaRechazo.text
        except AttributeError:
            pass
        return data

    @property
    def periodicidad_facturacion(self):
        data = ''
        try:
            data = self.notificacion_cambios_atr_desde_distribuidor.PeriodicidadFacturacion.text
        except AttributeError:
            pass
        return data

    @property
    def ind_esencial(self):
        data = False
        try:
            data = self.notificacion_cambios_atr_desde_distribuidor.IndEsencial.text
        except AttributeError:
            pass
        return data

    @property
    def fecha_ultimo_movimiento_ind_esencial(self):
        data = False
        try:
            data = self.notificacion_cambios_atr_desde_distribuidor.FechaUltimoMovimientoIndEsencial.text
        except AttributeError:
            pass
        return data

    @property
    def info_registro_autocons(self):
        data = ''
        try:
            data = InfoRegistroAutocons(self.notificacion_cambios_atr_desde_distribuidor.InfoRegistroAutocons)
        except AttributeError:
            pass
        return data

    @property
    def info_retardo_activ_autocons(self):
        data = []
        try:
            for datos in self.notificacion_cambios_atr_desde_distribuidor.InfoRetardoActivAutocons:
                data.append(InfoRetardoActivAutocons(datos))
        except AttributeError:
            pass
        return data


class AnulacionNotificacionCambiosATRDesdeDistribuidor(object):

    def __init__(self, data):
        self.anulacion_notificacion_cambios_atr_desde_distribuidor = data

    @property
    def datos_anulacion(self):
        data = ''
        try:
            data = DatosAnulacion(self.anulacion_notificacion_cambios_atr_desde_distribuidor.DatosAnulacion)
        except AttributeError:
            pass
        return data


class DatosAnulacion(object):

    def __init__(self, data):
        self.datos_anulacion = data

    @property
    def fecha_anulacion(self):
        data = ''
        try:
            data = self.datos_anulacion.FechaAnulacion.text
        except AttributeError:
            pass
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
