# -*- coding: utf-8 -*-

from libcomxml.core import XmlModel, XmlField
from gestionatr.output.messages.base import Cabecera, rep_fecha, \
    rep_fecha_sin_hora, rep_decimal, rep_entera, rep_entera2, rep_ruedas, rep_cut
from gestionatr.output.messages.sw_c1 import IdCliente
from gestionatr.output.messages.sw_c2 import Direccion


class Facturacion(XmlModel):
    _sort_order = ('mensaje', 'cabecera', 'facturas', 'otros_datos_factura')

    def __init__(self):
        self.doc_root = None
        self.mensaje = XmlField(
            'MensajeFacturacion',
            attributes={'xmlns': 'http://localhost/elegibilidad'}
        )
        self.cabecera = Cabecera()
        self.facturas = Facturas()
        self.otros_datos_factura = OtrosDatosFactura()
        self.firmar = XmlField('Firmar')
        super(Facturacion, self).__init__('MensajeFacturacion', 'mensaje')


class Facturas(XmlModel):

    _sort_order = ('facturas', 'factura_atr', 'otras_facturas', 'registro_fin')

    def __init__(self):
        self.facturas = XmlField('Facturas')
        self.factura_atr = FacturaATR()
        self.otras_facturas = OtrasFacturas()
        self.registro_fin = RegistroFin()
        super(Facturas, self).__init__('Facturacion', 'facturas')


class FacturaATR(XmlModel):

    _sort_order = (
        'factura_atr', 'datos_generales_factura_atr', 'potencia',
        'exceso_potencia', 'energia_activa', 'energia_reactiva',
        'energia_capacitiva', 'autoconsumo', 'cargos',
        'impuesto_electrico', 'alquileres', 'importe_intereses',
        'concepto_repercutible', 'iva', 'iva_reducido', 'medidas',
        'informacion_al_consumidor'
    )

    def __init__(self):
        self.factura_atr = XmlField('FacturaATR')
        self.datos_generales_factura_atr = DatosGeneralesFacturaATR()
        self.potencia = Potencia()
        self.exceso_potencia = ExcesoPotencia()
        self.energia_activa = EnergiaActiva()
        self.energia_reactiva = EnergiaReactiva()
        self.energia_capacitiva = EnergiaCapacitiva()
        self.autoconsumo = Autoconsumo()
        self.cargos = Cargos()
        self.impuesto_electrico = ImpuestoElectrico()
        self.alquileres = Alquileres()
        self.importe_intereses = XmlField('ImporteIntereses')
        self.concepto_repercutible = ConceptoRepercutible()
        self.iva = IVA()
        self.iva_reducido = IVAReducido()
        self.medidas = Medidas()
        self.informacion_al_consumidor = InformacionAlConsumidor()
        super(FacturaATR, self).__init__('FacturaATR', 'factura_atr')


class DatosGeneralesFacturaATR(XmlModel):

    _sort_order = (
        'datos_generales_factura_atr', 'direccion_suministro', 'cliente',
        'cod_contrato', 'datos_generales_factura', 'datos_factura_atr'
    )

    def __init__(self):
        self.datos_generales_factura_atr = XmlField('DatosGeneralesFacturaATR')
        self.direccion_suministro = DireccionSuministro()
        self.cliente = Cliente()
        self.cod_contrato = XmlField('CodContrato')
        self.datos_generales_factura = DatosGeneralesFactura()
        self.datos_factura_atr = DatosFacturaATR()
        super(DatosGeneralesFacturaATR, self).__init__(
            'DatosGeneralesFacturaATR', 'datos_generales_factura_atr'
        )


class Cliente(IdCliente):

    def __init__(self):
        super(Cliente, self).__init__(name='Cliente')


class DatosGeneralesFactura(XmlModel):

    _sort_order = (
        'datos_generales_factura', 'codigo_fiscal_factura', 'tipo_factura',
        'motivo_facturacion', 'codigo_factura_rectificada_anulada',
        'expediente', 'fecha_factura', 'identificador_emisora', 'comentarios',
        'importe_total_factura', 'saldo_factura', 'tipo_moneda'
    )

    def __init__(self):
        self.datos_generales_factura = XmlField('DatosGeneralesFactura')
        self.codigo_fiscal_factura = XmlField('CodigoFiscalFactura')
        self.tipo_factura = XmlField('TipoFactura')
        self.motivo_facturacion = XmlField('MotivoFacturacion')
        self.codigo_factura_rectificada_anulada = XmlField(
            'CodigoFacturaRectificadaAnulada'
        )
        self.expediente = Expediente()
        self.fecha_factura = XmlField('FechaFactura')
        self.identificador_emisora = XmlField('IdentificadorEmisora')
        self.comentarios = XmlField('Comentarios')
        self.importe_total_factura = XmlField('ImporteTotalFactura')
        self.saldo_factura = XmlField('SaldoFactura')
        self.tipo_moneda = XmlField('TipoMoneda')
        super(DatosGeneralesFactura, self).__init__(
            'DatosGeneralesFactura', 'datos_generales_factura'
        )


