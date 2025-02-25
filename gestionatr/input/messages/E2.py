# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from .E1 import E1, DatosActivacion, DatosNotificacion
from .C2 import Direccion
from .C1 import RegistroDoc
from gestionatr.utils import get_rec_attr


class E2(E1):
    """Classe que implementa E2."""

    # Datos paso 01

    @property
    def tipo_de_reposicion(self):
        tree = '{0}.TipoDeReposicion'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data:
            return data.text
        else:
            return False


    @property
    def datos_notificacion(self):
        tree = '{0}.DatosNotificacion'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data not in [None, False]:
            return DatosNotificacion(data)
        else:
            return False

    @property
    def datos_activacion(self):
        tree = '{0}.DatosActivacion'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data not in [None, False]:
            return DatosActivacion(data)
        else:
            return False

    # Dades de E214
    @property
    def solicitud_reposicion(self):
        tree = 'SolicitudReposicion'
        data = get_rec_attr(self.obj, tree, False)
        if data not in [None, False]:
            return SolicitudReposicion(data)
        else:
            return False

    @property
    def direccion_ps(self):
        tree = 'DireccionPS'
        data = get_rec_attr(self.obj, tree, False)
        if data not in [None, False]:
            return Direccion(data)
        else:
            return False

    @property
    def registros_documento(self):
        data = []
        obj = get_rec_attr(self.obj, self._header, False)
        if (hasattr(obj, 'RegistrosDocumento') and
                hasattr(obj.RegistrosDocumento, 'RegistroDoc')):
            for d in obj.RegistrosDocumento.RegistroDoc:
                data.append(RegistroDoc(d))
        return data

    @property
    def aceptacion_reposicion(self):
        tree = '{0}.AceptacionReposicion'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data:
            return data.text
        else:
            return False


class DatosNotificacion(DatosNotificacion):

    @property
    def codigo_sol_corte(self):
        data = ''
        try:
            data = self.datos_notificacion.CodigoSolCorte.text
        except AttributeError:
            pass
        return data

    @property
    def ind_esencial(self):
        data = ''
        try:
            data = self.datos_notificacion.IndEsencial.text
        except AttributeError:
            pass
        return data

    @property
    def fecha_ultimo_movimiento_ind_esencial(self):
        data = False
        try:
            data = self.datos_notificacion.FechaUltimoMovimientoIndEsencial.text
        except AttributeError:
            pass
        return data


class DatosActivacion(DatosActivacion):
    @property
    def resultado_activacion(self):
        data = False
        try:
            data = self.datos_activacion.ResultadoActivacion.text
        except AttributeError:
            pass
        return data


# Dades del pas 14
class SolicitudReposicion(object):

    def __init__(self, data):
        self.solicitud_reposicion = data

    @property
    def codigo_de_solicitud_ref(self):
        data = False
        try:
            data = self.solicitud_reposicion.CodigoDeSolicitudRef.text
        except AttributeError:
            pass
        return data

    @property
    def tipo_de_reposicion(self):
        data = False
        try:
            data = self.solicitud_reposicion.TipoDeReposicion.text
        except AttributeError:
            pass
        return data

    @property
    def fecha_prevista_accion(self):
        data = False
        try:
            data = self.solicitud_reposicion.FechaPrevistaAccion.text
        except AttributeError:
            pass
        return data

    @property
    def actuacion_campo(self):
        data = False
        try:
            data = self.solicitud_reposicion.ActuacionCampo.text
        except AttributeError:
            pass
        return data