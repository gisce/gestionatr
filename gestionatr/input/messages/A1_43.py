# -*- coding: utf-8 -*-
from A1_42 import *
from A1_48 import *


class A1_43(A1_42, A1_48):

    steps = []

    # Datos paso a242
    # ja tenim de les herències

    # Datos paso a2542
    # ja tenim de les herències

    # Datos paso a442
    # ja tenim de les herències

    # Datos paso a342
    # ja tenim de les herències

    # Datos paso a2s42
    # ja tenim de les herències

    # Datos paso a3s42
    # ja tenim de les herències

    # Datos paso a4s42
    # ja tenim de les herències

    @property
    def stateincidence(self):
        tree = '{0}.stateincidence'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def contact(self):
        tree = '{0}.contact'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return contact(data)
        else:
            return False


class contact(contact):

    @property
    def contacttelephone1(self):
        tree = 'contacttelephone1'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def contacttelephone2(self):
        tree = 'contacttelephone2'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def contacttelephone3(self):
        tree = 'contacttelephone3'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False
