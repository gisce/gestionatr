# -*- coding: utf-8 -*-
from A1_03 import *


class A1_38(A1_03):

    steps = []

    # Pas a2

    @property
    def qhgranted(self):
        tree = '{0}.qhgranted'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def clientyearlyconsumption(self):
        tree = '{0}.clientyearlyconsumption'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    # Pas a25
    @property
    def visitdate(self):
        tree = '{0}.visitdate'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def visithour(self):
        tree = '{0}.visithour'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def informationtype(self):
        tree = '{0}.informationtype'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def informationtypedesc(self):
        tree = '{0}.informationtypedesc'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    # Pas a3

    # Pas a4
