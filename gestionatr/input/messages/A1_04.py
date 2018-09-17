# -*- coding: utf-8 -*-
from message_gas import MessageGas
from Deadlines import ProcessDeadline, DeadLine, Workdays, Naturaldays
from gestionatr.utils import get_rec_attr
from A1_41 import A1_41
from A1_44 import registerdoc


class A1_04(A1_41):
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
    def operationnum(self):
        tree = '{0}.operationnum'.format(self._header)
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

    @property
    def registerdoclist(self):
        data = []
        obj = get_rec_attr(self.obj, self._header, False)
        if (hasattr(obj, 'registerdoclist') and
                hasattr(obj.registerdoclist, 'registerdoc')):
            for d in obj.registerdoclist.registerdoc:
                data.append(registerdoc(d))
        return data
