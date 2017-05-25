# -*- coding: utf-8 -*-
"""Setup per la llibreria de gestionatr"""
import os
import shutil
from distutils.command.clean import clean as _clean
from setuptools import setup, find_packages
from gestionatr import __version__

PACKAGES_DATA = {'gestionatr': ['data/*.xsd']}


class Clean(_clean):
    """Eliminem el directory build i els bindings creats."""
    def run(self):
        """Comença la tasca de neteja."""
        _clean.run(self)
        if os.path.exists(self.build_base):
            print "Cleaning %s dir" % self.build_base
            shutil.rmtree(self.build_base)

setup(name='gestionatr',
      description='Llibreria de Gestió ATR',
      author='GISCE Enginyeria',
      author_email='devel@gisce.net',
      url='http://www.gisce.net',
      version=__version__,
      license='General Public Licence 2',
      long_description='''Long description''',
      provides=['gestionatr'],
      install_requires=['lxml>=3.7.3', 'libcomxml', 'workdays'],
      tests_require=['expects'],
      packages=find_packages(),
      package_data=PACKAGES_DATA,
      scripts=[],
      cmdclass={'clean': Clean},
      test_suite='tests',
)

