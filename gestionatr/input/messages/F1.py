# -*- coding: utf-8 -*-
from message import Message
from gestionatr.input.messages.C2 import Direccion
from gestionatr.defs import TARIFES_SEMPRE_MAX, TARIFES_TD
from datetime import datetime, date, timedelta
from gestionatr.utils import repartir_consums_entre_lectures

# Magnituds d'OCSUM
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

PERIODES_NO_TD = [x for x in PERIODE_OCSUM.keys() if x[0] not in ['A', '9']]

CODIS_REG_REFACT = {
    'RGT42011': '40',
    'RGT12012': '41',
    'RGM42012': '42',
}

CODIS_AUTOCONSUM = {
    '51': 'autoconsum',
    '52': 'autoconsum',
    '53': 'autoconsum',
    '54': 'autoconsum',
    '55': 'autoconsum',
    '56': 'autoconsum',
    '61': 'generacio',
    '62': 'generacio',
    '63': 'generacio',
    '64': 'generacio',
    '65': 'generacio',
    '66': 'generacio',
    '71': 'excedent',
    '72': 'excedent',
    '73': 'excedent',
    '74': 'excedent',
    '75': 'excedent',
    '76': 'excedent',
    '81': 'informacio',
    '82': 'informacio',
}

# Totalitzadors a ignorar
SKIP_TOTALITZADORS = ('00', '60')

PERIODES_PER_TARIFA = {
    '018': {
        'A': 3,
        'S': 3,
        'R': 3,
        'RC': 3,
        'M': 2,
        'EP': 2,
    },
    '019': {
        'A': 6,
        'S': 6,
        'R': 6,
        'RC': 6,
        'M': 6,
        'EP': 6,
    },
    '021': {
        'A': 6,
        'S': 6,
        'R': 6,
        'RC': 6,
        'M': 6,
        'EP': 6,
    },
    '022': {
        'A': 6,
        'S': 6,
        'R': 6,
        'RC': 6,
        'M': 6,
        'EP': 6,
    },
    '023': {
        'A': 6,
        'S': 6,
        'R': 6,
        'RC': 6,
        'M': 6,
        'EP': 6,
    },
    '024': {
        'A': 6,
        'S': 6,
        'R': 6,
        'RC': 6,
        'M': 6,
        'EP': 6,
    },
    '025': {
        'A': 6,
        'S': 6,
        'R': 6,
        'RC': 6,
        'M': 6,
        'EP': 6,
    },
}


class F1(Message):
    """Clase que implementa F1."""

    @property
    def otras_facturas(self):
        data = []
        if hasattr(self.obj, 'Facturas'):
            if hasattr(self.obj.Facturas, 'OtrasFacturas'):
                for d in self.obj.Facturas.OtrasFacturas:
                    data.append(OtraFactura(d))
        return data

    @property
    def facturas_atr(self):
        data = []
        if hasattr(self.obj, 'Facturas'):
            if hasattr(self.obj.Facturas, 'FacturaATR'):
                for d in self.obj.Facturas.FacturaATR:
                    data.append(FacturaATR(d))
        return data

    @property
    def registro(self):
        if hasattr(self.obj, 'Facturas'):
            if hasattr(self.obj.Facturas, 'RegistroFin'):
                return RegistroFin(self.obj.Facturas.RegistroFin)
        return None


class Expediente(object):

    def __init__(self, data):
        self.expediente = data

    @property
    def numero_expediente(self):
        if hasattr(self.expediente, 'NumeroExpediente'):
            return self.expediente.NumeroExpediente.text.strip()
        return None

    @property
    def codigo_solicitud(self):
        if hasattr(self.expediente, 'CodigoSolicitud'):
            return self.expediente.CodigoSolicitud.text.strip()
        return None


class DatosGenerales(object):

    def __init__(self, data):
        self.datos_generales = data

    @property
    def direccion_suministro(self):
        if hasattr(self.datos_generales, 'DireccionSuministro'):
            return Direccion(self.datos_generales.DireccionSuministro)

    @property
    def cliente(self):
        if hasattr(self.datos_generales, 'Cliente'):
            return Cliente(self.datos_generales.Cliente)

    @property
    def cod_contrato(self):
        if hasattr(self.datos_generales, 'CodContrato'):
            return self.datos_generales.CodContrato.text.strip()
        return None

    @property
    def _datos_generales_factura(self):
        if hasattr(self.datos_generales, 'DatosGeneralesFactura'):
            return self.datos_generales.DatosGeneralesFactura
        return None

    @property
    def codigo_fiscal_factura(self):
        if hasattr(self._datos_generales_factura, 'CodigoFiscalFactura'):
            return self._datos_generales_factura.CodigoFiscalFactura.text.strip()
        return None

    @property
    def tipo_factura(self):
        if hasattr(self._datos_generales_factura, 'TipoFactura'):
            return self._datos_generales_factura.TipoFactura.text.strip()
        return None

    @property
    def motivo_facturacion(self):
        if hasattr(self._datos_generales_factura, 'MotivoFacturacion'):
            return self._datos_generales_factura.MotivoFacturacion.text.strip()
        return None

    @property
    def codigo_factura_rectificada_anulada(self):
        has_attr = hasattr(
            self._datos_generales_factura, 'CodigoFacturaRectificadaAnulada'
        )
        if has_attr:
            datos_generales_fact = self._datos_generales_factura
            return datos_generales_fact.CodigoFacturaRectificadaAnulada.text.strip()
        return None

    @property
    def expediente(self):
        if hasattr(self._datos_generales_factura, 'Expediente'):
            return Expediente(self._datos_generales_factura.Expediente)
        return None

    @property
    def fecha_factura(self):
        if hasattr(self._datos_generales_factura, 'FechaFactura'):
            return self._datos_generales_factura.FechaFactura.text.strip()
        return None

    @property
    def identificador_emisora(self):
        if hasattr(self._datos_generales_factura, 'IdentificadorEmisora'):
            return self._datos_generales_factura.IdentificadorEmisora.text.strip()
        return None

    @property
    def comentarios(self):
        if hasattr(self._datos_generales_factura, 'Comentarios'):
            return self._datos_generales_factura.Comentarios.text.strip()
        return None

    @property
    def importe_total_factura(self):
        if hasattr(self._datos_generales_factura, 'ImporteTotalFactura'):
            return float(self._datos_generales_factura.ImporteTotalFactura.text.strip())
        return None

    @property
    def saldo_factura(self):
        if hasattr(self._datos_generales_factura, 'SaldoFactura'):
            return float(self._datos_generales_factura.SaldoFactura.text.strip())
        return None

    @property
    def tipo_moneda(self):
        if hasattr(self._datos_generales_factura, 'TipoMoneda'):
            return self._datos_generales_factura.TipoMoneda.text.strip()
        return None


class DatosGeneralesATR(DatosGenerales):

    @property
    def _datos_factura_atr(self):
        if hasattr(self.datos_generales, 'DatosFacturaATR'):
            return self.datos_generales.DatosFacturaATR
        return None

    @property
    def fecha_boe(self):
        if hasattr(self._datos_factura_atr, 'FechaBOE'):
            return self._datos_factura_atr.FechaBOE.text.strip()
        return None

    @property
    def tipo_autoconsumo(self):
        if hasattr(self._datos_factura_atr, 'TipoAutoconsumo'):
            return self._datos_factura_atr.TipoAutoconsumo.text.strip()

    @property
    def cau(self):
        if hasattr(self._datos_factura_atr, 'CAU'):
            return self._datos_factura_atr.CAU.text.strip()

    @property
    def duracion_inf_anio(self):
        if hasattr(self._datos_factura_atr, 'DuracionInfAnio'):
            return self._datos_factura_atr.DuracionInfAnio.text.strip()

    @property
    def tarifa_atr_fact(self):
        if hasattr(self._datos_factura_atr, 'TarifaATRFact'):
            return self._datos_factura_atr.TarifaATRFact.text.strip()
        return None

    @property
    def modo_control_potencia(self):
        if hasattr(self._datos_factura_atr, 'ModoControlPotencia'):
            return self._datos_factura_atr.ModoControlPotencia.text.strip()
        return None

    @property
    def marca_medida_con_perdidas(self):
        if hasattr(self._datos_factura_atr, 'MarcaMedidaConPerdidas'):
            return self._datos_factura_atr.MarcaMedidaConPerdidas.text.strip()
        return None

    @property
    def vas_trafo(self):
        if hasattr(self._datos_factura_atr, 'VAsTrafo'):
            return float(self._datos_factura_atr.VAsTrafo.text.strip())
        return None

    @property
    def porcentaje_perdidas(self):
        if hasattr(self._datos_factura_atr, 'PorcentajePerdidas'):
            return float(self._datos_factura_atr.PorcentajePerdidas.text.strip())
        return None

    @property
    def indicativo_curva_carga(self):
        if hasattr(self._datos_factura_atr, 'IndicativoCurvaCarga'):
            return self._datos_factura_atr.IndicativoCurvaCarga.text.strip()
        return None

    @property
    def _periodo_cch(self):
        if hasattr(self._datos_factura_atr, 'PeriodoCCH'):
            return self._datos_factura_atr.PeriodoCCH
        return None

    @property
    def _fecha_desde_cch(self):
        if hasattr(self._periodo_cch, 'FechaDesdeCCH'):
            return self._periodo.FechaDesdeCCH.text.strip()
        return None

    @property
    def _fecha_hasta_cch(self):
        if hasattr(self._periodo_cch, 'FechaHastaCCH'):
            return self._periodo.FechaHastaCCH.text.strip()
        return None

    @property
    def _periodo(self):
        if hasattr(self._datos_factura_atr, 'Periodo'):
            return self._datos_factura_atr.Periodo
        return None

    @property
    def fecha_desde_factura(self):
        if hasattr(self._periodo, 'FechaDesdeFactura'):
            return self._periodo.FechaDesdeFactura.text.strip()
        return None

    @property
    def fecha_hasta_factura(self):
        if hasattr(self._periodo, 'FechaHastaFactura'):
            return self._periodo.FechaHastaFactura.text.strip()
        return None

    @property
    def numero_dias(self):
        if hasattr(self._periodo, 'NumeroDias'):
            return int(self._periodo.NumeroDias.text.strip())
        return None

    @property
    def tipo_pm(self):
        if hasattr(self._periodo, 'TipoPM'):
            return int(self._periodo.TipoPM.text.strip())
        return None


class DatosGeneralesOtras(DatosGenerales):

    @property
    def fecha_boe(self):
        if hasattr(self.datos_generales, 'FechaBOE'):
            return self.datos_generales.FechaBOE.text.strip()
        return None


