# -*- coding: utf-8 -*-
from gestionatr.input.messages import A1_41
from gestionatr.input.messages.Deadlines import (
    DeadLine, Workdays, Naturaldays,
)
from gestionatr.utils import get_rec_attr


class A13_50(A1_41):
    """Clase que implementa A13_50."""

    steps = [
        DeadLine('a14', Workdays(6)),
        DeadLine('a15', Workdays(1)),
    ]
    steps_glp = [
        DeadLine('a14', Workdays(6)),
        DeadLine('a15', Workdays(7)),
    ]

    @property
    def reqcode(self):
        tree = '{0}.reqcode'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

