# -*- coding: utf-8 -*-
from A1_02 import *
from gestionatr.utils import get_rec_attr


class A1_05(A1_02):
    """Clase que implementa M1."""

    steps = []

    # Datos paso a105
    # TODO

    # Datos paso a205
    @property
    def finaltolltypegranted(self):
        tree = '{0}.finaltolltypegranted'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data not in [None, False]:
            return data.text
        else:
            return False

    # Datos paso a305
    @property
    def telephone(self):
        tree = '{0}.telephone'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data not in [None, False]:
            return data.text
        else:
            return False

    @property
    def fax(self):
        tree = '{0}.fax'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data not in [None, False]:
            return data.text
        else:
            return False

    @property
    def caecode(self):
        tree = '{0}.caecode'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data not in [None, False]:
            return data.text
        else:
            return False

    # Paso a405 ya soportado con los datos que tenemos
