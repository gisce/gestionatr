# -*- coding: utf-8 -*-
from gestionatr.utils import get_rec_attr
from message import Message
from Deadlines import ProcessDeadline, DeadLine, Workdays, Naturaldays


class W1(Message, ProcessDeadline):
    """Classe que implementa W1."""

    steps = [
        DeadLine('01', Workdays(5), '02'),
    ]

    @property
    def datos_solicitud_aportacion_lectura(self):
        tree = 'DatosSolicitudAportacionLectura'
        data = get_rec_attr(self.obj, tree, False)
        if data:
            return DatosSolicitudAportacionLectura(data)
        else:
            return False

    @property
    def lecturas_aportadas(self):
        data = []
        for i in self.obj.LecturaAportada:
            data.append(LecturaAportada(i))
        return data


class DatosSolicitudAportacionLectura(object):

    def __init__(self, data):
        self.datos = data

    @property
    def fecha_lectura(self):
        data = ''
        try:
            data = self.datos.FechaLectura.text
        except AttributeError:
            pass
        return data

    @property
    def tipo_dhedm(self):
        data = ''
        try:
            data = self.datos.TipoDHEdM.text
        except AttributeError:
            pass
        return data


class LecturaAportada(object):

    def __init__(self, data):
        self.lectura = data

    @property
    def integrador(self):
        data = ''
        try:
            data = self.lectura.Integrador.text
        except AttributeError:
            pass
        return data

    @property
    def tipo_codigo_periodo_dh(self):
        data = ''
        try:
            data = self.lectura.TipoCodigoPeriodoDH.text
        except AttributeError:
            pass
        return data

    @property
    def lectura_propuesta(self):
        data = ''
        try:
            data = self.lectura.LecturaPropuesta.text
        except AttributeError:
            pass
        return data
