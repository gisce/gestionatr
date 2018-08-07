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

    def test_atr_test_default_e(self):
        runner = CliRunner()

        result = runner.invoke(test, ['-f', get_data('f101_factura_atr.xml')])
        expect(result.output).to(equal('Correct File\n'))

    def test_atr_test_e(self):
        runner = CliRunner()

        result = runner.invoke(test, ['-s' ,'e', '-f', get_data('f101_factura_atr.xml')])
        expect(result.output).to(equal('Correct File\n'))

    def test_atr_test_e_fails(self):
        runner = CliRunner()

        result = runner.invoke(test, ['-s', 'e', '-f', get_data('f101_factura_atr_bad.xml')])
        expect(result.output).to(start_with('WARNING: Invalid File: '))

    def test_atr_test_e_no_e(self):
        runner = CliRunner()

        result = runner.invoke(test, ['-s', 'e', '-f', get_data('a441.xml')])
        expect(result.output).to(start_with('WARNING: Invalid File: '))

    def test_atr_test_g(self):
        runner = CliRunner()

        result = runner.invoke(test, ['-s', 'g', '-f', get_data('a441.xml')])
        expect(result.output).to(equal('Correct File\n'))

    def test_atr_test_g_fails(self):
        runner = CliRunner()

        result = runner.invoke(test, ['-s', 'g', '-f', get_data('a441_bad.xml')])
        expect(result.output).to(start_with('WARNING: Invalid File: '))

    def test_atr_test_g_no_g(self):
        runner = CliRunner()

        result = runner.invoke(test, ['-s', 'g', '-f', get_data('f101_factura_atr.xml')])
        expect(result.output).to(start_with('WARNING: Invalid File: '))
