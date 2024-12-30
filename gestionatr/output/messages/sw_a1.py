# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from libcomxml.core import XmlModel, XmlField

from gestionatr.output.messages.base import CabeceraAutoconsumo, CabeceraAutoconsumoRechazo


# Paso 01
class A101(XmlModel):

    _sort_order = ('mensaje', 'cabecera', 'info_registro_autocons')

    def __init__(self):
        self.mensaje = XmlField('A101',
                                attributes={'xmlns': 'http://localhost/elegibilidad'})
        self.cabecera = CabeceraAutoconsumo()
        self.info_registro_autocons = InfoRegistroAutoconsA1()
        super(A101, self).__init__('A101', 'mensaje')


class InfoRegistroAutoconsA1(XmlModel):

    _sort_order = ('info_registro_autocons', 'movimiento', 'autoconsumo', 'datos_suministro', 'datos_inst_gen',
                   'comentarios')

    def __init__(self):
        self.info_registro_autocons = XmlField('A101')
        self.movimiento = XmlField('Movimiento')
        self.autoconsumo = Autoconsumo()
        self.datos_suministro = DatosSuministro()
        self.datos_inst_gen = DatosInstGen()
        self.comentarios = XmlField('Comentarios')
        super(InfoRegistroAutoconsA1, self).__init__('InfoRegistoAutoconsA1', 'info_registro_autocons')


# Paso 02
class MensajeA102(XmlModel):

    _sort_order = ('mensaje', 'cabecera', 'a102')

    def __init__(self):
        self.mensaje = XmlField('A102',
                                attributes={'xmlns': 'http://localhost/elegibilidad'})
        self.cabecera = CabeceraAutoconsumoRechazo()
        self.a102 = A102()
        super(MensajeA102, self).__init__('A102', 'mensaje')


class A102(XmlModel):

    _sort_order = ('a102', 'cau', 'rechazos', 'comentarios')

    def __init__(self):
        self.a102 = XmlField('A102')
        self.cau = XmlField('CAU')
        self.rechazos = Rechazos()
        self.comentarios = XmlField('Comentarios')
        super(A102, self).__init__('A102', 'a102')


class Rechazos(XmlModel):

    _sort_order = ('rechazos', 'fecha_rechazo', 'rechazo_list')

    def __init__(self):
        self.rechazos = XmlField('Rechazos')
        self.fecha_rechazo = XmlField('FechaRechazo')
        self.rechazo_list = []
        super(Rechazos, self).__init__('Rechazos', 'rechazos')


class Rechazo(XmlModel):

    _sort_order = ('rechazo', 'secuencial', 'codigo_motivo', 'comentarios')

    def __init__(self):
        self.rechazo = XmlField('Rechazo')
        self.secuencial = XmlField('Secuencial')
        self.codigo_motivo = XmlField('CodigoMotivo')
        self.comentarios = XmlField('Comentarios')
        super(Rechazo, self).__init__('Rechazo', 'rechazo')


class Autoconsumo(XmlModel):

    _sort_order = ('autoconsumo', 'cau', 'seccion_registro', 'sub_seccion', 'colectivo')

    def __init__(self):
        self.autoconsumo = XmlField('Autoconsumo')
        self.cau = XmlField('CAU')
        self.seccion_registro = XmlField('SeccionRegistro')
        self.sub_seccion = XmlField('SubSeccion')
        self.colectivo = XmlField('Colectivo')
        super(Autoconsumo, self).__init__('Autoconsumo', 'autoconsumo')


class DatosSuministro(XmlModel):

    _sort_order = ('datos_suministro', 'cups', 'tipo_cups', 'ref_catastro')

    def __init__(self):
        self.datos_suministro = XmlField('DatosSuministro')
        self.cups = XmlField('CUPS')
        self.tipo_cups = XmlField('TipoCUPS')
        self.ref_catastro = XmlField('RefCatastro')
        super(DatosSuministro, self).__init__('DatosSuministro', 'datos_suministro')


