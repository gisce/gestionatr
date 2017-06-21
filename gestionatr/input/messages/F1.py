# -*- coding: utf-8 -*-
from message import Message
from gestionatr.input.messages.C2 import Direccion
from datetime import datetime

# Magnituds d'OCSUM
MAGNITUDS_OCSUM = {
    'AE': 'A',
    'R1': 'R',
    'PM': 'M',
    'EP': 'EP'
}

# Retorna el nom de periode segons el periode d'OCSUM
PERIODE_OCSUM = {
    '01': 'P1',  # Punta + Llano
    '03': 'P2',  # Valle
    '10': 'P1',  # Totalizador
    '21': 'P1',  # P1 Tarifes: 004, 006
    '22': 'P2',  # P2 Tarifes: 004, 006
    '31': 'P1',  # P1 Tarifa 011
    '32': 'P2',  # P2 Tarifa 011
    '33': 'P3',  # P3 Tarifa 011
    '61': 'P1',  # Periodo 1 Tarifes: 003, 011, 012 - 017
    '62': 'P2',  # Periodo 2 Tarifes: 003, 011, 012 - 017
    '63': 'P3',  # Periodo 3 Tarifes: 003, 011, 012 - 017
    '64': 'P4',  # Periodo 4 Tarifes: 003, 011, 012 - 017
    '65': 'P5',  # Periodo 5 Tarifes: 003, 011, 012 - 017
    '66': 'P6',  # Periodo 6 Tarifes: 003, 011, 012 - 017
    '81': 'P1',  # P1 Tarifa 007
    '82': 'P2',  # P2 Tarifa 007
    '83': 'P3',  # P3 Tarifa 007
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
            return self.expediente.NumeroExpediente.text
        return None

    @property
    def codigo_solicitud(self):
        if hasattr(self.expediente, 'CodigoSolicitud'):
            return self.expediente.CodigoSolicitud.text
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
            return self.datos_generales.CodContrato.text
        return None

    @property
    def _datos_generales_factura(self):
        if hasattr(self.datos_generales, 'DatosGeneralesFactura'):
            return self.datos_generales.DatosGeneralesFactura
        return None

    @property
    def codigo_fiscal_factura(self):
        if hasattr(self._datos_generales_factura, 'CodigoFiscalFactura'):
            return self._datos_generales_factura.CodigoFiscalFactura.text
        return None

    @property
    def tipo_factura(self):
        if hasattr(self._datos_generales_factura, 'TipoFactura'):
            return self._datos_generales_factura.TipoFactura.text
        return None

    @property
    def motivo_facturacion(self):
        if hasattr(self._datos_generales_factura, 'MotivoFacturacion'):
            return self._datos_generales_factura.MotivoFacturacion.text
        return None

    @property
    def codigo_factura_rectificada_anulada(self):
        has_attr = hasattr(
            self._datos_generales_factura, 'CodigoFacturaRectificadaAnulada'
        )
        if has_attr:
            datos_generales_fact = self._datos_generales_factura
            return datos_generales_fact.CodigoFacturaRectificadaAnulada.text
        return None

    @property
    def expediente(self):
        if hasattr(self._datos_generales_factura, 'Expediente'):
            return Expediente(self._datos_generales_factura.Expediente)
        return None

    @property
    def fecha_factura(self):
        if hasattr(self._datos_generales_factura, 'FechaFactura'):
            return self._datos_generales_factura.FechaFactura.text
        return None

    @property
    def identificador_emisora(self):
        if hasattr(self._datos_generales_factura, 'IdentificadorEmisora'):
            return self._datos_generales_factura.IdentificadorEmisora.text
        return None

    @property
    def comentarios(self):
        if hasattr(self._datos_generales_factura, 'Comentarios'):
            return self._datos_generales_factura.Comentarios.text
        return None

    @property
    def importe_total_factura(self):
        if hasattr(self._datos_generales_factura, 'ImporteTotalFactura'):
            return self._datos_generales_factura.ImporteTotalFactura
        return None

    @property
    def saldo_factura(self):
        if hasattr(self._datos_generales_factura, 'SaldoFactura'):
            return self._datos_generales_factura.SaldoFactura
        return None

    @property
    def tipo_moneda(self):
        if hasattr(self._datos_generales_factura, 'TipoMoneda'):
            return self._datos_generales_factura.TipoMoneda.text
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
            return self._datos_factura_atr.FechaBOE.text
        return None

    @property
    def tarifa_atr_fact(self):
        if hasattr(self._datos_factura_atr, 'TarifaATRFact'):
            return self._datos_factura_atr.TarifaATRFact.text
        return None

    @property
    def modo_control_potencia(self):
        if hasattr(self._datos_factura_atr, 'ModoControlPotencia'):
            return self._datos_factura_atr.ModoControlPotencia.text
        return None

    @property
    def marca_medida_con_perdidas(self):
        if hasattr(self._datos_factura_atr, 'MarcaMedidaConPerdidas'):
            return self._datos_factura_atr.MarcaMedidaConPerdidas.text
        return None

    @property
    def vas_trafo(self):
        if hasattr(self._datos_factura_atr, 'VAsTrafo'):
            return self._datos_factura_atr.VAsTrafo
        return None

    @property
    def porcentaje_perdidas(self):
        if hasattr(self._datos_factura_atr, 'PorcentajePerdidas'):
            return self._datos_factura_atr.PorcentajePerdidas
        return None

    @property
    def indicativo_curva_carga(self):
        if hasattr(self._datos_factura_atr, 'IndicativoCurvaCarga'):
            return self._datos_factura_atr.IndicativoCurvaCarga.text
        return None

    @property
    def _periodo_cch(self):
        if hasattr(self._datos_factura_atr, 'PeriodoCCH'):
            return self._datos_factura_atr.PeriodoCCH
        return None

    @property
    def _fecha_desde_cch(self):
        if hasattr(self._periodo_cch, 'FechaDesdeCCH'):
            return self._periodo.FechaDesdeCCH.text
        return None

    @property
    def _fecha_hasta_cch(self):
        if hasattr(self._periodo_cch, 'FechaHastaCCH'):
            return self._periodo.FechaHastaCCH.text
        return None

    @property
    def _periodo(self):
        if hasattr(self._datos_factura_atr, 'Periodo'):
            return self._datos_factura_atr.Periodo
        return None

    @property
    def fecha_desde_factura(self):
        if hasattr(self._periodo, 'FechaDesdeFactura'):
            return self._periodo.FechaDesdeFactura.text
        return None

    @property
    def fecha_hasta_factura(self):
        if hasattr(self._periodo, 'FechaHastaFactura'):
            return self._periodo.FechaHastaFactura.text
        return None

    @property
    def numero_dias(self):
        if hasattr(self._periodo, 'NumeroDias'):
            return self._periodo.NumeroDias
        return None


class DatosGeneralesOtras(DatosGenerales):

    @property
    def fecha_boe(self):
        if hasattr(self.datos_generales, 'FechaBOE'):
            return self.datos_generales.FechaBOE.text
        return None


class Cliente(object):

    def __init__(self, data):
        self.cliente = data

    @property
    def tipo_identificador(self):
        return getattr(self.cliente, 'TipoIdentificador', None)

    @property
    def identificador(self):
        return getattr(self.cliente, 'Identificador', None)

    @property
    def tipo_persona(self):
        return getattr(self.cliente, 'TipoPersona', None)


class Factura(object):

    DATOS_GENERALES_NAME = None
    DATOS_GENERALES_OBJECT = DatosGenerales

    def __init__(self, data):
        self.factura = data

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
        return data

    @property
    def conceptos_repercutibles(self):
        data = []
        if hasattr(self.factura, 'ConceptoRepercutible'):
            for d in self.factura.ConceptoRepercutible:
                data.append(ConceptoRepercutible(d))
        return data

    def sin_base_imponible(self):
        for iva in self.ivas:
            if iva.base != 0:
                return False

        return True


class Periodo(object):

    NOMBRE_PRECIO = None

    def __init__(self, data, name):
        self.periodo = data
        self._name = name

    @property
    def nombre(self):
        return self._name

    @property
    def precio(self):
        if self.NOMBRE_PRECIO:
            return getattr(self.periodo, self.NOMBRE_PRECIO, None)
        return None

    def es_facturable(self):
        "Algunas empresas envian periodos que no se deben facturar con precio 0"
        return bool(self.precio)

class PeriodoPotencia(Periodo):

    NOMBRE_PRECIO = 'PrecioPotencia'

    @property
    def potencia_contratada(self):
        if hasattr(self.periodo, 'PotenciaContratada'):
            return self.periodo.PotenciaContratada
        return None

    @property
    def potencia_max_demandada(self):
        if hasattr(self.periodo, 'PotenciaMaxDemandada'):
            return self.periodo.PotenciaMaxDemandada
        return None

    @property
    def potencia_a_facturar(self):
        if hasattr(self.periodo, 'PotenciaAFacturar'):
            return self.periodo.PotenciaAFacturar
        return None


class Termino(object):

    PERIODO_TYPE = Periodo

    def __init__(self, data):
        self.termino = data

    @property
    def periodos(self):
        data = []
        if hasattr(self.termino, 'Periodo'):
            period_name = 1

            for d in self.termino.Periodo:
                period = self.PERIODO_TYPE(d, 'P{0}'.format(period_name))
                if period.es_facturable():
                    data.append(period)
                    period_name += 1
        return data


class TerminoPotencia(Termino):

    PERIODO_TYPE = PeriodoPotencia

    @property
    def fecha_desde(self):
        if hasattr(self.termino, 'FechaDesde'):
            return self.termino.FechaDesde.text
        return None

    @property
    def fecha_hasta(self):
        if hasattr(self.termino, 'FechaHasta'):
            return self.termino.FechaHasta.text
        return None


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
            return self.potencia.PenalizacionNoICP.text
        return None

    @property
    def importe_total(self):
        if hasattr(self.potencia, 'ImporteTotalTerminoPotencia'):
            return self.potencia.ImporteTotalTerminoPotencia
        return None


class PeriodoEnergiaActiva(Periodo):

    NOMBRE_PRECIO = 'PrecioEnergia'

    @property
    def valor_energia_activa(self):
        if hasattr(self.periodo, 'ValorEnergiaActiva'):
            return self.periodo.ValorEnergiaActiva
        return None


class TerminoEnergiaActiva(Termino):

    PERIODO_TYPE = PeriodoEnergiaActiva

    @property
    def fecha_desde(self):
        if hasattr(self.termino, 'FechaDesde'):
            return self.termino.FechaDesde.text
        return None

    @property
    def fecha_hasta(self):
        if hasattr(self.termino, 'FechaHasta'):
            return self.termino.FechaHasta.text
        return None


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
            return self.energia_activa.ImporteTotalEnergiaActiva
        return None


class PeriodoEnergiaReactiva(Periodo):

    NOMBRE_PRECIO = 'PrecioEnergiaReactiva'

    @property
    def valor_energia_reactiva(self):
        if hasattr(self.periodo, 'ValorEnergiaReactiva'):
            return self.periodo.ValorEnergiaReactiva
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
            return self.energia_reactiva.ImporteTotalEnergiaReactiva
        return None


class Impuesto(object):

    def __init__(self, data):
        self.impuesto = data

    @property
    def base(self):
        if hasattr(self.impuesto, 'BaseImponible'):
            return self.impuesto.BaseImponible
        return None

    @property
    def porcentaje(self):
        if hasattr(self.impuesto, 'Porcentaje'):
            return self.impuesto.Porcentaje
        return None

    @property
    def importe(self):
        if hasattr(self.impuesto, 'Importe'):
            return self.impuesto.Importe
        return None


class ImpuestoElectrico(Impuesto):

    pass


class IVA(Impuesto):

    pass


class Lectura(object):

    def __init__(self, data):
        self.lectura_data = data

    @property
    def fecha(self):
        if hasattr(self.lectura_data, 'Fecha'):
            return self.lectura_data.Fecha.text
        return None

    @property
    def procedencia(self):
        if hasattr(self.lectura_data, 'Procedencia'):
            return self.lectura_data.Procedencia.text
        return None

    @property
    def lectura(self):
        if hasattr(self.lectura_data, 'Lectura'):
            return self.lectura_data.Lectura
        return None


class Integrador(object):

    def __init__(self, data):
        self.integrador = data

    @property
    def magnitud(self):
        if hasattr(self.integrador, 'Magnitud'):
            return self.integrador.Magnitud.text
        return None

    @property
    def codigo_periodo(self):
        if hasattr(self.integrador, 'CodigoPeriodo'):
            return self.integrador.CodigoPeriodo.text
        return None

    @property
    def constante_multiplicadora(self):
        if hasattr(self.integrador, 'ConstanteMultiplicadora'):
            return self.integrador.ConstanteMultiplicadora
        return None

    @property
    def numero_ruedas_enteras(self):
        if hasattr(self.integrador, 'NumeroRuedasEnteras'):
            return self.integrador.NumeroRuedasEnteras
        return None

    @property
    def numero_ruedas_decimales(self):
        if hasattr(self.integrador, 'NumeroRuedasDecimales'):
            return self.integrador.NumeroRuedasDecimales
        return None

    @property
    def consumo_calculado(self):
        if hasattr(self.integrador, 'ConsumoCalculado'):
            return self.integrador.ConsumoCalculado
        return None

    @property
    def lectura_desde(self):
        if hasattr(self.integrador, 'LecturaDesde'):
            return Lectura(self.integrador.LecturaDesde)
        return None

    @property
    def lectura_hasta(self):
        if hasattr(self.integrador, 'LecturaHasta'):
            return Lectura(self.integrador.LecturaHasta)
        return None

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


class ModeloAparato(object):

    def __init__(self, data):
        self.modelo_aparato = data

    @property
    def tipo_aparato(self):
        if hasattr(self.modelo_aparato, 'TipoAparato'):
            return self.modelo_aparato.TipoAparato.text
        return None

    @property
    def marca_aparato(self):
        if hasattr(self.modelo_aparato, 'MarcaAparato'):
            return self.modelo_aparato.MarcaAparato.text
        return None

    @property
    def numero_serie(self):
        if hasattr(self.modelo_aparato, 'NumeroSerie'):
            return self.modelo_aparato.NumeroSerie.text
        return None

    @property
    def tipo_dhedm(self):
        if hasattr(self.modelo_aparato, 'TipoDHEdM'):
            return self.modelo_aparato.TipoDHEdM.text
        return None

    @property
    def integradores(self):
        data = []
        if hasattr(self.modelo_aparato, 'Integrador'):
            for d in self.modelo_aparato.Integrador:
                data.append(Integrador(d))
        return data

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
        return lectures

    def get_lectures_activa(self):
        return self.get_lectures(['A'])

    def get_lectures_reactiva(self):
        return self.get_lectures(['R'])

    def get_lectures_energia(self):
        return self.get_lectures(['A', 'R'])

    def get_lectures_maximetre(self):
        return self.get_lectures(['M'])


class Medida(object):

    def __init__(self, data):
        self.medida = data

    @property
    def cod_pm(self):
        if hasattr(self.medida, 'CodPM'):
            return self.medida.CodPM
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

    @property
    def potencia(self):
        if hasattr(self.factura, 'Potencia'):
            return Potencia(self.factura.Potencia)
        return None

    # TODO: ExcesoPotencia

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
    def medidas(self):
        data = []
        if hasattr(self.factura, 'Medidas'):
            for d in self.factura.Medidas:
                data.append(Medida(d))
        return data

    def get_comptadors(self):
        """Retorna totes les lectures en una llista de comptadors"""
        comptadors = []
        for medida in self.medidas:
            for aparell in medida.modelos_aparatos:
                di, df = aparell.get_dates_inici_i_final()
                comptadors.append((di, df, aparell))
        return [a[2] for a in sorted(comptadors, lambda x,y: cmp(x[0], y[0]))]


class ConceptoRepercutible(object):

    def __init__(self, data):
        self.concepto = data

    @property
    def concepto_repercutible(self):
        if hasattr(self.concepto, 'ConceptoRepercutible'):
            return self.concepto.ConceptoRepercutible.text
        return None

    @property
    def tipo_impositivo(self):
        if hasattr(self.concepto, 'TipoImpositivoConceptoRepercutible'):
            return self.concepto.TipoImpositivoConceptoRepercutible.text
        return None

    @property
    def fecha_operacion(self):
        if hasattr(self.concepto, 'FechaOperacion'):
            return self.concepto.FechaOperacion.text
        return None

    @property
    def fecha_desde(self):
        if hasattr(self.concepto, 'FechaDesde'):
            return self.concepto.FechaDesde.text
        return None

    @property
    def fecha_hasta(self):
        if hasattr(self.concepto, 'FechaHasta'):
            return self.concepto.FechaHasta.text
        return None

    @property
    def unidades(self):
        if hasattr(self.concepto, 'UnidadesConceptoRepercutible'):
            return self.concepto.UnidadesConceptoRepercutible
        return None

    @property
    def precio_unidad(self):
        if hasattr(self.concepto, 'PrecioUnidadConceptoRepercutible'):
            return self.concepto.PrecioUnidadConceptoRepercutible
        return None

    @property
    def importe(self):
        if hasattr(self.concepto, 'ImporteTotalConceptoRepercutible'):
            return self.concepto.ImporteTotalConceptoRepercutible
        return None

    @property
    def comentarios(self):
        if hasattr(self.concepto, 'Comentarios'):
            return self.concepto.Comentarios.text
        return None


class OtraFactura(Factura):
    DATOS_GENERALES_NAME = 'DatosGeneralesOtrasFacturas'
    DATOS_GENERALES_OBJECT = DatosGeneralesOtras


class RegistroFin(object):

    def __init__(self, data):
        self.registro = data

    @property
    def importe_total(self):
        if hasattr(self.registro, 'ImporteTotal'):
            return self.registro.ImporteTotal
        return None

    @property
    def saldo_total(self):
        if hasattr(self.registro, 'SaldoTotalFacturacion'):
            return self.registro.SaldoTotalFacturacion
        return None

    @property
    def total_recibos(self):
        if hasattr(self.registro, 'TotalRecibos'):
            return self.registro.TotalRecibos
        return None

    @property
    def tipo_moneda(self):
        if hasattr(self.registro, 'TipoMoneda'):
            return self.registro.TipoMoneda.text
        return None

    @property
    def fecha_valor(self):
        if hasattr(self.registro, 'FechaValor'):
            return self.registro.FechaValor.text
        return None

    @property
    def fecha_limite_pago(self):
        if hasattr(self.registro, 'FechaLimitePago'):
            return self.registro.FechaLimitePago.text
        return None

    @property
    def iban(self):
        if hasattr(self.registro, 'IBAN'):
            return self.registro.IBAN.text
        return None

    @property
    def id_remesa(self):
        if hasattr(self.registro, 'IdRemesa'):
            return self.registro.IdRemesa.text
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
