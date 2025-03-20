# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from libcomxml.core import XmlModel, XmlField
from gestionatr.output.messages.base import Cabecera
from gestionatr.output.messages.sw_f1 import PeriodoCCH, Periodo, EnergiaActiva, Expediente, InformacionAlConsumidor, Autoconsumo


class MensajeSaldoLecturasFacturacion(XmlModel):

    _sort_order = ('mensaje', 'cabecera', 'datos', 'energia_activa', 'autoconsumo', 'medidas', 'informacion_consumidor')

    def __init__(self):
        self.mensaje = XmlField('MensajeSaldoLecturasFacturacion',
                                attributes={'xmlns': 'http://localhost/elegibilidad'})
        self.cabecera = Cabecera()
        self.datos = Datos()
        self.energia_activa = EnergiaActiva()
        self.autoconsumo = Autoconsumo()
        self.medidas = Medidas()
        self.informacion_consumidor = InformacionAlConsumidor()
        super(MensajeSaldoLecturasFacturacion, self).__init__('MensajeSaldoLecturasFacturacion', 'mensaje')


class Cabecera(Cabecera):

    _sort_order = ('cabecera', 'codigo_ree_empresa_emisora', 'codigo_ree_empresa_destino', 'codigo_del_proceso',
                   'codigo_del_paso', 'codigo_de_solicitud', 'secuencial_de_solicitud', 'fecha', 'cups',
                   'codigo_fiscal_factura', 'tipo_factura', 'motivo_facturacion', 'codigo_factura_rectificada_anulada',
                   'expediente')

    def __init__(self):
        super(Cabecera, self).__init__()
        self.codigo_fiscal_factura = XmlField('CodigoFiscalFactura')
        self.tipo_factura = XmlField('TipoFactura')
        self.motivo_facturacion = XmlField('MotivoFacturacion')
        self.codigo_factura_rectificada_anulada = XmlField('CodigoFacturaRectificadaAnulada')
        self.expediente = Expediente()


class Datos(XmlModel):

    _sort_order = ('datos', 'tipo_autoconsumo', 'tipo_subseccion', 'datos_cau', 'tipo_cups',
                   'marca_medida_con_perdidas', 'vas_trafo', 'porcentaje_perdidas', 'indicativo_curva_carga',
                   'periodo_cch', 'periodo', 'tipo_pm')

    def __init__(self):
        self.datos = XmlField('Datos')
        self.tipo_autoconsumo = XmlField('TipoAutoconsumo')
        self.tipo_subseccion = XmlField('TipoSubseccion')
        self.tipo_cups = XmlField('TipoCUPS')
        self.marca_medida_con_perdidas = XmlField('MarcaMedidaConPerdidas')
        self.vas_trafo = XmlField('VAsTrafo')
        self.porcentaje_perdidas = XmlField('PorcentajePerdidas')
        self.indicativo_curva_carga = XmlField('IndicativoCurvaCarga')
        self.periodo_cch = PeriodoCCH()
        self.periodo = Periodo()
        self.tipo_pm = XmlField('TipoPM')
        super(Datos, self).__init__('Datos', 'datos')


class Medidas(XmlModel):

    _sort_order = ('medidas', 'cod_pm', 'modelo_aparato_list')

    def __init__(self):
        self.medidas = XmlField('Medidas')
        self.cod_pm = XmlField('CodPM')
        self.modelo_aparato_list = []
        super(Medidas, self).__init__('Medidas', 'medidas')


class ModeloAparato(XmlModel):

    _sort_order = ('modelo_aparato', 'tipo_aparato', 'marca_aparato', 'numero_serie', 'tipo_dhedm', 'integrador_list')

    def __init__(self):
        self.modelo_aparato = XmlField('ModeloAparato')
        self.tipo_aparato = XmlField('TipoAparato')
        self.marca_aparato = XmlField('MarcaAparato')
        self.numero_serie = XmlField('NumeroSerie')
        self.tipo_dhedm = XmlField('TipoDHEdM')
        self.integrador_list = []
        super(ModeloAparato, self).__init__('ModeloAparato', 'modelo_aparato')


class Integrador(XmlModel):

    _sort_order = ('integrador', 'magnitud', 'codigo_periodo', 'constante_multiplicadora', 'numero_ruedas_enteras', 'numero_ruedas_decimales', 'consumo_calculado', 'lectura_desde', 'lectura_hasta', 'ajuste', 'anomalia', 'fecha_hora_maximetro')

    def __init__(self):
        self.integrador = XmlField('Integrador')
        self.magnitud = XmlField('Magnitud')
        self.codigo_periodo = XmlField('CodigoPeriodo')
        self.constante_multiplicadora = XmlField('ConstanteMultiplicadora')
        self.numero_ruedas_enteras = XmlField('NumeroRuedasEnteras')
        self.numero_ruedas_decimales = XmlField('NumeroRuedasDecimales')
        self.consumo_calculado = XmlField('ConsumoCalculado')
        self.lectura_desde = LecturaDesde()
        self.lectura_hasta = LecturaHasta()
        self.ajuste = Ajuste()
        self.anomalia = Anomalia()
        self.fecha_hora_maximetro = XmlField('FechaHoraMaximetro')
        super(Integrador, self).__init__('Integrador', 'integrador')


class LecturaDesde(XmlModel):

    _sort_order = ('lectura_desde', 'fecha', 'procedencia', 'lectura')

    def __init__(self):
        self.lectura_desde = XmlField('LecturaDesde')
        self.fecha = XmlField('Fecha')
        self.procedencia = XmlField('Procedencia')
        self.lectura = XmlField('Lectura')
        super(LecturaDesde, self).__init__('LecturaDesde', 'lectura_desde')


class LecturaHasta(XmlModel):

    _sort_order = ('lectura_hasta', 'fecha', 'procedencia', 'lectura')

    def __init__(self):
        self.lectura_hasta = XmlField('LecturaHasta')
        self.fecha = XmlField('Fecha')
        self.procedencia = XmlField('Procedencia')
        self.lectura = XmlField('Lectura')
        super(LecturaHasta, self).__init__('LecturaHasta', 'lectura_hasta')


class Ajuste(XmlModel):

    _sort_order = ('ajuste', 'codigo_motivo_ajuste', 'ajuste_por_integrador', 'comentarios')

    def __init__(self):
        self.ajuste = XmlField('Ajuste')
        self.codigo_motivo_ajuste = XmlField('CodigoMotivoAjuste')
        self.ajuste_por_integrador = XmlField('AjustePorIntegrador')
        self.comentarios = XmlField('Comentarios')
        super(Ajuste, self).__init__('Ajuste', 'ajuste')


class Anomalia(XmlModel):

    _sort_order = ('anomalia', 'tipo_anomalia', 'comentarios')

    def __init__(self):
        self.anomalia = XmlField('Anomalia')
        self.tipo_anomalia = XmlField('TipoAnomalia')
        self.comentarios = XmlField('Comentarios')
        super(Anomalia, self).__init__('Anomalia', 'anomalia')
