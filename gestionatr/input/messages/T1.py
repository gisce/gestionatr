# -*- coding: utf-8 -*-

from C2 import C2, Direccion
from gestionatr.utils import get_rec_attr


class T1(C2):
    """Classe que implementa B1."""

    # Datos paso 01
    @property
    def datos_solicitud(self):
        tree = '{0}.DatosSolicitud'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data not in [None, False]:
            return DatosSolicitud(data)
        else:
            return False

    @property
    def direccion_ps(self):
        tree = '{0}.DireccionPS'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data not in [None, False]:
            return Direccion(data)
        else:
            return False

    # Datos paso 05
    @property
    def datos_activacion(self):
        tree = '{0}.DatosActivacion'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data not in [None, False]:
            return DatosActivacion(data)
        else:
            return False

    # Datos paso 06
    @property
    def datos_notificacion(self):
        tree = '{0}.DatosNotificacion'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data not in [None, False]:
            return DatosNotificacion(data)
        else:
            return False


class DatosSolicitud(object):

    def __init__(self, data):
        self.datos_solicitud = data

    @property
    def motivo_traspaso(self):
        data = ''
        try:
            data = self.datos_solicitud.MotivoTraspaso.text
        except AttributeError:
            pass
        return data

    @property
    def fecha_prevista_accion(self):
        data = ''
        try:
            data = self.datos_solicitud.FechaPrevistaAccion.text
        except AttributeError:
            pass
        return data

    @property
    def cnae(self):
        data = ''
        try:
            data = self.datos_solicitud.CNAE.text
        except AttributeError:
            pass
        return data

    @property
    def ind_esencial(self):
        data = ''
        try:
            data = self.datos_solicitud.IndEsencial.text
        except AttributeError:
            pass
        return data

    @property
    def susp_baja_impago_en_curso(self):
        data = ''
        try:
            data = self.datos_solicitud.SuspBajaImpagoEnCurso.text
        except AttributeError:
            pass
        return data


class DatosActivacion(object):

    def __init__(self, data):
        self.datos_activacion = data

    @property
    def fecha_activacion(self):
        data = ''
        try:
            data = self.datos_activacion.FechaActivacion.text
        except AttributeError:
            pass
        return data

    @property
    def en_servicio(self):
        data = ''
        try:
            data = self.datos_activacion.EnServicio.text
        except AttributeError:
            pass
        return data


class DatosNotificacion(object):

    def __init__(self, data):
        self.datos_notificacion = data

    @property
    def fecha_activacion(self):
        data = ''
        try:
            data = self.datos_notificacion.FechaActivacion.text
        except AttributeError:
            pass
        return data
