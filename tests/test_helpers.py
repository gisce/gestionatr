#!/usr/bin/env python
# -*- coding: utf-8 -*-
from . import unittest
from gestionatr.helpers import *
from .utils import get_data
from gestionatr.input.messages import Message


class TestsHelpers(unittest.TestCase):

    def test_codi_refact(self):
        self.assertEqual(codi_refact('RT42011'), '40')
        self.assertEqual(codi_refact('NOT_A_REFACT'), False)

    def test_nom_refact(self):
        self.assertEqual(nom_refact('40'), 'RT42011')
        self.assertEqual(nom_refact('NOT_A_REFACT'), False)

    def test_nom_ref_refact(self):
        self.assertEqual(nom_reg_refact('40'), 'RGT42011')
        self.assertEqual(nom_reg_refact('NOT_A_REFACT'), False)

    def test_parse_totals_refact(self):
        total1, total2 = parse_totals_refact(
            'Refact. T1 2012 Consum: 1740.00 kWh. Total: 48.96 €'
        )

        self.assertEqual(total1, 1740.0)
        self.assertEqual(total2, 48.96)

    def test_validate_xml(self):
        from gestionatr.utils import validate_xml
        xml_c101_minim = open(get_data("c101_minim.xml"), "r")
        xml_c101_ok = xml_c101_minim.read()
        res = validate_xml(xml_c101_ok)
        self.assertTrue(res.valid)
