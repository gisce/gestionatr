# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from .A1_44 import *


class A1_51(A1_44):

    steps = []

    @property
    def solicitudreferencia(self):
        tree = '{0}.solicitudreferencia'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def tiporeposicion(self):
        tree = '{0}.tiporeposicion'.format(self._header)
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

    @property
    def stateincidence(self):
        tree = '{0}.stateincidence'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def streettype(self):
        tree = '{0}.streettype'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def street(self):
        tree = '{0}.street'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def streetnumber(self):
        tree = '{0}.streetnumber'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def portal(self):
        tree = '{0}.portal'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def staircase(self):
        tree = '{0}.staircase'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def floor(self):
        tree = '{0}.floor'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def door(self):
        tree = '{0}.door'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def province(self):
        tree = '{0}.province'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def city(self):
        tree = '{0}.city'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def zipcode(self):
        tree = '{0}.zipcode'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

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

    @property
    def contact(self):
        tree = '{0}.contact'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return contact(data)
        else:
            return False

class contact(object):

    def __init__(self, data):
        self.obj = data

    @property
    def contactname(self):
        tree = 'contactname'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

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


    @property
    def contactemail(self):
        tree = 'contactemail'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False