class Cliente(object):

    def __init__(self, data):
        self.cliente = data

    @property
    def tipo_identificador(self):
        return getattr(self.cliente, 'TipoIdentificador', None)

    @property
    def identificador(self):
        if hasattr(self.cliente, 'Identificador'):
            return self.cliente.Identificador.text.strip()
        return None

    @property
    def tipo_persona(self):
        return getattr(self.cliente, 'TipoPersona', None)


class Factura(object):

    DATOS_GENERALES_NAME = None
    DATOS_GENERALES_OBJECT = DatosGenerales

    def __init__(self, data):
        self.factura = data

        self.GETTERS_LINEAS_FACTURA = [
            ('altres', self.get_info_conceptes_repercutibles),
        ]

    @property
    def datos_factura(self):
        if self.DATOS_GENERALES_NAME:
            if hasattr(self.factura, self.DATOS_GENERALES_NAME):
                return self.DATOS_GENERALES_OBJECT(
                    getattr(self.factura, self.DATOS_GENERALES_NAME)
                )

    @property
    def ivas(self):
        data = []
        if hasattr(self.factura, 'IVA'):
            for d in self.factura.IVA:
                data.append(IVA(d))
        if hasattr(self.factura, 'IVAReducido'):
            for d in self.factura.IVAReducido:
                data.append(IVA(d))
        return data

    @property
    def conceptos_repercutibles(self):
        data = []
        if hasattr(self.factura, 'ConceptoRepercutible'):
            for d in self.factura.ConceptoRepercutible:
                data.append(ConceptoRepercutible(d))
        return data

    def get_tipus_punt_mesura(self):
        try:
            if self.factura.DatosGeneralesFacturaATR and self.factura.DatosGeneralesFacturaATR.DatosFacturaATR:
                if self.factura.DatosGeneralesFacturaATR.DatosFacturaATR.TipoPM:
                    return self.factura.DatosGeneralesFacturaATR.DatosFacturaATR.TipoPM.text
        except AttributeError:
            # We might not have any "TipoPM" in DatosFacturaATR
            pass

    def get_coeficient_repartiment(self):
        try:
            if self.factura.Autoconsumo and self.factura.Autoconsumo.InstalacionGenAutoconsumo:
                beta_list = []
                for instalacio in self.factura.Autoconsumo.InstalacionGenAutoconsumo:
                    if instalacio.EnergiaNetaGen:
                        for terme in instalacio.EnergiaNetaGen.TerminoEnergiaNetaGen:
                            for periode in terme.Periodo:
                                if periode and (float(periode.Beta.text) or float(periode.Beta.text) == 0.0):
                                    beta_list.append(float(periode.Beta.text))
                return list(set(beta_list))
        except AttributeError:
            # We might not have any "Coeficient de repartiment" in EnergiaNetaGen
            pass

    def get_coeficient_repartiment_from_cr(self):
        try:
            for concepte in self.conceptos_repercutibles:
                if concepte.concepto_repercutible == '82':
                    return concepte.unidades
        except AttributeError:
            # We might not have any "Coeficient de repartiment" in conceptos repercutibles
            pass

    def get_info_conceptes_repercutibles(self):
        conceptes = []
        total = 0
        try:
            for concepte in self.conceptos_repercutibles:
                # Si és una regularització refacturació 40, 41 i 42 el valor
                # només pot ser negatiu.
                # Es comprova ja que hi ha empreses que envien la refacturació
                # i també el ConceptoIVA i s'importaria dues vegades.
                codigo = concepte.concepto_repercutible
                if codigo is None:
                    continue
                regulating_concept = codigo in CODIS_REG_REFACT.values()
                if regulating_concept and concepte.total >= 0:
                    continue
                elif concepte.is_autoconsum():
                    conceptes.append(concepte)
                elif concepte.importe:
                    total += concepte.importe
                    conceptes.append(concepte)
        except AttributeError:
            # We might not have any "ConceptoIVA"
            pass
        return conceptes, total

    def get_linies_factura_by_type(self):
        res = {}
        res_to_join = {}

        to_join = {
            'potencia_cargos': 'potencia',
            'energia_cargos': 'energia'
        }
        for type, method in self.GETTERS_LINEAS_FACTURA:
            lines, sub_total = method()

            if lines:
                if type in to_join.keys():
                    aux_res = res_to_join
                else:
                    aux_res = res

                aux_res.setdefault(type, {'total': 0.0, 'lines': []})

                aux_res[type]['lines'] += lines
                new_total = aux_res[type]['total'] + sub_total
                aux_res[type]['total'] = round(new_total, 2)

        for tipus, info in res_to_join.items():
            tipus_join = to_join.get(tipus)
            if not res.get(tipus_join):
                continue
            base = 1.0
            res[tipus_join]['total'] += info['total']
            for l in info['lines']:
                for l2 in res[tipus_join]['lines']:
                    if l2.nombre == l.nombre and l2.cantidad == l.cantidad:
                        l2.precio += round(l.precio*base, 9)

        return res

    def sin_base_imponible(self):
        for iva in self.ivas:
            if iva.base != 0:
                return False

        return True

    def get_create_invoice_params(self):
        return {
            'tipo_rectificadora': self.datos_factura.tipo_factura,
            'tipo_factura': self.datos_factura.motivo_facturacion,
            'date_invoice': self.datos_factura.fecha_factura,
            'check_total': -1 * self.datos_factura.importe_total_factura
            if self.datos_factura.tipo_factura in ('A',)
            else self.datos_factura.importe_total_factura,
            'origin': self.datos_factura.codigo_fiscal_factura,
            'origin_date_invoice': self.datos_factura.fecha_factura,
            'reference': self.datos_factura.codigo_fiscal_factura,
        }


class Periodo(object):

    NOMBRE_PRECIO = None
    NOMBRE_CANTIDAD = None

    def __init__(self, data, name, fecha_desde=None, fecha_hasta=None):
        self.periodo = data
        self._name = name
        self.fecha_desde = fecha_desde
        self.fecha_hasta = fecha_hasta
        self._precio = 0.0

    @property
    def nombre(self):
        return self._name

    @property
    def precio(self):
        if self._precio:
            return self._precio
        elif self.NOMBRE_PRECIO:
            if hasattr(self.periodo, self.NOMBRE_PRECIO):
                return float(getattr(self.periodo, self.NOMBRE_PRECIO).text.strip())
        return None

    @precio.setter
    def precio(self, value):
        self._precio = value

    @property
    def cantidad(self):
        if self.NOMBRE_CANTIDAD:
            if hasattr(self.periodo, self.NOMBRE_CANTIDAD):
                return float(getattr(self.periodo, self.NOMBRE_CANTIDAD).text.strip())
        return None

    def es_facturable(self):
        """Algunas empresas envian periodos que no se deben facturar.
        Esos tienen precio 0. Pese a eso, si tienen cantidad los facturaremos
        igual ya que tambien hay empresas que quieren facturar lineas pero dejan
        el precio a 0"""
        return bool(self.precio) or bool(self.cantidad)


class PeriodoPotencia(Periodo):

    NOMBRE_PRECIO = 'PrecioPotencia'
    NOMBRE_CANTIDAD = 'PotenciaAFacturar'

    @property
    def potencia_contratada(self):
        if hasattr(self.periodo, 'PotenciaContratada'):
            return int(self.periodo.PotenciaContratada.text.strip())
        return None

    @property
    def potencia_max_demandada(self):
        if hasattr(self.periodo, 'PotenciaMaxDemandada'):
            return int(self.periodo.PotenciaMaxDemandada.text.strip())
        return None

    @property
    def potencia_a_facturar(self):
        if hasattr(self.periodo, 'PotenciaAFacturar'):
            return int(self.periodo.PotenciaAFacturar.text.strip())
        return None

    @property
    def recargo_inf_anio(self):
        if hasattr(self.periodo, 'RecargoInfAnio'):
            return int(float(self.periodo.RecargoInfAnio.text.strip()))
        return None


class Termino(object):

    PERIODO_TYPE = Periodo

    def __init__(self, data):
        self.termino = data

    @property
    def periodos(self):
        data = []
        periodes_no_facturables = []
        if hasattr(self.termino, 'Periodo'):
            period_number = 1
            max_facturat = period_number

            for d in self.termino.Periodo:
                period_name = 'P{0}'.format(period_number)
                period = self.PERIODO_TYPE(
                    d, period_name, self.fecha_desde, self.fecha_hasta
                )
                if period.es_facturable():
                    data.append(period)
                    max_facturat = period_number
                else:
                    periodes_no_facturables.append((d, period_number))
                period_number += 1

            if periodes_no_facturables:
                max_no_facturat = max([x[1] for x in periodes_no_facturables])
                # Per les 6.1 ens envien periodes amb preu i quantitat 0 pero si que els hem de gestionar
                if max_facturat > max_no_facturat:
                    for d, period_number in periodes_no_facturables:
                        period_name = 'P{0}'.format(period_number)
                        period = self.PERIODO_TYPE(
                            d, period_name, self.fecha_desde, self.fecha_hasta
                        )
                        data.append(period)

        return data

    @property
    def fecha_desde(self):
        if hasattr(self.termino, 'FechaDesde'):
            return self.termino.FechaDesde.text.strip()
        return None

    @property
    def fecha_hasta(self):
        if hasattr(self.termino, 'FechaHasta'):
            return self.termino.FechaHasta.text.strip()
        return None


class TerminoPotencia(Termino):

    PERIODO_TYPE = PeriodoPotencia

    def get_contracted_periods_by_period(self, use_facturada=False):
        cont_per = {}

        for period in self.periodos:
            if not use_facturada:
                cont_per[period.nombre] = period.potencia_contratada
            else:
                cont_per[period.nombre] = period.potencia_a_facturar

        return cont_per


class Potencia(object):

    def __init__(self, data):
        self.potencia = data

    @property
    def terminos_potencia(self):
        data = []
        if hasattr(self.potencia, 'TerminoPotencia'):
            for d in self.potencia.TerminoPotencia:
                data.append(TerminoPotencia(d))
        return data

    @property
    def penalizacion_no_icp(self):
        if hasattr(self.potencia, 'PenalizacionNoICP'):
            return self.potencia.PenalizacionNoICP.text.strip()
        return None

    @property
    def importe_total(self):
        if hasattr(self.potencia, 'ImporteTotalTerminoPotencia'):
            return float(self.potencia.ImporteTotalTerminoPotencia.text.strip())
        return None


class PeriodoExcesoPotencia(Periodo):
    @property
    def valor_exceso_potencia(self):
        if hasattr(self.periodo, 'ValorExcesoPotencia'):
            return float(self.periodo.ValorExcesoPotencia.text.strip())
        return None

    @property
    def name(self):
        return self._name

    @property
    def nombre(self):
        return self._name

    def es_facturable(self):
        """Algunas empresas envian periodos que no se deben facturar.
        Esos tienen precio 0. Pese a eso, si tienen cantidad los facturaremos
        igual ya que tambien hay empresas que quieren facturar lineas pero dejan
        el precio a 0"""
        return bool(self.valor_exceso_potencia)


