# -*- coding: utf-8 -*-
from message_gas import MessageGas
from Deadlines import ProcessDeadline, DeadLine, Workdays, Naturaldays
from gestionatr.utils import get_rec_attr
from A12_26 import *


class A19_45(A12_26):

    steps = []

    @property
    def countertype(self):
        tree = '{0}.countertype'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def inspectionorig(self):
        tree = '{0}.inspectionorig'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def counternumber(self):
        tree = '{0}.counternumber'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def counterproperty(self):
        tree = '{0}.counterproperty'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def reallecture(self):
        tree = '{0}.reallecture'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def counterpressure(self):
        tree = '{0}.counterpressure'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False
