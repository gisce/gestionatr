# -*- coding: utf-8 -*-
from gestionatr.input.messages import A1_04
from gestionatr.utils import get_rec_attr


class A12_24(A1_04):
    """Clase que implementa A1_44."""
    @property
    def productcode(self):
        tree = '{0}.productcode'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def communicationreason(self):
        tree = '{0}.communicationreason'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False
