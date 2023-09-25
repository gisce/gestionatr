# -*- coding: utf-8 -*-

from libcomxml.core import XmlModel, XmlField
from gestionatr.output.messages.base_gas import Cabecera


class MensajeA529(XmlModel):
    _sort_order = ('mensaje', 'cabecera', 'a529')

    def __init__(self):
        self.doc_root = None
        self.mensaje = XmlField(
            'sctdapplication', attributes={'xmlns': 'http://localhost/sctd/A529'}
        )
        self.cabecera = Cabecera()
        self.a529 = A529()
        super(MensajeA529, self).__init__('sctdapplication', 'mensaje')


class A529(XmlModel):
    _sort_order = (
        'a529', 'fechacreacion', 'horacreacion', 'cups', 'historicoconsumo', 'validacioncliente'
    )

    def __init__(self):
        self.a529 = XmlField('a529')
        self.fechacreacion = XmlField('fechacreacion')
        self.horacreacion = XmlField('horacreacion')
        self.cups = XmlField('cups')
        self.historicoconsumo = XmlField('historicoconsumo')
        self.validacioncliente = ValidacionClienteA529()

        super(A529, self).__init__('a529', 'a529')


class ValidacionClienteA529(XmlModel):
    _sort_order = (
        'validacioncliente', 'tipodocumento', 'numdocumento'
    )

    def __init__(self):
        self.validacioncliente = XmlField('validacioncliente')
        self.tipodocumento = XmlField('tipodocumento')
        self.numdocumento = XmlField('numdocumento')

        super(ValidacionClienteA529, self).__init__('validacioncliente', 'validacioncliente')


GAS_ENVELOPE_TEMPLATE_AMB_NAMESPACE_AL_PAS = """
<soap:Envelope 
xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" 
xmlns:eleg="http://localhost/sctd/wsrps"
>
    <soap:Header />
    <soap:Body>
        <eleg:consultaCups>
            <eleg:consultaCups>
                {xml_str}
            </eleg:consultaCups>
        </eleg:consultaCups>
    </soap:Body>
</soap:Envelope>
"""

GAS_ENVELOPE_TEMPLATE_SENSE_NAMESPACE_AL_PAS01 = """
<soap:Envelope 
xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" 
xmlns:eleg="http://localhost/sctd/wsrps"
>
    <soap:Header />
    <soap:Body>
        <eleg:consultaCups>
            <consultaCups>
                {xml_str}
            </consultaCups>
        </eleg:consultaCups>
    </soap:Body>
</soap:Envelope>
"""

GAS_ENVELOPE_TEMPLATE_CHATGPT = """
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:wsrps="http://localhost/sctd/wsrps" xmlns:a529="http://localhost/sctd/A529">
   <soapenv:Header/>
   <soapenv:Body>
      <wsrps:consultaCups>
         <wsrps:consultaCups>
{xml_str}
         </wsrps:consultaCups>
      </wsrps:consultaCups>
   </soapenv:Body>
</soapenv:Envelope>
"""


ENVELOP_GAS_BY_DISTR = {
    'altres': {
        'template': GAS_ENVELOPE_TEMPLATE_SENSE_NAMESPACE_AL_PAS01,
        'extra_headers': {
            "soapAction": ""
        },
    },
    'reintent': {
        'template': GAS_ENVELOPE_TEMPLATE_AMB_NAMESPACE_AL_PAS,
        'extra_headers': {
            "soapAction": ""
        },
    },
    'reintent2': {
        'template': GAS_ENVELOPE_TEMPLATE_CHATGPT,
        'extra_headers': {
            "soapAction": ""
        },
    },
    'reintent3': {
        'template': GAS_ENVELOPE_TEMPLATE_CHATGPT,
        'extra_headers': {
        },
    },
}