class Expediente(XmlModel):

    _sort_order = ('expediente', 'numero_expediente', 'codigo_solicitud')

    def __init__(self):
        self.expediente = XmlField('Expediente')
        self.numero_expediente = XmlField('NumeroExpediente')
        self.codigo_solicitud = XmlField('CodigoSolicitud')
        super(Expediente, self).__init__('Expediente', 'expediente')


class DatosFacturaATR(XmlModel):

    _sort_order = (
        'datos_factura_atr', 'fecha_boe', 'tipo_autoconsumo', 'cau',
        'duracion_inf_anio', 'tarifa_atr_fact', 'modo_control_potencia',
        'marca_medida_con_perdidas', 'vas_trafo', 'porcentaje_perdidas',
        'indicativo_curva_carga', 'periodo_cch', 'periodo', 'tipo_pm'
    )

    def __init__(self):
        self.datos_factura_atr = XmlField('DatosFacturaATR')
        self.fecha_boe = XmlField('FechaBOE', rep=rep_fecha_sin_hora)
        self.tipo_autoconsumo = XmlField('TipoAutoconsumo')
        self.cau = XmlField('CAU')
        self.duracion_inf_anio = XmlField('DuracionInfAnio')
        self.tarifa_atr_fact = XmlField('TarifaATRFact')
        self.modo_control_potencia = XmlField('ModoControlPotencia')
        self.marca_medida_con_perdidas = XmlField('MarcaMedidaConPerdidas')
        self.vas_trafo = XmlField('VAsTrafo', rep=rep_entera)
        self.porcentaje_perdidas = XmlField(
            'PorcentajePerdidas', rep=rep_decimal(2)
        )
        self.indicativo_curva_carga = XmlField('IndicativoCurvaCarga')
        self.periodo_cch = PeriodoCCH()
        self.periodo = Periodo()
        self.tipo_pm = XmlField('TipoPM')
        super(DatosFacturaATR, self).__init__(
            'DatosFacturaATR', 'datos_factura_atr'
        )


class PeriodoCCH(XmlModel):

    _sort_order = ('periodo_cch', 'fecha_desde_cch', 'fecha_hasta_cch')

    def __init__(self):
        self.periodo_cch = XmlField('PeriodoCCH')
        self.fecha_desde_cch = XmlField('FechaDesdeCCH', rep=rep_fecha_sin_hora)
        self.fecha_hasta_cch = XmlField('FechaHastaCCH', rep=rep_fecha_sin_hora)
        super(PeriodoCCH, self).__init__('PeriodoCCH', 'periodo_cch')


class Periodo(XmlModel):

    _sort_order = (
        'periodo', 'fecha_desde_factura', 'fecha_hasta_factura',
        'numero_dias'
    )

    def __init__(self):
        self.periodo = XmlField('Periodo')
        self.fecha_desde_factura = XmlField(
            'FechaDesdeFactura', rep=rep_fecha_sin_hora
        )
        self.fecha_hasta_factura = XmlField(
            'FechaHastaFactura', rep=rep_fecha_sin_hora
        )
        self.numero_dias = XmlField('NumeroDias')
        super(Periodo, self).__init__('Periodo', 'periodo')


class Potencia(XmlModel):

    _sort_order = (
        'potencia', 'termino_potencia', 'penalizacion_no_icp',
        'importe_total_termino_potencia'
    )

    def __init__(self):
        self.potencia = XmlField('Potencia')
        self.termino_potencia = TerminoPotencia()
        self.penalizacion_no_icp = XmlField('PenalizacionNoICP')
        self.importe_total_termino_potencia = XmlField(
            'ImporteTotalTerminoPotencia', rep=rep_decimal(2)
        )
        super(Potencia, self).__init__('Potencia', 'potencia')


class TerminoPotencia(XmlModel):

    _sort_order = ('termino_potencia', 'fecha_desde', 'fecha_hasta', 'periodos')

    def __init__(self):
        self.termino_potencia = XmlField('TerminoPotencia')
        self.fecha_desde = XmlField('FechaDesde', rep=rep_fecha_sin_hora)
        self.fecha_hasta = XmlField('FechaHasta', rep=rep_fecha_sin_hora)
        self.periodos = PeriodoPotencia()
        super(TerminoPotencia, self).__init__(
            'TerminoPotencia', 'termino_potencia'
        )


class PeriodoPotencia(XmlModel):

    _sort_order = (
        'periodo', 'potencia_contratada', 'potencia_max_demandada',
        'potencia_a_facturar', 'precio_potencia', 'recargo_inf_anio'
    )

    def __init__(self):
        self.periodo = XmlField('Periodo')
        self.potencia_contratada = XmlField(
            'PotenciaContratada', rep=rep_entera2
        )
        self.potencia_max_demandada = XmlField(
            'PotenciaMaxDemandada', rep=rep_entera2
        )
        self.potencia_a_facturar = XmlField(
            'PotenciaAFacturar', rep=rep_entera2
        )
        self.precio_potencia = XmlField('PrecioPotencia', rep=rep_decimal(9))
        self.recargo_inf_anio = XmlField('RecargoInfAnio', rep=rep_decimal(2))
        super(PeriodoPotencia, self).__init__('Periodo', 'periodo')


