# -*- coding: utf-8 -*-
from message_gas import MessageGas
from Deadlines import ProcessDeadline, DeadLine, Workdays, Naturaldays
from gestionatr.utils import get_rec_attr
from A1_05 import *


class A1_44(A1_05):
    """Clase que implementa A1_44."""

    steps = []

    # Datos paso a144
    # TODO

    # Datos paso a244
    @property
    def reqcode(self):
        tree = '{0}.reqcode'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False
    @property
    def reqdate(self):
        tree = '{0}.reqdate'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def reqhour(self):
        tree = '{0}.reqhour'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def operationtype(self):
        tree = '{0}.operationtype'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def srcode(self):
        tree = '{0}.srcode'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    # Datos paso a344
    @property
    def reqdescription(self):
        tree = '{0}.reqdescription'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def interventionhour(self):
        tree = '{0}.interventionhour'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def resultinspection(self):
        tree = '{0}.resultinspection'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def resultinspectiondesc(self):
        tree = '{0}.resultinspectiondesc'.format(self._header)
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
    def counterchange(self):
        tree = '{0}.counterchange'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def removallecture(self):
        tree = '{0}.removallecture'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def supplystatus(self):
        tree = '{0}.supplystatus'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def supplystatusdesc(self):
        tree = '{0}.supplystatusdesc'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def servicestatus(self):
        tree = '{0}.servicestatus'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def servicestatusdesc(self):
        tree = '{0}.servicestatusdesc'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def conceptnumber(self):
        tree = '{0}.conceptnumber'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def conceptlist(self):
        data = []
        obj = get_rec_attr(self.obj, self._header, False)
        if (hasattr(obj, 'conceptlist') and
                hasattr(obj.conceptlist, 'concept')):
            for d in obj.conceptlist.concept:
                data.append(concept(d))
        return data

    @property
    def defectlist(self):
        data = []
        obj = get_rec_attr(self.obj, self._header, False)
        if (hasattr(obj, 'defectlist') and
                hasattr(obj.defectlist, 'defect')):
            for d in obj.defectlist.defect:
                data.append(defect(d))
        return data

    @property
    def registerdoclist(self):
        data = []
        obj = get_rec_attr(self.obj, self._header, False)
        if (hasattr(obj, 'registerdoclist') and
                hasattr(obj.registerdoclist, 'registerdoc')):
            for d in obj.registerdoclist.registerdoc:
                data.append(registerdoc(d))
        return data


class concept(object):

    def __init__(self, data):
        self.obj = data

    @property
    def level(self):
        tree = 'level'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def code(self):
        tree = 'code'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def description(self):
        tree = 'description'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def periodicity(self):
        tree = 'periodicity'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def units(self):
        tree = 'units'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def unitimport(self):
        tree = 'unitimport'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def import_(self):
        tree = 'import'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False


class defect(object):

    def __init__(self, data):
        self.obj = data

    @property
    def code(self):
        tree = 'code'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def description(self):
        tree = 'description'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False


class registerdoc(object):

    def __init__(self, data):
        self.obj = data

    @property
    def date(self):
        tree = 'date'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def doctype(self):
        tree = 'doctype'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def url(self):
        tree = 'url'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def extrainfo(self):
        tree = 'extrainfo'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False
