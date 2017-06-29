# -*- coding: utf-8 -*-
from message import Message
from Deadlines import ProcessDeadline
from gestionatr.utils import get_rec_attr


class D1(Message, ProcessDeadline):
    """Clase que implementa D1."""

    @property
    def motivo_cambio_atr_desde_distribuidora(self):
        tree = '{0}.MotivoCambioATRDesdeDistribuidora'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data:
            return data.text
        else:
            return False

    @property
    def fecha_prevista_aplicacion_cambio_atr(self):
        tree = '{0}.FechaPrevistaAplicacionCambioATR'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data:
            return data.text
        else:
            return False

    @property
    def periodicidad_facturacion(self):
        tree = '{0}.PeriodicidadFacturacion'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data:
            return data.text
        else:
            return False
