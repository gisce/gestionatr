# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gestionatr.utils import get_rec_attr
from .Deadlines import DeadLine, Workdays, Naturaldays
from .A1_44 import A1_44


class A1_04(A1_44):
    """Clase que implementa A1_44."""

    steps = [
        DeadLine('a0', Workdays(-6)),
        DeadLine('a1', Workdays(6)),
        DeadLine('a2', Workdays(1)),
        DeadLine('a25', Naturaldays(30)),
        DeadLine('a26', Naturaldays(30)),
        DeadLine('a3', Workdays(1)),
    ]
    steps_911 = [
        DeadLine('a25', Workdays(2)),
        DeadLine('a26', Workdays(2)),
    ]
    steps_912 = steps_911

    @property
    def cancelreason(self):
        tree = '{0}.cancelreason'.format(self._header)
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
