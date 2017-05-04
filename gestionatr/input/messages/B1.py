# -*- coding: utf-8 -*-

from C2 import C2, DatosSolicitud, Contacto
from C1 import DatosAceptacion
from Deadlines import ProcessDeadline, DeadLine, Workdays, Naturaldays
from gestionatr.utils import get_rec_attr


class B1(C2):
    """Classe que implementa B1."""

    steps = None

    steps_01 = [
        DeadLine('01', Workdays(5), '02'),
        DeadLine('02_activation', Workdays(1), '05'),
        DeadLine('02',  Workdays(6), '05'),
        DeadLine('03', Workdays(5), '04'),
        DeadLine('05_activation', Workdays(1), '05'),
    ]

    steps_02 = [
        DeadLine('01', Workdays(5), '02'),
        DeadLine('02_activation', Workdays(1), '05'),
        DeadLine('02', Naturaldays(60), '05'),
        DeadLine('03', Workdays(5), '04'),
        DeadLine('05_activation', Workdays(1), '05'),
    ]

    steps_03 = [
        DeadLine('02_activation', Workdays(1), '05'),
        DeadLine('02', Naturaldays(60), '05'),
        DeadLine('05_activation', Workdays(1), '05'),
    ]

    steps_04 = steps_01

    @classmethod
    def get_deadline(cls, step, activation=False, motiu='01'):
        steps = getattr(cls, 'steps_{0}'.format(motiu))
        if activation:
            step = '{0}_activation'.format(step)
        for s in steps:
            if s.step == step:
                return s

    # Datos paso 01
    @property
    def datos_solicitud(self):
        tree = '{0}.DatosSolicitud'.format(self._header)
        sol = get_rec_attr(self.obj, tree, False)
        if sol not in [None, False]:
            return DatosSolicitud(sol)
        else:
            return False

    @property
    def iban(self):
        tree = '{0}.IBAN'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data:
            return data.text
        else:
            return False

    @property
    def contacto(self):
        tree = '{0}.Contacto'.format(self._header)
        cli = get_rec_attr(self.obj, tree, False)
        if cli not in [None, False]:
            return Contacto(cli)
        else:
            return False

    # Datos paso 02
    @property
    def datos_aceptacion(self):
        tree = '{0}.DatosAceptacion'.format(self._header)
        sol = get_rec_attr(self.obj, tree, False)
        if sol not in [None, False]:
            return DatosAceptacion(sol)
        else:
            return False

    # Datos paso 04
    @property
    def hora_aceptacion(self):
        tree = '{0}.HoraAceptacion'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data:
            return data.text
        else:
            return False

    # Datos paso 05
    @property
    def datos_activacion_baja(self):
        tree = '{0}.DatosActivacionBaja'.format(self._header)
        sol = get_rec_attr(self.obj, tree, False)
        if sol not in [None, False]:
            return DatosActivacionBaja(sol)
        else:
            return False


class DatosSolicitud(DatosSolicitud):

    @property
    def motivo(self):
        data = ''
        try:
            data = self.datos_solicitud.Motivo.text
        except AttributeError:
            pass
        return data


class DatosAceptacion(DatosAceptacion):

    @property
    def tipo_activacion_prevista(self):
        data = ''
        try:
            data = self.datos_aceptacion.TipoActivacionPrevista.text
        except AttributeError:
            pass
        return data

    @property
    def fecha_activacion_prevista(self):
        data = False
        try:
            data = self.datos_aceptacion.FechaActivacionPrevista.text
        except AttributeError:
            pass
        return data


class DatosActivacionBaja(object):

    def __init__(self, data):
        self.datos_activacion_baja = data

    @property
    def fecha_activacion(self):
        data = False
        try:
            data = self.datos_activacion_baja.FechaActivacion.text
        except AttributeError:
            pass
        return data
