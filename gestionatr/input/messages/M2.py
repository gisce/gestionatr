# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from .M1 import M1
from .C1 import DatosActivacion, DatosCAU
from gestionatr.utils import get_rec_attr


class M2(M1):
    """Classe que implementa M2."""

    # Datos paso 05
    @property
    def datos_activacion(self):
        tree = '{0}.DatosActivacion'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data not in [None, False]:
            return DatosActivacion(data)
        else:
            return False

    @property
    def datos_cau(self):
        obj = getattr(self.obj, 'DatosCAU')
        data = []
        if obj not in [None, False]:
            for i in obj.DatosCAU:
                data.append(DatosCAU(i))
            return data
        return data

    @property
    def datos_cau(self):
        data = []
        obj = get_rec_attr(self.obj, self._header, False)
        if not hasattr(obj, 'DatosCAU'):
            obj = get_rec_attr(self.obj, 'Rechazos', False)
        if hasattr(obj, 'DatosCAU'):
            for d in obj.DatosCAU:
                data.append(DatosCAU(d))
        return data


class DatosActivacion(DatosActivacion):
    @property
    def motivo_activacion_unidireccional(self):
        data = []
        try:
            for datos in self.datos_activacion.MotivoActivacionUnidireccional:
                data.append(MotivoActivacionUnidireccional(datos))
        except AttributeError:
            pass
        return data


class MotivoActivacionUnidireccional(object):

    def __init__(self, data):
        self.motivo_activacion_unidireccional = data

    @property
    def motivo(self):
        data = False
        try:
            data = self.motivo_activacion_unidireccional.Motivo.text
        except AttributeError:
            pass
        return data
