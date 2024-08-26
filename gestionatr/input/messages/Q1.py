# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from .message import Message
from datetime import datetime
from gestionatr.utils import get_rec_attr
from .Deadlines import ProcessDeadline

MAGNITUDS_OCSUM = {
    'AE': 'A',
    'AS': 'S',
    'R1': 'R',
    'R4': 'RC',
    'PM': 'M',
    'EP': 'EP'
}

# Retorna el nom de periode segons el periode d'OCSUM
PERIODE_OCSUM = {
    '01': 'P1',  # Punta + Llano
    '03': 'P2',  # Valle
    '10': 'P1',  # Totalizador (2.0A y 2.1A)
    '20': 'P1',  # Totalizador (2.1DHA y 2.0DHA)
    '21': 'P1',  # P1 Tarifes: 004, 006
    '22': 'P2',  # P2 Tarifes: 004, 006
    '31': 'P1',  # P1 Tarifa 003
    '32': 'P2',  # P2 Tarifa 003
    '33': 'P3',  # P3 Tarifa 003
    '41': 'P1',  # P1 Tarifa 011
    '42': 'P2',  # P2 Tarifa 011
    '43': 'P3',  # P3 Tarifa 011
    '61': 'P1',  # Periodo 1 Tarifes: 003, 011, 012 - 017
    '62': 'P2',  # Periodo 2 Tarifes: 003, 011, 012 - 017
    '63': 'P3',  # Periodo 3 Tarifes: 003, 011, 012 - 017
    '64': 'P4',  # Periodo 4 Tarifes: 003, 011, 012 - 017
    '65': 'P5',  # Periodo 5 Tarifes: 003, 011, 012 - 017
    '66': 'P6',  # Periodo 6 Tarifes: 003, 011, 012 - 017
    '80': 'P1',  # Totalizador Maximetro Tarifa 007
    '81': 'P1',  # P1 Tarifa 007
    '82': 'P2',  # P2 Tarifa 007
    '83': 'P3',  # P3 Tarifa 007
    '90': 'P1',  # P1 de peaje de acceso 2.0TD.
    '91': 'P1',  # P1 de peaje de acceso 2.0TD.
    '92': 'P2',  # P2 de peaje de acceso 2.0TD.
    '93': 'P3',  # P3 de peaje de acceso 2.0TD.
    'A0': 'P1',  # P1 de los peajes de acceso 3.0TD, 3.0TDVE, 6.1TD, 6.1TDVE, 6.2TD. 6.3TD. 6.4TD
    'A1': 'P1',  # P1 de los peajes de acceso 3.0TD, 3.0TDVE, 6.1TD, 6.1TDVE, 6.2TD. 6.3TD. 6.4TD
    'A2': 'P2',  # P2 de los peajes de acceso 3.0TD, 3.0TDVE, 6.1TD, 6.1TDVE, 6.2TD. 6.3TD. 6.4TD
    'A3': 'P3',  # P3 de los peajes de acceso 3.0TD, 3.0TDVE, 6.1TD, 6.1TDVE, 6.2TD. 6.3TD. 6.4TD
    'A4': 'P4',  # P4 de los peajes de acceso 3.0TD, 3.0TDVE, 6.1TD, 6.1TDVE, 6.2TD. 6.3TD. 6.4TD
    'A5': 'P5',  # P5 de los peajes de acceso 3.0TD, 3.0TDVE, 6.1TD, 6.1TDVE, 6.2TD. 6.3TD. 6.4TD
    'A6': 'P6',  # P6 de los peajes de acceso 3.0TD, 3.0TDVE, 6.1TD, 6.1TDVE, 6.2TD. 6.3TD. 6.4TD

}

SKIP_TOTALITZADORS = ('00', '60')

