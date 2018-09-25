# -*- coding: utf-8 -*-
from lxml import objectify, etree
from gestionatr import utils
from message import XSD_DATA, MAIN_MESSAGE_XSD, Message, except_f1
from gestionatr.utils import get_rec_attr

XSD_DATA.update({
    '41': {
        'A1': 'A141.xsd',
        'A2': 'A241.xsd',
        'A3': 'A341.xsd',
        'A4': 'A441.xsd',
        'A3S': 'A3S41.xsd',
    },
    'B70': {
        '31': 'B7031.xsd',
        '32': 'B7032.xsd',
        '33': 'B7033.xsd',
    },
    '02': {
        'A1': 'A102.xsd',
        'A2': 'A202.xsd',
        'A3': 'A302.xsd',
        'A4': 'A402.xsd',
        'A3S': 'A3S02.xsd',
    },
    '05': {
        'A1': 'A105.xsd',
        'A2': 'A205.xsd',
        'A3': 'A305.xsd',
        'A4': 'A405.xsd',
    },
    '44': {
        'A1': 'A144.xsd',
        'A2': 'A244.xsd',
        'A3': 'A344.xsd',
        'A4': 'A444.xsd',
    },
    '03': {
        'A1': 'A103.xsd',
        'A2': 'A203.xsd',
        'A2S': 'A2S03.xsd',
    },
    '04': {
        'A1': 'A104.xsd',
        'A2': 'A204.xsd',
        'A3': 'A304.xsd',
        'A4': 'A404.xsd',
    },
    '48': {
        'A1': 'A148.xsd',
        'A2': 'A248.xsd',
        'A25': 'A2548.xsd',
        'A26': 'A2648.xsd',
        'A3': 'A348.xsd',
    },
})

MAIN_MESSAGE_XSD.update({
    # 41
    'A141': 'a141',
    'A241': 'a241',
    'A341': 'a341',
    'A441': 'a441',
    'A3S41': 'a3s41',
    'B7031': 'factura',
    'B7032': 'factura',
    'B7033': 'factura',
    # 02
    'A102': 'a102',
    'A202': 'a202',
    'A302': 'a302',
    'A402': 'a402',
    'A3S02': 'a3s02',
    # 05
    'A105': 'a105',
    'A205': 'a205',
    'A305': 'a305',
    'A405': 'a405',
    # 44
    'A144': 'a1',
    'A244': 'a2',
    'A344': 'a3',
    'A444': 'a4',
    # 03
    'A103': 'a103',
    'A203': 'a203',
    'A2S03': 'a2s03',
    # 48
    'A148': 'a1',
    'A248': 'a2',
    'A2548': 'a25',
    'A2648': 'a26',
    'A348': 'a3',
    # 04
    'A104': 'a104',
    'A204': 'a204',
    'A304': 'a304',
    'A404': 'a404',
})


class MessageGas(Message):
    """Clase base intercambio información comer-distri GAS"""

    def __init__(self, xml, force_tipus=None):
        super(Message, self).__init__(xml, force_tipus=force_tipus)
        self.processcode = self.tipus
        self.messagetype = self.pas
        self.codtipomensaje = self.tipus
        self.codproceso = self.pas
        self.main_message = ''

    def set_head(self):
        obj = objectify.fromstring(self.str_xml)
        try:
            self.head = obj.heading
        except Exception as e:
            self.head = obj.cabecera

    def set_tipus(self):
        """Definir tipo del mensaje"""
        try:
            # Per mantenir compatibilitat utilitzem els mateixos atributs que en
            # electricitat peró per seguir amb l'estandard de utilizar els noms
            # dels XMLs els copiem a nous atributs
            self.tipus = self.head.processcode.text
            self.processcode = self.tipus
            self.pas = self.head.messagetype.text
            self.messagetype = self.pas
        except:
            try:
                self.tipus = self.head.codtipomensaje.text
                self.codtipomensaje = self.tipus
                self.pas = self.head.codproceso.text
                self.codproceso = self.pas
            except:
                msg = u'No se puede identificar el código de proceso ' \
                      u'o código de paso'
                raise except_f1('Error', msg)


    # Funcions relacionades amb la capçalera del XML
    @property
    def get_codi_emisor(self):
        try:
            ref = self.head.dispatchingcompany.text
        except:
            try:
                ref = self.head.empresaemisora.text
            except:
                pass
        if not ref:
            raise except_f1('Error', u'Documento sin emisor')
        return ref

    @property
    def get_codi_destinatari(self):
        try:
            ref = self.head.destinycompany.text
        except:
            try:
                ref = self.head.empresadestino.text
            except:
                pass
        if not ref:
            raise except_f1('Error', u'Documento sin destinatario')
        return ref

    @property
    def cups(self):
        tree = '{0}.cups'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data not in [None, False]:
            return data.text
        else:
            raise except_f1('Error', u'Documento sin código')

    @property
    def codi_sollicitud(self):
        if self.tipus == 'B70':
            return ""
        tree = '{0}.comreferencenum'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data not in [None, False]:
            return data.text
        else:
            tree = '{0}.reqcode'.format(self._header)
            data = get_rec_attr(self.obj, tree, False)
            if data not in [None, False]:
                return data.text
            raise except_f1('Error', u'Documento sin código de solicitud')

    @property
    def data_sollicitud(self):
        try:
            ref = self.head.communicationsdate.text
            ref2 = self.head.communicationshour.text
        except:
            try:
                ref = self.head.fechacomunic.text
                ref2 = self.head.horacomunic.text
            except:
                pass
        if not ref:
            raise except_f1('Error', u'Documento sin fecha de solicitud')
        return ref + " " + ref2


class except_b70(except_f1):
    def __init__(self, name, value, values_dict=None):
        self.name = name
        self.value = value
        self.values_dict = values_dict or {}
