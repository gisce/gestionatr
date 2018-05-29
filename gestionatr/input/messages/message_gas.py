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
})

MAIN_MESSAGE_XSD.update({
    'A141': 'a141',
    'A241': 'a241',
    'A341': 'a341',
    'A441': 'a441',
    'A3S41': 'a3s41',
})


class MessageGas(Message):
    """Clase base intercambio información comer-distri GAS"""

    def __init__(self, xml, force_tipus=None):
        super(Message, self).__init__(xml, force_tipus=force_tipus)
        self.processcode = self.tipus
        self.messagetype = self.pas
        self.main_message = ''

    def set_head(self):
        obj = objectify.fromstring(self.str_xml)
        self.head = obj.heading

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
            msg = u'No se puede identificar el código de proceso ' \
                  u'o código de paso'
            raise except_f1('Error', msg)


    # Funcions relacionades amb la capçalera del XML
    @property
    def get_codi_emisor(self):
        ref = self.head.dispatchingcompany.text
        if not ref:
            raise except_f1('Error', u'Documento sin emisor')
        return ref

    @property
    def get_codi_destinatari(self):
        ref = self.head.destinycompany.text
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
        ref = self.head.communicationsdate.text
        if not ref:
            raise except_f1('Error', u'Documento sin fecha de solicitud')
        return ref + " " + self.head.communicationshour.text
