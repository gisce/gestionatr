# -*- coding: utf-8 -*-

from C2 import C2, DatosSolicitud
from Deadlines import ProcessDeadline, DeadLine, Workdays, Naturaldays
from gestionatr.utils import get_rec_attr


class M1(C2):
    """Classe que implementa M1."""

    steps_T = [
        DeadLine('01', Workdays(5)),
        DeadLine('02', Workdays(1)),
        DeadLine('03', Naturaldays(30)),
        DeadLine('05', Workdays(1)),
        DeadLine('06', Workdays(5)),
    ]

    steps_S = [
        DeadLine('01', Workdays(5)),
        DeadLine('02', Workdays(5)),
        DeadLine('06', Workdays(5)),
    ]
    steps_A = steps_S
    steps_C = steps_S

    steps_P = steps_T

    steps = steps_T

    # Datos paso 01
    @property
    def datos_solicitud(self):
        tree = '{0}.DatosSolicitud'.format(self._header)
        sol = get_rec_attr(self.obj, tree, False)
        if sol not in [None, False]:
            return DatosSolicitud(sol)
        else:
            return False


class DatosSolicitud(DatosSolicitud):

    @property
    def periodicidad_facturacion(self):
        data = ''
        try:
            data = self.datos_solicitud.PeriodicidadFacturacion.text
        except AttributeError:
            pass
        return data