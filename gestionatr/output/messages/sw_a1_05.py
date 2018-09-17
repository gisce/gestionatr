# -*- coding: utf-8 -*-

from libcomxml.core import XmlModel, XmlField
from gestionatr.output.messages.base_gas import Heading
from gestionatr.output.messages.sw_a1_41 import Registerdoclist, Registerdoc


# Paso 01
class MensajeA105(XmlModel):
    _sort_order = ('mensaje', 'heading', 'a105')

    def __init__(self):
        self.doc_root = None
        self.mensaje = XmlField(
            'sctdapplication', attributes={'xmlns': 'http://localhost/sctd/A105'}
        )
        self.heading = Heading()
        self.a105 = A105()
        super(MensajeA105, self).__init__('sctdapplication', 'mensaje')


class A105(XmlModel):
    _sort_order = (
        'a105', 'comreferencenum', 'reqdate', 'reqhour', 'nationality',
        'documenttype', 'documentnum', 'cups', 'modeffectdate',
        'reqtransferdate', 'updatereason', 'surrogacy', 'newtolltype',
        'newreqqd', 'newnationality', 'newdocumenttype', 'newdocumentnum',
        'newfirstname', 'newfamilyname1', 'newfamilyname2', 'newtitulartype',
        'newregularaddress', 'newtelephone', 'newfax', 'newemail',
        'newcaecode', 'newprovinceowner', 'newcityowner', 'newzipcodeowner',
        'newstreettypeowner', 'newstreetowner', 'newstreetnumberowner',
        'newportalowner', 'newstaircaseowner', 'newfloorowner', 'newdoorowner',
        'extrainfo', 'registerdoclist'
    )

    def __init__(self):
        self.a105 = XmlField('a105')
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
        self.newtolltype = XmlField('newtolltype')
        self.newreqqd = XmlField('newreqqd')
        self.newnationality = XmlField('newnationality')
        self.newdocumenttype = XmlField('newdocumenttype')
        self.newdocumentnum = XmlField('newdocumentnum')
        self.newfirstname = XmlField('newfirstname')
        self.newfamilyname1 = XmlField('newfamilyname1')
        self.newfamilyname2 = XmlField('newfamilyname2')
        self.newtitulartype = XmlField('newtitulartype')
        self.newregularaddress = XmlField('newregularaddress')
        self.newtelephone = XmlField('newtelephone')
        self.newfax = XmlField('newfax')
        self.newemail = XmlField('newemail')
        self.newcaecode = XmlField('newcaecode')
        self.newprovinceowner = XmlField('newprovinceowner')
        self.newcityowner = XmlField('newcityowner')
        self.newzipcodeowner = XmlField('newzipcodeowner')
        self.newstreettypeowner = XmlField('newstreettypeowner')
        self.newstreetowner = XmlField('newstreetowner')
        self.newstreetnumberowner = XmlField('newstreetnumberowner')
        self.newportalowner = XmlField('newportalowner')
        self.newstaircaseowner = XmlField('newstaircaseowner')
        self.newfloorowner = XmlField('newfloorowner')
        self.newdoorowner = XmlField('newdoorowner')
        self.extrainfo = XmlField('extrainfo')
        self.registerdoclist = Registerdoclist()
        super(A105, self).__init__('a105', 'a105')
