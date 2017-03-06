# -*- coding: utf-8 -*-
from C2 import C2
from Deadlines import DeadLine, Workdays, Naturaldays
from gestionatr.utils import get_rec_attr


class A3(C2):
    """Clase que implementa A3."""

    steps = [
        DeadLine('01', Workdays(5), '02'),
        DeadLine('02_activation', Workdays(1), '05'),
        DeadLine('02', Naturaldays(60), '05'),
        DeadLine('03', Naturaldays(30), '05'),
        DeadLine('05_activation', Workdays(1), '05'),
        DeadLine('06', Workdays(5), '07'),
    ]

