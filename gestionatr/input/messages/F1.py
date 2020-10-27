# -*- coding: utf-8 -*-
from message import Message
from gestionatr.input.messages.C2 import Direccion
from gestionatr.defs import TARIFES_SEMPRE_MAX
from datetime import datetime, date
from gestionatr.utils import repartir_consums_entre_lectures

# Magnituds d'OCSUM
MAGNITUDS_OCSUM = {
    'AE': 'A',
    'AS': 'S',
    'R1': 'R',
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
}

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

    def get_coeficient_repartiment(self):
        try:
            for concepte in self.conceptos_repercutibles:
                if concepte.concepto_repercutible == '82':
                    return concepte.unidades
        except AttributeError:
            # We might not have any "Coeficient de repartiment"
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

        for type, method in self.GETTERS_LINEAS_FACTURA:
            lines, sub_total = method()

            if lines:
                res.setdefault(type, {'total': 0.0, 'lines': []})

                res[type]['lines'] += lines
                new_total = res[type]['total'] + sub_total
                res[type]['total'] = round(new_total, 2)

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
            'check_total': abs(self.datos_factura.importe_total_factura)
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

    @property
    def nombre(self):
        return self._name

    @property
    def precio(self):
        if self.NOMBRE_PRECIO:
            if hasattr(self.periodo, self.NOMBRE_PRECIO):
                return float(getattr(self.periodo, self.NOMBRE_PRECIO).text.strip())
        return None

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


class PeriodoExcesoPotencia(object):

    def __init__(self, data, name):
        self.periodo = data
        self._name = name

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


class ExcesoPotencia(object):

    def __init__(self, data):
        self.exceso_potencia = data

    @property
    def periodos(self):
        data = []
        if hasattr(self.exceso_potencia, 'Periodo'):
            period_name = 1

            for d in self.exceso_potencia.Periodo:
                period = PeriodoExcesoPotencia(d, 'P{0}'.format(period_name))
                data.append(period)
                period_name += 1
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


class TerminoEnergiaReactiva(TerminoEnergiaActiva):

    PERIODO_TYPE = PeriodoEnergiaReactiva


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
    def lectura(self):
        if self._lectura is not None:
            return self._lectura
        if hasattr(self.lectura_data, 'Lectura'):
            return float(self.lectura_data.Lectura.text.strip())
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
        return PERIODE_OCSUM.get(self.codigo_periodo, None)

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
            for d in self.modelo_aparato.Integrador:
                integrador = Integrador(d)
                if integrador.codigo_periodo in ['21', '22', '81', '82', '83'] and integrador.magnitud == 'PM':
                    # Algunes distris envien 2/3 periodes de potencia en les DHx ...
                    # Diuen que només facturen la mes gran i la CNMC diu que esta be :(
                    # Els guardem per tractarlos despres
                    integradors_dh_per_data.setdefault(integrador.lectura_hasta.fecha, [])
                    integradors_dh_per_data[integrador.lectura_hasta.fecha].append(integrador)
                else:
                    data.append(integrador)

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
        for lect in self.get_lectures():
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

    def get_lectures(self, tipus=None):
        """Retorna totes les lectures en una llista de Lectura"""
        lectures = []
        try:
            for integrador in self.integradores:
                # If we don't have any type requirements or the current
                # reading is in them
                if not tipus or integrador.tipus in tipus:
                    lectures.append(integrador)
        except AttributeError:
            pass

        if (not tipus or "S" in tipus) and self.factura and self.factura.get_consum_facturat(tipus='S', periode=None) and not self.factura.has_AS_lectures():
            # Si no tenim lectures AS pero si que ens han cobrat excedents,
            # creem unes lectures AS ficticies a 0 (puta ENDESA)
            lectures.extend(self.factura.get_fake_AS_lectures())
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
        return self.get_lectures(['A', 'S', 'R'])

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


