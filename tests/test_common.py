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
        self.xml_c104 = open(get_data("c104.xml"), "r")
        self.xml_c105 = open(get_data("c105.xml"), "r")
        self.xml_c106 = open(get_data("c106.xml"), "r")

    def tearDown(self):
        self.xml_c101_completo.close()
        self.xml_c101_minim.close()
        self.xml_c102_accept.close()
        self.xml_c102_reject.close()
        self.xml_c104.close()
        self.xml_c105.close()
        self.xml_c106.close()

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

    def test_c104(self):
        c = C1(self.xml_c104)
        c.parse_xml()
        self.assertEqual(c.fecha_rechazo, '2016-07-20')
        self.assertEqual(len(c.registros_documento), 0)
        self.assertEqual(len(c.rechazos), 1)
        rej1 = c.rechazos[0]
        self.assertEqual(rej1.secuencial, '1')
        self.assertEqual(rej1.codigo_motivo, '01')
        self.assertEqual(rej1.comentarios, 'Motiu de rebuig 01: No existe Punto de Suministro asociado al CUPS')

    def test_c105(self):
        c = C1(self.xml_c105)
        c.parse_xml()
        self.assertEqual(c.datos_activacion.fecha, '2016-08-21')
        # Contrato
        self.assertEqual(c.contrato.cod_contrato, '00001')
        self.assertEqual(c.contrato.tipo_autoconsumo, '00')
        self.assertEqual(c.contrato.tipo_contrato_atr, '02')
        self.assertEqual(c.contrato.tarifa_atr, '003')
        self.assertEqual(c.contrato.periodicidad_facturacion, '01')
        self.assertEqual(c.contrato.tipo_de_telegestion, '01')
        self.assertEqual(c.contrato.modo_control_potencia, '1')
        self.assertEqual(c.contrato.marca_medida_con_perdidas, 'S')
        self.assertEqual(c.contrato.tension_del_suministro, '10')
        self.assertEqual(c.contrato.vas_trafo, '50')
        self.assertEqual(c.contrato.porcentaje_perdidas, '05')
        self.assertEqual(len(c.contrato.potencias_contratadas), 2)
        pot1 = c.contrato.potencias_contratadas[0]
        pot2 = c.contrato.potencias_contratadas[1]
        self.assertEqual(pot1, '1000')
        self.assertEqual(pot2, '2000')
        # Puntos Medida
        self.assertEqual(len(c.puntos_medida), 1)
        pm = c.puntos_medida[0]
        self.assertEqual(pm.cod_pm, 'ES1234000000000001JN0F')
        self.assertEqual(pm.tipo_movimiento, 'A')
        self.assertEqual(pm.tipo_pm, '03')
        self.assertEqual(pm.cod_pm_principal, 'ES1234000000000002JN0F')
        self.assertEqual(pm.modo_lectura, '1')
        self.assertEqual(pm.funcion, 'P')
        self.assertEqual(pm.direccion_enlace, '39522')
        self.assertEqual(pm.direccion_punto_medida, '000000001')
        self.assertEqual(pm.num_linea, '12')
        self.assertEqual(pm.telefono_telemedida, '987654321')
        self.assertEqual(pm.estado_telefono, '1')
        self.assertEqual(pm.clave_acceso, '0000000007')
        self.assertEqual(pm.tension_pm, '0')
        self.assertEqual(pm.fecha_vigor, '2003-01-01')
        self.assertEqual(pm.fecha_alta, '2003-01-01')
        self.assertEqual(pm.fecha_baja, '2003-02-01')
        self.assertEqual(pm.comentarios, 'Comentarios Varios')
        # Aparatos
        self.assertEqual(len(pm.aparatos), 1)
        ap = pm.aparatos[0]
        self.assertEqual(ap.cod_precinto, '02')
        self.assertEqual(ap.constante_energia, '1.000')
        self.assertEqual(ap.constante_maximetro, '1.000')
        self.assertEqual(ap.funcion_aparato, 'M')
        self.assertEqual(ap.lectura_directa, 'N')
        self.assertEqual(ap.marca_aparato, '132')
        self.assertEqual(ap.modelo_marca, '011')
        self.assertEqual(ap.modo_medida_potencia, '1')
        self.assertEqual(ap.num_integradores, '18')
        self.assertEqual(ap.numero_serie, '0000539522')
        self.assertEqual(ap.periodo_fabricacion, '2005')
        self.assertEqual(ap.propietario, 'Desc. Propietario')
        self.assertEqual(ap.ruedas_decimales, '02')
        self.assertEqual(ap.ruedas_enteras, '08')
        self.assertEqual(ap.tipo_aparato, 'CG')
        self.assertEqual(ap.tipo_dhedm, '6')
        self.assertEqual(ap.tipo_equipo_medida, 'L03')
        self.assertEqual(ap.tipo_movimiento, 'CX')
        self.assertEqual(ap.tipo_propiedad_aparato, '1')
        # Medidas
        self.assertEqual(len(pm.medidas), 2)
        md = pm.medidas[0]
        self.assertEqual(md.anomalia, '01')
        self.assertEqual(md.comentarios, 'Comentario sobre anomalia')
        self.assertEqual(md.fecha_lectura_firme, '2003-01-02')
        self.assertEqual(md.magnitud_medida, 'PM')
        self.assertEqual(md.periodo, '65')
        self.assertEqual(md.procedencia, '30')
        self.assertEqual(md.tipo_dhedm, '6')
        self.assertEqual(md.ultima_lectura_firme, '6.00')
        md2 = pm.medidas[1]
        self.assertFalse(md2.anomalia)
        self.assertFalse(md2.comentarios)
        self.assertEqual(md2.fecha_lectura_firme, '2003-01-03')

    def test_c106(self):
        c = C1(self.xml_c106)
        c.parse_xml()
        self.assertEqual(c.datos_notificacion.fecha_activacion, '2016-08-21')
        # Contrato
        self.assertEqual(c.contrato.cod_contrato, '00001')
        # Puntos Medida
        self.assertEqual(len(c.puntos_medida), 1)
        pm = c.puntos_medida[0]
        self.assertEqual(pm.cod_pm, 'ES1234000000000001JN0F')
        self.assertEqual(pm.tipo_movimiento, 'A')
        self.assertEqual(pm.tipo_pm, '03')
        self.assertEqual(pm.cod_pm_principal, 'ES1234000000000002JN0F')
        self.assertEqual(pm.modo_lectura, '1')
        self.assertEqual(pm.funcion, 'P')
        self.assertEqual(pm.direccion_enlace, '39522')
        self.assertEqual(pm.direccion_punto_medida, '000000001')
        self.assertEqual(pm.num_linea, '12')
        self.assertEqual(pm.telefono_telemedida, '987654321')
        self.assertEqual(pm.estado_telefono, '1')
        self.assertEqual(pm.clave_acceso, '0000000007')
        self.assertEqual(pm.tension_pm, '0')
        self.assertEqual(pm.fecha_vigor, '2003-01-01')
        self.assertEqual(pm.fecha_alta, '2003-01-01')
        self.assertEqual(pm.fecha_baja, '2003-02-01')
        self.assertEqual(pm.comentarios, 'Comentarios Varios')
        # Aparatos
        self.assertEqual(len(pm.aparatos), 1)
        ap = pm.aparatos[0]
        self.assertEqual(ap.cod_precinto, '02')
        self.assertEqual(ap.constante_energia, '1.000')
        self.assertEqual(ap.constante_maximetro, '1.000')
        self.assertEqual(ap.funcion_aparato, 'M')
        self.assertEqual(ap.lectura_directa, 'N')
        self.assertEqual(ap.marca_aparato, '132')
        self.assertEqual(ap.modelo_marca, '011')
        self.assertEqual(ap.modo_medida_potencia, '1')
        self.assertEqual(ap.num_integradores, '18')
        self.assertEqual(ap.numero_serie, '0000539522')
        self.assertEqual(ap.periodo_fabricacion, '2005')
        self.assertEqual(ap.propietario, 'Desc. Propietario')
        self.assertEqual(ap.ruedas_decimales, '02')
        self.assertEqual(ap.ruedas_enteras, '08')
        self.assertEqual(ap.tipo_aparato, 'CG')
        self.assertEqual(ap.tipo_dhedm, '6')
        self.assertEqual(ap.tipo_equipo_medida, 'L03')
        self.assertEqual(ap.tipo_movimiento, 'CX')
        self.assertEqual(ap.tipo_propiedad_aparato, '1')
        # Medidas
        self.assertEqual(len(pm.medidas), 2)
        md = pm.medidas[0]
        self.assertEqual(md.anomalia, '01')
        self.assertEqual(md.comentarios, 'Comentario sobre anomalia')
        self.assertEqual(md.fecha_lectura_firme, '2003-01-02')
        self.assertEqual(md.magnitud_medida, 'PM')
        self.assertEqual(md.periodo, '65')
        self.assertEqual(md.procedencia, '30')
        self.assertEqual(md.tipo_dhedm, '6')
        self.assertEqual(md.ultima_lectura_firme, '6.00')
        md2 = pm.medidas[1]
        self.assertFalse(md2.anomalia)
        self.assertFalse(md2.comentarios)
        self.assertEqual(md2.fecha_lectura_firme, '2003-01-03')