class ExcesoPotencia(object):

    PERIODO_TYPE = PeriodoExcesoPotencia

    def __init__(self, data):
        self.exceso_potencia = data

    @property
    def periodos(self):
        data = []
        periodes_no_facturables = []
        if hasattr(self.exceso_potencia, 'Periodo'):
            period_number = 1
            max_facturat = period_number

            for d in self.exceso_potencia.Periodo:
                period_name = 'P{0}'.format(period_number)
                period = self.PERIODO_TYPE(
                    d, period_name
                )
                if period.es_facturable():
                    data.append(period)
                    max_facturat = period_number
                else:
                    periodes_no_facturables.append((d, period_number))
                period_number += 1

            if periodes_no_facturables:
                max_no_facturat = max([x[1] for x in periodes_no_facturables])
                # Per les 6.1 ens envien periodes amb preu i quantitat 0 pero si que els hem de gestionar
                if max_facturat > max_no_facturat:
                    for d, period_number in periodes_no_facturables:
                        period_name = 'P{0}'.format(period_number)
                        period = self.PERIODO_TYPE(
                            d, period_name
                        )
                        data.append(period)

        return data

    @property
    def importe_total(self):
        if hasattr(self.exceso_potencia, 'ImporteTotalExcesos'):
            return float(self.exceso_potencia.ImporteTotalExcesos.text.strip())
        return None


class PeriodoEnergiaActiva(Periodo):

    NOMBRE_PRECIO = 'PrecioEnergia'
    NOMBRE_CANTIDAD = 'ValorEnergiaActiva'

    @property
    def valor_energia_activa(self):
        if hasattr(self.periodo, 'ValorEnergiaActiva'):
            return float(self.periodo.ValorEnergiaActiva.text.strip())
        return None


class TerminoEnergiaActiva(Termino):

    PERIODO_TYPE = PeriodoEnergiaActiva


class EnergiaActiva(object):

    def __init__(self, data):
        self.energia_activa = data

    @property
    def terminos_energia_activa(self):
        data = []
        if hasattr(self.energia_activa, 'TerminoEnergiaActiva'):
            for d in self.energia_activa.TerminoEnergiaActiva:
                data.append(TerminoEnergiaActiva(d))
        return data

    @property
    def importe_total(self):
        if hasattr(self.energia_activa, 'ImporteTotalEnergiaActiva'):
            return float(self.energia_activa.ImporteTotalEnergiaActiva.text.strip())
        return None


class PeriodoEnergiaReactiva(Periodo):

    NOMBRE_PRECIO = 'PrecioEnergiaReactiva'
    NOMBRE_CANTIDAD = 'ValorEnergiaReactiva'

    @property
    def valor_energia_reactiva(self):
        if hasattr(self.periodo, 'ValorEnergiaReactiva'):
            return float(self.periodo.ValorEnergiaReactiva.text.strip())
        return None


class PeriodoEnergiaCapacitiva(Periodo):

    NOMBRE_PRECIO = 'PrecioEnergiaCapacitiva'
    NOMBRE_CANTIDAD = 'ValorEnergiaCapacitiva'

    @property
    def valor_energia_capacitiva(self):
        if hasattr(self.periodo, 'ValorEnergiaCapacitiva'):
            return float(self.periodo.ValorEnergiaCapacitiva.text.strip())
        return None


class PeriodoEnergiaNetaGen(Periodo):

    NOMBRE_CANTIDAD = 'ValorEnergiaNetaGen'

    @property
    def valor_energia_neta_gen(self):
        if hasattr(self.periodo, 'ValorEnergiaNetaGen'):
            return float(self.periodo.ValorEnergiaNetaGen.text.strip())
        return None

    @property
    def beta(self):
        if hasattr(self.periodo, 'Beta'):
            return float(self.periodo.Beta.text.strip())
        return None

    @property
    def relacion_generacion(self):
        if hasattr(self.periodo, 'RelacionGeneracion'):
            return float(self.periodo.RelacionGeneracion.text.strip())
        return None


class PeriodoEnergiaAutoconsumida(Periodo):

    NOMBRE_CANTIDAD = 'ValorEnergiaAutoconsumida'
    NOMBRE_PRECIO = "PagoTDA"

    @property
    def valor_energia_autoconsumida(self):
        if hasattr(self.periodo, 'ValorEnergiaAutoconsumida'):
            return float(self.periodo.ValorEnergiaAutoconsumida.text.strip())
        return None

    @property
    def pago_tda(self):
        if hasattr(self.periodo, 'PagoTDA'):
            return float(self.periodo.PagoTDA.text.strip())
        return None


class PeriodoEnergiaExcedentaria(Periodo):

    NOMBRE_CANTIDAD = 'ValorEnergiaExcedentaria'

    @property
    def valor_energia_excedentaria(self):
        if hasattr(self.periodo, 'ValorEnergiaExcedentaria'):
            return float(self.periodo.ValorEnergiaExcedentaria.text.strip())
        return None


class PeriodoCargo(Periodo):

    NOMBRE_PRECIO = "PrecioCargo"

    @property
    def energia(self):
        if hasattr(self.periodo, 'Energia'):
            return float(self.periodo.Energia.text.strip())
        return None

    @property
    def potencia(self):
        if hasattr(self.periodo, 'Potencia'):
            return float(self.periodo.Potencia.text.strip())
        return None

    @property
    def precio_cargo(self):
        if hasattr(self.periodo, 'PrecioCargo'):
            return float(self.periodo.PrecioCargo.text.strip())
        return None

    def es_facturable(self):
        return bool(self.precio_cargo) or bool(self.potencia) or bool(self.energia)

    @property
    def cantidad(self):
        return self.potencia or self.energia or 0.0

class TerminoEnergiaReactiva(TerminoEnergiaActiva):

    PERIODO_TYPE = PeriodoEnergiaReactiva


class TerminoEnergiaCapacitiva(TerminoEnergiaActiva):

    PERIODO_TYPE = PeriodoEnergiaCapacitiva


class TerminoEnergiaNetaGen(TerminoEnergiaActiva):

    PERIODO_TYPE = PeriodoEnergiaNetaGen


class TerminoEnergiaAutoconsumida(TerminoEnergiaActiva):

    PERIODO_TYPE = PeriodoEnergiaAutoconsumida


class TerminoEnergiaExcedentaria(TerminoEnergiaActiva):

    PERIODO_TYPE = PeriodoEnergiaExcedentaria


class TerminoCargo(TerminoEnergiaActiva):

    PERIODO_TYPE = PeriodoCargo


class InstalacionGenAutoconsumo(object):
    def __init__(self, data):
        self.instalacion_gen_autoconsumo = data

    @property
    def tipo_instalacion(self):
        if hasattr(self.instalacion_gen_autoconsumo, 'TipoInstalacion'):
            return self.instalacion_gen_autoconsumo.TipoInstalacion.text.strip()
        return None

    @property
    def exento_cargos(self):
        if hasattr(self.instalacion_gen_autoconsumo, 'ExentoCargos'):
            return self.instalacion_gen_autoconsumo.ExentoCargos.text.strip()
        return None

    @property
    def energia_neta_gen(self):
        if hasattr(self.instalacion_gen_autoconsumo, 'EnergiaNetaGen'):
            return EnergiaNetaGen(self.instalacion_gen_autoconsumo.EnergiaNetaGen)
        return None

    @property
    def energia_autoconsumida(self):
        if hasattr(self.instalacion_gen_autoconsumo, 'EnergiaAutoconsumida'):
            return EnergiaAutoconsumida(self.instalacion_gen_autoconsumo.EnergiaAutoconsumida)
        return None


class EnergiaReactiva(object):

    def __init__(self, data):
        self.energia_reactiva = data

    @property
    def terminos_energia_reactiva(self):
        data = []
        if hasattr(self.energia_reactiva, 'TerminoEnergiaReactiva'):
            for d in self.energia_reactiva.TerminoEnergiaReactiva:
                data.append(TerminoEnergiaReactiva(d))
        return data

    @property
    def importe_total(self):
        if hasattr(self.energia_reactiva, 'ImporteTotalEnergiaReactiva'):
            return float(self.energia_reactiva.ImporteTotalEnergiaReactiva.text.strip())
        return None


class EnergiaCapacitiva(object):

    def __init__(self, data):
        self.energia_capacitiva = data

    @property
    def terminos_energia_capacitiva(self):
        data = []
        if hasattr(self.energia_capacitiva, 'TerminoEnergiaCapacitiva'):
            for d in self.energia_capacitiva.TerminoEnergiaCapacitiva:
                data.append(TerminoEnergiaCapacitiva(d))
        return data

    @property
    def importe_total(self):
        if hasattr(self.energia_capacitiva, 'ImporteTotalEnergiaCapcitiva'):
            return float(self.energia_capacitiva.ImporteTotalEnergiaCapcitiva.text.strip())
        return None


class EnergiaNetaGen(object):

    def __init__(self, data):
        self.energia_neta_gen = data

    @property
    def terminos_energia_neta_gen(self):
        data = []
        if hasattr(self.energia_neta_gen, 'TerminoEnergiaNetaGen'):
            for d in self.energia_neta_gen.TerminoEnergiaNetaGen:
                data.append(TerminoEnergiaNetaGen(d))
        return data

    @property
    def importe_total(self):
        if hasattr(self.energia_neta_gen, 'TotalEnergiaNetaGenBeta'):
            return float(self.energia_neta_gen.TotalEnergiaNetaGenBeta.text.strip())
        return None


class EnergiaAutoconsumida(object):

    def __init__(self, data):
        self.energia_autoconsumida = data

    @property
    def terminos_energia_autoconsumida(self):
        data = []
        if hasattr(self.energia_autoconsumida, 'TerminoEnergiaAutoconsumida'):
            for d in self.energia_autoconsumida.TerminoEnergiaAutoconsumida:
                data.append(TerminoEnergiaAutoconsumida(d))
        return data

    @property
    def importe_total(self):
        if hasattr(self.energia_autoconsumida, 'ImporteTotalEnergiaActivaAutoconsumida'):
            return float(self.energia_autoconsumida.ImporteTotalEnergiaActivaAutoconsumida.text.strip())
        return None


class EnergiaExcedentaria(object):

    def __init__(self, data):
        self.energia_excedentaria = data

    @property
    def terminos_energia_excedentaria(self):
        data = []
        if hasattr(self.energia_excedentaria, 'TerminoEnergiaExcedentaria'):
            for d in self.energia_excedentaria.TerminoEnergiaExcedentaria:
                data.append(TerminoEnergiaExcedentaria(d))
        return data

    @property
    def importe_total(self):
        if hasattr(self.energia_excedentaria, 'ValorTotalEnergiaExcedentaria'):
            return float(self.energia_excedentaria.ValorTotalEnergiaExcedentaria.text.strip())
        return None


