# -*- coding: utf-8 -*-
from A1_38 import *




class A1_42(A1_38):

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


class product(product):

    @property
    def reqtype(self):
        tree = 'reqtype'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False