class Q1(Message, ProcessDeadline):
    """Clase que implementa Q1."""

    @property
    def cod_pm(self):
        tree = '{0}.CodPM'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data:
            return data.text
        else:
            return False

    @property
    def medidas(self):
        medidas = []
        data = get_rec_attr(self.obj, 'Medidas')
        for medida in data:
            medidas.append(Medida(medida))

        return medidas

    @property
    def comptadors(self):
        """Retorna totes les lectures en una llista de comptadors"""
        contadores_agrupados = {}
        for medida in self.medidas:
            for aparato in medida.aparatos:
                contadores_agrupados.setdefault(
                    aparato.numero_serie, []
                ).append(aparato)

        contadores = []
        for lista_aparatos in contadores_agrupados.values():
            fd = aparato.fecha_desde
            fh = aparato.fecha_hasta
            contadores.append((fd, fh, aparato))
        return [a[2] for a in sorted(contadores, key=lambda x: x[0])]

class Medida(object):
    def __init__(self, data):
        self.datos_medida = data

    @property
    def cod_pm(self):
        cod_pm = self.datos_medida.CodPM
        return cod_pm

    @property
    def aparatos(self):
        aparatos = []
        data = get_rec_attr(self.datos_medida, 'ModeloAparato')
        for aparato in data:
            aparatos.append(ModeloAparato(aparato))
        return aparatos

class ModeloAparato(object):

    def __init__(self, data):
        self.modelo_aparato = data

    @property
    def tipo_aparato(self):
        data = ''
        try:
            data = self.modelo_aparato.TipoAparato.text
        except AttributeError:
            pass
        return data

    @property
    def marca_aparato(self):
        data = ''
        try:
            data = self.modelo_aparato.MarcaAparato.text
        except AttributeError:
            pass
        return data

    @property
    def numero_serie(self):
        data = ''
        try:
            data = self.modelo_aparato.NumeroSerie.text
        except AttributeError:
            pass
        return data

    @property
    def tipo_dhedm(self):
        data = ''
        try:
            data = self.modelo_aparato.TipoDHEdM.text
        except AttributeError:
            pass
        return data

    @property
    def integradores(self):
        integradores = []
        data = get_rec_attr(self.modelo_aparato, 'Integrador')
        for i in data:
            integradores.append(Integrador(i))
        return integradores

    @property
    def fecha_desde(self):
        fecha_desde = False
        for integrador in self.integradores:
            fecha_in_compt = datetime.strptime(
                integrador.lectura_desde.fecha[:10], '%Y-%m-%d'
            )
            if not fecha_desde or fecha_in_compt < fecha_desde:
                fecha_desde = fecha_in_compt

        return fecha_desde

    @property
    def fecha_hasta(self):
        fecha_hasta = False
        for integrador in self.integradores:
            fecha_fi_compt = datetime.strptime(
                integrador.lectura_hasta.fecha[:10], '%Y-%m-%d'
            )
            if not fecha_hasta or fecha_fi_compt > fecha_hasta:
                fecha_hasta = fecha_fi_compt

        return fecha_hasta

    @property
    def lectures(self,  tipos=None):
        """Retorna totes les lectures en una llista de Lectura"""
        lectures = []
        try:
            for integrador in self.integradores:
                if not tipos or (integrador.tipus and integrador.tipus in tipos):
                    integrador.comptador = self
                    lectures.append(integrador)
        except AttributeError:
            pass
        lectures = sorted(lectures, key=lambda x: x.lectura_desde.fecha)
        return lectures

    @property
    def gir_contador(self):
        giros_lect = [
            int.gir_contador for int in self.integradores
        ]

        return max(giros_lect)