class Cargo(object):

    def __init__(self, data):
        self.cargo = data

    @property
    def tipo_cargo(self):
        if hasattr(self.cargo, 'TipoCargo'):
            return float(self.cargo.TipoCargo.text.strip())
        return None

    @property
    def termino_cargo(self):
        data = []
        if hasattr(self.cargo, 'TerminoCargo'):
            for d in self.cargo.TerminoCargo:
                data.append(TerminoCargo(d))
        return data

    @property
    def importe_total(self):
        if hasattr(self.cargo, 'TotalImporteTipoCargo'):
            return float(self.cargo.TotalImporteTipoCargo.text.strip())
        return None


class Autoconsumo(object):

    def __init__(self, data):
        self.autoconsumo = data

    @property
    def instalacion_gen_autoconsumo(self):
        data = []
        if hasattr(self.autoconsumo, 'InstalacionGenAutoconsumo'):
            for d in self.autoconsumo.InstalacionGenAutoconsumo:
                data.append(InstalacionGenAutoconsumo(d))
        return data

    @property
    def energia_excedentaria(self):
        if hasattr(self.autoconsumo, 'EnergiaExcedentaria'):
            return EnergiaExcedentaria(self.autoconsumo.EnergiaExcedentaria)
        return None


class Cargos(object):

    def __init__(self, data):
        self.cargos = data

    @property
    def cargo(self):
        data = []
        if hasattr(self.cargos, 'Cargo'):
            for d in self.cargos.Cargo:
                data.append(Cargo(d))
        return data

    @property
    def total_cargos(self):
        if hasattr(self.cargos, 'TotalImporteCargos'):
            return float(self.cargos.TotalImporteCargos.text.strip())
        return None


class Impuesto(object):

    def __init__(self, data):
        self.impuesto = data

    @property
    def base(self):
        if hasattr(self.impuesto, 'BaseImponible'):
            return float(self.impuesto.BaseImponible.text.strip())
        return None

    @property
    def porcentaje(self):
        if hasattr(self.impuesto, 'Porcentaje'):
            return float(self.impuesto.Porcentaje.text.strip())
        return None

    @property
    def importe(self):
        if hasattr(self.impuesto, 'Importe'):
            return float(self.impuesto.Importe.text.strip())
        return None


class ImpuestoElectrico(Impuesto):

    pass


class PrecioAlquiler(object):

    def __init__(self, data):
        self.precio_alquiler = data

    @property
    def precio_dia(self):
        if hasattr(self.precio_alquiler, 'PrecioDia'):
            return float(self.precio_alquiler.PrecioDia.text.strip())
        return None

    @property
    def numero_dias(self):
        if hasattr(self.precio_alquiler, 'NumeroDias'):
            return int(self.precio_alquiler.NumeroDias.text.strip())
        return None

    def es_facturable(self):
        return self.precio_dia or self.numero_dias


class Alquiler(object):

    def __init__(self, data):
        self.alquiler = data

    @property
    def precios_alquiler(self):
        data = []
        if hasattr(self.alquiler, 'PrecioDiarioAlquiler'):
            for d in self.alquiler.PrecioDiarioAlquiler:
                precio = PrecioAlquiler(d)
                if precio.es_facturable():
                    data.append(precio)
        return data

    @property
    def importe_total(self):
        if hasattr(self.alquiler, 'ImporteFacturacionAlquileres'):
            return float(self.alquiler.ImporteFacturacionAlquileres.text.strip())
        return None


class IVA(Impuesto):

    pass


class Lectura(object):

    def __init__(self, data):
        self.lectura_data = data
        self._fecha = None
        self._lectura = None
        self._procedencia = None

    @property
    def fecha(self):
        if self._fecha:
            return self._fecha
        if hasattr(self.lectura_data, 'Fecha'):
            return self.lectura_data.Fecha.text.strip()
        return None

    @fecha.setter
    def fecha(self, value):
        self._fecha = value

    @property
    def procedencia(self):
        if self._procedencia:
            return self._procedencia
        if hasattr(self.lectura_data, 'Procedencia'):
            return self.lectura_data.Procedencia.text.strip()
        return None

    @procedencia.setter
    def procedencia(self, value):
        self._procedencia = value

    @property
    def lectura_float(self):
        if hasattr(self.lectura_data, 'Lectura'):
            return float(self.lectura_data.Lectura.text.strip())
        return None

    @property
    def lectura(self):
        if self._lectura is not None:
            return self._lectura
        if hasattr(self.lectura_data, 'Lectura'):
            return int(float(self.lectura_data.Lectura.text.strip()))
        return None

    @lectura.setter
    def lectura(self, value):
        self._lectura = value


class Ajuste(object):

    def __init__(self, data):
        self.ajuste = data
        self._codigo_motivo = None
        self._ajuste_por_integrador = None
        self._comentario = None

    @property
    def codigo_motivo(self):
        if self._codigo_motivo:
            return self._codigo_motivo
        if hasattr(self.ajuste, 'CodigoMotivoAjuste'):
            return self.ajuste.CodigoMotivoAjuste.text.strip()
        return None

    @codigo_motivo.setter
    def codigo_motivo(self, value):
        self._codigo_motivo = value

    @property
    def ajuste_por_integrador(self):
        if self._ajuste_por_integrador:
            return self._ajuste_por_integrador
        if hasattr(self.ajuste, 'AjustePorIntegrador'):
            return float(self.ajuste.AjustePorIntegrador.text.strip())
        return None

    @ajuste_por_integrador.setter
    def ajuste_por_integrador(self, value):
        self._ajuste_por_integrador = value

    @property
    def comentario(self):
        if self._comentario:
            return self._comentario
        if hasattr(self.ajuste, 'Comentarios'):
            return self.ajuste.Comentarios.text
        return None

    @comentario.setter
    def comentario(self, value):
        self._comentario = value


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

    def unique_name(self):
        return '_'.join([self.codigo_periodo, self.tipus, self.lectura_desde.fecha,  self.lectura_hasta.fecha])

    @property
    def magnitud(self):
        if self._magnitud:
            return self._magnitud
        if hasattr(self.integrador, 'Magnitud'):
            return self.integrador.Magnitud.text.strip()
        return None

    @magnitud.setter
    def magnitud(self, value):
        self._magnitud = value

    @property
    def codigo_periodo(self):
        if self._periode:
            return self._periode
        elif hasattr(self.integrador, 'CodigoPeriodo'):
            return self.integrador.CodigoPeriodo.text.strip()
        else:
            return None

    @codigo_periodo.setter
    def codigo_periodo(self, value):
        self._periode = value

    @property
    def constante_multiplicadora(self):
        if hasattr(self.integrador, 'ConstanteMultiplicadora'):
            return float(self.integrador.ConstanteMultiplicadora.text.strip())
        return None

    @property
    def numero_ruedas_enteras(self):
        if self._numero_ruedas_enteras is not None:
            return self._numero_ruedas_enteras
        if hasattr(self.integrador, 'NumeroRuedasEnteras'):
            return float(self.integrador.NumeroRuedasEnteras.text.strip())
        return None

    @numero_ruedas_enteras.setter
    def numero_ruedas_enteras(self, value):
        self._numero_ruedas_enteras = value

    @property
    def numero_ruedas_decimales(self):
        if hasattr(self.integrador, 'NumeroRuedasDecimales'):
            return float(self.integrador.NumeroRuedasDecimales.text.strip())
        return None

    @property
    def consumo_calculado(self):
        if hasattr(self.integrador, 'ConsumoCalculado'):
            return float(self.integrador.ConsumoCalculado.text.strip())
        return 0

    @property
    def lectura_desde(self):
        if self._lectura_desde:
            return self._lectura_desde
        if hasattr(self.integrador, 'LecturaDesde'):
            return Lectura(self.integrador.LecturaDesde)
        return None

    @lectura_desde.setter
    def lectura_desde(self, value):
        self._lectura_desde = value

    @property
    def lectura_hasta(self):
        if self._lectura_hasta:
            return self._lectura_hasta
        if hasattr(self.integrador, 'LecturaHasta'):
            return Lectura(self.integrador.LecturaHasta)
        return None

    @lectura_hasta.setter
    def lectura_hasta(self, value):
        self._lectura_hasta = value

    @property
    def tipus(self):
        return MAGNITUDS_OCSUM.get(self.magnitud)

    @property
    def periode(self):
        p = PERIODE_OCSUM.get(self.codigo_periodo, None)
        if not p and self.codigo_periodo in PERIODE_OCSUM.values():
            return self.codigo_periodo
        if self.codigo_periodo == '93' and p == 'P3' and self.magnitud in ('PM', 'EP'):
            return "P2"
        return p

    @property
    def gir_comptador(self):
        if self.numero_ruedas_enteras == 99:
            return 10
        return 10 ** self.numero_ruedas_enteras

    @property
    def ajuste(self):
        if self._ajuste:
            return self._ajuste
        if hasattr(self.integrador, 'Ajuste'):
            return Ajuste(self.integrador.Ajuste)
        return None

    @ajuste.setter
    def ajuste(self, value):
        self._ajuste = value

    @property
    def ometre(self):
        return self.codigo_periodo in SKIP_TOTALITZADORS