class ExcesoPotencia(XmlModel):

    _sort_order = ('exceso_potencia', 'periodo', 'importe_total_excesos')

    def __init__(self):
        self.exceso_potencia = XmlField('ExcesoPotencia')
        self.periodo = PeriodoExcesoPotencia()
        self.importe_total_excesos = XmlField(
            'ImporteTotalExcesos', rep=rep_decimal(2)
        )
        super(ExcesoPotencia, self).__init__(
            'ExcesoPotencia', 'exceso_potencia'
        )


class PeriodoExcesoPotencia(XmlModel):

    _sort_order = ('periodo', 'valor_exceso_potencia')

    def __init__(self):
        self.periodo = XmlField('Periodo')
        self.valor_exceso_potencia = XmlField(
            'ValorExcesoPotencia', rep=rep_decimal(2)
        )
        super(PeriodoExcesoPotencia, self).__init__('Periodo', 'periodo')


class EnergiaActiva(XmlModel):

    _sort_order = (
        'energia_activa', 'termino_energia_activa',
        'importe_total_energia_activa'
    )

    def __init__(self):
        self.energia_activa = XmlField('EnergiaActiva')
        self.termino_energia_activa = TerminoEnergiaActiva()
        self.importe_total_energia_activa = XmlField(
            'ImporteTotalEnergiaActiva', rep=rep_decimal(2)
        )
        super(EnergiaActiva, self).__init__('EnergiaActiva', 'energia_activa')


class TerminoEnergiaActiva(XmlModel):

    _sort_order = (
        'termino_energia_activa', 'fecha_desde', 'fecha_hasta', 'periodos'
    )

    def __init__(self):
        self.termino_energia_activa = XmlField('TerminoEnergiaActiva')
        self.fecha_desde = XmlField('FechaDesde', rep=rep_fecha_sin_hora)
        self.fecha_hasta = XmlField('FechaHasta', rep=rep_fecha_sin_hora)
        self.periodos = PeriodoEnergiaActiva()
        super(TerminoEnergiaActiva, self).__init__(
            'TerminoEnergiaActiva', 'termino_energia_activa'
        )


class PeriodoEnergiaActiva(XmlModel):

    _sort_order = ('periodo', 'valor_energia_activa', 'precio_energia')

    def __init__(self):
        self.periodo = XmlField('Periodo')
        self.valor_energia_activa = XmlField(
            'ValorEnergiaActiva', rep=rep_decimal(2)
        )
        self.precio_energia = XmlField('PrecioEnergia', rep=rep_decimal(9))
        super(PeriodoEnergiaActiva, self).__init__('Periodo', 'periodo')


class EnergiaReactiva(XmlModel):

    _sort_order = (
        'energia_reactiva', 'termino_energia_reactiva',
        'importe_total_energia_reactiva'
    )

    def __init__(self):
        self.energia_reactiva = XmlField('EnergiaReactiva')
        self.termino_energia_reactiva = TerminoEnergiaReactiva()
        self.importe_total_energia_reactiva = XmlField(
            'ImporteTotalEnergiaReactiva', rep=rep_decimal(2)
        )
        super(EnergiaReactiva, self).__init__(
            'EnergiaReactiva', 'energia_reactiva'
        )


class EnergiaCapacitiva(XmlModel):

    _sort_order = (
        'energia_capacitiva', 'termino_energia_capacitiva',
        'importe_total_energia_capacitiva'
    )

    def __init__(self):
        self.energia_capacitiva = XmlField('EnergiaCapacitiva')
        self.termino_energia_capacitiva = TerminoEnergiaCapacitiva()
        self.importe_total_energia_capacitiva = XmlField(
            'ImporteTotalEnergiaCapacitiva', rep=rep_decimal(2)
        )
        super(EnergiaCapacitiva, self).__init__(
            'EnergiaCapacitiva', 'energia_capacitiva'
        )


class EnergiaNetaGen(XmlModel):

    _sort_order = (
        'energia_neta_gen', 'termino_energia_neta_gen',
        'total_energia_neta_gen'
    )

    def __init__(self):
        self.energia_neta_gen = XmlField('EnergiaNetaGen')
        self.termino_energia_neta_gen = TerminoEnergiaNetaGen()
        self.total_energia_neta_gen = XmlField(
            'TotalEnergiaNetaGenBeta', rep=rep_decimal(2)
        )
        super(EnergiaNetaGen, self).__init__(
            'EnergiaNetaGen', 'energia_neta_gen'
        )