class FacturaATR(Factura):
    DATOS_GENERALES_NAME = 'DatosGeneralesFacturaATR'
    DATOS_GENERALES_OBJECT = DatosGeneralesATR

    def __init__(self, data):
        super(FacturaATR, self).__init__(data)

        self.GETTERS_LINEAS_FACTURA += [
            ('potencia', self.get_info_potencia),
            ('exces_potencia', self.get_info_exces),
            ('energia', self.get_info_activa),
            ('reactiva', self.get_info_reactiva),
            ('lloguer', self.get_info_lloguer),
        ]

    def te_autoconsum(self):
        for concepte in self.conceptos_repercutibles:
            if concepte.concepto_repercutible in CODIS_AUTOCONSUM.keys():
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

    def get_consum_facturat(self, tipus, periode=None):
        if tipus not in ['A', 'S']:
            return None

        if tipus == 'A' and self.energia_activa:
            res = []
            for activa in self.energia_activa.terminos_energia_activa:
                for periode_activa in activa.periodos:
                    if periode_activa.nombre == periode or not periode:
                        res.append(periode_activa.cantidad)
            return res

        if tipus == 'S':
            res = []
            for concepte in self.conceptos_repercutibles:
                if concepte.concepto_repercutible[0] == '7' and (not periode or concepte.concepto_repercutible[1] == periode[1]):
                    res.append(concepte.unidades)
            return res

        return None

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

        else:  # if tipus == 'S':
            for concepte in self.conceptos_repercutibles:
                if concepte.concepto_repercutible[0] == '7' and concepte.concepto_repercutible not in res:
                    res[concepte.concepto_repercutible] = True

        return len(res.keys()) != nperiodes_lectures

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

    def get_fake_AS_lectures(self):
        res = []
        comptador_amb_lectures = None
        for medida in self.medidas:
            for c in medida.modelos_aparatos:
                if c.get_lectures_activa_entrant():
                    comptador_amb_lectures = c
                    break
        if comptador_amb_lectures:
            base_info = comptador_amb_lectures.get_lectures_activa_entrant()[0]
            for concepte in self.conceptos_repercutibles:
                if concepte.concepto_repercutible[0] == '7':
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
                    new_integrador.codigo_periodo = base_info.codigo_periodo[0] + concepte.concepto_repercutible[1]
                    if not new_integrador.periode:
                        new_integrador.codigo_periodo = base_info.codigo_periodo
                    new_integrador.lectura_desde = l1
                    new_integrador.lectura_hasta = l2
                    res.append(new_integrador)
        return res

    def get_lectures_amb_ajust_quadrat_amb_consum(self, tipus='S', ajust_balancejat=True, motiu_ajust="98"):
        lectures_per_periode = {}
        for comptador in self.get_comptadors():
            for lectura in comptador.get_lectures(tipus):
                lectura.comptador = comptador
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
                        del lectures_per_periode[periode_agrupat]

        res = {}
        for periode, lectures in lectures_per_periode.iteritems():
            if ajust_balancejat:
                consums_desitjats = self.get_consum_facturat(tipus=tipus, periode=periode)
                if not consums_desitjats:
                    continue
                consums_repartits = repartir_consums_entre_lectures(consums_desitjats, lectures)
                for lectura, consum in consums_repartits.iteritems():
                    if not lectura.ajuste:
                        lectura.ajuste = Ajuste(None)
                    else:
                        lectura.ajuste = Ajuste(lectura.ajuste.ajuste)
                    old_ajust = lectura.ajuste and lectura.ajuste.ajuste_por_integrador or 0.0
                    new_val = consum - (lectura.lectura_hasta.lectura - lectura.lectura_desde.lectura + old_ajust)
                    if new_val != (lectura.lectura_hasta.lectura - lectura.lectura_desde.lectura + old_ajust):
                        lectura.ajuste.ajuste_por_integrador = consum - (lectura.lectura_hasta.lectura - lectura.lectura_desde.lectura)
                        lectura.ajuste.codigo_motivo = motiu_ajust  # normalment 98 - Autoconsumo
            for l in lectures:
                if not res.get(l.comptador):
                    res[l.comptador] = []
                res[l.comptador].append(l)
        return res

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

        if self.potencia.penalizacion_no_icp == 'S':
            return 'recarrec'

        return mode


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