class ModeloAparato(object):

    def __init__(self, data, factura=None):
        self.modelo_aparato = data
        self.factura = factura

    @property
    def tipo_aparato(self):
        if hasattr(self.modelo_aparato, 'TipoAparato'):
            return self.modelo_aparato.TipoAparato.text.strip()
        return None

    @property
    def marca_aparato(self):
        if hasattr(self.modelo_aparato, 'MarcaAparato'):
            return self.modelo_aparato.MarcaAparato.text.strip()
        return None

    @property
    def numero_serie(self):
        if hasattr(self.modelo_aparato, 'NumeroSerie'):
            return self.modelo_aparato.NumeroSerie.text.strip()
        return None

    @property
    def tipo_dhedm(self):
        if hasattr(self.modelo_aparato, 'TipoDHEdM'):
            return self.modelo_aparato.TipoDHEdM.text.strip()
        return None

    @property
    def integradores(self):
        data = []
        if hasattr(self.modelo_aparato, 'Integrador'):
            integradors_dh_per_data = {}
            totalitzadors_per_data = {}
            integradors_per_data_i_periode = {}
            for d in self.modelo_aparato.Integrador:
                integrador = Integrador(d)
                if integrador.codigo_periodo in ['21', '22', '81', '82', '83'] and integrador.magnitud == 'PM':
                    # Algunes distris envien 2/3 periodes de potencia en les DHx ...
                    # Diuen que només facturen la mes gran i la CNMC diu que esta be :(
                    # Els guardem per tractarlos despres
                    integradors_dh_per_data.setdefault(integrador.lectura_hasta.fecha, [])
                    integradors_dh_per_data[integrador.lectura_hasta.fecha].append(integrador)
                elif integrador.codigo_periodo in ['90', 'A0']:
                    totalitzadors_per_data.setdefault(integrador.lectura_hasta.fecha, [])
                    totalitzadors_per_data[integrador.lectura_hasta.fecha].append(integrador)
                else:
                    integradors_per_data_i_periode.setdefault(integrador.lectura_hasta.fecha, {})
                    integradors_per_data_i_periode[integrador.lectura_hasta.fecha].setdefault(integrador.periode, [])
                    integradors_per_data_i_periode[integrador.lectura_hasta.fecha][integrador.periode].append(integrador)
                    data.append(integrador)

            for data_totalitzador, totalitzadors in totalitzadors_per_data.items():
                for totalitzador in totalitzadors_per_data[data_totalitzador]:
                    if data_totalitzador not in integradors_per_data_i_periode:
                        data.append(totalitzador)
                    elif totalitzador.periode not in integradors_per_data_i_periode[data_totalitzador]:
                        data.append(totalitzador)

            # Per tractar els multiples periodes en una DH nosaltres agafarem
            # la lectura mes gran de cada data com a P1 ja que no hi ha altres
            # Px de potencia per una DHx.
            for dlects_xml in integradors_dh_per_data.values():
                if len(dlects_xml) > 1:
                    max_lect = dlects_xml[0]
                    for dlect_xml in dlects_xml:
                        # Ens quedem amb la mes gran per aquesta data
                        if dlect_xml.lectura_hasta.lectura >= max_lect.lectura_hasta.lectura:
                            max_lect = dlect_xml
                            max_lect.codigo_periodo = max_lect.codigo_periodo[0] + '1'
                    data.append(max_lect)
                else:
                    data.append(dlects_xml[0])
        return data

    @property
    def gir_comptador(self):
        giros_lect = [
            int.gir_comptador for int in self.integradores
        ]

        return max(giros_lect)

    def get_dates_inici_i_final(self):
        data_inici = ''
        data_final = ''
        for lect in self.get_lectures(force_no_transforma_no_td_a_td=True):
            data_in_compt = datetime.strptime(
                lect.lectura_desde.fecha, '%Y-%m-%d'
            )
            data_fi_compt = datetime.strptime(
                lect.lectura_hasta.fecha, '%Y-%m-%d'
            )

            if not data_inici or data_in_compt < data_inici:
                data_inici = data_in_compt
            if not data_final or data_in_compt > data_final:
                data_final = data_fi_compt

        return data_inici, data_final

    def get_lectures(self, tipus=None, force_no_transforma_no_td_a_td=False):
        """Retorna totes les lectures en una llista de Lectura"""
        lectures = []
        try:
            for integrador in self.integradores:
                # If we don't have any type requirements or the current
                # reading is in them
                if not tipus or (integrador.tipus and integrador.tipus in tipus):
                    integrador.comptador = self
                    lectures.append(integrador)
        except AttributeError:
            pass

        if (not tipus or "S" in tipus) and self.factura and self.factura.get_consum_facturat(tipus='S', periode=None) \
                and not self.factura.has_AS_lectures():
            # Si no tenim lectures AS pero si que ens han cobrat excedents,
            # creem unes lectures AS ficticies a 0 (puta ENDESA)
            lectures.extend(self.factura.get_fake_AS_lectures())
        if (not tipus or "S" in tipus) and self.factura and self.factura.has_AS_lectures_only_p0() \
                and len(self.factura.get_consum_facturat(tipus='S', periode=None)) > 1 \
                and self.factura.datos_factura.tarifa_atr_fact not in ['001', '005']:
            # Si nomes ens envien el P0 de excedents pero ens cobren varis periodes
            # creem una lectura e P2 AS ficticies a 0 (puta FENOSA)
            lectures.extend(self.factura.get_fake_AS_p2_lectures())

        if not force_no_transforma_no_td_a_td and self.factura:
            lectures = self.factura.transforma_no_td_a_td(lectures, tipus=tipus)
        lectures = sorted(lectures, key=lambda x: x.lectura_desde.fecha)
        return lectures

    def get_lectures_activa(self):
        return self.get_lectures(['A', 'S'])

    def get_lectures_activa_entrant(self):
        return self.get_lectures(['A'])

    def get_lectures_activa_sortint(self):
        return self.get_lectures(['S'])

    def get_lectures_reactiva(self):
        return self.get_lectures(['R'])

    def get_lectures_energia(self):
        return self.get_lectures(['A', 'S', 'R', 'RC'])

    def get_lectures_maximetre(self):
        return self.get_lectures(['M'])


class MultiModeloAparato(ModeloAparato):
    """This is to solve the perfectly reasonable decision made by a certain
    company in their exportation of F1. Namely, the fact that they decided to
    repeat both the field Medidas and ModeloAparato despite the fact that they
    are only providing two different periods for the same meter"""

    def __init__(self, meter_list, factura=None):
        self.meters = meter_list
        super(MultiModeloAparato, self).__init__(meter_list[0], factura=factura)

    def _get_single_attribute(self, attribute):
        for meter in self.meters:
            attr_val = getattr(meter, attribute, None)
            if attr_val is not None:
                return attr_val

        return None

    def _get_list_attribute(self, attribute):
        res = []

        for meter in self.meters:
            if hasattr(meter, attribute):
                res += getattr(meter, attribute)

        return res

    @property
    def tipo_aparato(self):
        return self._get_single_attribute('tipo_aparato')

    @property
    def cod_pm(self):
        return self._get_single_attribute('cod_pm')

    @property
    def marca_aparato(self):
        return self._get_single_attribute('marca_aparato')

    @property
    def numero_serie(self):
        return self._get_single_attribute('numero_serie')

    @property
    def tipo_dhedm(self):
        return self._get_single_attribute('tipo_dhedm')

    @property
    def integradores(self):
        return self._get_list_attribute('integradores')

    @property
    def gir_comptador(self):
        return self._get_single_attribute('gir_comptador')


class Medida(object):

    def __init__(self, data):
        self.medida = data

    @property
    def cod_pm(self):
        if hasattr(self.medida, 'CodPM'):
            return self.medida.CodPM.text.strip()
        return None

    @property
    def modelos_aparatos(self):
        data = []
        if hasattr(self.medida, 'ModeloAparato'):
            for d in self.medida.ModeloAparato:
                data.append(ModeloAparato(d))
        return data


class PeriodoMaximetroConsumidor(Periodo):

    @property
    def potencia_max_demandada_anio_movil(self):
        if hasattr(self.periodo, 'PotenciaMaxDemandadaAnioMovil'):
            return int(self.periodo.PotenciaMaxDemandadaAnioMovil.text.strip())
        return None

    @property
    def name(self):
        return self._name

    @property
    def nombre(self):
        return self._name

    def es_facturable(self):
        """Algunas empresas envian periodos que no se deben facturar.
        Esos tienen precio 0. Pese a eso, si tienen cantidad los facturaremos
        igual ya que tambien hay empresas que quieren facturar lineas pero dejan
        el precio a 0"""
        return bool(self.potencia_max_demandada_anio_movil)


class InformacionAlConsumidor(object):

    PERIODO_TYPE = PeriodoMaximetroConsumidor

    def __init__(self, data):
        self.informacion_al_consumidor = data

    @property
    def fecha_inicio_anio_movil(self):
        if hasattr(self.informacion_al_consumidor, 'FechaInicioAnioMovil'):
            return self.informacion_al_consumidor.FechaInicioAnioMovil.text.strip()
        return None

    @property
    def periodos(self):
        data = []
        periodes_no_facturables = []
        if hasattr(self.informacion_al_consumidor, 'Periodo'):
            period_number = 1
            max_facturat = period_number

            for d in self.informacion_al_consumidor.Periodo:
                period_name = 'P{0}'.format(period_number)
                period = self.PERIODO_TYPE(
                    d, period_name
                )
                if period.es_facturable():
                    data.append(period)
                    max_facturat = period_number
                else:
                    periodes_no_facturables.append((d, period_number))
                period_number += 1

            if periodes_no_facturables:
                max_no_facturat = max([x[1] for x in periodes_no_facturables])
                # Per les 6.1 ens envien periodes amb preu i quantitat 0 pero si que els hem de gestionar
                if max_facturat > max_no_facturat:
                    for d, period_number in periodes_no_facturables:
                        period_name = 'P{0}'.format(period_number)
                        period = self.PERIODO_TYPE(
                            d, period_name
                        )
                        data.append(period)

        return data


