# -*- coding: utf-8 -*-
import unittest

from gestionatr.utils import get_description

from expects import *


class TestDefsTables(unittest.TestCase):
    def test_get_description(self):
        expect(
            get_description('02', 'TABLA_80')
        ).to(equal('Improcedente / Desfavorable'))

        expect(
            get_description('CODIGO_INVENTADO', 'TABLA_80')
        ).to(raise_error(ValueError))

        expect(
            get_description('01', 'TABLA_INVENTADA')
        ).to(raise_error(ValueError))
