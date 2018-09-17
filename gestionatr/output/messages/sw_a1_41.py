# -*- coding: utf-8 -*-

from libcomxml.core import XmlModel, XmlField
from gestionatr.output.messages.base_gas import Heading


# Paso 01
class MensajeA141(XmlModel):
    _sort_order = ('mensaje', 'heading', 'a141')

    def __init__(self):
        self.doc_root = None
        self.mensaje = XmlField(
            'sctdapplication', attributes={'xmlns': 'http://localhost/sctd/A141'}
        )
        self.heading = Heading()
        self.a141 = A141()
        super(MensajeA141, self).__init__('sctdapplication', 'mensaje')


class A141(XmlModel):

    _sort_order = (
        'a141', 'comreferencenum', 'reqdate', 'reqhour', 'nationality',
        'documenttype', 'documentnum', 'cups', 'modeffectdate',
        'reqtransferdate', 'updatereason', 'surrogacy', 'newnationality',
        'newdocumenttype', 'newdocumentnum', 'newfirstname', 'newfamilyname1',
        'newfamilyname2', 'newtitulartype', 'newregularaddress',
        'newtelephone1', 'newtelephone2', 'newemail', 'newlanguage',
        'newprovinceowner', 'newcityowner', 'newzipcodeowner',
        'newstreettypeowner', 'newstreetowner', 'newstreetnumberowner',
        'newportal', 'newstaircase', 'newfloor', 'newdoor', 'newreqqd',
        'disconnectedserviceaccepted', 'extrainfo', 'registerdoclist'
    )

    def __init__(self):
        self.a141 = XmlField('a141')
        self.comreferencenum = XmlField('comreferencenum')
        self.reqdate = XmlField('reqdate')
        self.reqhour = XmlField('reqhour')
        self.nationality = XmlField('nationality')
        self.documenttype = XmlField('documenttype')
        self.documentnum = XmlField('documentnum')
        self.cups = XmlField('cups')
        self.modeffectdate = XmlField('modeffectdate')
        self.reqtransferdate = XmlField('reqtransferdate')
        self.updatereason = XmlField('updatereason')
        self.surrogacy = XmlField('surrogacy')
        self.newnationality = XmlField('newnationality')
        self.newdocumenttype = XmlField('newdocumenttype')
        self.newdocumentnum = XmlField('newdocumentnum')
        self.newfirstname = XmlField('newfirstname')
        self.newfamilyname1 = XmlField('newfamilyname1')
        self.newfamilyname2 = XmlField('newfamilyname2')
        self.newtitulartype = XmlField('newtitulartype')
        self.newregularaddress = XmlField('newregularaddress')
        self.newtelephone1 = XmlField('newtelephone1')
        self.newtelephone2 = XmlField('newtelephone2')
        self.newemail = XmlField('newemail')
        self.newlanguage = XmlField('newlanguage')
        self.newprovinceowner = XmlField('newprovinceowner')
        self.newcityowner = XmlField('newcityowner')
        self.newzipcodeowner = XmlField('newzipcodeowner')
        self.newstreettypeowner = XmlField('newstreettypeowner')
        self.newstreetowner = XmlField('newstreetowner')
        self.newstreetnumberowner = XmlField('newstreetnumberowner')
        self.newportal = XmlField('newportal')
        self.newstaircase = XmlField('newstaircase')
        self.newfloor = XmlField('newfloor')
        self.newdoor = XmlField('newdoor')
        self.newreqqd = XmlField('newreqqd')
        self.disconnectedserviceaccepted = XmlField('disconnectedserviceaccepted')
        self.extrainfo = XmlField('extrainfo')
        self.registerdoclist = Registerdoclist()
        super(A141, self).__init__('a141', 'a141')


class Registerdoclist(XmlModel):

    _sort_order = ('registerdoclist', 'registerdoc_list')

    def __init__(self):
        self.registerdoclist = XmlField('registerdoclist')
        self.registerdoc_list = []
        super(Registerdoclist, self).__init__('registerdoclist', 'registerdoclist')


class Registerdoc(XmlModel):

    _sort_order = ('registerdoc', 'date', 'doctype', 'url', 'extrainfo')

    def __init__(self):
        self.registerdoc = XmlField('registerdoc')
        self.date = XmlField('date')
        self.doctype = XmlField('doctype')
        self.url = XmlField('url')
        self.extrainfo = XmlField('extrainfo')
        super(Registerdoc, self).__init__('registerdoc', 'registerdoc')
