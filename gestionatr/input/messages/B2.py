# -*- coding: utf-8 -*-
from B1 import B1, DatosActivacionBaja
from gestionatr.utils import get_rec_attr


class B2(B1):
    """Classe que implementa B2."""
    # Datos paso 05
    @property
    def datos_activacion_baja(self):
        tree = '{0}.DatosActivacionBaja'.format(self._header)
        sol = get_rec_attr(self.obj, tree, False)
        if sol not in [None, False]:
            return DatosActivacionBaja(sol)
        else:
            return False


class DatosActivacionBaja(DatosActivacionBaja):

    @property
    def motivo(self):
        data = False
        try:
            data = self.datos_activacion_baja.Motivo.text
        except AttributeError:
            pass
        return data