class EnergiaAutoconsumida(XmlModel):
    _sort_order = (
        'energia_autoconsumida', 'termino_energia_autoconsumida',
        'importe_total_energia_activa_autoconsumida'
    )

    def __init__(self):
        self.energia_autoconsumida = XmlField('EnergiaAutoconsumida')
        self.termino_energia_autoconsumida = TerminoEnergiaAutoconsumida()
        self.importe_total_energia_activa_autoconsumida = XmlField(
            'ImporteTotalEnergiaActivaAutoconsumida', rep=rep_decimal(2)
        )
        super(EnergiaAutoconsumida, self).__init__(
            'EnergiaAutoconsumida', 'energia_autoconsumida'
        )


class EnergiaExcedentaria(XmlModel):

    _sort_order = (
        'energia_excedentaria', 'termino_energia_excedentaria',
        'valor_total_energia_excedentaria'
    )

    def __init__(self):
        self.energia_excedentaria = XmlField('EnergiaExcedentaria')
        self.termino_energia_excedentaria = TerminoEnergiaExcedentaria()
        self.valor_total_energia_excedentaria = XmlField(
            'ValorTotalEnergiaExcedentaria', rep=rep_decimal(2)
        )
        super(EnergiaExcedentaria, self).__init__(
            'EnergiaExcedentaria', 'energia_excedentaria'
        )


class Cargo(XmlModel):

    _sort_order = (
        'cargo', 'tipo_cargo', 'termino_cargo',
        'total_importe_tipo_cargo'
    )

    def __init__(self):
        self.cargo = XmlField('Cargo')
        self.tipo_cargo = XmlField('TipoCargo')
        self.termino_cargo = TerminoCargo()
        self.total_importe_tipo_cargo = XmlField(
            'TotalImporteTipoCargo', rep=rep_decimal(2)
        )
        super(Cargo, self).__init__(
            'Cargo', 'cargo'
        )


class TerminoEnergiaReactiva(XmlModel):

    _sort_order = (
        'termino_energia_reactiva', 'fecha_desde', 'fecha_hasta', 'periodos'
    )

    def __init__(self):
        self.termino_energia_reactiva = XmlField('TerminoEnergiaReactiva')
        self.fecha_desde = XmlField('FechaDesde', rep=rep_fecha_sin_hora)
        self.fecha_hasta = XmlField('FechaHasta', rep=rep_fecha_sin_hora)
        self.periodos = PeriodoEnergiaReactiva()
        super(TerminoEnergiaReactiva, self).__init__(
            'TerminoEnergiaReactiva', 'termino_energia_reactiva'
        )


class TerminoEnergiaCapacitiva(XmlModel):

    _sort_order = (
        'termino_energia_capacitiva', 'fecha_desde', 'fecha_hasta', 'periodos'
    )

    def __init__(self):
        self.termino_energia_capacitiva = XmlField('TerminoEnergiaCapacitiva')
        self.fecha_desde = XmlField('FechaDesde', rep=rep_fecha_sin_hora)
        self.fecha_hasta = XmlField('FechaHasta', rep=rep_fecha_sin_hora)
        self.periodos = PeriodoEnergiaCapacitiva()
        super(TerminoEnergiaCapacitiva, self).__init__(
            'TerminoEnergiaCapacitiva', 'termino_energia_capacitiva'
        )


class TerminoEnergiaNetaGen(XmlModel):

    _sort_order = (
        'termino_energia_neta_gen', 'fecha_desde', 'fecha_hasta', 'periodos'
    )

    def __init__(self):
        self.termino_energia_neta_gen = XmlField('TerminoEnergiaNetaGen')
        self.fecha_desde = XmlField('FechaDesde', rep=rep_fecha_sin_hora)
        self.fecha_hasta = XmlField('FechaHasta', rep=rep_fecha_sin_hora)
        self.periodos = PeriodoEnergiaNetaGen()
        super(TerminoEnergiaNetaGen, self).__init__(
            'TerminoEnergiaNetaGen', 'termino_energia_neta_gen'
        )


class TerminoEnergiaAutoconsumida(XmlModel):

    _sort_order = (
        'termino_energia_autoconsumida', 'fecha_desde', 'fecha_hasta', 'periodos'
    )

    def __init__(self):
        self.termino_energia_autoconsumida = XmlField('TerminoEnergiaAutoconsumida')
        self.fecha_desde = XmlField('FechaDesde', rep=rep_fecha_sin_hora)
        self.fecha_hasta = XmlField('FechaHasta', rep=rep_fecha_sin_hora)
        self.periodos = PeriodoEnergiaAutoconsumida()
        super(TerminoEnergiaAutoconsumida, self).__init__(
            'TerminoEnergiaAutoconsumida', 'termino_energia_autoconsumida'
        )


class TerminoEnergiaExcedentaria(XmlModel):

    _sort_order = (
        'termino_energia_excedentaria', 'fecha_desde', 'fecha_hasta', 'periodos'
    )

    def __init__(self):
        self.termino_energia_excedentaria = XmlField('TerminoEnergiaExcedentaria')
        self.fecha_desde = XmlField('FechaDesde', rep=rep_fecha_sin_hora)
        self.fecha_hasta = XmlField('FechaHasta', rep=rep_fecha_sin_hora)
        self.periodos = PeriodoEnergiaExcedentaria()
        super(TerminoEnergiaExcedentaria, self).__init__(
            'TerminoEnergiaExcedentaria', 'termino_energia_excedentaria'
        )


