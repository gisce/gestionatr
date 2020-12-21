# -*- coding: utf-8 -*-

from libcomxml.core import XmlModel, XmlField
from gestionatr.output.messages.base_gas import Heading
from gestionatr.output.messages.sw_a1_41 import Registerdoclist, Registerdoc
from gestionatr.output.messages.sw_a1_42 import ProductList, Product


# Paso 01
class MensajeA138(XmlModel):
    _sort_order = ('mensaje', 'heading', 'a138')

    def __init__(self):
        self.doc_root = None
        self.mensaje = XmlField(
            'sctdapplication', attributes={'xmlns': 'http://localhost/sctd/A138'}
        )
        self.heading = Heading()
        self.a138 = A138()
        super(MensajeA138, self).__init__('sctdapplication', 'mensaje')


class A138(XmlModel):

    _sort_order = (
        'a138', 'comreferencenum', 'reqdate', 'reqhour', 'titulartype', 'nationality', 'documenttype', 'documentnum',
        'firstname', 'familyname1', 'familyname2', 'telephone1', 'telephone2', 'fax', 'email', 'language', 'province',
        'city', 'zipcode', 'streettype', 'street', 'streetnumber', 'portal', 'staircase', 'floor', 'door',
        'regularaddress', 'provinceowner', 'cityowner', 'zipcodeowner', 'streettypeowner', 'streetowner',
        'streetnumberowner', 'portalowner', 'staircaseowner', 'floorowner', 'doorowner', 'cups', 'reqqd', 'reqqh',
        'reqestimatedqa', 'reqoutgoingpressure', 'gasusetype', 'tolltype', 'counterproperty', 'aptransind',
        'aptransnumber', 'reig', 'designpower', 'iricertificatedate', 'terminstexist', 'modeffectdate',
        'reqactivationdate', 'extrainfo', 'productlist', 'registerdoclist'
    )

    def __init__(self):
        self.a138 = XmlField('a138')
        self.comreferencenum = XmlField('comreferencenum')
        self.reqdate = XmlField('reqdate')
        self.reqhour = XmlField('reqhour')
        self.titulartype = XmlField('titulartype')
        self.nationality = XmlField('nationality')
        self.documenttype = XmlField('documenttype')
        self.documentnum = XmlField('documentnum')
        self.firstname = XmlField('firstname')
        self.familyname1 = XmlField('familyname1')
        self.familyname2 = XmlField('familyname2')
        self.telephone1 = XmlField('telephone1')
        self.telephone2 = XmlField('telephone2')
        self.fax = XmlField('fax')
        self.email = XmlField('email')
        self.language = XmlField('language')
        self.province = XmlField('province')
        self.city = XmlField('city')
        self.zipcode = XmlField('zipcode')
        self.streettype = XmlField('streettype')
        self.street = XmlField('street')
        self.streetnumber = XmlField('streetnumber')
        self.portal = XmlField('portal')
        self.staircase = XmlField('staircase')
        self.floor = XmlField('floor')
        self.door = XmlField('door')
        self.regularaddress = XmlField('regularaddress')
        self.provinceowner = XmlField('provinceowner')
        self.cityowner = XmlField('cityowner')
        self.zipcodeowner = XmlField('zipcodeowner')
        self.streettypeowner = XmlField('streettypeowner')
        self.streetowner = XmlField('streetowner')
        self.streetnumberowner = XmlField('streetnumberowner')
        self.portalowner = XmlField('portalowner')
        self.staircaseowner = XmlField('staircaseowner')
        self.floorowner = XmlField('floorowner')
        self.doorowner = XmlField('doorowner')
        self.cups = XmlField('cups')
        self.reqqd = XmlField('reqqd')
        self.reqqh = XmlField('reqqh')
        self.reqestimatedqa = XmlField('reqestimatedqa')
        self.reqoutgoingpressure = XmlField('reqoutgoingpressure')
        self.gasusetype = XmlField('gasusetype')
        self.tolltype = XmlField('tolltype')
        self.counterproperty = XmlField('counterproperty')
        self.aptransind = XmlField('aptransind')
        self.aptransnumber = XmlField('aptransnumber')
        self.reig = XmlField('reig')
        self.designpower = XmlField('designpower')
        self.iricertificatedate = XmlField('iricertificatedate')
        self.terminstexist = XmlField('terminstexist')
        self.modeffectdate = XmlField('modeffectdate')
        self.reqactivationdate = XmlField('reqactivationdate')
        self.extrainfo = XmlField('extrainfo')
        self.productlist = ProductList()
        self.registerdoclist = Registerdoclist()
        super(A138, self).__init__('a138', 'a138')