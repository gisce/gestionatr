#!/usr/bin/env python
# -*- coding: utf-8 -*-
from click.testing import CliRunner
from .utils import get_data
from gestionatr.cli import atr, test
from gestionatr import __version__
from . import unittest
from expects import *


class CommandTest(unittest.TestCase):
    def test_version(self):
        runner = CliRunner()

        result = runner.invoke(atr, ['--version'])
        expect(result.output).to(
            equal('ATR library version (gestionatr) : {}\n'.format(__version__)))

    def test_atr_test(self):
        runner = CliRunner()

        result = runner.invoke(test, ['-f', get_data('f101_factura_atr.xml')])
        expect(result.output).to(equal('Correct File\n'))
