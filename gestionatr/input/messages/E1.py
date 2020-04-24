# -*- coding: utf-8 -*-

from C2 import C2, Contacto
from gestionatr.input.messages.C1 import DatosNotificacion, DatosActivacion
from gestionatr.utils import get_rec_attr


class E1(C2):
    """Classe que implementa B1."""

    # Datos paso 01
    @property
    def codigo_de_solicitud_ref(self):
        tree = '{0}.CodigoDeSolicitudRef'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data:
            return data.text
        else:
            return False

    @property
    def tipo_de_solicitud(self):
        tree = '{0}.TipoDeSolicitud'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data:
            return data.text
        else:
            return False

    @property
    def id_cliente(self):
        tree = '{0}.IdCliente'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data not in [None, False]:
            return IDCliente(data)
        else:
            return False

    # Datos paso 02
    @property
    def ind_anulable(self):
        tree = '{0}.IndAnulable'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data:
            return data.text
        else:
            return False

    @property
    def actuacion_campo(self):
        tree = '{0}.ActuacionCampo'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data:
            return data.text
        else:
            return False

    # Datos paso 05
    @property
    def datos_notificacion(self):
        tree = '{0}.DatosNotificacion'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data not in [None, False]:
            return DatosNotificacion(data)
        else:
            return False

    # Datos paso 06
    @property
    def datos_activacion(self):
        tree = '{0}.DatosActivacion'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data not in [None, False]:
            return DatosActivacion(data)
        else:
            return False

    # Datos paso 13
    @property
    def contestacion_incidencia(self):
        tree = '{0}.ContestacionIncidencia'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data:
            return data.text
        else:
            return False


class IDCliente(object):

    def __init__(self, data):
        self.id_cliente = data

    @property
    def tipo_identificador(self):
        data = ''
        try:
            data = self.id_cliente.TipoIdentificador.text
        except AttributeError:
            pass
        return data

    @property
    def identificador(self):
        data = ''
        try:
            data = self.id_cliente.Identificador.text
        except AttributeError:
            pass
        return data

    @property
    def tipo_persona(self):
        data = ''
        try:
            data = self.id_cliente.TipoPersona.text
        except AttributeError:
            pass
        return data


class DatosNotificacion(DatosNotificacion):

    @property
    def resultado_activacion(self):
        data = ''
        try:
            data = self.datos_notificacion.ResultadoActivacion.text
        except AttributeError:
            pass
        return data

    @property
    def ind_anulable(self):
        data = ''
        try:
            data = self.datos_notificacion.IndAnulable.text
        except AttributeError:
            pass
        return data


class DatosActivacion(DatosActivacion):

    @property
    def en_servicio(self):
        data = ''
        try:
            data = self.datos_activacion.EnServicio.text
        except AttributeError:
            pass
        return data

    @property
    def ind_anulable(self):
        data = ''
        try:
            data = self.datos_activacion.IndAnulable.text
        except AttributeError:
            pass
        return data