class TerminoCargo(XmlModel):

    _sort_order = (
        'termino_cargo', 'fecha_desde', 'fecha_hasta', 'periodos'
    )

    def __init__(self):
        self.termino_cargo = XmlField('TerminoCargo')
        self.fecha_desde = XmlField('FechaDesde', rep=rep_fecha_sin_hora)
        self.fecha_hasta = XmlField('FechaHasta', rep=rep_fecha_sin_hora)
        self.periodos = PeriodoCargo()
        super(TerminoCargo, self).__init__(
            'TerminoCargo', 'termino_cargo'
        )


class PeriodoEnergiaReactiva(XmlModel):

    _sort_order = ('periodo', 'valor_energia_reactiva', 'precio_energia')

    def __init__(self):
        self.periodo = XmlField('Periodo')
        self.valor_energia_reactiva = XmlField(
            'ValorEnergiaReactiva', rep=rep_decimal(2)
        )
        self.precio_energia = XmlField(
            'PrecioEnergiaReactiva', rep=rep_decimal(9)
        )
        super(PeriodoEnergiaReactiva, self).__init__('Periodo', 'periodo')


class PeriodoEnergiaCapacitiva(XmlModel):

    _sort_order = ('periodo', 'valor_energia_capacitiva', 'precio_energia')

    def __init__(self):
        self.periodo = XmlField('Periodo')
        self.valor_energia_capacitiva = XmlField(
            'ValorEnergiaCapacitiva', rep=rep_decimal(2)
        )
        self.precio_energia = XmlField(
            'PrecioEnergiaCapacitiva', rep=rep_decimal(9)
        )
        super(PeriodoEnergiaCapacitiva, self).__init__('Periodo', 'periodo')


class PeriodoEnergiaNetaGen(XmlModel):

    _sort_order = ('periodo', 'valor_energia_neta_gen', 'beta', 'relacion_generacion')

    def __init__(self):
        self.periodo = XmlField('Periodo')
        self.valor_energia_neta_gen = XmlField(
            'ValorEnergiaNetaGen', rep=rep_decimal(2)
        )
        self.beta = XmlField('Beta')
        self.relacion_generacion = XmlField('RelacionGeneracion')
        super(PeriodoEnergiaNetaGen, self).__init__('Periodo', 'periodo')


class PeriodoEnergiaAutoconsumida(XmlModel):

    _sort_order = ('periodo', 'valor_energia_autoconsumida', 'pago_tda')

    def __init__(self):
        self.periodo = XmlField('Periodo')
        self.valor_energia_autoconsumida = XmlField(
            'ValorEnergiaAutoconsumida', rep=rep_decimal(2)
        )
        self.pago_tda = XmlField('PagoTDA')
        super(PeriodoEnergiaAutoconsumida, self).__init__('Periodo', 'periodo')


class PeriodoEnergiaExcedentaria(XmlModel):

    _sort_order = ('periodo', 'valor_energia_excedentaria')

    def __init__(self):
        self.periodo = XmlField('Periodo')
        self.valor_energia_excedentaria = XmlField(
            'ValorEnergiaExcedentaria', rep=rep_decimal(2)
        )
        super(PeriodoEnergiaExcedentaria, self).__init__('Periodo', 'periodo')


class PeriodoCargo(XmlModel):

    _sort_order = ('periodo', 'energia', 'potencia', 'precio_cargo')

    def __init__(self):
        self.periodo = XmlField('Periodo')
        self.energia = XmlField('Energia', rep=rep_decimal(2))
        self.potencia = XmlField('Potencia', rep=rep_entera2)
        self.precio_cargo = XmlField('PrecioCargo', rep=rep_decimal(9))
        super(PeriodoCargo, self).__init__('Periodo', 'periodo')


class InstalacionGenAutoconsumo(XmlModel):
    _sort_order = (
        'instalacion_gen_autoconsumo', 'tipo_instalacion', 'exento_cargos',
        'energia_neta_gen', 'energia_autoconsumida'
    )

    def __init__(self):
        self.instalacion_gen_autoconsumo = XmlField('InstalacionGenAutoconsumo')
        self.tipo_instalacion = XmlField('TipoInstalacion')
        self.exento_cargos = XmlField('ExentoCargos')
        self.energia_neta_gen = EnergiaNetaGen()
        self.energia_autoconsumida = EnergiaAutoconsumida()
        super(InstalacionGenAutoconsumo, self).__init__(
            'InstalacionGenAutoconsumo', 'instalacion_gen_autoconsumo'
        )


