# -*- coding: utf-8 -*-

from libcomxml.core import XmlModel, XmlField
from gestionatr.output.messages.base_gas import Heading
from gestionatr.output.messages.sw_a1_05 import Registerdoclist, Registerdoc


# Paso 01
class MensajeA148(XmlModel):
    _sort_order = ('mensaje', 'heading', 'a1')

    def __init__(self):
        self.doc_root = None
        self.mensaje = XmlField(
            'sctdapplication', attributes={'xmlns': 'http://localhost/sctd/A148'}
        )
        self.heading = Heading()
        self.a1 = A148()
        super(MensajeA148, self).__init__('sctdapplication', 'mensaje')


class A148(XmlModel):

    _sort_order = ('a1', 'reqdate', 'reqhour', 'comreferencenum', 'claimertype',
                   'claimer', 'claimtype', 'claimsubtype', 'originreference',
                   'claimreferencelist', 'cups', 'legallimitdate', 'priority',
                   'extrainfo', 'registerdoclist')

    def __init__(self):
        self.a1 = XmlField('a1')
        self.reqdate = XmlField('reqdate')
        self.reqhour = XmlField('reqhour')
        self.comreferencenum = XmlField('comreferencenum')
        self.claimertype = XmlField('claimertype')
        self.claimer = claimer()
        self.claimtype = XmlField('claimtype')
        self.claimsubtype = XmlField('claimsubtype')
        self.originreference = XmlField('originreference')
        self.claimreferencelist = claimreferencelist()
        self.cups = XmlField('cups')
        self.legallimitdate = XmlField('legallimitdate')
        self.priority = XmlField('priority')
        self.extrainfo = XmlField('extrainfo')
        self.registerdoclist = Registerdoclist()
        super(A148, self).__init__('a1', 'a1')


class claimer(XmlModel):

    _sort_order = ('claimer', 'claimerid', 'claimername', 'claimertelephone', 'claimeremail')

    def __init__(self):
        self.claimer = XmlField('claimer')
        self.claimerid = claimerid()
        self.claimername = claimername()
        self.claimertelephone = claimertelephone()
        self.claimeremail = XmlField('claimeremail')
        super(claimer, self).__init__('claimer', 'claimer')


class claimerid(XmlModel):

    _sort_order = ('claimerid', 'claimerdocumenttype', 'claimerdocumentnum')

    def __init__(self):
        self.claimerid = XmlField('claimerid')
        self.claimerdocumenttype = XmlField('claimerdocumenttype')
        self.claimerdocumentnum = XmlField('claimerdocumentnum')
        super(claimerid, self).__init__('claimerid', 'claimerid')


class claimername(XmlModel):

    _sort_order = ('claimername', 'claimerfirstname', 'claimerlastname', 'claimersecondname', 'claimerbusinessname')

    def __init__(self):
        self.claimername = XmlField('claimername')
        self.claimerfirstname = XmlField('claimerfirstname')
        self.claimerlastname = XmlField('claimerlastname')
        self.claimersecondname = XmlField('claimersecondname')
        self.claimerbusinessname = XmlField('claimerbusinessname')
        super(claimername, self).__init__('claimername', 'claimername')


class claimertelephone(XmlModel):

    _sort_order = ('claimertelephone', 'claimerprefixtel1', 'claimertelephone1')

    def __init__(self):
        self.claimertelephone = XmlField('claimertelephone')
        self.claimerprefixtel1 = XmlField('claimerprefixtel1')
        self.claimertelephone1 = XmlField('claimertelephone1')
        super(claimertelephone, self).__init__('claimertelephone', 'claimertelephone')


class claimreferencelist(XmlModel):

    _sort_order = ('claimreferencelist', 'claimreference_list')

    def __init__(self):
        self.claimreferencelist = XmlField('claimreferencelist')
        self.claimreference_list = []
        super(claimreferencelist, self).__init__('claimreferencelist', 'claimreferencelist')


class claimreference(XmlModel):

    _sort_order = ('claimreference', 'wrongattentiontype', 'comreferencenum', 'targetclaimcomreferencenum', 'conceptcontract', 'conceptfacturation', 'contact', 'nnssexpedient', 'fraudrecordnum', 'incidentperiod', 'invoicenumber', 'incidentlocation', 'reading', 'incident', 'client', 'claimedcompensation', 'iban')

    def __init__(self):
        self.claimreference = XmlField('claimreference')
        self.wrongattentiontype = XmlField('wrongattentiontype')
        self.comreferencenum = XmlField('comreferencenum')
        self.targetclaimcomreferencenum = XmlField('targetclaimcomreferencenum')
        self.conceptcontract = XmlField('conceptcontract')
        self.conceptfacturation = XmlField('conceptfacturation')
        self.contact = contact()
        self.nnssexpedient = XmlField('nnssexpedient')
        self.fraudrecordnum = XmlField('fraudrecordnum')
        self.incidentperiod = incidentperiod()
        self.invoicenumber = XmlField('invoicenumber')
        self.incidentlocation = incidentlocation()
        self.reading = reading()
        self.incident = incident()
        self.client = client()
        self.claimedcompensation = XmlField('claimedcompensation')
        self.iban = XmlField('iban')
        super(claimreference, self).__init__('claimreference', 'claimreference')


