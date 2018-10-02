# -*- coding: utf-8 -*-
from message_gas import MessageGas
from Deadlines import ProcessDeadline, DeadLine, Workdays, Naturaldays
from gestionatr.utils import get_rec_attr
from A1_04 import *
from gestionatr.defs_gas import SUBTYPES_A1_48


class A1_48(A1_04):

    steps = []

    @property
    def claimertype(self):
        tree = '{0}.claimertype'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def claimer(self):
        tree = '{0}.claimer'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return claimer(data)
        else:
            return False

    @property
    def claimtype(self):
        tree = '{0}.claimtype'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def claimsubtype(self):
        tree = '{0}.claimsubtype'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def originreference(self):
        tree = '{0}.originreference'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def claimreferencelist(self):
        data = []
        obj = get_rec_attr(self.obj, self._header, False)
        if (hasattr(obj, 'claimreferencelist') and
                hasattr(obj.claimreferencelist, 'claimreference')):
            for d in obj.claimreferencelist.claimreference:
                data.append(claimreference(d))
        return data

    @property
    def legallimitdate(self):
        tree = '{0}.legallimitdate'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def priority(self):
        tree = '{0}.priority'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    # step a25
    @property
    def sequential(self):
        tree = '{0}.sequential'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def interventiontype(self):
        tree = '{0}.interventiontype'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def newclaimtype(self):
        tree = '{0}.newclaimtype'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def newclaimsubtype(self):
        tree = '{0}.newclaimsubtype'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def visitdate(self):
        tree = '{0}.visitdate'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def visithour(self):
        tree = '{0}.visithour'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def informationtype(self):
        tree = '{0}.informationtype'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def resultreasonintervention(self):
        tree = '{0}.resultreasonintervention'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def informationlist(self):
        data = []
        obj = get_rec_attr(self.obj, self._header, False)
        if (hasattr(obj, 'informationlist') and
                hasattr(obj.informationlist, 'information')):
            for d in obj.informationlist.information:
                data.append(information(d))
        return data

    # step a26
    @property
    def informationdate(self):
        tree = '{0}.informationdate'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def variableinflist(self):
        data = []
        obj = get_rec_attr(self.obj, self._header, False)
        if (hasattr(obj, 'variableinflist') and
                hasattr(obj.variableinflist, 'variableinf')):
            for d in obj.variableinflist.variableinf:
                data.append(variableinf(d))
        return data

    # step a3
    @property
    def resolutiondetail(self):
        tree = '{0}.resolutiondetail'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def resolutiondetaildesc(self):
        tree = '{0}.resolutiondetaildesc'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def creditedcompensation(self):
        tree = '{0}.creditedcompensation'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def anomalyfraudrecordnum(self):
        tree = '{0}.anomalyfraudrecordnum'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def movementdate(self):
        tree = '{0}.movementdate'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False


class variableinf(object):

    def __init__(self, data):
        self.obj = data

    @property
    def moreinformationtype(self):
        tree = 'moreinformationtype'
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
    def variabletype(self):
        tree = 'variabletype'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def variablevalue(self):
        tree = 'variablevalue'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False



class information(object):

    def __init__(self, data):
        self.obj = data

    @property
    def moreinformation(self):
        tree = 'moreinformation'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def moreinformationtype(self):
        tree = 'moreinformationtype'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def limitsenddate(self):
        tree = 'limitsenddate'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False


class client(object):

    def __init__(self, data):
        self.obj = data

    @property
    def document(self):
        tree = 'document'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return document(data)
        else:
            return False

    @property
    def titulartype(self):
        tree = 'titulartype'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def name(self):
        tree = 'name'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return name(data)
        else:
            return False

    @property
    def telephone(self):
        tree = 'telephone'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return telephone(data)
        else:
            return False

    @property
    def email(self):
        tree = 'email'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def clientaddress(self):
        tree = 'clientAddress'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return clientaddress(data)
        else:
            return False


class incidentperiod(object):

    def __init__(self, data):
        self.obj = data

    @property
    def datefrom(self):
        tree = 'datefrom'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def dateto(self):
        tree = 'dateto'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False


class name(object):

    def __init__(self, data):
        self.obj = data

    @property
    def firstname(self):
        tree = 'firstname'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def familyname1(self):
        tree = 'familyname1'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def familyname2(self):
        tree = 'familyname2'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def businessname(self):
        tree = 'businessname'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False


class reading(object):

    def __init__(self, data):
        self.obj = data

    @property
    def readingdate(self):
        tree = 'readingdate'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def readingvalue(self):
        tree = 'readingvalue'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False


class claimername(object):

    def __init__(self, data):
        self.obj = data

    @property
    def claimerfirstname(self):
        tree = 'claimerfirstname'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def claimerlastname(self):
        tree = 'claimerlastname'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def claimersecondname(self):
        tree = 'claimersecondname'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def claimerbusinessname(self):
        tree = 'claimerbusinessname'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False


class telephone(object):

    def __init__(self, data):
        self.obj = data

    @property
    def telephoneprefix(self):
        tree = 'telephoneprefix'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def telephonenumber(self):
        tree = 'telephonenumber'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False