class Autoconsumo(XmlModel):

    _sort_order = (
        'autoconsumo', 'instalacion_gen_autoconsumo', 'energia_excedentaria'
    )

    def __init__(self):
        self.autoconsumo = XmlField('Autoconsumo')
        self.instalacion_gen_autoconsumo = InstalacionGenAutoconsumo()
        self.energia_excedentaria = EnergiaExcedentaria()
        super(Autoconsumo, self).__init__(
            'Autoconsumo', 'autoconsumo'
        )


class Cargos(XmlModel):

    _sort_order = (
        'cargos', 'cargo_list', 'total_importe_cargos'
    )

    def __init__(self):
        self.cargos = XmlField('Cargos')
        self.cargo_list = Cargo()
        self.total_importe_cargos = XmlField('TotalImporteCargos', rep=rep_decimal(2))
        super(Cargos, self).__init__(
            'Cargos', 'cargos'
        )


class ImpuestoElectrico(XmlModel):

    _sort_order = (
        'impuesto_electrico', 'base_imponible', 'porcentaje', 'importe'
    )

    def __init__(self):
        self.impuesto_electrico = XmlField('ImpuestoElectrico')
        self.base_imponible = XmlField('BaseImponible', rep=rep_decimal(2))
        self.porcentaje = XmlField('Porcentaje', rep=rep_decimal(8))
        self.importe = XmlField('Importe', rep=rep_decimal(2))
        super(ImpuestoElectrico, self).__init__(
            'ImpuestoElectrico', 'impuesto_electrico'
        )


class Alquileres(XmlModel):

    _sort_order = (
        'alquileres', 'precio_diario_alquiler', 'importe_facturacion_alquileres'
    )

    def __init__(self):
        self.alquileres = XmlField('Alquileres')
        self.precio_diario_alquiler = PrecioDiarioAlquiler()
        self.importe_facturacion_alquileres = XmlField(
            'ImporteFacturacionAlquileres'
        )
        super(Alquileres, self).__init__('Alquileres', 'alquileres')


class PrecioDiarioAlquiler(XmlModel):

    _sort_order = ('precio_diario_alquiler', 'precio_dia', 'numero_dias')

    def __init__(self):
        self.precio_diario_alquiler = XmlField('PrecioDiarioAlquiler')
        self.precio_dia = XmlField('PrecioDia')
        self.numero_dias = XmlField('NumeroDias', rep=rep_entera)
        super(PrecioDiarioAlquiler, self).__init__(
            'PrecioDiarioAlquiler', 'precio_diario_alquiler'
        )


class IVA(XmlModel):

    _sort_order = ('iva', 'base_imponible', 'porcentaje', 'importe')

    def __init__(self):
        self.iva = XmlField('IVA')
        self.base_imponible = XmlField('BaseImponible', rep=rep_decimal(2))
        self.porcentaje = XmlField('Porcentaje', rep=rep_decimal(2))
        self.importe = XmlField('Importe', rep=rep_decimal(2))
        super(IVA, self).__init__('IVA', 'iva')


class IVAReducido(XmlModel):

    _sort_order = ('iva_reducido', 'base_imponible', 'porcentaje', 'importe')

    def __init__(self):
        self.iva_reducido = XmlField('IVAReducido')
        self.base_imponible = XmlField('BaseImponible', rep=rep_decimal(2))
        self.porcentaje = XmlField('Porcentaje', rep=rep_decimal(2))
        self.importe = XmlField('Importe', rep=rep_decimal(2))
        super(IVAReducido, self).__init__('IVAReducido', 'iva_reducido')


class Medidas(XmlModel):

    _sort_order = ('medidas', 'cod_pm', 'modelo_aparato')

    def __init__(self):
        self.medidas = XmlField('Medidas')
        self.cod_pm = XmlField('CodPM')
        self.modelo_aparato = ModeloAparato()
        super(Medidas, self).__init__('Medidas', 'medidas')


class ModeloAparato(XmlModel):

    _sort_order = (
        'modelo_aparato', 'tipo_aparato', 'marca_aparato', 'numero_serie',
        'tipo_dhedm', 'integrador'
    )

    def __init__(self):
        self.modelo_aparato = XmlField('ModeloAparato')
        self.tipo_aparato = XmlField('TipoAparato')
        self.marca_aparato = XmlField('MarcaAparato')
        self.numero_serie = XmlField('NumeroSerie')
        self.tipo_dhedm = XmlField('TipoDHEdM')
        self.integrador = Integrador()
        super(ModeloAparato, self).__init__('ModeloAparato', 'modelo_aparato')


