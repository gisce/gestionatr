#!/usr/bin/env python
# -*- coding: utf-8 -*-
from . import unittest
from .utils import get_data
from gestionatr.input.messages import C1


class test_MessageBase(unittest.TestCase):

    def setUp(self):
        self.xml_c101_cabecera = open(get_data("c101.xml"), "r")

    def tearDown(self):
        self.xml_c101_cabecera.close()

    def test_cabecera_model(self):
        c = C1(self.xml_c101_cabecera)
        c.parse_xml()
        self.assertEqual(c.tipus, 'C1')
        self.assertEqual(c.pas, '01')
        self.assertEqual(c.get_pas_xml(), '01')
        self.assertEqual(c.get_codi_emisor, '1234')
        self.assertEqual(c.get_codi_destinatari, '4321')
        self.assertEqual(c.cups, 'ES1234000000000001JN0F')
        self.assertEqual(c.codi_sollicitud, '201607211259')
        self.assertEqual(c.seq_sollicitud, '01')
        self.assertEqual(c.data_sollicitud, '2016-07-21 12:59:47')






