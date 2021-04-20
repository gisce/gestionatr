# -*- coding: utf-8 -*-

from libcomxml.core import XmlModel, XmlField
from gestionatr.output.messages.base_gas import Heading

from gestionatr.output.messages.base import rep_decimal

from sw_a1_41 import Registerdoc, Registerdoclist


# Paso 01
class MensajeA142(XmlModel):
    _sort_order = ('mensaje', 'heading', 'a142')

    def __init__(self):
        self.doc_root = None
        self.mensaje = XmlField(
            'sctdapplication', attributes={'xmlns': 'http://localhost/sctd/A142'}
        )
        self.heading = Heading()
        self.a142 = A142()
        super(MensajeA142, self).__init__('sctdapplication', 'mensaje')


class A142(XmlModel):

    _sort_order = (
        'a142',
        'comreferencenum',
        'reqdate',
        'reqhour',
        'titulartype',
        'nationality',
        'documenttype',
        'documentnum',
        'cups',
        'modeffectdate',
        'reqtransferdate',
        'updatereason',
        'surrogacy',
        'newowner',
        'disconnectedserviceaccepted',
        'extrainfo',
        'productlist',
        'registerdoclist',
    )

    def __init__(self):
        self.a142 = XmlField('a142')
        self.comreferencenum = XmlField('comreferencenum')
        self.reqdate = XmlField('reqdate')
        self.reqhour = XmlField('reqhour')
        self.titulartype = XmlField('titulartype')
        self.nationality = XmlField('nationality')
        self.documenttype = XmlField('documenttype')
        self.documentnum = XmlField('documentnum')
        self.cups = XmlField('cups')
        self.modeffectdate = XmlField('modeffectdate')
        self.reqtransferdate = XmlField('reqtransferdate')
        self.updatereason = XmlField('updatereason')
        self.surrogacy = XmlField('surrogacy')
        self.newowner = Newowner()
        self.disconnectedserviceaccepted = XmlField('disconnectedserviceaccepted')
        self.extrainfo = XmlField('extrainfo')
        self.productlist = ProductList()
        self.registerdoclist = Registerdoclist()

        super(A142, self).__init__('a142', 'a142')


class ProductList(XmlModel):

    _sort_order = ('productlist', 'product_list')

    def __init__(self):
        self.productlist = XmlField('productlist')
        self.product_list = []
        super(ProductList, self).__init__('productlist', 'productlist')


class Newclient(XmlModel):

    _sort_order = (
        'newnationality',
        'newdocumenttype',
        'newdocumentnum',
        'newfirstname',
        'newfamilyname1',
        'newfamilyname2',
        'newtitulartype',
        'newtelephone1',
        'newtelephone2',
        'newtelephone3',
        'newemail',
        'newlanguage',
    )

    def __init__(self):
        self.newclient = XmlField('newclient')
        self.newnationality = XmlField('newnationality')
        self.newdocumenttype = XmlField('newdocumenttype')
        self.newdocumentnum = XmlField('newdocumentnum')
        self.newfirstname = XmlField('newfirstname')
        self.newfamilyname1 = XmlField('newfamilyname1')
        self.newfamilyname2 = XmlField('newfamilyname2')
        self.newtitulartype = XmlField('newtitulartype')
        self.newtelephone1 = XmlField('newtelephone1')
        self.newtelephone2 = XmlField('newtelephone2')
        self.newtelephone3 = XmlField('newtelephone3')
        self.newemail = XmlField('newemail')
        self.newlanguage = XmlField('newlanguage')
        super(Newclient, self).__init__('newclient','newclient')


class Street(XmlModel):

    _sort_order = (
        'street',
        'streettype',
        'street_name',
        'streetnumber',
        'portal',
        'staircase',
        'floor',
        'door',
        )

    def __init__(self):
        self.street = XmlField('street')
        self.streettype = XmlField('streettype')
        self.street_name = XmlField('street')
        self.streetnumber = XmlField('streetnumber')
        self.portal = XmlField('portal')
        self.staircase = XmlField('staircase')
        self.floor = XmlField('floor')
        self.door = XmlField('door')
        super(Street,self).__init__('street','street')

class Address(XmlModel):

    _sort_order = ('address', 'province', 'city', 'zipcode', 'street')

    def __init__(self):
        self.address = XmlField('address')
        self.province = XmlField('province')
        self.city = XmlField('city')
        self.zipcode = XmlField('zipcode')
        self.street = Street()
        super(Address, self).__init__('address','address')

class AddressPS(XmlModel):

    _sort_order = ('addressPS', 'province', 'city', 'zipcode', 'street')

    def __init__(self):
        self.addressPS = XmlField('addressPS')
        self.province = XmlField('province')
        self.city = XmlField('city')
        self.zipcode = XmlField('zipcode')
        self.street = Street()
        super(AddressPS, self).__init__('addressPS', 'addressPS')


class Newowner(XmlModel):

    _sort_order = ('newowner', 'newclient','newregularaddress','typefiscaladdress','addressPS','address')

    def __init__(self):
        self.newowner = XmlField('newowner')
        self.newclient = Newclient()
        self.newregularaddress = XmlField('newregularaddress')
        self.typefiscaladdress = XmlField('typefiscaladdress')
        self.addressPS = AddressPS()
        self.address = Address()
        super(Newowner, self).__init__('newowner','newowner')

class Product(XmlModel):
    _sort_order = (
    'product', 'reqtype', 'productcode', 'producttype', 'producttolltype', 'productqd', 'productqa', 'productstartdate',
    'productenddate',)

    def __init__(self):
        self.product = XmlField('product')
        self.reqtype = XmlField('reqtype')
        self.productcode = XmlField('productcode')
        self.producttype = XmlField('producttype')
        self.producttolltype = XmlField('producttolltype')
        self.productqd = XmlField('productqd', rep=rep_decimal(7))
        self.productqa = XmlField('productqa')
        self.productstartdate = XmlField('productstartdate')
        self.productenddate = XmlField('productenddate')
        super(Product, self).__init__('product', 'product')