class Integrador(XmlModel):

    _sort_order = (
        'integrador', 'magnitud', 'codigo_periodo', 'constante_multiplicadora',
        'numero_ruedas_enteras', 'numero_ruedas_decimales', 'consumo_calculado',
        'lectura_desde', 'lectura_hasta', 'ajuste', 'anomalia',
        'fecha_hora_maximetro'
    )

    def __init__(self):
        self.integrador = XmlField('Integrador')
        self.magnitud = XmlField('Magnitud')
        self.codigo_periodo = XmlField('CodigoPeriodo')
        self.constante_multiplicadora = XmlField('ConstanteMultiplicadora')
        self.numero_ruedas_enteras = XmlField(
            'NumeroRuedasEnteras', rep=rep_ruedas
        )
        self.numero_ruedas_decimales = XmlField(
            'NumeroRuedasDecimales', rep=rep_ruedas
        )
        self.consumo_calculado = XmlField(
            'ConsumoCalculado', rep=rep_decimal(2)
        )
        self.lectura_desde = LecturaDesde()
        self.lectura_hasta = LecturaHasta()
        self.ajuste = Ajuste()
        self.anomalia = Anomalia()
        self.fecha_hora_maximetro = XmlField(
            'FechaHoraMaximetro', rep=rep_fecha
        )
        super(Integrador, self).__init__('Integrador', 'integrador')


class LecturaDesde(XmlModel):

    _sort_order = ('lectura_desde', 'fecha', 'procedencia', 'lectura')

    def __init__(self):
        self.lectura_desde = XmlField('LecturaDesde')
        self.fecha = XmlField('Fecha', rep=rep_fecha_sin_hora)
        self.procedencia = XmlField('Procedencia')
        self.lectura = XmlField('Lectura', rep=rep_decimal(2))
        super(LecturaDesde, self).__init__('LecturaDesde', 'lectura_desde')


class LecturaHasta(XmlModel):

    _sort_order = ('lectura_hasta', 'fecha', 'procedencia', 'lectura')

    def __init__(self):
        self.lectura_hasta = XmlField('LecturaHasta')
        self.fecha = XmlField('Fecha', rep=rep_fecha_sin_hora)
        self.procedencia = XmlField('Procedencia')
        self.lectura = XmlField('Lectura', rep=rep_decimal(2))
        super(LecturaHasta, self).__init__('LecturaHasta', 'lectura_hasta')


class Ajuste(XmlModel):

    _sort_order = (
        'ajuste', 'codigo_motivo_ajuste', 'ajuste_por_integrador', 'comentarios'
    )

    def __init__(self):
        self.ajuste = XmlField('Ajuste')
        self.codigo_motivo_ajuste = XmlField('CodigoMotivoAjuste')
        self.ajuste_por_integrador = XmlField('AjustePorIntegrador')
        self.comentarios = XmlField('Comentarios')
        super(Ajuste, self).__init__('Ajuste', 'ajuste')


class InformacionAlConsumidor(XmlModel):

    _sort_order = (
        'informacion_al_consumidor', 'fecha_inicio_anio_movil', 'periodos', 'valor_energia_media_cp'
    )

    def __init__(self):
        self.informacion_al_consumidor = XmlField('InformacionAlConsumidor')
        self.fecha_inicio_anio_movil = XmlField('FechaInicioAnioMovil', rep=rep_fecha_sin_hora)
        self.periodos = PeriodoInfoAlConsumidor()
        self.valor_energia_media_cp = XmlField('ValorEnergiaMediaCP')
        super(InformacionAlConsumidor, self).__init__('InformacionAlConsumidor', 'informacion_al_consumidor')


class PeriodoInfoAlConsumidor(XmlModel):

    _sort_order = (
        'periodo', 'potencia_max_demandada_anio_movil'
    )

    def __init__(self):
        self.periodo = XmlField('Periodo')
        self.potencia_max_demandada_anio_movil = XmlField('PotenciaMaxDemandadaAnioMovil', rep=rep_entera2)
        super(PeriodoInfoAlConsumidor, self).__init__('Periodo', 'periodo')


class Anomalia(XmlModel):

    _sort_order = ('anomalia', 'tipo_anomalia', 'comentarios')

    def __init__(self):
        self.anomalia = XmlField('Anomalia')
        self.tipo_anomalia = XmlField('TipoAnomalia')
        self.comentarios = XmlField('Comentarios')
        super(Anomalia, self).__init__('Anomalia', 'anomalia')


class OtrasFacturas(XmlModel):

    _sort_order = (
        'otras_facturas', 'datos_generales_otras_facturas',
        'concepto_repercutible', 'iva', 'iva_reducido'
    )

    def __init__(self):
        self.otras_facturas = XmlField('OtrasFacturas')
        self.datos_generales_otras_facturas = DatosGeneralesOtrasFacturas()
        self.concepto_repercutible = ConceptoRepercutible()
        self.iva = IVA()
        self.iva_reducido = IVAReducido()
        super(OtrasFacturas, self).__init__('OtrasFacturas', 'otras_facturas')


class DatosGeneralesOtrasFacturas(XmlModel):

    _sort_order = (
        'datos_generales_otras_facturas', 'direccion_suministro', 'cliente',
        'cod_contrato', 'datos_generales_factura', 'fecha_boe'
    )

    def __init__(self):
        self.datos_generales_otras_facturas = XmlField(
            'DatosGeneralesOtrasFacturas'
        )
        self.direccion_suministro = DireccionSuministro()
        self.cliente = Cliente()
        self.cod_contrato = XmlField('CodContrato')
        self.datos_generales_factura = DatosGeneralesFactura()
        self.fecha_boe = XmlField('FechaBOE', rep=rep_fecha_sin_hora)
        super(DatosGeneralesOtrasFacturas, self).__init__(
            'DatosGeneralesOtrasFacturas', 'datos_generales_otras_facturas'
        )


