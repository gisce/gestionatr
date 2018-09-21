# -*- coding: utf-8 -*-
from A1_44 import *


class A1_03(A1_44):

    steps = []

    @property
    def annulmentreason(self):
        tree = '{0}.annulmentreason'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False
