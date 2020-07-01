# -*- coding: utf-8 -*-
from A1_38 import *


class A1_49(A1_38):

    # Pas a2
    @property
    def indanulable(self):
        tree = '{0}.indanulable'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def indactcampo(self):
        tree = '{0}.indactcampo'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    # Pas a3
    @property
    def resactivacion(self):
        tree = '{0}.resactivacion'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def enservicio(self):
        tree = '{0}.enservicio'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False