class contact(XmlModel):

    _sort_order = ('contact', 'contactname', 'contacttelephone', 'contactemail')

    def __init__(self):
        self.contact = XmlField('contact')
        self.contactname = XmlField('contactname')
        self.contacttelephone = contacttelephone()
        self.contactemail = XmlField('contactemail')
        super(contact, self).__init__('contact', 'contact')


class contacttelephone(XmlModel):

    _sort_order = ('contacttelephone', 'telephoneprefix', 'telephonenumber')

    def __init__(self):
        self.contacttelephone = XmlField('contacttelephone')
        self.telephoneprefix = XmlField('telephoneprefix')
        self.telephonenumber = XmlField('telephonenumber')
        super(contacttelephone, self).__init__('contacttelephone', 'contacttelephone')


class incidentperiod(XmlModel):

    _sort_order = ('incidentperiod', 'datefrom', 'dateto')

    def __init__(self):
        self.incidentperiod = XmlField('incidentperiod')
        self.datefrom = XmlField('datefrom')
        self.dateto = XmlField('dateto')
        super(incidentperiod, self).__init__('incidentperiod', 'incidentperiod')


class incidentlocation(XmlModel):

    _sort_order = ('incidentlocation', 'incidentlocationdesc', 'incidentlocationprovince', 'incidentlocationcity', 'incidentlocationcitysubdivision', 'incidentlocationzipcode')

    def __init__(self):
        self.incidentlocation = XmlField('incidentlocation')
        self.incidentlocationdesc = XmlField('incidentlocationdesc')
        self.incidentlocationprovince = XmlField('incidentlocationprovince')
        self.incidentlocationcity = XmlField('incidentlocationcity')
        self.incidentlocationcitysubdivision = XmlField('incidentlocationcitysubdivision')
        self.incidentlocationzipcode = XmlField('incidentlocationzipcode')
        super(incidentlocation, self).__init__('incidentlocation', 'incidentlocation')


class reading(XmlModel):

    _sort_order = ('reading', 'readingdate', 'readingvalue')

    def __init__(self):
        self.reading = XmlField('reading')
        self.readingdate = XmlField('readingdate')
        self.readingvalue = XmlField('readingvalue')
        super(reading, self).__init__('reading', 'reading')


class incident(XmlModel):

    _sort_order = ('incident', 'incidentdate')

    def __init__(self):
        self.incident = XmlField('incident')
        self.incidentdate = XmlField('incidentdate')
        super(incident, self).__init__('incident', 'incident')


class client(XmlModel):

    _sort_order = ('client', 'document', 'titulartype', 'cname', 'telephone', 'email', 'clientAddress')

    def __init__(self):
        self.client = XmlField('client')
        self.document = document()
        self.titulartype = XmlField('titulartype')
        self.cname = cname()
        self.telephone = telephone()
        self.email = XmlField('email')
        self.clientAddress = clientAddress()
        super(client, self).__init__('client', 'client')


class document(XmlModel):

    _sort_order = ('document', 'documenttype', 'documentnum')

    def __init__(self):
        self.document = XmlField('document')
        self.documenttype = XmlField('documenttype')
        self.documentnum = XmlField('documentnum')
        super(document, self).__init__('document', 'document')


class cname(XmlModel):

    _sort_order = ('cname', 'firstname', 'familyname1', 'familyname2', 'businessName')

    def __init__(self):
        self.cname = XmlField('name')
        self.firstname = XmlField('firstname')
        self.familyname1 = XmlField('familyname1')
        self.familyname2 = XmlField('familyname2')
        self.businessName = XmlField('businessName')
        super(cname, self).__init__('cname', 'cname')


class telephone(XmlModel):

    _sort_order = ('telephone', 'telephoneprefix', 'telephonenumber')

    def __init__(self):
        self.telephone = XmlField('telephone')
        self.telephoneprefix = XmlField('telephoneprefix')
        self.telephonenumber = XmlField('telephonenumber')
        super(telephone, self).__init__('telephone', 'telephone')


class clientAddress(XmlModel):

    _sort_order = ('client_address', 'province', 'city', 'zipcode', 'streettype', 'street', 'streetnumber', 'portal', 'staircase', 'floor', 'door')

    def __init__(self):
        self.client_address = XmlField('clientAddress')
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
        super(clientAddress, self).__init__('clientAddress', 'client_address')
