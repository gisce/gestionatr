# -*- coding: utf-8 -*-
from gestionatr.utils import get_rec_attr
from A1_44 import A1_44


class A1_04(A1_44):
    """Clase que implementa A1_44."""
    @property
    def cancelreason(self):
        tree = '{0}.cancelreason'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def moreinformation(self):
        tree = '{0}.moreinformation'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False
