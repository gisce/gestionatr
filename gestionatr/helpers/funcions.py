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


def extreu_periode(name):
    """Extreu el nom del període del name de la lectura
    """
    if '(' not in name:
        return name
    return name.split('(')[-1].split(')')[0]


def codi_periode(codi_dh, periode):
    """Retorna el codi OCSUM del periode segons
       http://172.26.0.42:2500/wiki/show/Codificacio_Periodes_OCSUM
       Taula 42 del document d'OCSUM:
       OCSUM - E - Tablas de códigos 2012.05.23.doc

    :param codi_dh: codi dh de la tarifa
    :param periode: nom del periode en format Px on x = {1...6}
    """

    if codi_dh == '1':
        return '10'
    else:
        return '%s%s' % (codi_dh, periode[-1])


def codi_dh(tarifa, nlectures=6):
    """Retorna el codi ocsum de discriminació horaria
       Taules 35 i 107 del document d'OCSUM:
       OCSUM - E - Tablas de códigos 2012.05.23.doc

    :param tarifa: codi de la tarifa
    :param nlectures: nombre de lectures
    """

    if tarifa in ('001', '005'):
        return '1'
    elif tarifa in ('004', '006'):
        return '2'
    elif tarifa in ('003', '012', '013', '014', '015', '016', '017'):
        return '6'
    elif tarifa == '011':
        if nlectures in (6, 5):
            return '6'
        else:
            return '3'
    elif tarifa in ('007', '008'):
        return '8'
