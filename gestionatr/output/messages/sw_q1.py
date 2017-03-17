# -*- coding: utf-8 -*-

from libcomxml.core import XmlModel, XmlField
from gestionatr.output.messages.base import Cabecera


class MensajeSaldoLecturasFacturacion(XmlModel):

    _sort_order = ('mensaje', 'cabecera', 'medidas')

    def __init__(self):
        self.mensaje = XmlField('MensajeSaldoLecturasFacturacion',
                                attributes={'xmlns': 'http://localhost/elegibilidad'})
        self.cabecera = Cabecera()
        self.medidas = Medidas()
        super(MensajeSaldoLecturasFacturacion, self).__init__('MensajeSaldoLecturasFacturacion', 'mensaje')


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