class FacturaATR(Factura):
    DATOS_GENERALES_NAME = 'DatosGeneralesFacturaATR'
    DATOS_GENERALES_OBJECT = DatosGeneralesATR

    def __init__(self, data):
        super(FacturaATR, self).__init__(data)

        self.GETTERS_LINEAS_FACTURA += [
            ('potencia', self.get_info_potencia),
            ('potencia_cargos', self.get_info_potencia_cargos),
            ('exces_potencia', self.get_info_exces),
            ('energia', self.get_info_activa),
            ('energia_cargos', self.get_info_energia_cargos),
            ('reactiva', self.get_info_reactiva),
            ('lloguer', self.get_info_lloguer),
            ('generacio', self.get_info_generacio),
            ('generacio_neta', self.get_info_generacio_neta),
            ('autoconsum', self.get_info_autoconsumo),
        ]

    def te_autoconsum(self):
        if self.datos_factura and self.datos_factura.tipo_autoconsumo and self.datos_factura.tipo_autoconsumo not in ['00', '01', '2A', '2B', '2G']:
            return True
        for concepte in self.conceptos_repercutibles:
            if concepte.concepto_repercutible in CODIS_AUTOCONSUM.keys():
                return True
        return False

    def te_lectures_pre_td_amb_tarifa_td(self):
        if self.datos_factura.tarifa_atr_fact not in TARIFES_TD:
            return False

        for c in self.get_comptadors():
            for l in c.get_lectures(force_no_transforma_no_td_a_td=True):
                if l.codigo_periodo in PERIODES_NO_TD:
                    return True

        return False

    def te_lectures_amb_decimals(self):
        if self.datos_factura.tarifa_atr_fact not in TARIFES_TD:
            return False
        if self.datos_factura.tipo_factura in ('C', ):
            return False
        if self.datos_factura.vas_trafo or self.datos_factura.porcentaje_perdidas:
            return False
        for c in self.get_comptadors():
            for l in c.get_lectures(force_no_transforma_no_td_a_td=True):
                if isinstance(l.consumo_calculado, int):
                    return False
                if not l.ajuste and not l.consumo_calculado.is_integer():
                    return True

        return False

    @property
    def potencia(self):
        if hasattr(self.factura, 'Potencia'):
            return Potencia(self.factura.Potencia)
        return None

    @property
    def exceso_potencia(self):
        if hasattr(self.factura, 'ExcesoPotencia'):
            return ExcesoPotencia(self.factura.ExcesoPotencia)
        return None

    @property
    def energia_activa(self):
        if hasattr(self.factura, 'EnergiaActiva'):
            return EnergiaActiva(self.factura.EnergiaActiva)
        return None

    @property
    def energia_reactiva(self):
        if hasattr(self.factura, 'EnergiaReactiva'):
            return EnergiaReactiva(self.factura.EnergiaReactiva)
        return None

    @property
    def energia_capacitiva(self):
        if hasattr(self.factura, 'EnergiaCapacitiva'):
            return EnergiaCapacitiva(self.factura.EnergiaCapacitiva)
        return None

    @property
    def autoconsumo(self):
        if hasattr(self.factura, 'Autoconsumo'):
            return Autoconsumo(self.factura.Autoconsumo)
        return None

    @property
    def cargos(self):
        if hasattr(self.factura, 'Cargos'):
            return Cargos(self.factura.Cargos)
        return None

    @property
    def impuesto_electrico(self):
        if hasattr(self.factura, 'ImpuestoElectrico'):
            return ImpuestoElectrico(self.factura.ImpuestoElectrico)
        return None

    @property
    def alquiler(self):
        if hasattr(self.factura, 'Alquileres'):
            return Alquiler(self.factura.Alquileres)
        return None

    @property
    def medidas(self):
        data = []
        if hasattr(self.factura, 'Medidas'):
            for d in self.factura.Medidas:
                data.append(Medida(d))
        return data

    @property
    def informacion_al_consumidor(self):
        if hasattr(self.factura, 'InformacionAlConsumidor'):
            return InformacionAlConsumidor(self.factura.InformacionAlConsumidor)
        return None

    def transforma_no_td_a_td(self, lectures, tipus=None):
        if self.datos_factura.tarifa_atr_fact not in TARIFES_TD:
            return lectures

        if not self.te_lectures_pre_td_amb_tarifa_td():
            return lectures

        if not tipus:
            tipus_lectures = ['A', 'S', 'R', 'RC', 'M', 'EP']
        else:
            tipus_lectures = tipus

        res = []
        for t in tipus_lectures:
            lectures_td = self.get_lectures_amb_periodes_td(lectures, t)
            lectures_amb_ajustos = self.get_lectures_amb_ajust_quadrat_amb_consum(t, lectures=lectures_td, motiu_ajust='97')
            for aux in lectures_amb_ajustos.values():
                res.extend(aux)
        return res

    def get_lectures_amb_periodes_td(self, lectures, tipus):
        res = []
        tarifa_atr = self.datos_factura.tarifa_atr_fact
        nperiodes_td = PERIODES_PER_TARIFA.get(tarifa_atr, {}).get(tipus, None)
        if not nperiodes_td:
            return [x for x in lectures if x.tipus == tipus]

        lectures_by_date = {}
        for l in lectures:
            if l.lectura_desde.fecha not in lectures_by_date:
                lectures_by_date[l.lectura_desde.fecha] = []
            lectures_by_date[l.lectura_desde.fecha].append(l)

        lectures_per_periode = {}
        for periode in range(1, nperiodes_td+1):
            pname = "P"+str(periode)
            lectures_per_periode[pname] = []

        base_lectura = None
        for l in lectures:
            if l.tipus == tipus:
                lectures_per_periode[l.periode].append(l)
                base_lectura = l

        if not base_lectura:
            return [x for x in lectures if x.tipus == tipus]

        for periode in lectures_per_periode:
            if not lectures_per_periode.get(periode) and base_lectura:
                try:
                    for ldate in lectures_by_date.keys():
                        base_lectura = lectures_by_date[ldate][0]
                        aux = self.get_fake_pX_lectura(tipus, periode, base_lectura)
                        res.append(aux)
                except:
                    # Lo de dal es una mandanga que es una basura que estem obligats a fer. Si falla, no vull que falli
                    # la resta del F1. Si es un F1 amb cara i ulls ni hi passara per aqui
                    pass
            else:
                if len(lectures_per_periode.get(periode)) > 1:
                    oldest = min([l.lectura_desde.fecha for l in lectures_per_periode.get(periode)])
                    lectua_a_canviar = [x for x in lectures_per_periode.get(periode) if x.lectura_desde.fecha == oldest][0]
                    must_have_value = [l.lectura_desde.lectura for l in lectures_per_periode.get(periode) if l.lectura_desde.fecha == lectua_a_canviar.lectura_hasta.fecha]
                    if len(must_have_value) == 1:

                        if not lectua_a_canviar.ajuste:
                            lectua_a_canviar.ajuste = Ajuste(None)
                        else:
                            lectua_a_canviar.ajuste = Ajuste(lectua_a_canviar.ajuste.ajuste)
                        old_ajust = lectua_a_canviar.ajuste and lectua_a_canviar.ajuste.ajuste_por_integrador or 0.0
                        consum_original = (lectua_a_canviar.lectura_hasta.lectura - lectua_a_canviar.lectura_desde.lectura + old_ajust)

                        lectua_a_canviar.lectura_hasta = lectua_a_canviar.lectura_hasta
                        lectua_a_canviar.lectura_hasta.lectura = must_have_value[0]

                        new_val = consum_original - (lectua_a_canviar.lectura_hasta.lectura - lectua_a_canviar.lectura_desde.lectura + old_ajust)
                        if new_val != (lectua_a_canviar.lectura_hasta.lectura - lectua_a_canviar.lectura_desde.lectura + old_ajust):
                            lectua_a_canviar.ajuste.ajuste_por_integrador = consum_original - (lectua_a_canviar.lectura_hasta.lectura - lectua_a_canviar.lectura_desde.lectura)
                            lectua_a_canviar.ajuste.codigo_motivo = '98'

                res.extend(lectures_per_periode.get(periode))
                done_reads = [l.lectura_desde.fecha for l in lectures_per_periode.get(periode)]
                try:
                    for ldate in lectures_by_date.keys():
                        if ldate not in done_reads:
                            base_lectura = lectures_by_date[ldate][0]
                            lectura_desde_val = 0
                            lectura_hasta_val = 0
                            for same_period_l in lectures_per_periode.get(periode):
                                if same_period_l.lectura_desde.fecha == base_lectura.lectura_hasta.fecha:
                                    lectura_desde_val = same_period_l.lectura_desde.lectura
                                    lectura_hasta_val = same_period_l.lectura_desde.lectura
                            aux = self.get_fake_pX_lectura(tipus, periode, base_lectura, lectura_desde=lectura_desde_val, lectura_hasta=lectura_hasta_val)
                            res.append(aux)
                except:
                    # Lo de dal es una mandanga que es una basura que estem obligats a fer. Si falla, no vull que falli
                    # la resta del F1. Si es un F1 amb cara i ulls ni hi passara per aqui
                    pass
        return res

    def get_consum_facturat(self, tipus, periode=None):
        if tipus not in ['A', 'S', 'R']:
            return None

        if self.datos_factura.tipo_factura == 'G' and tipus == 'A':
            res = []
            for comptador in self.get_comptadors():
                for lectura in comptador.get_lectures(tipus, force_no_transforma_no_td_a_td=True):
                    consum = round(lectura.lectura_hasta.lectura_float - lectura.lectura_desde.lectura_float, 2)
                    if lectura.ajuste:
                        consum += lectura.ajuste.ajuste_por_integrador
                    if not periode or periode == lectura.periode:
                        res.append(consum)
            if not res:
                res.append(0.0)
            return res

        if tipus == 'A' and self.energia_activa:
            res = []
            for activa in self.energia_activa.terminos_energia_activa:
                for periode_activa in activa.periodos:
                    if periode_activa.nombre == periode or not periode:
                        res.append(periode_activa.cantidad)
            if not res:
                res.append(0.0)
            return res

        if tipus == 'S':
            res = []
            if self.autoconsumo and self.autoconsumo.energia_excedentaria:
                for terme in self.autoconsumo.energia_excedentaria.terminos_energia_excedentaria:
                    for periode_ex in terme.periodos:
                        if periode_ex.nombre == periode or not periode:
                            res.append(periode_ex.cantidad)
            else:
                for concepte in self.conceptos_repercutibles:
                    if concepte.concepto_repercutible[0] == '7' and (not periode or concepte.concepto_repercutible[1] == periode[1]):
                        res.append(concepte.unidades)
            if not res:
                res.append(0.0)
            return res

        if tipus == 'R':
            res = []
            if self.energia_reactiva and self.energia_reactiva.terminos_energia_reactiva:
                for reactiva in self.energia_reactiva.terminos_energia_reactiva:
                    for periode_reactiva in reactiva.periodos:
                        if periode_reactiva.nombre == periode or not periode:
                            res.append(periode_reactiva.cantidad)
            if not res:
                res.append(0.0)
            return res

        return None

    def get_consums_reactiva_capacitiva_a_facturar(self):
        res = {}
        if not self.energia_capacitiva:
            return {}
        if not self.energia_capacitiva.terminos_energia_capacitiva:
            return {}
        for capacitiva in self.energia_capacitiva.terminos_energia_capacitiva:
            for periode in capacitiva.periodos:
                if periode.nombre not in res:
                    res[periode.nombre] = 0.0
                res[periode.nombre] += periode.cantidad
        # El metode esta preparat per si ens envien 6 periodes, 5 amb valor 0 i l'ultim (el p6) amb valor ple
        # Pero com que no se si faran aixo o nomes m'enviaran el P6, fem aquesta mandanga:
        if len(res) == 1 and "P1" in res:
            res['P6'] = res['P1']
            del res['P1']
        return res

    def get_consums_autoconsumida_a_facturar(self):
        res = {}
        info, total = self.get_info_autoconsumo()
        for periode in info:
            if periode.nombre not in res:
                res[periode.nombre] = 0.0
            res[periode.nombre] += periode.cantidad
        return res

    def get_lectures_amb_ajust_autoconsum(self, tipus='S', ajust_balancejat=True, motiu_ajust="98"):
        return self.get_lectures_amb_ajust_quadrat_amb_consum(tipus=tipus, ajust_balancejat=ajust_balancejat, motiu_ajust=motiu_ajust)

    def periodes_facturats_agrupats(self, nperiodes_lectures, tipus='A'):
        if tipus not in ['A', 'S']:
            return None

        res = {}
        if tipus == 'A' and self.energia_activa:
            for activa in self.energia_activa.terminos_energia_activa:
                for periode_activa in activa.periodos:
                    if periode_activa.nombre not in res:
                        res[periode_activa.nombre] = True

        elif tipus == 'S':
            for concepte in self.conceptos_repercutibles:
                if concepte.concepto_repercutible[0] == '7' and concepte.concepto_repercutible not in res:
                    res[concepte.concepto_repercutible] = True
            if self.autoconsumo and self.autoconsumo.energia_excedentaria:
                for excedent in self.autoconsumo.energia_excedentaria.terminos_energia_excedentaria:
                    for periode in excedent.periodos:
                        if periode.nombre not in res:
                            res[periode.nombre] = True

        return len(res.keys()) * 2 == nperiodes_lectures

    def has_AS_lectures(self):
        for medida in self.medidas:
            for aparell in medida.modelos_aparatos:
                try:
                    for integrador in aparell.integradores:
                        if integrador.tipus == 'S':
                            return True
                except AttributeError:
                    pass
        return False

    def has_AS_lectures_only_p0(self):
        has_p0 = False
        for medida in self.medidas:
            for aparell in medida.modelos_aparatos:
                try:
                    for integrador in aparell.integradores:
                        if integrador.tipus == 'S' and  integrador.codigo_periodo not in ('10', '20', '30', '90'):
                            return False
                        elif integrador.tipus == 'S' and  integrador.codigo_periodo in ('10', '20', '30', '90'):
                            has_p0 = True
                except AttributeError:
                    pass
        return has_p0

    def get_fake_AS_lectures(self):
        res = []
        comptador_amb_lectures = None
        for medida in self.medidas:
            for c in medida.modelos_aparatos:
                if c.get_lectures_activa_entrant():
                    comptador_amb_lectures = c
                    break
        if comptador_amb_lectures:
            te_autoconsum = (self.autoconsumo and self.autoconsumo.energia_excedentaria) or ([x for x in (self.conceptos_repercutibles or []) if '7' == x.concepto_repercutible[0]])
            if not te_autoconsum:
                return res
            base_info = comptador_amb_lectures.get_lectures_activa_entrant()[0]
            i = 0
            for consum in self.get_consum_facturat(tipus='S'):
                i += 1
                l1 = Lectura(None)
                l1.fecha = base_info.lectura_desde.fecha
                l1.lectura = 0
                l1.procedencia = base_info.lectura_desde.procedencia
                l2 = Lectura(None)
                l2.fecha = base_info.lectura_hasta.fecha
                l2.lectura = 0
                l2.procedencia = base_info.lectura_hasta.procedencia
                new_integrador = Integrador(base_info.integrador)
                new_integrador.magnitud = "AS"
                new_integrador.numero_ruedas_enteras = base_info.numero_ruedas_enteras
                new_integrador.codigo_periodo = base_info.codigo_periodo[0] + str(i)
                if not new_integrador.periode:
                    new_integrador.codigo_periodo = base_info.codigo_periodo
                new_integrador.lectura_desde = l1
                new_integrador.lectura_hasta = l2
                res.append(new_integrador)
        return res

    def get_fake_pX_lectura(self, tipus, periode, base_info, lectura_desde=0, lectura_hasta=0):
        l1 = Lectura(None)
        l1.fecha = base_info.lectura_desde.fecha
        l1.lectura = lectura_desde
        l1.procedencia = base_info.lectura_desde.procedencia
        l2 = Lectura(None)
        l2.fecha = base_info.lectura_hasta.fecha
        l2.lectura = lectura_hasta
        l2.procedencia = base_info.lectura_hasta.procedencia

        new_integrador = Integrador(None)
        new_integrador.magnitud = {v: k for k, v in MAGNITUDS_OCSUM.iteritems()}.get(tipus, tipus)
        new_integrador.numero_ruedas_enteras = base_info.numero_ruedas_enteras
        new_integrador.codigo_periodo = periode
        new_integrador.lectura_desde = l1
        new_integrador.lectura_hasta = l2

        # consums_desitjats = self.get_consum_facturat(tipus=tipus, periode=periode)
        # if consums_desitjats and len(consums_desitjats) > 1:
        #     raise Exception("No es poden calcular els ajustos de les lectures perque hi ha varis consums per 1 periode")
        # elif consums_desitjats:
        #     consum = consums_desitjats[0]
        #     if not new_integrador.ajuste:
        #         new_integrador.ajuste = Ajuste(None)
        #     new_integrador.ajuste = Ajuste(new_integrador.ajuste.ajuste)
        #     old_ajust = new_integrador.ajuste and new_integrador.ajuste.ajuste_por_integrador or 0.0
        #     new_val = consum - (l2.lectura - l1.lectura + old_ajust)
        #     if new_val != (l2.lectura - l1.lectura + old_ajust):
        #         new_integrador.ajuste.ajuste_por_integrador = consum - (l2.lectura - l1.lectura)
        #         new_integrador.ajuste.codigo_motivo = "99"

        return new_integrador

    def get_fake_AS_p2_lectures(self):
        res = []
        comptador_amb_lectures = None
        for medida in self.medidas:
            for c in medida.modelos_aparatos:
                if c.get_lectures_activa_sortint():
                    comptador_amb_lectures = c
                    break
        if comptador_amb_lectures:
            te_autoconsum = (self.autoconsumo and self.autoconsumo.energia_excedentaria) or ([x for x in (self.conceptos_repercutibles or []) if '7' == x.concepto_repercutible[0]])
            if not te_autoconsum:
                return res
            base_info = comptador_amb_lectures.get_lectures_activa_entrant()[0]
            i = 0
            for consum in self.get_consum_facturat(tipus='S'):
                i += 1
                if i <= 1:
                    continue
                l1 = Lectura(None)
                l1.fecha = base_info.lectura_desde.fecha
                l1.lectura = 0
                l1.procedencia = base_info.lectura_desde.procedencia
                l2 = Lectura(None)
                l2.fecha = base_info.lectura_hasta.fecha
                l2.lectura = 0
                l2.procedencia = base_info.lectura_hasta.procedencia
                new_integrador = Integrador(None)
                new_integrador.magnitud = "AS"
                new_integrador.numero_ruedas_enteras = base_info.numero_ruedas_enteras
                new_integrador.codigo_periodo = base_info.codigo_periodo[0] + str(i)
                if not new_integrador.periode:
                    new_integrador.codigo_periodo = base_info.codigo_periodo
                new_integrador.lectura_desde = l1
                new_integrador.lectura_hasta = l2
                res.append(new_integrador)
        return res

    def get_lectures_amb_ajust_quadrat_amb_consum(self, tipus='S', ajust_balancejat=True, motiu_ajust="98", lectures=None):
        lectures_per_periode = {}
        lectures_del_tipus = []
        if lectures is None:
            for comptador in self.get_comptadors():
                for lectura in comptador.get_lectures(tipus, force_no_transforma_no_td_a_td=True):
                    lectura.comptador = comptador
                    lectures_del_tipus.append(lectura)
        else:
            for lectura in lectures:
                if lectura.tipus == tipus:
                    lectures_del_tipus.append(lectura)

        if not lectures_del_tipus:
            return {}

        for lectura in lectures_del_tipus:
            periode = lectura.periode
            if not lectures_per_periode.get(periode):
                lectures_per_periode[periode] = []
            lectures_per_periode[periode].append(lectura)

            nperiodes = len([l for l in lectures_per_periode.keys() if l])
            if self.periodes_facturats_agrupats(nperiodes, tipus=tipus) and ajust_balancejat:
                for periode in lectures_per_periode.keys():
                    if not periode:
                        continue
                    periode_agrupat = "P{0}".format(int(periode[1:]) + nperiodes/2)
                    if lectures_per_periode.get(periode_agrupat):
                        lectures_per_periode[periode].extend(lectures_per_periode.get(periode_agrupat))
                        if periode_agrupat != periode:
                            del lectures_per_periode[periode_agrupat]

        res = {}
        for periode, lectures in lectures_per_periode.iteritems():
            if ajust_balancejat:
                consums_desitjats = self.get_consum_facturat(tipus=tipus, periode=periode)
                if consums_desitjats:
                    consums_repartits = repartir_consums_entre_lectures(consums_desitjats, lectures)
                    for lectura, consum in consums_repartits.iteritems():
                        new_val = self.get_ajust_from_consum_desitjat(lectura, consum)
                        if new_val:
                            lectura.ajuste.ajuste_por_integrador = new_val
                            lectura.ajuste.codigo_motivo = motiu_ajust  # normalment 98 - Autoconsumo
            for l in lectures:
                if not res.get(l.comptador):
                    res[l.comptador] = []
                res[l.comptador].append(l)
        return res

    def get_ajust_from_consum_desitjat(self, lectura_a_ajustar, consum_desitjat):
        if not lectura_a_ajustar.ajuste:
            lectura_a_ajustar.ajuste = Ajuste(None)
        else:
            lectura_a_ajustar.ajuste = Ajuste(lectura_a_ajustar.ajuste.ajuste)

        if lectura_a_ajustar.magnitud in ('AE', 'AS'):
            new_val = self.get_ajust_from_consum_desitjat_Ax(lectura_a_ajustar, consum_desitjat)
        elif lectura_a_ajustar.magnitud in ('R1', 'R2', 'R3', 'R4'):
            new_val = self.get_ajust_from_consum_desitjat_Rx(lectura_a_ajustar, consum_desitjat)
        else:
            new_val = 0.0

        return new_val

    def get_ajust_from_consum_desitjat_Ax(self, lectura_a_ajustar, consum_desitjat):
        new_val = consum_desitjat - (lectura_a_ajustar.lectura_hasta.lectura - lectura_a_ajustar.lectura_desde.lectura)
        return new_val

    def get_ajust_from_consum_desitjat_Rx(self, lectura_a_ajustar, consum_desitjat):
        if consum_desitjat == 0:
            old_ajust = lectura_a_ajustar.ajuste and lectura_a_ajustar.ajuste.ajuste_por_integrador or 0.0
            return -(lectura_a_ajustar.lectura_hasta.lectura - lectura_a_ajustar.lectura_desde.lectura + old_ajust)

        consums_facturats_activa = self.get_consum_facturat(tipus='A', periode=lectura_a_ajustar.periode)
        consum_facturat_activa = sum(consums_facturats_activa)

        reactiva_real_mesurada = consum_desitjat + (consum_facturat_activa * 0.33)

        old_ajust = lectura_a_ajustar.ajuste and lectura_a_ajustar.ajuste.ajuste_por_integrador or 0.0
        new_val = reactiva_real_mesurada - (lectura_a_ajustar.lectura_hasta.lectura - lectura_a_ajustar.lectura_desde.lectura + old_ajust)
        return new_val

    def get_lectures_activa_entrant(self, ajust_balancejat=True, motiu_ajust="98"):
        return self.get_lectures_amb_ajust_quadrat_amb_consum(tipus='A', ajust_balancejat=ajust_balancejat, motiu_ajust=motiu_ajust)

    def get_lectures_activa_sortint(self, ajust_balancejat=True, motiu_ajust="98"):
        return self.get_lectures_amb_ajust_quadrat_amb_consum(tipus='S', ajust_balancejat=ajust_balancejat, motiu_ajust=motiu_ajust)

    def get_comptadors(self):
        """Retorna totes les lectures en una llista de comptadors"""
        comptadors_agrupats = {}
        for medida in self.medidas:
            for aparell in medida.modelos_aparatos:
                aparell.cod_pm = medida.cod_pm
                comptadors_agrupats.setdefault(
                    aparell.numero_serie, []
                ).append(aparell)

        comptadors = []
        for llista_aparells in comptadors_agrupats.values():
            aparell_multi = MultiModeloAparato(llista_aparells, self)

            di, df = aparell_multi.get_dates_inici_i_final()
            comptadors.append((di, df, aparell_multi))
        return [a[2] for a in sorted(comptadors, lambda x,y: cmp(x[0], y[0]))]

    def get_info_potencia(self):
        """Retorna els periodes de potència"""
        periodes = []
        total = 0
        try:
            if self.potencia:
                for pot in self.potencia.terminos_potencia:
                    periodes += pot.periodos
                total = self.potencia.importe_total
        except AttributeError:
            pass
        return periodes, total

    def get_info_potencia_cargos(self):
        return self.get_info_cargos(tipo_cargo=1)

    def get_info_energia_cargos(self):
        return self.get_info_cargos(tipo_cargo=2)

    def get_info_cargos(self, tipo_cargo):
        periodes = []
        total = 0
        try:
            if self.cargos and self.cargos.cargo:
                for cargo_by_type in self.cargos.cargo:
                    if cargo_by_type.tipo_cargo == tipo_cargo:
                        for termino_pot in cargo_by_type.termino_cargo:
                            periodes += termino_pot.periodos
                        total += cargo_by_type.importe_total
        except AttributeError:
            pass
        return periodes, total

    def get_info_exces(self):
        """Retorna els periodes de potència"""
        periodes = []
        total = 0
        try:
            if self.exceso_potencia:
                periodes += self.exceso_potencia.periodos
                total = self.exceso_potencia.importe_total
        except AttributeError:
            pass
        return periodes, total

    def get_info_activa(self):
        periodes = []
        total = 0

        if self.energia_activa:
            total = self.energia_activa.importe_total

            for activa in self.energia_activa.terminos_energia_activa:
                periodes += activa.periodos

        return periodes, total

    def get_info_generacio(self):
        periodes = []
        total = 0

        if self.autoconsumo and self.autoconsumo.energia_excedentaria:
            total = 0

            for activa in self.autoconsumo.energia_excedentaria.terminos_energia_excedentaria:
                periodes += activa.periodos

        return periodes, total

    def get_info_generacio_neta(self):
        periodes = []
        total = 0

        if self.autoconsumo and self.autoconsumo.instalacion_gen_autoconsumo:
            for inst in self.autoconsumo.instalacion_gen_autoconsumo:
                for activa in inst.energia_neta_gen.terminos_energia_neta_gen:
                    periodes += activa.periodos

        return periodes, total

    def get_info_autoconsumo(self):
        periodes = []
        total = 0

        if self.autoconsumo and self.autoconsumo.instalacion_gen_autoconsumo:
            for inst in self.autoconsumo.instalacion_gen_autoconsumo:
                total += inst.energia_autoconsumida.importe_total
                for activa in inst.energia_autoconsumida.terminos_energia_autoconsumida:
                    periodes += activa.periodos

        return periodes, total

    def get_info_reactiva(self):
        periodes = []
        total = 0

        if self.energia_reactiva:
            total = self.energia_reactiva.importe_total

            for reactiva in self.energia_reactiva.terminos_energia_reactiva:
                periodes += reactiva.periodos

        return periodes, total

    def get_info_lloguer(self):
        lloguers = []
        total = 0

        if self.alquiler:
            lloguers = self.alquiler.precios_alquiler
            total = self.alquiler.importe_total

        return lloguers, total

    def get_info_facturacio_potencia(self):
        """
        Retorna el mode de control de potència en funció de la tarifa,
        el mode control potencia y penalització NO ICP
        :return:
          'max': per maxímetre
          'icp': per icp
          'recarrec': recàrrec per no ICP
        """
        if self.datos_factura.tarifa_atr_fact in TARIFES_SEMPRE_MAX:
            return 'max'

        if self.datos_factura.modo_control_potencia == '2':
            mode = 'max'
        else:
            mode = 'icp'

        if self.potencia and self.potencia.penalizacion_no_icp == 'S':
            return 'recarrec'

        return mode

    def get_maximetres_consumidor(self):
        data = []
        if hasattr(self, 'informacion_al_consumidor') and bool(self.informacion_al_consumidor):
            informacion_al_consumidor = self.informacion_al_consumidor
            fecha_hasta = self.datos_factura.fecha_hasta_factura
            if hasattr(informacion_al_consumidor, 'fecha_inicio_anio_movil') and bool(informacion_al_consumidor.fecha_inicio_anio_movil):
                fecha_desde = informacion_al_consumidor.fecha_inicio_anio_movil
            else:
                data_inici = datetime.strptime(fecha_hasta, '%Y-%m-%d')
                data_inici = data_inici - timedelta(days=365)
                fecha_desde = data_inici.strftime('%Y-%m-%d')

            num_periode = 1

            for periodo in informacion_al_consumidor.periodos:
                period_name = 'P{}'.format(num_periode)
                maximetro = periodo.potencia_max_demandada_anio_movil

                vals = {
                    'fecha_desde': fecha_desde,
                    'fecha_hasta': fecha_hasta,
                    'periode': period_name,
                    'maximetre_consumidor': maximetro / 1000.0,
                }
                data.append(vals)
                num_periode += 1
        return data