class claimer(object):

    def __init__(self, data):
        self.obj = data

    @property
    def claimerid(self):
        tree = 'claimerid'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return claimerid(data)
        else:
            return False

    @property
    def claimername(self):
        tree = 'claimername'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return claimername(data)
        else:
            return False

    @property
    def claimertelephone(self):
        tree = 'claimertelephone'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return claimertelephone(data)
        else:
            return False

    @property
    def claimeremail(self):
        tree = 'claimeremail'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False


class contact(object):

    def __init__(self, data):
        self.obj = data

    @property
    def contactname(self):
        tree = 'contactname'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def contacttelephone(self):
        tree = 'contacttelephone'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return contacttelephone(data)
        else:
            return False

    @property
    def contactemail(self):
        tree = 'contactemail'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False


class incident(object):

    def __init__(self, data):
        self.obj = data

    @property
    def incidentdate(self):
        tree = 'incidentdate'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False


class claimertelephone(object):

    def __init__(self, data):
        self.obj = data

    @property
    def claimerprefixtel1(self):
        tree = 'claimerprefixtel1'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def claimertelephone1(self):
        tree = 'claimertelephone1'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False


class claimreference(object):

    def __init__(self, data):
        self.obj = data

    @property
    def numfactura(self):
        tree = 'numfactura'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def wrongattentiontype(self):
        tree = 'wrongattentiontype'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def comreferencenum(self):
        tree = 'comreferencenum'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def targetclaimcomreferencenum(self):
        tree = 'targetclaimcomreferencenum'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def conceptcontract(self):
        tree = 'conceptcontract'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def conceptfacturation(self):
        tree = 'conceptfacturation'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def contact(self):
        tree = 'contact'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return contact(data)
        else:
            return False

    @property
    def nnssexpedient(self):
        tree = 'nnssexpedient'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def fraudrecordnum(self):
        tree = 'fraudrecordnum'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def incidentperiod(self):
        tree = 'incidentperiod'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return incidentperiod(data)
        else:
            return False

    @property
    def invoicenumber(self):
        tree = 'invoicenumber'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def incidentlocation(self):
        tree = 'incidentlocation'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return incidentlocation(data)
        else:
            return False

    @property
    def reading(self):
        tree = 'reading'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return reading(data)
        else:
            return False

    @property
    def incident(self):
        tree = 'incident'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return incident(data)
        else:
            return False

    @property
    def client(self):
        tree = 'client'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return client(data)
        else:
            return False

    @property
    def claimedcompensation(self):
        tree = 'claimedcompensation'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def iban(self):
        tree = 'iban'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False


class incidentlocation(object):

    def __init__(self, data):
        self.obj = data

    @property
    def incidentlocationdesc(self):
        tree = 'incidentlocationdesc'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def incidentlocationprovince(self):
        tree = 'incidentlocationprovince'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def incidentlocationcity(self):
        tree = 'incidentlocationcity'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def incidentlocationcitysubdivision(self):
        tree = 'incidentlocationcitysubdivision'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def incidentlocationzipcode(self):
        tree = 'incidentlocationzipcode'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False


class contacttelephone(object):

    def __init__(self, data):
        self.obj = data

    @property
    def telephoneprefix(self):
        tree = 'telephoneprefix'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def telephonenumber(self):
        tree = 'telephonenumber'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def inventat(self):
        tree = 'inventat'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False


class clientaddress(object):

    def __init__(self, data):
        self.obj = data

    @property
    def province(self):
        tree = 'province'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def city(self):
        tree = 'city'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def zipcode(self):
        tree = 'zipcode'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def streettype(self):
        tree = 'streettype'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def street(self):
        tree = 'street'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def streetnumber(self):
        tree = 'streetnumber'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def portal(self):
        tree = 'portal'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def staircase(self):
        tree = 'staircase'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def floor(self):
        tree = 'floor'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def door(self):
        tree = 'door'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False


class claimerid(object):

    def __init__(self, data):
        self.obj = data

    @property
    def claimerdocumenttype(self):
        tree = 'claimerdocumenttype'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def claimerdocumentnum(self):
        tree = 'claimerdocumentnum'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False


class claimreferencelist(object):

    def __init__(self, data):
        self.obj = data

    @property
    def claimreference(self):
        tree = 'claimreference'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return claimreference(data)
        else:
            return False


class document(object):

    def __init__(self, data):
        self.obj = data

    @property
    def documenttype(self):
        tree = 'documenttype'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def documentnum(self):
        tree = 'documentnum'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False


# Module Functions
def get_minimum_fields(r1_subtype):
    for x in SUBTYPES_A1_48:
        if x['code'] == r1_subtype:
            return x['min_fields']
    return []


def get_subtypes(r1_type):
    return [x['code'] for x in SUBTYPES_A1_48 if x['type'] == r1_type]


def get_type_from_subtype(r1_subtype):
    for x in SUBTYPES_A1_48:
        if x['code'] == r1_subtype:
            return x['type']
    return []