# -*- coding: utf-8 -*-
from gestionatr.input.messages import A1_41
from gestionatr.utils import get_rec_attr


class A13_50(A1_41):
    """Clase que implementa A13_50."""

    @property
    def reqcode(self):
        tree = '{0}.reqcode'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

