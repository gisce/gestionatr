# -*- coding: utf-8 -*-
import unittest

from gestionatr.utils import get_description

from expects import *


class TestDefsTables(unittest.TestCase):
    def test_get_description(self):
        expect(
            get_description('02', 'TABLA_80')
        ).to(equal('Improcedente / Desfavorable'))

        def get_non_existent_code():
            return get_description('CODIGO_INVENTADO', 'TABLA_80')

        expect(get_non_existent_code).to(raise_error(ValueError))

        def get_non_existent_table():
            return get_description('01', 'TABLA_INVENTADA')

        expect(get_non_existent_table).to(raise_error(ValueError))
