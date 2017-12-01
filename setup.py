# -*- coding: utf-8 -*-
"""Setup per la llibreria de gestionatr"""
from __future__ import print_function

import os
import shutil
from distutils.command.clean import clean as _clean
from setuptools import setup, find_packages
from gestionatr import __version__

PACKAGES_DATA = {'gestionatr': ['data/*.xsd']}

with open('requirements.txt', 'r') as f:
    INSTALL_REQUIRES = f.readlines()

with open('requirements-dev.txt', 'r') as f:
    TESTS_REQUIRE = f.readlines()


class Clean(_clean):
    """Eliminem el directory build i els bindings creats."""

    def run(self):
        """Comença la tasca de neteja."""
        _clean.run(self)
        if os.path.exists(self.build_base):
            print("Cleaning {} dir".format(self.build_base))
            shutil.rmtree(self.build_base)


setup(
    name='gestionatr',
    description='Llibreria de Gestió ATR',
    author='GISCE Enginyeria',
    author_email='devel@gisce.net',
    url='http://www.gisce.net',
    version=__version__,
    license='General Public Licence 2',
    long_description='''Long description''',
    provides=['gestionatr'],
    install_requires=INSTALL_REQUIRES,
    tests_require=TESTS_REQUIRE,
    packages=find_packages(),
    package_data=PACKAGES_DATA,
    scripts=[],
    cmdclass={'clean': Clean},
    test_suite='tests',
    entry_points='''
      [console_scripts]
      atr=gestionatr.cli:atr
    '''
)