class DatosInstGen(XmlModel):

    _sort_order = ('datos_inst_gen', 'cil', 'tec_generador', 'combustible', 'pot_instalada_gen', 'tipo_instalacion',
                   'esquema_medida', 'ssaa', 'ref_catastro', 'utm', 'titular_representante_gen')

    def __init__(self):
        self.datos_inst_gen = XmlField('DatosInstGen')
        self.cil = XmlField('CIL')
        self.tec_generador = XmlField('TecGenerador')
        self.combustible = XmlField('Combustible')
        self.pot_instalada_gen = XmlField('PotInstaladaGen')
        self.tipo_instalacion = XmlField('TipoInstalacion')
        self.esquema_medida = XmlField('EsquemaMedida')
        self.ssaa = XmlField('SSAA')
        self.ref_catastro = XmlField('RefCatastro')
        self.utm = UTM()
        self.titular_representante_gen = TitularRepresentanteGen()
        super(DatosInstGen, self).__init__('DatosInstGen', 'datos_inst_gen')


class UTM(XmlModel):

    _sort_order = ('utm', 'x', 'y', 'huso', 'banda')

    def __init__(self):
        self.utm = XmlField('UTM')
        self.x = XmlField('X')
        self.y = XmlField('Y')
        self.huso = XmlField('Huso')
        self.banda = XmlField('Banda')
        super(UTM, self).__init__('UTM', 'utm')


class TitularRepresentanteGen(XmlModel):

    _sort_order = ('titular_representante_gen', 'id_titular', 'nombre', 'telefono', 'correo_electronico',
                   'direccion')

    def __init__(self):
        self.titular_representante_gen = XmlField('TitularRepresentanteGen')
        self.id_titular = IdTitular()
        self.nombre = Nombre()
        self.telefono = Telefono()
        self.correo_electronico = XmlField('CorreoElectronico')
        self.direccion = Direccion()
        super(TitularRepresentanteGen, self).__init__('TitularRepresentanteGen', 'titular_representante_gen')


class IdTitular(XmlModel):

    _sort_order = ('id_titular', 'tipo_identificador', 'identificador')

    def __init__(self):
        self.id_titular = XmlField('IdTitular')
        self.tipo_identificador = XmlField('TipoIdentificador')
        self.identificador = XmlField('Identificador')
        super(IdTitular, self).__init__('IdTitular', 'id_titular')


class Nombre(XmlModel):

    _sort_order = ('nombre', 'nombre_de_pila', 'primer_apellido', 'segundo_apellido', 'razon_social')

    def __init__(self):
        self.nombre = XmlField('Nombre')
        self.nombre_de_pila = XmlField('NombreDePila')
        self.primer_apellido = XmlField('PrimerApellido')
        self.segundo_apellido = XmlField('SegundoApellido')
        self.razon_social = XmlField('RazonSocial')
        super(Nombre, self).__init__('Nombre', 'nombre')


class Telefono(XmlModel):

    _sort_order = ('telefono', 'prefijo_pais', 'numero')

    def __init__(self):
        self.telefono = XmlField('Telefono')
        self.prefijo_pais = XmlField('PrefijoPais')
        self.numero = XmlField('Numero')
        super(Telefono, self).__init__('Telefono', 'telefono')


class Direccion(XmlModel):

    _sort_order = ('direccion', 'pais', 'provincia', 'municipio', 'poblacion', 'cod_postal', 'via',
                   'apartado_de_correos')

    def __init__(self):
        self.direccion = XmlField('Direccion')
        self.pais = XmlField('Pais')
        self.provincia = XmlField('Provincia')
        self.municipio = XmlField('Municipio')
        self.poblacion = XmlField('Poblacion')
        self.cod_postal = XmlField('CodPostal')
        self.via = Via()
        self.apartado_de_correos = XmlField('ApartadoDeCorreos')
        super(Direccion, self).__init__('Direccion', 'direccion')


class Via(XmlModel):

    _sort_order = ('via', 'tipo_via', 'calle', 'numero_finca', 'duplicador_finca', 'escalera', 'piso', 'puerta',
                   'tipo_aclarador_finca', 'aclarador_finca')

    def __init__(self):
        self.via = XmlField('Via')
        self.tipo_via = XmlField('TipoVia')
        self.calle = XmlField('Calle')
        self.numero_finca = XmlField('NumeroFinca')
        self.duplicador_finca = XmlField('DuplicadorFinca')
        self.escalera = XmlField('Escalera')
        self.piso = XmlField('Piso')
        self.puerta = XmlField('Puerta')
        self.tipo_aclarador_finca = XmlField('TipoAclaradorFinca')
        self.aclarador_finca = XmlField('AclaradorFinca')
        super(Via, self).__init__('Via', 'via')