class DireccionSuministro(XmlModel):

    _sort_order = ('direccion', 'pais', 'provincia', 'municipio', 'poblacion', 'tipo_via', 'cod_postal', 'calle', 'numero_finca', 'duplicador_finca', 'escalera', 'piso', 'puerta', 'tipo_aclarador_finca', 'aclarador_finca')

    def __init__(self, name='DireccionSuministro'):
        self.direccion = XmlField(name)
        self.pais = XmlField('Pais')
        self.provincia = XmlField('Provincia')
        self.municipio = XmlField('Municipio')
        self.poblacion = XmlField('Poblacion')
        self.tipo_via = XmlField('TipoVia')
        self.cod_postal = XmlField('CodPostal')
        self.calle = XmlField('Calle', rep=rep_cut(30))
        self.numero_finca = XmlField('NumeroFinca', rep=rep_cut(5))
        self.duplicador_finca = XmlField('DuplicadorFinca', rep=rep_cut(3))
        self.escalera = XmlField('Escalera', rep=rep_cut(3))
        self.piso = XmlField('Piso', rep=rep_cut(3))
        self.puerta = XmlField('Puerta', rep=rep_cut(3))
        self.tipo_aclarador_finca = XmlField(
            'TipoAclaradorFinca', rep=rep_cut(2)
        )
        self.aclarador_finca = XmlField('AclaradorFinca', rep=rep_cut(40))
        super(DireccionSuministro, self).__init__(name, 'direccion')


class ConceptoRepercutible(XmlModel):

    _sort_order = (
        'concepto_repercutible_fact', 'concepto_repercutible',
        'tipo_impositivo_concepto_repercutible', 'fecha_desde', 'fecha_hasta',
        'fecha_operacion', 'unidades_concepto_repercutible',
        'precio_unidad_concepto_repercutible',
        'importe_total_concepto_repercutible', 'comentarios'
    )

    def __init__(self, drop_empty=False):
        self.concepto_repercutible_fact = XmlField('ConceptoRepercutible')
        self.concepto_repercutible = XmlField('ConceptoRepercutible')
        self.tipo_impositivo_concepto_repercutible = XmlField(
            'TipoImpositivoConceptoRepercutible'
        )
        self.fecha_desde = XmlField('FechaDesde')
        self.fecha_hasta = XmlField('FechaHasta')
        self.fecha_operacion = XmlField('FechaOperacion')
        self.unidades_concepto_repercutible = XmlField(
            'UnidadesConceptoRepercutible'
        )
        self.precio_unidad_concepto_repercutible = XmlField(
            'PrecioUnidadConceptoRepercutible', rep=rep_decimal(2)
        )
        self.importe_total_concepto_repercutible = XmlField(
            'ImporteTotalConceptoRepercutible', rep=rep_decimal(2)
        )
        self.comentarios = XmlField('Comentarios')
        super(ConceptoRepercutible, self).__init__(
            'ConceptoRepercutible', 'concepto_repercutible_fact'
        )


class RegistroFin(XmlModel):

    _sort_order = (
        'registro_fin', 'importe_total', 'saldo_total_facturacion',
        'total_recibos', 'tipo_moneda', 'fecha_valor', 'fecha_limite_pago',
        'iban', 'id_remesa'
    )

    def __init__(self):
        self.registro_fin = XmlField('RegistroFin')
        self.importe_total = XmlField('ImporteTotal')
        self.saldo_total_facturacion = XmlField('SaldoTotalFacturacion')
        self.total_recibos = XmlField('TotalRecibos')
        self.tipo_moneda = XmlField('TipoMoneda')
        self.fecha_valor = XmlField('FechaValor', rep=rep_fecha_sin_hora)
        self.fecha_limite_pago = XmlField(
            'FechaLimitePago', rep=rep_fecha_sin_hora
        )
        self.iban = XmlField('IBAN')
        self.id_remesa = XmlField('IdRemesa')
        super(RegistroFin, self).__init__('RegistroFin', 'registro_fin')


class OtrosDatosFactura(XmlModel):

    _sort_order = (
        'otros_datos_factura', 'sociedad_mercantil_emisora',
        'socideda_mercantil_destino', 'direccion_emisora', 'direccion_destino'
    )

    def __init__(self):
        self.otros_datos_factura = XmlField('OtrosDatosFactura')
        self.sociedad_mercantil_emisora = XmlField('SociedadMercantilEmisora')
        self.sociedad_mercantil_destino = XmlField('SociedadMercantilDestino')
        self.direccion_emisora = XmlField('DireccionEmisora')
        self.direccion_destino = XmlField('DireccionDestino')
        super(OtrosDatosFactura, self).__init__(
            'OtrosDatosFactura', 'otros_datos_factura'
        )
