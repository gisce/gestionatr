# -*- coding: utf-8 -*-
from message_gas import MessageGas
from Deadlines import ProcessDeadline, DeadLine, Workdays, Naturaldays
from gestionatr.utils import get_rec_attr


class A1_41(MessageGas, ProcessDeadline):
    """Clase que implementa C1."""

    steps = []

    # Datos paso a141
    # TODO

    # Datos paso a241
    @property
    def reqcode(self):
        tree = '{0}.reqcode'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data not in [None, False]:
            return data.text
        else:
            return False

    @property
    def responsedate(self):
        tree = '{0}.responsedate'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data not in [None, False]:
            return data.text
        else:
            return False

    @property
    def responsehour(self):
        tree = '{0}.responsehour'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data not in [None, False]:
            return data.text
        else:
            return False

    @property
    def comreferencenum(self):
        tree = '{0}.comreferencenum'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data not in [None, False]:
            return data.text
        else:
            return False

    @property
    def result(self):
        tree = '{0}.result'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data not in [None, False]:
            return data.text
        else:
            return False

    @property
    def resultdesc(self):
        tree = '{0}.resultdesc'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data not in [None, False]:
            return data.text
        else:
            return False

    @property
    def resultreason(self):
        tree = '{0}.resultreason'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data not in [None, False]:
            return data.text
        else:
            return False

    @property
    def resultreasondesc(self):
        tree = '{0}.resultreasondesc'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data not in [None, False]:
            return data.text
        else:
            return False

    @property
    def nationality(self):
        tree = '{0}.nationality'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data not in [None, False]:
            return data.text
        else:
            return False

    @property
    def documenttype(self):
        tree = '{0}.documenttype'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data not in [None, False]:
            return data.text
        else:
            return False

    @property
    def documentnum(self):
        tree = '{0}.documentnum'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data not in [None, False]:
            return data.text
        else:
            return False

    @property
    def cups(self):
        tree = '{0}.cups'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data not in [None, False]:
            return data.text
        else:
            return False

    @property
    def updatereason(self):
        tree = '{0}.updatereason'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data not in [None, False]:
            return data.text
        else:
            return False

    @property
    def reqqd(self):
        tree = '{0}.reqqd'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data not in [None, False]:
            return data.text
        else:
            return False

    @property
    def reqqh(self):
        tree = '{0}.reqqh'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data not in [None, False]:
            return data.text
        else:
            return False

    @property
    def reqestimatedqa(self):
        tree = '{0}.reqestimatedqa'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data not in [None, False]:
            return data.text
        else:
            return False

    @property
    def reqoutgoingpressure(self):
        tree = '{0}.reqoutgoingpressure'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data not in [None, False]:
            return data.text
        else:
            return False

    @property
    def tolltype(self):
        tree = '{0}.tolltype'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data not in [None, False]:
            return data.text
        else:
            return False

    @property
    def qdgranted(self):
        tree = '{0}.qdgranted'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data not in [None, False]:
            return data.text
        else:
            return False

    @property
    def singlenomination(self):
        tree = '{0}.singlenomination'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data not in [None, False]:
            return data.text
        else:
            return False

    @property
    def netsituation(self):
        tree = '{0}.netsituation'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data not in [None, False]:
            return data.text
        else:
            return False

    @property
    def newmodeffectdate(self):
        tree = '{0}.newmodeffectdate'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data not in [None, False]:
            return data.text
        else:
            return False

    @property
    def foreseentransferdate(self):
        tree = '{0}.foreseentransferdate'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data not in [None, False]:
            return data.text
        else:
            return False

    @property
    def StatusPS(self):
        tree = '{0}.StatusPS'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data not in [None, False]:
            return data.text
        else:
            return False

    @property
    def extrainfo(self):
        tree = '{0}.extrainfo'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data not in [None, False]:
            return data.text
        else:
            return False