class ConceptoRepercutible(object):

    def __init__(self, data):
        self.concepto = data

    @property
    def concepto_repercutible(self):
        if hasattr(self.concepto, 'ConceptoRepercutible'):
            return self.concepto.ConceptoRepercutible.text.strip()
        return None

    @property
    def tipo_impositivo(self):
        if hasattr(self.concepto, 'TipoImpositivoConceptoRepercutible'):
            return self.concepto.TipoImpositivoConceptoRepercutible.text.strip()
        return None

    @property
    def fecha_operacion(self):
        if hasattr(self.concepto, 'FechaOperacion'):
            return self.concepto.FechaOperacion.text.strip()
        return None

    @property
    def fecha_desde(self):
        if hasattr(self.concepto, 'FechaDesde'):
            return self.concepto.FechaDesde.text.strip()
        return None

    @property
    def fecha_hasta(self):
        if hasattr(self.concepto, 'FechaHasta'):
            return self.concepto.FechaHasta.text.strip()
        return None

    @property
    def unidades(self):
        if hasattr(self.concepto, 'UnidadesConceptoRepercutible'):
            return float(self.concepto.UnidadesConceptoRepercutible.text.strip())
        return None

    @property
    def precio_unidad(self):
        if hasattr(self.concepto, 'PrecioUnidadConceptoRepercutible'):
            return float(self.concepto.PrecioUnidadConceptoRepercutible.text.strip())
        return None

    @property
    def importe(self):
        if hasattr(self.concepto, 'ImporteTotalConceptoRepercutible'):
            return float(self.concepto.ImporteTotalConceptoRepercutible.text.strip())
        return None

    @property
    def comentarios(self):
        if hasattr(self.concepto, 'Comentarios'):
            return self.concepto.Comentarios.text
        return None

    def is_autoconsum(self):
        return self.concepto_repercutible in CODIS_AUTOCONSUM.keys()

