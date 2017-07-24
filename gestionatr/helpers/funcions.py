# -*- coding: utf-8 -*-

"""Helper functions for libComXml
"""

CODIS_REFACT = {'RT42011': '40',
                'RT12012': '41',
                'RM42012': '42'}

CODIS_REG_REFACT = {'RGT42011': '40',
                    'RGT12012': '41',
                    'RGM42012': '42'}

PERIODES_AGRUPATS = [('P1', 'P4'), ('P2', 'P5'), ('P3', 'P6')]


def codi_refact(producte):
    """Retorna el codi ocsum de refacturació

    :param producte: nom del producte
    """
    return CODIS_REFACT.get(producte, False)


def nom_refact(producte):
    """Retorna el nom del producte

    :param producte: codi ocsum del producte
    """
    ref = dict(((v, k) for k, v in CODIS_REFACT.items()))
    return ref.get(producte, False)


def nom_reg_refact(producte):
    """Retorna el nom del producte

    :param producte: codi ocsum del producte
    """
    ref = dict(((v, k) for k, v in CODIS_REG_REFACT.items()))
    return ref.get(producte, False)


def parse_totals_refact(cadena):
    """Retorna els totals de les línies de refacturacio"""
    totals = []
    for i, x in enumerate(cadena.split(' ')):
        if i in (4, 7):
            totals.append(float(x))
    return totals[0], totals[1]
