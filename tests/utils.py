import os
from gestionatr.output.messages.base import Cabecera
from . import unittest

_ROOT = os.path.abspath(os.path.dirname(__file__))


def get_data(path):
    filename = isinstance(path, (list, tuple)) and path[0] or path
    return os.path.join(_ROOT, 'data', filename)


def get_header(process='C1', step='01', code='201607211259', date='2016-07-21T12:59:47'):
    header = Cabecera()
    vals = {
        'codigo_del_proceso': process,
        'codigo_del_paso': step,
        'codigo_de_solicitud': code,
        'secuencial_de_solicitud': '01',
        'cups': 'ES1234000000000001JN0F',
        'codigo_ree_empresa_emisora': '1234',
        'codigo_ree_empresa_destino': '4321',
        'fecha': date,
    }
    header.feed(vals)
    return header


def assertXmlEqual(got, want):
    from lxml.doctestcompare import LXMLOutputChecker
    from doctest import Example

    checker = LXMLOutputChecker()
    if checker.check_output(want, got, 0):
        return
    message = checker.output_difference(Example("", want), got, 0)
    raise AssertionError(message)

unittest.TestCase.assertXmlEqual = assertXmlEqual
unittest.TestCase.__str__ = unittest.TestCase.id