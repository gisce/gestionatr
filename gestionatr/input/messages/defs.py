# -*- coding: utf-8 -*-

# Definició de variables de llibreria
# Taula 107 del document d'OCSUM:
# OCSUM - E - Tablas de códigos 2012.05.23.doc
INFO_TARIFA = {
             #ocsum    descripcio  marge_reactiva   agrupar_consums
             '001': {'name': '2.0A', 'marge': 0.5, 'agrupat': False,
                     'reactiva': ['P1']},
             '005': {'name': '2.1A', 'marge': 0.5, 'agrupat': False,
                     'reactiva': ['P1']},
             '004': {'name': '2.0DHA', 'marge': 0.5, 'agrupat': False,
                     'reactiva': ['P1']},
             '007': {'name': '2.0DHS', 'marge': 0.5, 'agrupat': False,
                     'reactiva': ['P1']},
             '006': {'name': '2.1DHA', 'marge': 0.5, 'agrupat': False,
                     'reactiva': ['P1']},
             '008': {'name': '2.1DHS', 'marge': 0.5, 'agrupat': False,
                     'reactiva': ['P1']},
             '003': {'name': '3.0A', 'marge': 0.33, 'agrupat': True,
                     'reactiva': ['P1', 'P2']},
             '011': {'name': '3.1A', 'marge': 0.33, 'agrupat': True,
                     'reactiva': ['P1', 'P2']},
             '012': {'name': '6.1A', 'marge': 0.33, 'agrupat': False,
                     'reactiva': ['P1', 'P2', 'P3', 'P4', 'P5']},
             '013': {'name': '6.2', 'marge': 0.33, 'agrupat': False,
                     'reactiva': ['P1', 'P2', 'P3', 'P4', 'P5']},
             '014': {'name': '6.3', 'marge': 0.33, 'agrupat': False,
                     'reactiva': ['P1', 'P2', 'P3', 'P4', 'P5']},
             '015': {'name': '6.4', 'marge': 0.33, 'agrupat': False,
                     'reactiva': ['P1', 'P2', 'P3', 'P4', 'P5']},
             '016': {'name': '6.5', 'marge': 0.33, 'agrupat': False,
                     'reactiva': ['P1', 'P2', 'P3', 'P4', 'P5']},
             '017': {'name': '6.1B', 'marge': 0.33, 'agrupat': False,
                     'reactiva': ['P1', 'P2', 'P3', 'P4', 'P5']},
          }
