# -*- coding: utf-8 -*-
from B1 import B1, DatosActivacionBaja


class B2(B1):
    """Classe que implementa B2."""


class DatosActivacionBaja(DatosActivacionBaja):

    def __init__(self, data):
        self.datos_activacion_baja = data

    @property
    def motivo(self):
        data = False
        try:
            data = self.datos_activacion_baja.Motivo.text
        except AttributeError:
            pass
        return data
