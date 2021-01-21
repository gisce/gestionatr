# -*- coding: utf-8 -*-
from A1_41 import *
from gestionatr.utils import get_rec_attr


class A1_02(A1_41):
    """Clase que implementa C1."""

    steps = []

    # Datos paso a102
    # TODO

    # Datos paso a202
    @property
    def outgoingpressuregranted(self):
        tree = '{0}.outgoingpressuregranted'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data not in [None, False]:
            return data.text
        else:
            return False

    # Datos paso a302
    @property
    def caecode(self):
        tree = '{0}.caecode'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data not in [None, False]:
            return data.text
        else:
            return False

    # Paso a3s02 ya soportado con los datos que tenemos
    # Paso a402 ya soportado con los datos que tenemos