class Integrador(object):

    def __init__(self, data):
        self.integrador = data
        self._lectura_desde = None
        self._lectura_hasta = None
        self._magnitud = None
        self._periode = None
        self._numero_ruedas_enteras = None
        self._ajuste = None
        self.comptador = None

    @property
    def tipus(self):
        return MAGNITUDS_OCSUM.get(self.magnitud)

    @property
    def ometre(self):
        return self.codigo_periodo in SKIP_TOTALITZADORS

    @property
    def magnitud(self):
        data = ''
        try:
            data = self.integrador.Magnitud.text
        except AttributeError:
            pass
        return data

    @property
    def periode(self):
        p = PERIODE_OCSUM.get(self.codigo_periodo, None)
        if not p and self.codigo_periodo in PERIODE_OCSUM.values():
            return self.codigo_periodo
        if self.codigo_periodo == '93' and p == 'P3' and self.magnitud in ('PM', 'EP'):
            return "P2"
        return p

    @property
    def codigo_periodo(self):
        data = ''
        try:
            data = self.integrador.CodigoPeriodo.text
        except AttributeError:
            pass
        return data

    @property
    def constante_multiplicadora(self):
        data = ''
        try:
            data = self.integrador.ConstanteMultiplicadora.text
        except AttributeError:
            pass
        return data

    @property
    def numero_ruedas_enteras(self):
        data = False
        try:
            data = int(self.integrador.NumeroRuedasEnteras.text)
        except AttributeError:
            pass
        return data

    @property
    def numero_ruedas_decimales(self):
        data = False
        try:
            data = int(self.integrador.NumeroRuedasDecimales.text)
        except AttributeError:
            pass
        return data

    @property
    def gir_contador(self):
        ruedas_enteras = self.numero_ruedas_enteras
        if ruedas_enteras == 99:
            return 10
        return (10 ** ruedas_enteras)

    @property
    def consumo_calculado(self):
        data = False
        try:
            data = float(self.integrador.ConsumoCalculado.text.strip())
        except AttributeError:
            pass
        return data

    @property
    def lectura_desde(self):
        data = ''
        try:
            data = LecturaInfo(self.integrador.LecturaDesde)
        except AttributeError:
            pass
        return data

    @property
    def fecha_lectura_desde(self):
        return self.lectura_desde.fecha

    def valor_lectura_desde(self):
        return self.lectura_desde.lectura

    @property
    def lectura_hasta(self):
        data = ''
        try:
            data = LecturaInfo(self.integrador.LecturaHasta)
        except AttributeError:
            pass
        return data

    @property
    def fecha_lectura_hasta(self):
        return self.lectura_hasta.fecha

    @property
    def valor_lectura_hasta(self):
        return self.lectura_hasta.lectura


    @property
    def ajuste(self):
        data = ''
        try:
            data = Ajuste(self.integrador.Ajuste)
        except AttributeError:
            pass
        return data

    @property
    def anomalia(self):
        data = ''
        try:
            data = Anomalia(self.integrador.Anomalia)
        except AttributeError:
            pass
        return data

    @property
    def fecha_hora_maximetro(self):
        data = False
        try:
            data = self.integrador.FechaHoraMaximetro.text
        except AttributeError:
            pass
        return data


class LecturaInfo(object):

    def __init__(self, data):
        self.lect = data

    @property
    def fecha(self):
        data = False
        try:
            data = self.lect.Fecha.text
        except AttributeError:
            pass
        return data

    @property
    def procedencia(self):
        data = ''
        try:
            data = self.lect.Procedencia.text
        except AttributeError:
            pass
        return data

    @property
    def lectura(self):
        data = False
        try:
            data = float(self.lect.Lectura.text.strip())
        except AttributeError:
            pass
        return data


class Ajuste(object):

    def __init__(self, data):
        self.ajuste = data

    @property
    def codigo_motivo_ajuste(self):
        data = ''
        try:
            data = self.ajuste.CodigoMotivoAjuste.text
        except AttributeError:
            pass
        return data

    @property
    def ajuste_por_integrador(self):
        data = ''
        try:
            data = self.ajuste.AjustePorIntegrador.text
        except AttributeError:
            pass
        return data

    @property
    def comentarios(self):
        data = ''
        try:
            data = self.ajuste.Comentarios.text
        except AttributeError:
            pass
        return data


class Anomalia(object):

    def __init__(self, data):
        self.anomalia = data

    @property
    def tipo_anomalia(self):
        data = ''
        try:
            data = self.anomalia.TipoAnomalia.text
        except AttributeError:
            pass
        return data

    @property
    def comentarios(self):
        data = ''
        try:
            data = self.anomalia.Comentarios.text
        except AttributeError:
            pass
        return data