class OtraFactura(Factura):
    DATOS_GENERALES_NAME = 'DatosGeneralesOtrasFacturas'
    DATOS_GENERALES_OBJECT = DatosGeneralesOtras


class RegistroFin(object):

    def __init__(self, data):
        self.registro = data

    @property
    def importe_total(self):
        if hasattr(self.registro, 'ImporteTotal'):
            return float(self.registro.ImporteTotal.text.strip())
        return None

    @property
    def saldo_total(self):
        if hasattr(self.registro, 'SaldoTotalFacturacion'):
            return float(self.registro.SaldoTotalFacturacion.text.strip())
        return None

    @property
    def total_recibos(self):
        if hasattr(self.registro, 'TotalRecibos'):
            return float(self.registro.TotalRecibos.text.strip())
        return None

    @property
    def tipo_moneda(self):
        if hasattr(self.registro, 'TipoMoneda'):
            return self.registro.TipoMoneda.text.strip()
        return None

    @property
    def fecha_valor(self):
        if hasattr(self.registro, 'FechaValor'):
            return self.registro.FechaValor.text.strip()
        return None

    @property
    def fecha_limite_pago(self):
        if hasattr(self.registro, 'FechaLimitePago'):
            return self.registro.FechaLimitePago.text.strip()
        return None

    @property
    def iban(self):
        if hasattr(self.registro, 'IBAN'):
            return self.registro.IBAN.text.strip()
        return None

    @property
    def id_remesa(self):
        if hasattr(self.registro, 'IdRemesa'):
            return self.registro.IdRemesa.text.strip()
        return None

    def get_remesa(self):
        vals = {
           'id_remesa': self.id_remesa,
           'fecha_valor_remesa': self.fecha_valor,
           'data_limit_pagament': self.fecha_limite_pago,
           'total_importe_remesa': self.importe_total,
           'total_recibos_remesa': self.total_recibos,
        }
        return vals


def agrupar_lectures_per_data(lectures):
    """Retorna un diccionari de llistes en què les
       claus són les dates inicial i final de les lectures
    """
    lect = {}
    for i in lectures:
        if i.magnitud == 'PM':
            key = (i.lectura_hasta.fecha, i.lectura_hasta.fecha)
        else:
            key = (i.lectura_desde.fecha, i.lectura_hasta.fecha)
        if key not in lect:
            lect[key] = []
        lect[key].append(i)
    return lect


def obtenir_data_inici_i_final(dic):
    """Retorna la data inicial i final del diccionari retornat
       per la funció agrupar_lectures_per_data()
    """
    inici_conjunt = None
    final_conjunt = None
    for keys in dic.keys():
        if not inici_conjunt or inici_conjunt > keys[0]:
            inici_conjunt = keys[0]
        if not final_conjunt or final_conjunt < keys[1]:
            final_conjunt = keys[1]

    return inici_conjunt, final_conjunt
