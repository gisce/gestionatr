#!/usr/bin/env python
# -*- coding: utf-8 -*-
from . import unittest
from .utils import get_data
from gestionatr.input.messages import C1


class test_MessageBase(unittest.TestCase):

    def setUp(self):
        self.xml_c101_cabecera = open(get_data("c101.xml"), "r")

    def tearDown(self):
        self.xml_c101_cabecera.close()

    def test_cabecera_model(self):
        c = C1(self.xml_c101_cabecera)
        c.parse_xml()
        self.assertEqual(c.tipus, 'C1')
        self.assertEqual(c.pas, '01')
        self.assertEqual(c.get_pas_xml(), '01')
        self.assertEqual(c.get_codi_emisor, '1234')
        self.assertEqual(c.get_codi_destinatari, '4321')
        self.assertEqual(c.cups, 'ES1234000000000001JN0F')
        self.assertEqual(c.codi_sollicitud, '201607211259')
        self.assertEqual(c.seq_sollicitud, '01')
        self.assertEqual(c.data_sollicitud, '2016-07-21 12:59:47')


class test_C1(unittest.TestCase):

    def setUp(self):
        self.xml_c101_completo = open(get_data("c101.xml"), "r")
        self.xml_c101_minim = open(get_data("c101_minim.xml"), "r")
        self.xml_c102_accept = open(get_data("c102_accept.xml"), "r")
        self.xml_c102_reject = open(get_data("c102_reject.xml"), "r")

    def tearDown(self):
        self.xml_c101_completo.close()
        self.xml_c101_minim.close()
        self.xml_c102_accept.close()
        self.xml_c102_reject.close()

    def test_c101_completo(self):
        c = C1(self.xml_c101_completo)
        c.parse_xml()
        # Datos Solicitud
        self.assertEqual(c.datos_solicitud.ind_activacion, 'L')
        self.assertEqual(c.datos_solicitud.fecha_prevista_accion, '2016-06-06')
        self.assertEqual(c.datos_solicitud.contratacion_incondicional_ps, 'S')
        # Cliente
        self.assertEqual(c.cliente.tipo_identificador, 'NI')
        self.assertEqual(c.cliente.identificador, 'B36385870')
        self.assertEqual(c.cliente.tipo_persona, 'J')
        self.assertEqual(c.cliente.razon_social, 'ACC Y COMP DE COCINA MILLAN Y MUÑOZ')
        self.assertEqual(c.cliente.nombre, 'ACC Y COMP DE COCINA MILLAN Y MUÑOZ')
        self.assertFalse(c.cliente.nombre_de_pila)
        self.assertEqual(c.cliente.telfono_numero, '666777888')
        self.assertEqual(c.cliente.telfono_prefijo_pais, '34')
        self.assertEqual(c.cliente.correo_electronico, 'email@host')
        # Comentarios
        self.assertFalse(c.comentarios)
        # Registros Documento
        self.assertEqual(len(c.registros_documento), 2)
        doc1 = c.registros_documento[0]
        doc2 = c.registros_documento[1]
        self.assertEqual(doc1.tipo_doc_aportado, '08')
        self.assertEqual(doc1.direccion_url, 'http://eneracme.com/docs/NIF11111111H.pdf')
        self.assertEqual(doc2.tipo_doc_aportado, '07')
        self.assertEqual(doc2.direccion_url, 'http://eneracme.com/docs/NIF11111111H.pdf')

    def test_c101_minim(self):
        c = C1(self.xml_c101_minim)
        c.parse_xml()
        # Datos Solicitud
        self.assertEqual(c.datos_solicitud.ind_activacion, 'L')
        self.assertFalse(c.datos_solicitud.fecha_prevista_accion)
        self.assertEqual(c.datos_solicitud.contratacion_incondicional_ps, 'S')
        # Cliente
        self.assertEqual(c.cliente.tipo_identificador, 'NI')
        self.assertEqual(c.cliente.identificador, 'B36385870')
        self.assertEqual(c.cliente.tipo_persona, 'F')
        self.assertEqual(c.cliente.nombre_de_pila, 'NOMBRE')
        self.assertEqual(c.cliente.primer_apellido, 'APELLIDO1')
        self.assertFalse(c.cliente.segundo_apellido)
        self.assertEqual(c.cliente.nombre, 'APELLIDO1, NOMBRE')
        self.assertFalse(c.cliente.razon_social)
        self.assertFalse(c.cliente.telfono_numero)
        self.assertFalse(c.cliente.telfono_prefijo_pais)
        self.assertFalse(c.cliente.correo_electronico)
        # Comentarios
        self.assertFalse(c.comentarios)
        # Registros Documento
        self.assertFalse(c.registros_documento)

    def test_c102_accept(self):
        c = C1(self.xml_c102_accept)
        c.parse_xml()
        # Datos Aceptacion
        self.assertEqual(c.datos_aceptacion.fecha_aceptacion, '2016-06-06')
        self.assertEqual(c.datos_aceptacion.fecha_ultima_lectura_firme, '2016-06-01')
        # Contrato
        self.assertEqual(c.contrato.tipo_contrato_atr, '02')
        self.assertEqual(c.contrato.tipo_activacion_prevista, 'C0')
        self.assertEqual(c.contrato.fecha_activacion_prevista, '2016-07-06')
        self.assertEqual(c.contrato.tarifa_atr, '003')
        pots = c.contrato.potencias_contratadas
        self.assertEqual(len(pots), 2)
        self.assertEqual(pots[0], '1000')
        self.assertEqual(pots[1], '2000')

    def test_c102_reject(self):
        c = C1(self.xml_c102_reject)
        c.parse_xml()
        self.assertEqual(c.fecha_rechazo, '2016-07-20')
        self.assertEqual(len(c.registros_documento), 2)
        doc1 = c.registros_documento[0]
        doc2 = c.registros_documento[1]
        self.assertEqual(doc1.tipo_doc_aportado, '08')
        self.assertEqual(doc1.direccion_url, 'http://eneracme.com/docs/NIF11111111H.pdf')
        self.assertEqual(doc2.tipo_doc_aportado, '07')
        self.assertEqual(doc2.direccion_url, 'http://eneracme.com/docs/NIF11111111H.pdf')
        self.assertEqual(len(c.rechazos), 2)
        rej1 = c.rechazos[0]
        rej2 = c.rechazos[1]
        self.assertEqual(rej1.secuencial, '1')
        self.assertEqual(rej1.codigo_motivo, '01')
        self.assertEqual(rej1.comentarios, 'Motiu de rebuig 01: No existe Punto de Suministro asociado al CUPS')
        self.assertEqual(rej2.secuencial, '2')
        self.assertEqual(rej2.codigo_motivo, '03')
        self.assertEqual(rej2.comentarios, 'Cuando el CIF-NIF no coincide con el que figura en la base de datos del Distribuidor')
