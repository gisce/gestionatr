#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gestionatr.input.messages import A1, A3, B1, B2, C1, C2, D1, E1, M1, P0, Q1, R1, T1, W1, F1, Deadlines
from gestionatr.input.messages import A1_41, A1_02, A1_05, A1_44, A1_03, A1_48, A1_04, A1_46, A1_38, A1_49, A1_42, A1_43
from gestionatr.input.messages import B7031, B7032, A12_24, A12_26, A19_45, A20_36, A13_50
from gestionatr.input.messages.F1 import agrupar_lectures_per_data, obtenir_data_inici_i_final
from . import unittest
from .utils import get_data


class test_MessageBase(unittest.TestCase):

    def setUp(self):
        self.xml_c101_cabecera = open(get_data("c101.xml"), "r")

    def tearDown(self):
        self.xml_c101_cabecera.close()

    def test_cabecera_model(self):
        c = C1(self.xml_c101_cabecera)
        c.parse_xml()
        self.assertEqual(c.tipus, u'C1')
        self.assertEqual(c.pas, u'01')
        self.assertEqual(c.get_pas_xml(), u'01')
        self.assertEqual(c.get_codi_emisor, u'1234')
        self.assertEqual(c.get_codi_destinatari, u'4321')
        self.assertEqual(c.cups, u'ES1234000000000001JN0F')
        self.assertEqual(c.codi_sollicitud, u'201607211259')
        self.assertEqual(c.seq_sollicitud, u'01')
        self.assertEqual(c.data_sollicitud, u'2016-07-21 12:59:47')


class test_Deadline(unittest.TestCase):

    def setUp(self):
        self.xml_c101_completo = open(get_data("c101.xml"), "r")

    def test_limit(self):
        c = C1(self.xml_c101_completo)
        c.parse_xml()
        res = c.get_deadline('01')
        self.assertEqual(res, Deadlines.DeadLine(step='01', days=5))

    def tearDown(self):
        self.xml_c101_completo.close()


class test_C1(unittest.TestCase):

    def setUp(self):
        self.xml_c101_completo = open(get_data("c101.xml"), "r")
        self.xml_c101_minim = open(get_data("c101_minim.xml"), "r")
        self.xml_c102_accept = open(get_data("c102_accept.xml"), "r")
        self.xml_c102_reject = open(get_data("c102_reject.xml"), "r")
        self.xml_c104 = open(get_data("c104.xml"), "r")
        self.xml_c105 = open(get_data("c105.xml"), "r")
        self.xml_c106 = open(get_data("c106.xml"), "r")
        self.xml_c108 = open(get_data("c108.xml"), "r")
        self.xml_c109 = open(get_data("c109.xml"), "r")
        self.xml_c111 = open(get_data("c111.xml"), "r")
        self.xml_c112 = open(get_data("c112.xml"), "r")

    def tearDown(self):
        self.xml_c101_completo.close()
        self.xml_c101_minim.close()
        self.xml_c102_accept.close()
        self.xml_c102_reject.close()
        self.xml_c104.close()
        self.xml_c105.close()
        self.xml_c106.close()
        self.xml_c108.close()
        self.xml_c109.close()
        self.xml_c111.close()
        self.xml_c112.close()

    def test_c101_completo(self):
        c = C1(self.xml_c101_completo)
        c.parse_xml()
        # Datos Solicitud
        self.assertEqual(c.datos_solicitud.ind_activacion, u'L')
        self.assertEqual(c.datos_solicitud.fecha_prevista_accion, u'2016-06-06')
        self.assertEqual(c.datos_solicitud.contratacion_incondicional_ps, u'S')
        self.assertEqual(c.datos_solicitud.bono_social, u'0')
        self.assertEqual(c.datos_solicitud.contratacion_incondicional_bs, u'S')
        # Cliente
        self.assertEqual(c.cliente.tipo_identificador, u'NI')
        self.assertEqual(c.cliente.identificador, u'B36385870')
        self.assertEqual(c.cliente.tipo_persona, u'J')
        self.assertEqual(c.cliente.razon_social, u'ACC Y COMP DE COCINA MILLAN Y MUÑOZ')
        self.assertEqual(c.cliente.nombre, u'ACC Y COMP DE COCINA MILLAN Y MUÑOZ')
        self.assertFalse(c.cliente.nombre_de_pila)
        self.assertEqual(c.cliente.telefonos[2][1], u'666777888')
        self.assertEqual(c.cliente.telefonos[2][0], u'38')
        self.assertEqual(c.cliente.correo_electronico, u'email@host')
        # Comentarios
        self.assertFalse(c.comentarios)
        # Registros Documento
        self.assertEqual(len(c.registros_documento), 2)
        doc1 = c.registros_documento[0]
        doc2 = c.registros_documento[1]
        self.assertEqual(doc1.tipo_doc_aportado, u'08')
        self.assertEqual(doc1.direccion_url, u'http://eneracme.com/docs/NIF11111111H.pdf')
        self.assertEqual(doc2.tipo_doc_aportado, u'07')
        self.assertEqual(doc2.direccion_url, u'http://eneracme.com/docs/NIF11111111H.pdf')

    def test_c101_minim(self):
        c = C1(self.xml_c101_minim)
        c.parse_xml()
        # Datos Solicitud
        self.assertEqual(c.datos_solicitud.ind_activacion, u'L')
        self.assertFalse(c.datos_solicitud.fecha_prevista_accion)
        self.assertEqual(c.datos_solicitud.contratacion_incondicional_ps, u'S')
        # Cliente
        self.assertEqual(c.cliente.tipo_identificador, u'NI')
        self.assertEqual(c.cliente.identificador, u'B36385870')
        self.assertEqual(c.cliente.tipo_persona, u'F')
        self.assertEqual(c.cliente.nombre_de_pila, u'NOMBRE')
        self.assertEqual(c.cliente.primer_apellido, u'APELLIDO1')
        self.assertFalse(c.cliente.segundo_apellido)
        self.assertEqual(c.cliente.nombre, u'APELLIDO1, NOMBRE')
        self.assertFalse(c.cliente.razon_social)
        self.assertFalse(len(c.cliente.telefonos))
        self.assertFalse(c.cliente.correo_electronico)
        # Comentarios
        self.assertFalse(c.comentarios)
        # Registros Documento
        self.assertFalse(c.registros_documento)

    def test_c102_accept(self):
        c = C1(self.xml_c102_accept)
        c.parse_xml()
        # Datos Aceptacion
        self.assertEqual(c.datos_aceptacion.fecha_aceptacion, u'2016-06-06')
        self.assertEqual(c.datos_aceptacion.fecha_ultima_lectura_firme, u'2016-06-01')
        self.assertEqual(c.datos_aceptacion.actuacion_campo, u'S')
        # Contrato
        self.assertEqual(c.contrato.tipo_contrato_atr, u'02')
        self.assertEqual(c.contrato.tipo_activacion_prevista, u'C0')
        self.assertEqual(c.contrato.fecha_activacion_prevista, u'2016-07-06')
        self.assertEqual(c.contrato.tarifa_atr, u'003')
        self.assertEqual(c.datos_aceptacion.bono_social, u'0')
        pots = c.contrato.potencias_contratadas
        self.assertEqual(len(pots), 2)
        self.assertEqual(pots[0][1], 1000)
        self.assertEqual(pots[1][1], 2000)

    def test_c102_reject(self):
        c = C1(self.xml_c102_reject)
        c.parse_xml()
        self.assertEqual(c.fecha_rechazo, u'2016-07-20')
        self.assertEqual(len(c.registros_documento), 2)
        doc1 = c.registros_documento[0]
        doc2 = c.registros_documento[1]
        self.assertEqual(doc1.tipo_doc_aportado, u'08')
        self.assertEqual(doc1.direccion_url, u'http://eneracme.com/docs/NIF11111111H.pdf')
        self.assertEqual(doc2.tipo_doc_aportado, u'07')
        self.assertEqual(doc2.direccion_url, u'http://eneracme.com/docs/NIF11111111H.pdf')
        self.assertEqual(len(c.rechazos), 2)
        rej1 = c.rechazos[0]
        rej2 = c.rechazos[1]
        self.assertEqual(rej1.secuencial, u'1')
        self.assertEqual(rej1.codigo_motivo, u'01')
        self.assertEqual(rej1.comentarios, u'Motiu de rebuig 01: No existe Punto de Suministro asociado al CUPS')
        self.assertEqual(rej2.secuencial, u'2')
        self.assertEqual(rej2.codigo_motivo, u'03')
        self.assertEqual(rej2.comentarios, u'Cuando el CIF-NIF no coincide con el que figura en la base de datos del Distribuidor')

    def test_c104(self):
        c = C1(self.xml_c104)
        c.parse_xml()
        self.assertEqual(c.fecha_rechazo, u'2016-07-20')
        self.assertEqual(len(c.registros_documento), 0)
        self.assertEqual(len(c.rechazos), 1)
        rej1 = c.rechazos[0]
        self.assertEqual(rej1.secuencial, u'1')
        self.assertEqual(rej1.codigo_motivo, u'01')
        self.assertEqual(rej1.comentarios, u'Motiu de rebuig 01: No existe Punto de Suministro asociado al CUPS')

    def test_c105(self):
        c = C1(self.xml_c105)
        c.parse_xml()
        self.assertEqual(c.datos_activacion.fecha, u'2016-08-21')
        # Contrato
        self.assertEqual(c.contrato.cod_contrato, u'00001')
        self.assertEqual(c.contrato.data_finalitzacio, u'2020-01-01')
        self.assertEqual(c.contrato.tipo_autoconsumo, u'00')
        self.assertEqual(c.contrato.tipo_contrato_atr, u'02')
        self.assertEqual(c.contrato.tarifa_atr, u'003')
        self.assertEqual(c.contrato.periodicidad_facturacion, u'01')
        self.assertEqual(c.contrato.tipo_de_telegestion, u'01')
        self.assertEqual(c.contrato.modo_control_potencia, u'1')
        self.assertEqual(c.contrato.marca_medida_con_perdidas, u'S')
        self.assertEqual(c.contrato.tension_del_suministro, u'10')
        self.assertEqual(c.contrato.vas_trafo, u'50')
        self.assertEqual(c.contrato.porcentaje_perdidas, u'05')
        self.assertEqual(c.datos_activacion.bono_social, u'1')
        self.assertEqual(len(c.contrato.potencias_contratadas), 2)
        pot1 = c.contrato.potencias_contratadas[0]
        pot2 = c.contrato.potencias_contratadas[1]
        self.assertEqual(pot1[1], 1000)
        self.assertEqual(pot2[1], 2000)
        # Puntos Medida
        self.assertEqual(len(c.puntos_medida), 1)
        pm = c.puntos_medida[0]
        self.assertEqual(pm.cod_pm, u'ES1234000000000001JN0F')
        self.assertEqual(pm.tipo_movimiento, u'A')
        self.assertEqual(pm.tipo_pm, u'03')
        self.assertEqual(pm.cod_pm_principal, u'ES1234000000000002JN0F')
        self.assertEqual(pm.modo_lectura, u'1')
        self.assertEqual(pm.funcion, u'P')
        self.assertEqual(pm.direccion_enlace, u'39522')
        self.assertEqual(pm.direccion_punto_medida, u'000000001')
        self.assertEqual(pm.num_linea, u'12')
        self.assertEqual(pm.telefono_telemedida, u'987654321')
        self.assertEqual(pm.estado_telefono, u'1')
        self.assertEqual(pm.clave_acceso, u'0000000007')
        self.assertEqual(pm.tension_pm, u'0')
        self.assertEqual(pm.fecha_vigor, u'2003-01-01')
        self.assertEqual(pm.fecha_alta, u'2003-01-01')
        self.assertEqual(pm.fecha_baja, u'2003-02-01')
        self.assertEqual(pm.comentarios, u'Comentarios Varios')
        # Aparatos
        self.assertEqual(len(pm.aparatos), 1)
        ap = pm.aparatos[0]
        self.assertEqual(ap.cod_precinto, u'02')
        self.assertEqual(ap.constante_energia, u'1.000')
        self.assertEqual(ap.constante_maximetro, u'1.000')
        self.assertEqual(ap.funcion_aparato, u'M')
        self.assertEqual(ap.lectura_directa, u'N')
        self.assertEqual(ap.marca_aparato, u'132')
        self.assertEqual(ap.modelo_marca, u'011')
        self.assertEqual(ap.modo_medida_potencia, u'1')
        self.assertEqual(ap.num_integradores, u'18')
        self.assertEqual(ap.numero_serie, u'0000539522')
        self.assertEqual(ap.periodo_fabricacion, u'2005')
        self.assertEqual(ap.propietario, u'Desc. Propietario')
        self.assertEqual(ap.ruedas_decimales, u'02')
        self.assertEqual(ap.ruedas_enteras, u'08')
        self.assertEqual(ap.tipo_aparato, u'CG')
        self.assertEqual(ap.tipo_dhedm, u'6')
        self.assertEqual(ap.tipo_equipo_medida, u'L03')
        self.assertEqual(ap.tipo_movimiento, u'CX')
        self.assertEqual(ap.tipo_propiedad_aparato, u'1')
        # Medidas
        self.assertEqual(len(ap.medidas), 2)
        md = ap.medidas[0]
        self.assertEqual(md.anomalia, u'01')
        self.assertEqual(md.comentarios, u'Comentario sobre anomalia')
        self.assertEqual(md.fecha_lectura_firme, u'2003-01-02')
        self.assertEqual(md.magnitud_medida, u'PM')
        self.assertEqual(md.periodo, u'65')
        self.assertEqual(md.procedencia, u'30')
        self.assertEqual(md.tipo_dhedm, u'6')
        self.assertEqual(md.ultima_lectura_firme, u'0.00')
        md2 = ap.medidas[1]
        self.assertFalse(md2.anomalia)
        self.assertFalse(md2.comentarios)
        self.assertEqual(md2.fecha_lectura_firme, u'2003-01-03')

    def test_c106(self):
        c = C1(self.xml_c106)
        c.parse_xml()
        self.assertEqual(c.datos_notificacion.fecha_activacion, u'2016-08-21')
        self.assertEqual(c.datos_notificacion.ind_bono_social, u'S')
        # Contrato
        self.assertEqual(c.contrato.cod_contrato, u'00001')
        # Puntos Medida
        self.assertEqual(len(c.puntos_medida), 1)
        pm = c.puntos_medida[0]
        self.assertEqual(pm.cod_pm, u'ES1234000000000001JN0F')
        self.assertEqual(pm.tipo_movimiento, u'A')
        self.assertEqual(pm.tipo_pm, u'03')
        self.assertEqual(pm.cod_pm_principal, u'ES1234000000000002JN0F')
        self.assertEqual(pm.modo_lectura, u'1')
        self.assertEqual(pm.funcion, u'P')
        self.assertEqual(pm.direccion_enlace, u'39522')
        self.assertEqual(pm.direccion_punto_medida, u'000000001')
        self.assertEqual(pm.num_linea, u'12')
        self.assertEqual(pm.telefono_telemedida, u'987654321')
        self.assertEqual(pm.estado_telefono, u'1')
        self.assertEqual(pm.clave_acceso, u'0000000007')
        self.assertEqual(pm.tension_pm, u'0')
        self.assertEqual(pm.fecha_vigor, u'2003-01-01')
        self.assertEqual(pm.fecha_alta, u'2003-01-01')
        self.assertEqual(pm.fecha_baja, u'2003-02-01')
        self.assertEqual(pm.comentarios, u'Comentarios Varios')
        # Aparatos
        self.assertEqual(len(pm.aparatos), 1)
        ap = pm.aparatos[0]
        self.assertEqual(ap.cod_precinto, u'02')
        self.assertEqual(ap.constante_energia, u'1.000')
        self.assertEqual(ap.constante_maximetro, u'1.000')
        self.assertEqual(ap.funcion_aparato, u'M')
        self.assertEqual(ap.lectura_directa, u'N')
        self.assertEqual(ap.marca_aparato, u'132')
        self.assertEqual(ap.modelo_marca, u'011')
        self.assertEqual(ap.modo_medida_potencia, u'1')
        self.assertEqual(ap.num_integradores, u'18')
        self.assertEqual(ap.numero_serie, u'0000539522')
        self.assertEqual(ap.periodo_fabricacion, u'2005')
        self.assertEqual(ap.propietario, u'Desc. Propietario')
        self.assertEqual(ap.ruedas_decimales, u'02')
        self.assertEqual(ap.ruedas_enteras, u'08')
        self.assertEqual(ap.tipo_aparato, u'CG')
        self.assertEqual(ap.tipo_dhedm, u'6')
        self.assertEqual(ap.tipo_equipo_medida, u'L03')
        self.assertEqual(ap.tipo_movimiento, u'CX')
        self.assertEqual(ap.tipo_propiedad_aparato, u'1')
        # Medidas
        self.assertEqual(len(ap.medidas), 2)
        md = ap.medidas[0]
        self.assertEqual(md.anomalia, u'01')
        self.assertEqual(md.comentarios, u'Comentario sobre anomalia')
        self.assertEqual(md.fecha_lectura_firme, u'2003-01-02')
        self.assertEqual(md.magnitud_medida, u'PM')
        self.assertEqual(md.periodo, u'65')
        self.assertEqual(md.procedencia, u'30')
        self.assertEqual(md.tipo_dhedm, u'6')
        self.assertEqual(md.ultima_lectura_firme, u'0.00')
        md2 = ap.medidas[1]
        self.assertFalse(md2.anomalia)
        self.assertFalse(md2.comentarios)
        self.assertEqual(md2.fecha_lectura_firme, u'2003-01-03')

    def test_c108(self):
        c = C1(self.xml_c108)
        c.parse_xml()
        self.assertEqual(c.pas, u'08')

    def test_c109(self):
        c = C1(self.xml_c109)
        c.parse_xml()
        self.assertEqual(c.fecha_aceptacion, u'2017-02-02')

    def test_c111(self):
        c = C1(self.xml_c111)
        c.parse_xml()
        self.assertEqual(c.fecha_activacion_prevista, u'2017-02-02')
        self.assertEqual(c.ind_bono_social, u'N')

    def test_c112(self):
        c = C1(self.xml_c112)
        c.parse_xml()
        self.assertEqual(c.fecha_rechazo, u'2017-02-02')


class test_C2(unittest.TestCase):

    def setUp(self):
        self.xml_c201_completo = open(get_data("c201.xml"), "r")
        self.xml_c202_accept = open(get_data("c202_accept.xml"), "r")
        self.xml_c203 = open(get_data("c203.xml"), "r")
        self.xml_c213 = open(get_data("c213.xml"), "r")

    def tearDown(self):
        self.xml_c201_completo.close()
        self.xml_c202_accept.close()
        self.xml_c203.close()
        self.xml_c213.close()

    def test_c201_completo(self):
        c = C2(self.xml_c201_completo)
        c.parse_xml()
        # Datos Solicitud
        self.assertEqual(c.datos_solicitud.cnae, u'2222')
        self.assertEqual(c.datos_solicitud.contratacion_incondicional_ps, u'S')
        self.assertEqual(c.datos_solicitud.fecha_prevista_accion, u'2016-06-06')
        self.assertEqual(c.datos_solicitud.ind_activacion, u'L')
        self.assertEqual(c.datos_solicitud.tipo_modificacion, u'S')
        self.assertEqual(c.datos_solicitud.tipo_solicitud_administrativa, u'S')
        self.assertEqual(c.datos_solicitud.contratacion_incondicional_bs, u'N')
        self.assertEqual(c.datos_solicitud.bono_social, u'0')
        self.assertEqual(c.datos_solicitud.solicitud_tension, u'S')
        self.assertEqual(c.datos_solicitud.tension_solicitada, u'02')
        # Contrato
        contrato = c.contrato
        contacto = contrato.contacto
        self.assertEqual(contacto.correo_electronico, u'email@host')
        self.assertEqual(contacto.persona_de_contacto, u'Nombre Inventado')
        self.assertEqual(len(contacto.telefonos), 2)
        self.assertEqual(contacto.telefonos[1][1], u'666777999')
        self.assertEqual(contacto.telefonos[1][0], u'34')
        self.assertEqual(contrato.fecha_finalizacion, u'2018-01-01')
        self.assertEqual(contrato.modo_control_potencia, u'1')
        self.assertEqual(contrato.periodicidad_facturacion, u'01')
        self.assertEqual(contrato.consumo_anual_estimado, u'5000')
        pots = contrato.potencias_contratadas
        self.assertEqual(len(pots), 2)
        self.assertEqual(pots[0][1], 1000)
        self.assertEqual(pots[1][1], 2000)
        self.assertEqual(contrato.tarifa_atr, u'003')
        self.assertEqual(contrato.tipo_autoconsumo, u'00')
        self.assertEqual(contrato.tipo_contrato_atr, u'02')
        # Cliente
        cliente = c.cliente
        self.assertEqual(cliente.correo_electronico, u'email@host')
        self.assertEqual(cliente.identificador, u'B36385870')
        self.assertEqual(cliente.indicador_tipo_direccion, u'F')
        self.assertEqual(cliente.nombre, u'ACC Y COMP DE COCINA MILLAN Y MUÑOZ')
        self.assertEqual(cliente.razon_social, u'ACC Y COMP DE COCINA MILLAN Y MUÑOZ')
        self.assertEqual(len(cliente.telefonos), 3)
        self.assertEqual(cliente.telefonos[0][1], u'666777666')
        self.assertEqual(cliente.telefonos[0][0], u'36')
        self.assertEqual(cliente.telefonos[2][1], u'666777888')
        self.assertEqual(cliente.telefonos[2][0], u'38')
        self.assertEqual(cliente.tipo_identificador, u'NI')
        self.assertEqual(cliente.tipo_persona, u'J')
        direccion = cliente.direccion
        self.assertEqual(direccion.aclarador_finca, u'Bloque de Pisos')
        self.assertEqual(direccion.calle, u'MELA MUTERMILCH')
        self.assertEqual(direccion.cod_postal, u'17001')
        self.assertEqual(direccion.duplicador_finca, u'')
        self.assertEqual(direccion.escalera, u'')
        self.assertEqual(direccion.municipio, u'17079')
        self.assertEqual(direccion.numero_finca, u'2')
        self.assertEqual(direccion.pais, u'España')
        self.assertEqual(direccion.piso, u'001')
        self.assertEqual(direccion.poblacion, u'17079000501')
        self.assertEqual(direccion.provincia, u'17')
        self.assertEqual(direccion.puerta, u'001')
        self.assertEqual(direccion.tipo_aclarador_finca, u'BI')
        self.assertEqual(direccion.tipo_via, u'PZ')
        # Medida
        medida = c.medida
        self.assertEqual(medida.propiedad_equipo, u'C')
        self.assertEqual(medida.tipo_equipo_medida, u'L00')
        mod = medida.modelos_aparato
        self.assertEqual(len(mod), 2)
        mod1 = mod[0]
        mod2 = mod[1]
        self.assertEqual(mod1.marca_aparato, u'132')
        self.assertEqual(mod1.modelo_marca, u'011')
        self.assertEqual(mod1.tipo_aparato, u'CG')
        self.assertEqual(mod2.marca_aparato, u'132')
        self.assertEqual(mod2.modelo_marca, u'012')
        self.assertEqual(mod2.tipo_aparato, u'CG')
        # Datos CIE
        datos_cie = c.doc_tecnica.datos_cie
        self.assertFalse(datos_cie.cie_electronico)
        self.assertEqual(datos_cie.validez_cie, u'ES')
        cie_p = datos_cie.cie_papel
        self.assertEqual(cie_p.codigo_cie, u'1234567')
        self.assertFalse(cie_p.codigo_instalador)
        self.assertFalse(cie_p.fecha_caducidad_cie)
        self.assertEqual(cie_p.fecha_emision_cie, u'2015-06-04')
        self.assertEqual(cie_p.nif_instalador, u'12345678Z')
        self.assertEqual(cie_p.potencia_inst_bt, u'3500')
        self.assertEqual(cie_p.potencia_no_interrumpible, u'2000')
        self.assertEqual(cie_p.tension_suministro_cie, u'10')
        self.assertEqual(cie_p.tipo_suministro, u'VI')
        # Datos APM
        datos_apm = c.doc_tecnica.datos_apm
        self.assertEqual(datos_apm.codigo_apm, u'1111111111')
        self.assertEqual(datos_apm.codigo_instalador, u'0550')
        self.assertEqual(datos_apm.fecha_caducidad_apm, u'2016-06-04')
        self.assertEqual(datos_apm.fecha_emision_apm, u'2015-06-04')
        self.assertFalse(datos_apm.nif_instalador)
        self.assertEqual(datos_apm.potencia_inst_at, u'5000')
        self.assertEqual(datos_apm.tension_suministro_apm, u'20')
        # Comentarios
        self.assertEqual(c.comentarios, u'Comentario')
        self.assertFalse(c.registros_documento)

    def test_c202_accept(self):
        c = C2(self.xml_c202_accept)
        c.parse_xml()
        # Datos Aceptacion
        self.assertEqual(c.datos_aceptacion.fecha_aceptacion, u'2016-06-06')
        self.assertEqual(c.datos_aceptacion.potencia_actual, u'5000')
        self.assertEqual(c.datos_aceptacion.actuacion_campo, u'S')
        self.assertEqual(c.datos_aceptacion.fecha_ultima_lectura_firme, u'2016-06-01')
        self.assertEqual(c.datos_aceptacion.bono_social, u'1')
        # Contrato
        self.assertEqual(c.contrato.tipo_contrato_atr, u'02')
        self.assertEqual(c.contrato.tipo_activacion_prevista, u'C0')
        self.assertEqual(c.contrato.fecha_activacion_prevista, u'2016-07-06')
        self.assertEqual(c.contrato.tarifa_atr, u'003')
        self.assertEqual(c.contrato.modo_control_potencia, u'1')
        pots = c.contrato.potencias_contratadas
        self.assertEqual(len(pots), 2)
        self.assertEqual(pots[0][1], 1000)
        self.assertEqual(pots[1][1], 2000)

    def test_c203(self):
        c = C2(self.xml_c203)
        c.parse_xml()
        self.assertEqual(c.fecha_incidencia, u'2016-07-21')
        self.assertEqual(c.fecha_prevista_accion, u'2016-07-22')
        incidencies = c.incidencias
        self.assertEqual(len(incidencies), 2)
        i1 = incidencies[0]
        i2 = incidencies[1]
        self.assertEqual(i1.codigo_motivo, u'01')
        self.assertEqual(i1.secuencial, u'1')
        self.assertEqual(i1.comentarios, u'Com 1')
        self.assertEqual(i2.codigo_motivo, u'08')
        self.assertEqual(i2.secuencial, u'2')
        self.assertEqual(i2.comentarios, u'Com 2')

    def test_c213(self):
        c = C2(self.xml_c213)
        c.parse_xml()
        self.assertEqual(c.contestacion_incidencia, u'02')
        con = c.contacto
        self.assertEqual(con.persona_de_contacto, u'Nombre Inventado')
        self.assertEqual(con.correo_electronico, u'mail_falso@dominio.com')
        tels = con.telefonos
        self.assertEqual(len(tels), 1)
        self.assertEqual(tels[0][0], u'34')
        self.assertEqual(tels[0][1], u'683834841')


class test_A1(unittest.TestCase):

    def setUp(self):
        self.xml_a101 = open(get_data("a101.xml"), "r")
        self.xml_a102_accept = open(get_data("a102_accept.xml"), "r")
        self.xml_a102_reject = open(get_data("a102_reject.xml"), "r")

    def tearDown(self):
        self.xml_a101.close()
        self.xml_a102_accept.close()
        self.xml_a102_reject.close()

    def test_a101(self):
        a1 = A1(self.xml_a101)
        a1.parse_xml()

        self.assertEqual(a1.movimiento, u'A')
        autoconsumo = a1.autoconsumo
        self.assertEqual(autoconsumo.cau, u'ES1234000000000001JN0FA001')
        self.assertEqual(autoconsumo.seccion_registro, u'1')
        # self.assertEqual(autoconsumo.sub_seccion, u'a0')
        self.assertEqual(autoconsumo.colectivo, u'S')
        # Suministros
        # Suministro 1
        suministro = a1.datos_suministro[0]
        self.assertEqual(suministro.cups, u'ES1234000000000001JN0F')
        self.assertEqual(suministro.tipo_cups, u'01')
        self.assertEqual(suministro.ref_catastro, u'1234567890qwertyuiop')
        # Suministro 2
        suministro = a1.datos_suministro[1]
        self.assertEqual(suministro.cups, u'ES1234000000000002JN0F')
        self.assertEqual(suministro.tipo_cups, u'01')
        self.assertEqual(suministro.ref_catastro, u'1234567890qwertyuiop')
        # Suministro 3
        suministro = a1.datos_suministro[2]
        self.assertEqual(suministro.cups, u'ES1234000000000003JN0F')
        self.assertEqual(suministro.tipo_cups, u'01')
        self.assertEqual(suministro.ref_catastro, u'1234567890qwertyuiop')
        # Generadores
        # Generador_1
        inst_gen = a1.datos_inst_gen[0]
        self.assertEqual(inst_gen.cil, u'ES1234000000000001JN0F001')
        self.assertEqual(inst_gen.tec_generador, u'b12')
        self.assertEqual(inst_gen.combustible, u'Diesel')
        self.assertEqual(inst_gen.pot_instalada_gen, u'100')
        self.assertEqual(inst_gen.tipo_instalacion, u'01')
        self.assertEqual(inst_gen.esquema_medida, u'B')
        self.assertEqual(inst_gen.ssaa, u'S')
        self.assertEqual(inst_gen.ref_catastro, u'1234567890qwertyuidf')
        utm = inst_gen.utm
        self.assertEqual(utm.x, u'100')
        self.assertEqual(utm.y, u'200')
        self.assertEqual(utm.huso, u'40')
        self.assertEqual(utm.banda, u'E')
        titular = inst_gen.titular_representante_gen
        self.assertEqual(titular.id_titular.tipo_identificador, u'NI')
        self.assertEqual(titular.id_titular.identificador, u'111111111H')
        self.assertEqual(titular.nombre.nombre_de_pila, u'Juan')
        self.assertEqual(titular.nombre.primer_apellido, u'López')
        self.assertEqual(titular.nombre.segundo_apellido, u'Sánchez')
        self.assertEqual(titular.telefono[0][0], u'0034')
        self.assertEqual(titular.telefono[0][1], u'933834841')
        self.assertEqual(titular.correo_electronico, u'mail_falso@dominio.com')
        direccion = titular.direccion
        self.assertEqual(direccion.pais, u'España')
        self.assertEqual(direccion.provincia, u'17')
        self.assertEqual(direccion.municipio, u'171181')
        self.assertEqual(direccion.poblacion, u'17118000400')
        self.assertEqual(direccion.cod_postal, u'17230')
        self.assertEqual(direccion.tipo_via, u'CL')
        self.assertEqual(direccion.calle, u'Pau Casals')
        self.assertEqual(direccion.numero_finca, u'18')
        self.assertEqual(direccion.duplicador_finca, u'1')
        self.assertEqual(direccion.escalera, u'D')
        self.assertEqual(direccion.piso, u'3')
        self.assertEqual(direccion.puerta, u'2')
        self.assertEqual(direccion.tipo_aclarador_finca, u'BI')
        self.assertEqual(direccion.aclarador_finca, u'Bar')
        self.assertEqual(a1.comentarios, u'Esto es un comentario')
        # Generador 2
        inst_gen = a1.datos_inst_gen[1]
        self.assertEqual(inst_gen.cil, u'ES1234000000000002JN0F001')
        self.assertEqual(inst_gen.tec_generador, u'b11')
        self.assertEqual(inst_gen.combustible, u'')
        self.assertEqual(inst_gen.pot_instalada_gen, u'100')
        self.assertEqual(inst_gen.tipo_instalacion, u'01')
        self.assertEqual(inst_gen.esquema_medida, u'B')
        self.assertEqual(inst_gen.ssaa, u'S')
        self.assertEqual(inst_gen.ref_catastro, u'1234567890qwertyuidf')
        self.assertEqual(a1.comentarios, u'Esto es un comentario')

    def test_a102_accept(self):
        a1 = A1(self.xml_a102_accept)
        a1.parse_xml()

        self.assertEqual(a1.cau, u'ES1234000000000001JN0FA001')
        self.assertEqual(a1.comentarios, u'Esto es un comentario')

    def test_a102_reject(self):
        a1 = A1(self.xml_a102_reject)
        a1.parse_xml()

        self.assertEqual(a1.cau, u'ES1234000000000001JN0FA001')
        self.assertEqual(a1.comentarios, u'Esto es un comentario')
        rechazos = a1.rechazos
        self.assertEqual(len(rechazos.rechazo), 3)
        self.assertEqual(rechazos.fecha_rechazo, u'2016-06-08')
        # Rechazo 1
        rechazo1 = rechazos.rechazo[0]
        self.assertEqual(rechazo1.secuencial, u'00')
        self.assertEqual(rechazo1.codigo_motivo, u'01')
        self.assertEqual(rechazo1.comentarios, u'Comentario del rechazo')
        # Rechazo 2
        rechazo2 = rechazos.rechazo[1]
        self.assertEqual(rechazo2.secuencial, u'00')
        self.assertEqual(rechazo2.codigo_motivo, u'F1')
        self.assertEqual(rechazo2.comentarios, u'Comentario del rechazo')
        # Rechazo 3
        rechazo3 = rechazos.rechazo[2]
        self.assertEqual(rechazo3.secuencial, u'00')
        self.assertEqual(rechazo3.codigo_motivo, u'F4')
        self.assertEqual(rechazo3.comentarios, u'Comentario del rechazo')


class test_A3(unittest.TestCase):

    def setUp(self):
        self.xml_a301 = open(get_data("a301.xml"), "r")
        self.xml_a301_correos = open(get_data("a301_correos.xml"), "r")
        self.xml_a313 = open(get_data("a313.xml"), "r")

    def tearDown(self):
        self.xml_a301.close()
        self.xml_a301_correos.close()

    def test_a301_completo(self):
        a3 = A3(self.xml_a301)
        a3.parse_xml()
        # Datos Solicitud
        self.assertEqual(a3.datos_solicitud.cnae, u'2222')
        self.assertEqual(a3.datos_solicitud.fecha_prevista_accion, u'2016-06-06')
        self.assertEqual(a3.datos_solicitud.ind_activacion, u'L')
        # Contrato
        contrato = a3.contrato
        contacto = contrato.contacto
        self.assertEqual(contacto.persona_de_contacto, u'Nombre Inventado')
        self.assertEqual(len(contacto.telefonos), 2)
        self.assertEqual(contacto.telefonos[1][1], u'666777999')
        self.assertEqual(contacto.telefonos[1][0], u'34')
        self.assertEqual(contrato.fecha_finalizacion, u'2018-01-01')
        self.assertEqual(contrato.modo_control_potencia, u'1')
        pots = contrato.potencias_contratadas
        self.assertEqual(len(pots), 2)
        self.assertEqual(pots[0][1], 1000)
        self.assertEqual(pots[1][1], 2000)
        self.assertEqual(contrato.tarifa_atr, u'003')
        self.assertEqual(contrato.tipo_autoconsumo, u'00')
        self.assertEqual(contrato.tipo_contrato_atr, u'02')
        self.assertEqual(contrato.consumo_anual_estimado, u'5000')
        # Cliente
        cliente = a3.cliente
        self.assertEqual(cliente.correo_electronico, u'email@host')
        self.assertEqual(cliente.identificador, u'B36385870')
        self.assertEqual(cliente.indicador_tipo_direccion, u'F')
        self.assertEqual(cliente.nombre, u'ACC Y COMP DE COCINA MILLAN Y MUÑOZ')
        self.assertEqual(cliente.razon_social, u'ACC Y COMP DE COCINA MILLAN Y MUÑOZ')
        self.assertEqual(len(cliente.telefonos), 3)
        self.assertEqual(cliente.telefonos[0][1], u'666777666')
        self.assertEqual(cliente.telefonos[0][0], u'36')
        self.assertEqual(cliente.telefonos[2][1], u'666777888')
        self.assertEqual(cliente.telefonos[2][0], u'38')
        self.assertEqual(cliente.tipo_identificador, u'NI')
        self.assertEqual(cliente.tipo_persona, u'J')
        direccion = cliente.direccion
        self.assertEqual(direccion.aclarador_finca, u'Bloque de Pisos')
        self.assertEqual(direccion.calle, u'MELA MUTERMILCH')
        self.assertEqual(direccion.cod_postal, u'17001')
        self.assertEqual(direccion.duplicador_finca, u'')
        self.assertEqual(direccion.escalera, u'')
        self.assertEqual(direccion.municipio, u'17079')
        self.assertEqual(direccion.numero_finca, u'2')
        self.assertEqual(direccion.pais, u'España')
        self.assertEqual(direccion.piso, u'001')
        self.assertEqual(direccion.poblacion, u'17079000501')
        self.assertEqual(direccion.provincia, u'17')
        self.assertEqual(direccion.puerta, u'001')
        self.assertEqual(direccion.tipo_aclarador_finca, u'BI')
        self.assertEqual(direccion.tipo_via, u'PZ')
        # Medida
        medida = a3.medida
        self.assertEqual(medida.propiedad_equipo, u'C')
        self.assertEqual(medida.tipo_equipo_medida, u'L00')
        mod = medida.modelos_aparato
        self.assertEqual(len(mod), 2)
        mod1 = mod[0]
        mod2 = mod[1]
        self.assertEqual(mod1.marca_aparato, u'132')
        self.assertEqual(mod1.modelo_marca, u'011')
        self.assertEqual(mod1.tipo_aparato, u'CG')
        self.assertEqual(mod2.marca_aparato, u'132')
        self.assertEqual(mod2.modelo_marca, u'012')
        self.assertEqual(mod2.tipo_aparato, u'CG')
        # Datos CIE
        datos_cie = a3.doc_tecnica.datos_cie
        self.assertFalse(datos_cie.cie_papel)
        self.assertEqual(datos_cie.validez_cie, u'ES')
        cie_e = datos_cie.cie_electronico
        self.assertEqual(cie_e.codigo_cie, u'1234567')
        self.assertEqual(cie_e.sello_electronico, u'11111')
        datos_apm = a3.doc_tecnica.datos_apm
        self.assertEqual(datos_apm.codigo_apm, u'1111111111')
        self.assertEqual(datos_apm.codigo_instalador, u'0550')
        self.assertEqual(datos_apm.fecha_caducidad_apm, u'2016-06-04')
        self.assertEqual(datos_apm.fecha_emision_apm, u'2015-06-04')
        self.assertFalse(datos_apm.nif_instalador)
        self.assertEqual(datos_apm.potencia_inst_at, u'5000')
        self.assertEqual(datos_apm.tension_suministro_apm, u'20')
        # Comentarios
        self.assertEqual(a3.comentarios, u'Comentario')
        self.assertFalse(a3.registros_documento)

    def test_a301_correos(self):
        a3 = A3(self.xml_a301_correos)
        a3.parse_xml()
        # Cliente
        cliente = a3.cliente
        direccion = cliente.direccion
        self.assertEqual(direccion.cod_postal, u'17001')
        self.assertEqual(direccion.municipio, u'17079')
        self.assertEqual(direccion.pais, u'España')
        self.assertEqual(direccion.poblacion, u'17079000501')
        self.assertEqual(direccion.provincia, u'17')
        self.assertEqual(direccion.apartado_de_correos, u'A1234')

    def test_a313(self):
        a = A3(self.xml_a313)
        a.parse_xml()
        self.assertEqual(a.contestacion_incidencia, u'02')
        con = a.contacto
        self.assertEqual(con.persona_de_contacto, u'Nombre Inventado')
        self.assertEqual(con.correo_electronico, u'mail_falso@dominio.com')
        tels = con.telefonos
        self.assertEqual(len(tels), 1)
        self.assertEqual(tels[0][0], u'34')
        self.assertEqual(tels[0][1], u'683834841')


class test_B1(unittest.TestCase):

    def setUp(self):
        self.xml_b101 = open(get_data("b101.xml"), "r")
        self.xml_b102_accept = open(get_data("b102_accept.xml"), "r")
        self.xml_b104_accept = open(get_data("b104_accept.xml"), "r")
        self.xml_b105 = open(get_data("b105.xml"), "r")
        self.xml_b116 = open(get_data("b116.xml"), "r")

    def tearDown(self):
        self.xml_b101.close()
        self.xml_b102_accept.close()
        self.xml_b104_accept.close()
        self.xml_b105.close()
        self.xml_b116.close()

    def test_b101(self):
        b1 = B1(self.xml_b101)
        b1.parse_xml()
        self.assertEqual(b1.datos_solicitud.ind_activacion, u'L')
        self.assertEqual(b1.datos_solicitud.motivo, u'03')
        cliente = b1.cliente
        self.assertEqual(cliente.correo_electronico, u'email@host')
        self.assertEqual(cliente.identificador, u'B36385870')
        self.assertEqual(cliente.nombre, u'ACC Y COMP DE COCINA MILLAN Y MUÑOZ')
        self.assertEqual(cliente.razon_social, u'ACC Y COMP DE COCINA MILLAN Y MUÑOZ')
        self.assertEqual(len(cliente.telefonos), 3)
        self.assertEqual(cliente.telefonos[0][1], u'666777666')
        self.assertEqual(cliente.telefonos[0][0], u'36')
        self.assertEqual(cliente.telefonos[2][1], u'666777888')
        self.assertEqual(cliente.telefonos[2][0], u'38')
        self.assertEqual(cliente.tipo_identificador, u'NI')
        self.assertEqual(cliente.tipo_persona, u'J')
        self.assertEqual(b1.iban, u'444555666')
        self.assertFalse(b1.comentarios)

    def test_b102_accept(self):
        b1 = B1(self.xml_b102_accept)
        b1.parse_xml()
        # Datos Aceptacion
        self.assertEqual(b1.datos_aceptacion.fecha_aceptacion, u'2016-06-06')
        self.assertEqual(b1.datos_aceptacion.actuacion_campo, u'S')
        self.assertEqual(b1.datos_aceptacion.tipo_activacion_prevista, u'B1')
        self.assertEqual(b1.datos_aceptacion.fecha_activacion_prevista, u'2016-06-08')
        self.assertEqual(b1.datos_aceptacion.fecha_ultima_lectura_firme, u'2016-06-01')

    def test_b104_accept(self):
        b1 = B1(self.xml_b104_accept)
        b1.parse_xml()
        self.assertEqual(b1.fecha_aceptacion, u'2017-02-02')
        self.assertEqual(b1.hora_aceptacion, u'20:05:10')

    def test_b105(self):
        b1 = B1(self.xml_b105)
        b1.parse_xml()
        # Datos Activacion Baja
        self.assertEqual(b1.datos_activacion_baja.fecha_activacion, u'2016-08-21')
        # Contrato
        self.assertEqual(b1.contrato.cod_contrato, u'00001')
        # Puntos Medida
        self.assertEqual(len(b1.puntos_medida), 1)
        pm = b1.puntos_medida[0]
        self.assertEqual(pm.cod_pm, u'ES1234000000000001JN0F')
        self.assertEqual(pm.tipo_movimiento, u'A')
        self.assertEqual(pm.tipo_pm, u'03')
        self.assertEqual(pm.cod_pm_principal, u'ES1234000000000002JN0F')
        self.assertEqual(pm.modo_lectura, u'1')
        self.assertEqual(pm.funcion, u'P')
        self.assertEqual(pm.direccion_enlace, u'39522')
        self.assertEqual(pm.direccion_punto_medida, u'000000001')
        self.assertEqual(pm.num_linea, u'12')
        self.assertEqual(pm.telefono_telemedida, u'987654321')
        self.assertEqual(pm.estado_telefono, u'1')
        self.assertEqual(pm.clave_acceso, u'0000000007')
        self.assertEqual(pm.tension_pm, u'0')
        self.assertEqual(pm.fecha_vigor, u'2003-01-01')
        self.assertEqual(pm.fecha_alta, u'2003-01-01')
        self.assertEqual(pm.fecha_baja, u'2003-02-01')
        self.assertEqual(pm.comentarios, u'Comentarios Varios')
        # Aparatos
        self.assertEqual(len(pm.aparatos), 1)
        ap = pm.aparatos[0]
        self.assertEqual(ap.cod_precinto, u'02')
        self.assertEqual(ap.constante_energia, u'1.000')
        self.assertEqual(ap.constante_maximetro, u'1.000')
        self.assertEqual(ap.funcion_aparato, u'M')
        self.assertEqual(ap.lectura_directa, u'N')
        self.assertEqual(ap.marca_aparato, u'132')
        self.assertEqual(ap.modelo_marca, u'011')
        self.assertEqual(ap.modo_medida_potencia, u'1')
        self.assertEqual(ap.num_integradores, u'18')
        self.assertEqual(ap.numero_serie, u'0000539522')
        self.assertEqual(ap.periodo_fabricacion, u'2005')
        self.assertEqual(ap.propietario, u'Desc. Propietario')
        self.assertEqual(ap.ruedas_decimales, u'02')
        self.assertEqual(ap.ruedas_enteras, u'08')
        self.assertEqual(ap.tipo_aparato, u'CG')
        self.assertEqual(ap.tipo_dhedm, u'6')
        self.assertEqual(ap.tipo_equipo_medida, u'L03')
        self.assertEqual(ap.tipo_movimiento, u'CX')
        self.assertEqual(ap.tipo_propiedad_aparato, u'1')
        # Medidas
        self.assertEqual(len(ap.medidas), 2)
        md = ap.medidas[0]
        self.assertEqual(md.anomalia, u'01')
        self.assertEqual(md.comentarios, u'Comentario sobre anomalia')
        self.assertEqual(md.fecha_lectura_firme, u'2003-01-02')
        self.assertEqual(md.magnitud_medida, u'PM')
        self.assertEqual(md.periodo, u'65')
        self.assertEqual(md.procedencia, u'30')
        self.assertEqual(md.tipo_dhedm, u'6')
        self.assertEqual(md.ultima_lectura_firme, u'6.00')
        md2 = ap.medidas[1]
        self.assertFalse(md2.anomalia)
        self.assertFalse(md2.comentarios)
        self.assertEqual(md2.fecha_lectura_firme, u'2003-01-03')

    def test_b116(self):
        b1 = B1(self.xml_b116)
        b1.parse_xml()
        self.assertEqual(b1.contestacion_incidencia, u'02')
        self.assertEqual(b1.contacto.persona_de_contacto, u'Nombre Inventado')
        self.assertEqual(b1.contacto.telefonos[0][0], u'34')
        self.assertEqual(b1.contacto.telefonos[0][1], u'683834841')
        self.assertEqual(b1.contacto.correo_electronico, u'mail_falso@dominio.com')


class test_B2(unittest.TestCase):

    def setUp(self):
        self.xml_b205 = open(get_data("b205.xml"), "r")

    def tearDown(self):
        self.xml_b205.close()

    def test_b205(self):
        b2 = B2(self.xml_b205)
        b2.parse_xml()
        # Datos Activacion Baja
        self.assertEqual(b2.datos_activacion_baja.fecha_activacion, u'2016-08-21')
        # Contrato
        self.assertEqual(b2.contrato.cod_contrato, u'00001')
        # Puntos Medida
        self.assertEqual(len(b2.puntos_medida), 1)
        pm = b2.puntos_medida[0]
        self.assertEqual(pm.cod_pm, u'ES1234000000000001JN0F')
        self.assertEqual(pm.tipo_movimiento, u'A')
        self.assertEqual(pm.tipo_pm, u'03')
        self.assertEqual(pm.cod_pm_principal, u'ES1234000000000002JN0F')
        self.assertEqual(pm.modo_lectura, u'1')
        self.assertEqual(pm.funcion, u'P')
        self.assertEqual(pm.direccion_enlace, u'39522')
        self.assertEqual(pm.direccion_punto_medida, u'000000001')
        self.assertEqual(pm.num_linea, u'12')
        self.assertEqual(pm.telefono_telemedida, u'987654321')
        self.assertEqual(pm.estado_telefono, u'1')
        self.assertEqual(pm.clave_acceso, u'0000000007')
        self.assertEqual(pm.tension_pm, u'0')
        self.assertEqual(pm.fecha_vigor, u'2003-01-01')
        self.assertEqual(pm.fecha_alta, u'2003-01-01')
        self.assertEqual(pm.fecha_baja, u'2003-02-01')
        self.assertEqual(pm.comentarios, u'Comentarios Varios')
        # Aparatos
        self.assertEqual(len(pm.aparatos), 1)
        ap = pm.aparatos[0]
        self.assertEqual(ap.cod_precinto, u'02')
        self.assertEqual(ap.constante_energia, u'1.000')
        self.assertEqual(ap.constante_maximetro, u'1.000')
        self.assertEqual(ap.funcion_aparato, u'M')
        self.assertEqual(ap.lectura_directa, u'N')
        self.assertEqual(ap.marca_aparato, u'132')
        self.assertEqual(ap.modelo_marca, u'011')
        self.assertEqual(ap.modo_medida_potencia, u'1')
        self.assertEqual(ap.num_integradores, u'18')
        self.assertEqual(ap.numero_serie, u'0000539522')
        self.assertEqual(ap.periodo_fabricacion, u'2005')
        self.assertEqual(ap.propietario, u'Desc. Propietario')
        self.assertEqual(ap.ruedas_decimales, u'02')
        self.assertEqual(ap.ruedas_enteras, u'08')
        self.assertEqual(ap.tipo_aparato, u'CG')
        self.assertEqual(ap.tipo_dhedm, u'6')
        self.assertEqual(ap.tipo_equipo_medida, u'L03')
        self.assertEqual(ap.tipo_movimiento, u'CX')
        self.assertEqual(ap.tipo_propiedad_aparato, u'1')
        # Medidas
        self.assertEqual(len(ap.medidas), 2)
        md = ap.medidas[0]
        self.assertEqual(md.anomalia, u'01')
        self.assertEqual(md.comentarios, u'Comentario sobre anomalia')
        self.assertEqual(md.fecha_lectura_firme, u'2003-01-02')
        self.assertEqual(md.magnitud_medida, u'PM')
        self.assertEqual(md.periodo, u'65')
        self.assertEqual(md.procedencia, u'30')
        self.assertEqual(md.tipo_dhedm, u'6')
        self.assertEqual(md.ultima_lectura_firme, u'6.00')
        md2 = ap.medidas[1]
        self.assertFalse(md2.anomalia)
        self.assertFalse(md2.comentarios)
        self.assertEqual(md2.fecha_lectura_firme, u'2003-01-03')


class test_M1(unittest.TestCase):

    def setUp(self):
        self.xml_m101 = open(get_data("m101.xml"), "r")

    def tearDown(self):
        self.xml_m101.close()

    def test_m101(self):
        m1 = M1(self.xml_m101)
        m1.parse_xml()
        # Datos Solicitud
        self.assertEqual(m1.datos_solicitud.cnae, u'2222')
        self.assertEqual(m1.datos_solicitud.fecha_prevista_accion, u'2016-06-06')
        self.assertEqual(m1.datos_solicitud.ind_activacion, u'L')
        self.assertEqual(m1.datos_solicitud.tipo_modificacion, u'S')
        self.assertEqual(m1.datos_solicitud.tipo_solicitud_administrativa, u'S')
        self.assertEqual(m1.datos_solicitud.periodicidad_facturacion, u'01')
        self.assertEqual(m1.datos_solicitud.bono_social, u'1')
        # Contrato
        contrato = m1.contrato
        contacto = contrato.contacto
        self.assertEqual(contacto.persona_de_contacto, u'Nombre Inventado')
        self.assertEqual(len(contacto.telefonos), 2)
        self.assertEqual(contacto.telefonos[1][1], u'666777999')
        self.assertEqual(contacto.telefonos[1][0], u'34')
        self.assertEqual(contrato.fecha_finalizacion, u'2018-01-01')
        self.assertEqual(contrato.modo_control_potencia, u'1')
        pots = contrato.potencias_contratadas
        self.assertEqual(len(pots), 2)
        self.assertEqual(pots[0][1], 1000)
        self.assertEqual(pots[1][1], 2000)
        self.assertEqual(contrato.tarifa_atr, u'003')
        self.assertEqual(contrato.tipo_autoconsumo, u'00')
        self.assertEqual(contrato.tipo_contrato_atr, u'02')
        # Cliente
        cliente = m1.cliente
        self.assertEqual(cliente.correo_electronico, u'email@host')
        self.assertEqual(cliente.identificador, u'B36385870')
        self.assertEqual(cliente.indicador_tipo_direccion, u'S')
        self.assertEqual(cliente.nombre, u'ACC Y COMP DE COCINA MILLAN Y MUÑOZ')
        self.assertEqual(cliente.razon_social,
                         u'ACC Y COMP DE COCINA MILLAN Y MUÑOZ')
        self.assertEqual(len(cliente.telefonos), 3)
        self.assertEqual(cliente.telefonos[0][1], u'666777666')
        self.assertEqual(cliente.telefonos[0][0], u'36')
        self.assertEqual(cliente.telefonos[2][1], u'666777888')
        self.assertEqual(cliente.telefonos[2][0], u'38')
        self.assertEqual(cliente.tipo_identificador, u'NI')
        self.assertEqual(cliente.tipo_persona, u'J')
        self.assertFalse(cliente.direccion)
        # Medida
        medida = m1.medida
        self.assertEqual(medida.propiedad_equipo, u'C')
        self.assertEqual(medida.tipo_equipo_medida, u'L00')
        mod = medida.modelos_aparato
        self.assertEqual(len(mod), 0)
        # DocTec
        self.assertFalse(m1.doc_tecnica)
        # Comentarios
        self.assertFalse(m1.comentarios)


class test_D1(unittest.TestCase):

    def setUp(self):
        self.xml_d101 = open(get_data("d101.xml"), "r")
        self.xml_d101_min_with_info = open(get_data("d101_min_with_info.xml"), "r")
        self.xml_d101_fully_min = open(get_data("d101_fully_min.xml"), "r")
        self.xml_d102_accept = open(get_data("d102_accept.xml"), "r")
        self.xml_d102_reject = open(get_data("d102_reject.xml"), "r")

    def tearDown(self):
        self.xml_d101.close()
        self.xml_d101_fully_min.close()
        self.xml_d101_min_with_info.close()
        self.xml_d102_accept.close()
        self.xml_d102_reject.close()

    def test_d101(self):
        d1 = D1(self.xml_d101)
        d1.parse_xml()
        self.assertEqual(d1.periodicidad_facturacion, u'01')
        self.assertEqual(d1.fecha_prevista_aplicacion_cambio_atr, u'2016-06-09')
        self.assertEqual(d1.motivo_cambio_atr_desde_distribuidora, u'01')
        info = d1.info_registro_autocons
        autoconsumo = info.autoconsumo
        self.assertEqual(autoconsumo.cau, u'ES1234000000000001JN0FA001')
        self.assertEqual(autoconsumo.seccion_registro, u'2')
        self.assertEqual(autoconsumo.sub_seccion, u'a0')
        self.assertEqual(autoconsumo.colectivo, u'S')
        suministro = info.datos_suministro
        self.assertEqual(suministro.cups, u'ES1234000000000001JN0F')
        self.assertEqual(suministro.tipo_cups, u'01')
        self.assertEqual(suministro.ref_catastro, u'1234567890qwertyuiop')
        inst_gen_1 = info.datos_inst_gen[0]
        self.assertEqual(inst_gen_1.cil, u'ES1234000000000001JN0F001')
        self.assertEqual(inst_gen_1.tec_generador, u'b12')
        self.assertEqual(inst_gen_1.combustible, u'Diesel')
        self.assertEqual(inst_gen_1.pot_instalada_gen, u'100')
        self.assertEqual(inst_gen_1.tipo_instalacion, u'01')
        self.assertEqual(inst_gen_1.esquema_medida, u'B')
        self.assertEqual(inst_gen_1.ssaa, u'S')
        self.assertEqual(inst_gen_1.ref_catastro, u'1234567890qwertyuidf')
        utm_1 = inst_gen_1.utm
        self.assertEqual(utm_1.x, u'100')
        self.assertEqual(utm_1.y, u'200')
        self.assertEqual(utm_1.huso, u'40')
        self.assertEqual(utm_1.banda, u'E')

        inst_gen_2 = info.datos_inst_gen[1]
        self.assertEqual(inst_gen_2.cil, u'ES1234000000000001JN0F002')
        self.assertEqual(inst_gen_2.tec_generador, u'b11')
        self.assertEqual(inst_gen_2.pot_instalada_gen, u'100')
        self.assertEqual(inst_gen_2.tipo_instalacion, u'01')
        self.assertEqual(inst_gen_2.esquema_medida, u'B')
        self.assertEqual(inst_gen_2.ssaa, u'S')
        self.assertEqual(inst_gen_2.ref_catastro, u'1234567890qwertyuidf')
        utm_2 = inst_gen_2.utm
        self.assertEqual(utm_2.x, u'100')
        self.assertEqual(utm_2.y, u'200')
        self.assertEqual(utm_2.huso, u'40')
        self.assertEqual(utm_2.banda, u'E')
        titular = inst_gen_1.titular_representante_gen
        self.assertEqual(titular.id_titular.tipo_identificador, u'NI')
        self.assertEqual(titular.id_titular.identificador, u'111111111H')
        self.assertEqual(titular.nombre.nombre_de_pila, u'Juan')
        self.assertEqual(titular.nombre.primer_apellido, u'López')
        self.assertEqual(titular.nombre.segundo_apellido, u'Sánchez')
        self.assertEqual(titular.telefono[0][0], u'0034')
        self.assertEqual(titular.telefono[0][1], u'933834841')
        self.assertEqual(titular.correo_electronico, u'mail_falso@dominio.com')
        direccion = titular.direccion
        self.assertEqual(direccion.pais, u'España')
        self.assertEqual(direccion.provincia, u'17')
        self.assertEqual(direccion.municipio, u'171181')
        self.assertEqual(direccion.poblacion, u'17118000400')
        self.assertEqual(direccion.cod_postal, u'17230')
        self.assertEqual(direccion.tipo_via, u'CL')
        self.assertEqual(direccion.calle, u'Pau Casals')
        self.assertEqual(direccion.numero_finca, u'18')
        self.assertEqual(direccion.duplicador_finca, u'1')
        self.assertEqual(direccion.escalera, u'D')
        self.assertEqual(direccion.piso, u'3')
        self.assertEqual(direccion.puerta, u'2')
        self.assertEqual(direccion.tipo_aclarador_finca, u'BI')
        self.assertEqual(direccion.aclarador_finca, u'Bar')
        self.assertEqual(info.comentarios, u'Esto es un comentario')

    def test_d101_min_with_info(self):
        d1 = D1(self.xml_d101_min_with_info)
        d1.parse_xml()
        self.assertEqual(d1.motivo_cambio_atr_desde_distribuidora, u'04')
        info = d1.info_registro_autocons
        autoconsumo = info.autoconsumo
        self.assertEqual(autoconsumo.cau, u'ES1234000000000001JN0FA001')
        self.assertEqual(autoconsumo.seccion_registro, u'2')
        self.assertEqual(autoconsumo.colectivo, u'S')
        suministro = info.datos_suministro
        self.assertEqual(suministro.cups, u'ES1234000000000001JN0F')
        inst_gen = info.datos_inst_gen[0]
        self.assertEqual(inst_gen.tec_generador, u'b12')
        self.assertEqual(inst_gen.pot_instalada_gen, u'100')
        self.assertEqual(inst_gen.tipo_instalacion, u'01')
        self.assertEqual(inst_gen.ssaa, u'S')
        utm = inst_gen.utm
        self.assertEqual(utm.x, u'100')
        self.assertEqual(utm.y, u'200')
        self.assertEqual(utm.huso, u'40')
        titular = inst_gen.titular_representante_gen
        self.assertEqual(titular.id_titular.tipo_identificador, u'NI')
        self.assertEqual(titular.id_titular.identificador, u'111111111H')
        self.assertEqual(titular.nombre.nombre_de_pila, u'Juan')
        self.assertEqual(titular.nombre.primer_apellido, u'López')
        self.assertEqual(titular.telefono[0][0], u'0034')
        self.assertEqual(titular.telefono[0][1], u'933834841')
        direccion = titular.direccion
        self.assertEqual(direccion.pais, u'España')
        self.assertEqual(direccion.provincia, u'17')
        self.assertEqual(direccion.municipio, u'171181')
        self.assertEqual(direccion.cod_postal, u'17230')
        self.assertEqual(direccion.tipo_via, u'CL')
        self.assertEqual(direccion.calle, u'Pau Casals')
        self.assertEqual(direccion.numero_finca, u'18')

    def test_d101_fully_min(self):
        d1 = D1(self.xml_d101_fully_min)
        d1.parse_xml()
        self.assertEqual(d1.motivo_cambio_atr_desde_distribuidora, u'01')

    def test_d102_accept(self):
        d1 = D1(self.xml_d102_accept)
        d1.parse_xml()
        # Datos Aceptacion
        self.assertEqual(d1.datos_aceptacion.fecha_aceptacion, u'2016-06-06')

    def test_d102_reject(self):
        d1 = D1(self.xml_d102_reject)
        d1.parse_xml()
        self.assertEqual(d1.fecha_rechazo, u'2016-07-20')
        self.assertEqual(len(d1.registros_documento), 2)
        doc1 = d1.registros_documento[0]
        doc2 = d1.registros_documento[1]
        self.assertEqual(doc1.tipo_doc_aportado, u'08')
        self.assertEqual(doc1.direccion_url, u'http://eneracme.com/docs/NIF11111111H.pdf')
        self.assertEqual(doc2.tipo_doc_aportado, u'07')
        self.assertEqual(doc2.direccion_url, u'http://eneracme.com/docs/NIF11111111H.pdf')
        self.assertEqual(len(d1.rechazos), 1)
        rej = d1.rechazos[0]
        self.assertEqual(rej.secuencial, u'1')
        self.assertEqual(rej.codigo_motivo, u'F1')
        self.assertEqual(rej.comentarios, u'Motiu de rebuig F1')


class test_W1(unittest.TestCase):

    def setUp(self):
        self.xml_w101 = open(get_data("w101.xml"), "r")
        self.xml_w102_accept = open(get_data("w102_accept.xml"), "r")
        self.xml_w102_reject = open(get_data("w102_reject.xml"), "r")

    def tearDown(self):
        self.xml_w101.close()
        self.xml_w102_accept.close()
        self.xml_w102_reject.close()

    def test_w101(self):
        w1 = W1(self.xml_w101)
        w1.parse_xml()
        datos = w1.datos_solicitud_aportacion_lectura
        self.assertEqual(datos.fecha_lectura, u'2015-02-18')
        self.assertEqual(datos.tipo_dhedm, u'2')
        # Lecturas
        lecturas = w1.lecturas_aportadas
        self.assertEqual(len(lecturas), 2)
        l0 = lecturas[0]
        l1 = lecturas[1]
        self.assertEqual(l0.integrador, u'AE')
        self.assertEqual(l0.tipo_codigo_periodo_dh, u'21')
        self.assertEqual(l0.lectura_propuesta, u'0000001162.00')
        self.assertEqual(l1.integrador, u'AE')
        self.assertEqual(l1.tipo_codigo_periodo_dh, u'22')
        self.assertEqual(l1.lectura_propuesta, u'0000003106.00')

    def test_w102_accept(self):
        w1 = W1(self.xml_w102_accept)
        w1.parse_xml()
        # Datos Aceptacion
        self.assertEqual(w1.datos_aceptacion_lectura.fecha_aceptacion, u'2016-06-06')

    def test_w102_reject(self):
        w1 = W1(self.xml_w102_reject)
        w1.parse_xml()
        self.assertEqual(w1.fecha_rechazo, u'2016-07-20')
        self.assertEqual(len(w1.registros_documento), 1)
        doc1 = w1.registros_documento[0]
        self.assertEqual(doc1.tipo_doc_aportado, u'08')
        self.assertEqual(doc1.direccion_url, u'http://eneracme.com/docs/NIF11111111H.pdf')
        self.assertEqual(len(w1.rechazos), 1)
        rej1 = w1.rechazos[0]
        self.assertEqual(rej1.secuencial, u'1')
        self.assertEqual(rej1.codigo_motivo, u'01')
        self.assertEqual(rej1.comentarios,  'Motiu de rebuig 01: No existe Punto de Suministro asociado al CUPS')


class test_Q1(unittest.TestCase):

    def setUp(self):
        self.xml_q101 = open(get_data("q101.xml"), "r")

    def tearDown(self):
        self.xml_q101.close()

    def test_q101(self):
        q1 = Q1(self.xml_q101)
        q1.parse_xml()
        self.assertEqual(q1.cod_pm, u'1112223334445556667779')
        models = q1.modelos_aparato
        self.assertEqual(len(models), 2)
        self.assertEqual(models[1].tipo_aparato, u'CG')
        self.assertEqual(models[1].marca_aparato, u'136')
        self.assertEqual(models[1].numero_serie, u'012')
        self.assertEqual(models[1].tipo_dhedm, u'3')
        self.assertEqual(len(models[0].integradores), 1)
        self.assertEqual(len(models[1].integradores), 2)
        int2 = models[1].integradores[1]
        self.assertEqual(int2.codigo_periodo, u'30')
        self.assertEqual(int2.constante_multiplicadora, u'1')
        self.assertEqual(int2.consumo_calculado, u'5000')
        self.assertEqual(int2.fecha_hora_maximetro, u'2014-05-18T22:13:37')
        self.assertEqual(int2.magnitud, u'R3')
        self.assertEqual(int2.numero_ruedas_decimales, u'20')
        self.assertEqual(int2.numero_ruedas_enteras, u'10')
        ld = int2.lectura_desde
        self.assertEqual(ld.fecha, u'2014-04-18')
        self.assertEqual(ld.lectura, u'500')
        self.assertEqual(ld.procedencia, u'30')
        lh = int2.lectura_hasta
        self.assertEqual(lh.fecha, u'2014-05-18')
        self.assertEqual(lh.lectura, u'1500')
        self.assertEqual(lh.procedencia, u'40')
        ajuste = int2.ajuste
        self.assertEqual(ajuste.ajuste_por_integrador, u'1500')
        self.assertEqual(ajuste.codigo_motivo_ajuste, u'01')
        self.assertEqual(ajuste.comentarios, u'Comentario Ajuste')
        anomalia = int2.anomalia
        self.assertEqual(anomalia.comentarios, u'Comentarios Anomalia')
        self.assertEqual(anomalia.tipo_anomalia, u'05')


class test_R1(unittest.TestCase):

    def setUp(self):
        self.xml_r101 = open(get_data("r101.xml"), "r")
        self.xml_r102_accept = open(get_data("r102_accept.xml"), "r")
        self.xml_r103 = open(get_data("r103.xml"), "r")
        self.xml_r103_intervenciones = open(get_data("r103_intervenciones.xml"), "r")
        self.xml_r103_no_add_info = open(get_data("r103_no_add_info.xml"), "r")
        self.xml_r104 = open(get_data("r104.xml"), "r")
        self.xml_r105 = open(get_data("r105.xml"), "r")
        self.xml_r108 = open(get_data("r108.xml"), "r")
        self.xml_r109 = open(get_data("r109.xml"), "r")
        self.xml_r109_rej = open(get_data("r109_rej.xml"), "r")

    def tearDown(self):
        self.xml_r101.close()
        self.xml_r102_accept.close()
        self.xml_r103.close()
        self.xml_r103_intervenciones.close()
        self.xml_r103_no_add_info.close()
        self.xml_r104.close()
        self.xml_r105.close()
        self.xml_r108.close()
        self.xml_r109.close()
        self.xml_r109_rej.close()

    def test_r101(self):
        r1 = R1(self.xml_r101)
        r1.parse_xml()
        # Datos Solicitud
        self.assertEqual(r1.datos_solicitud.fecha_limite, u'2016-02-22')
        self.assertEqual(r1.datos_solicitud.prioritario, u'S')
        self.assertEqual(r1.datos_solicitud.referencia_origen, u'01')
        self.assertEqual(r1.datos_solicitud.subtipo, u'003')
        self.assertEqual(r1.datos_solicitud.tipo, u'02')
        # Variables Detalle Reclamacion
        vars = r1.variables_detalle_reclamacion
        self.assertEqual(len(vars), 2)
        var1 = vars[0]
        var2 = vars[1]
        self.assertEqual(var2.num_expediente_acometida, u'22222')
        self.assertEqual(var1.codigo_incidencia, u'01')
        self.assertEqual(var1.codigo_solicitud, u'33333')
        self.assertEqual(var1.codigo_solicitud_reclamacion, u'11111')
        self.assertEqual(var1.concepto_disconformidad, u'100')
        self.assertEqual(var1.fecha_desde, u'2017-02-05')
        self.assertEqual(var1.fecha_hasta, u'2017-04-05')
        self.assertEqual(var1.fecha_incidente, u'2016-02-10')
        self.assertEqual(var1.fecha_lectura, u'2016-01-20')
        self.assertEqual(var1.iban, u'4444222211113333')
        self.assertEqual(var1.importe_reclamado, u'5000')
        self.assertEqual(var1.num_expediente_acometida, u'11111')
        self.assertEqual(var1.num_expediente_fraude, u'22222')
        self.assertEqual(var1.num_factura_atr, u'243615')
        self.assertEqual(var1.parametro_contratacion, u'01')
        self.assertEqual(var1.tipo_concepto_facturado, u'01')
        self.assertEqual(var1.tipo_de_atencion_incorrecta, u'05')
        self.assertEqual(var1.tipo_dhedm, u'1')
        ubi = var1.ubicacion_incidencia
        self.assertEqual(ubi.des_ubicacion_incidencia, u'Destino')
        self.assertEqual(ubi.cod_postal, u'17001')
        self.assertEqual(ubi.municipio, u'17079')
        self.assertEqual(ubi.poblacion, u'17079000501')
        self.assertEqual(ubi.provincia, u'17')
        cont = var1.contacto
        self.assertEqual(cont.correo_electronico, u'perico@acme.com')
        self.assertEqual(cont.persona_de_contacto, u'Perico Palotes Largos')
        self.assertEqual(cont.telefonos[1][1], u'55512345')
        self.assertEqual(cont.telefonos[1][0], u'34')
        self.assertEqual(len(var1.lecturas_aportadas), 2)
        lect1 = var1.lecturas_aportadas[0]
        self.assertEqual(lect1.codigo_periodo_dh, u'21')
        self.assertEqual(lect1.integrador, u'AE')
        self.assertEqual(lect1.lectura_propuesta, u'0000001162.00')
        # Cliente
        cli = r1.cliente
        self.assertEqual(cli.correo_electronico, u'email@host')
        self.assertEqual(cli.identificador, u'B36385870')
        self.assertEqual(cli.indicador_tipo_direccion, u'F')
        self.assertEqual(cli.razon_social, u'ACC Y COMP DE COCINA MILLAN Y MUÑOZ')
        self.assertEqual(cli.segundo_apellido, u'')
        self.assertEqual(cli.telefonos[0][1], u'666777666')
        self.assertEqual(cli.telefonos[0][0], u'36')
        self.assertEqual(cli.tipo_identificador, u'NI')
        self.assertEqual(cli.tipo_persona, u'J')
        direccion = cli.direccion
        self.assertEqual(direccion.aclarador_finca, u'Bloque de Pisos')
        self.assertEqual(direccion.calle, u'MELA MUTERMILCH')
        self.assertEqual(direccion.cod_postal, u'17001')
        self.assertEqual(direccion.duplicador_finca, u'')
        self.assertEqual(direccion.escalera, u'')
        self.assertEqual(direccion.municipio, u'17079')
        self.assertEqual(direccion.numero_finca, u'2')
        self.assertEqual(direccion.pais, u'España')
        self.assertEqual(direccion.piso, u'001')
        self.assertEqual(direccion.poblacion, u'17079000501')
        self.assertEqual(direccion.provincia, u'17')
        self.assertEqual(direccion.puerta, u'001')
        self.assertEqual(direccion.tipo_aclarador_finca, u'BI')
        self.assertEqual(direccion.tipo_via, u'PZ')
        # Reclamante
        self.assertEqual(r1.tipo_reclamante, u'01')
        rec = r1.reclamante
        self.assertEqual(rec.correo_electronico, u'email@host')
        self.assertEqual(rec.identificador, u'B36385870')
        self.assertEqual(rec.razon_social, u'ACC Y COMP DE COCINA MILLAN Y MUÑOZ')
        self.assertEqual(rec.segundo_apellido, u'')
        self.assertEqual(rec.telefonos[2][1], u'666777555')
        self.assertEqual(rec.telefonos[2][0], u'34')
        self.assertEqual(rec.tipo_identificador, u'NI')
        # Comentarios
        self.assertEqual(r1.comentarios, u'no calcula sus consumos desea revisio y facturas')

    def test_r102_accept(self):
        r1 = R1(self.xml_r102_accept)
        r1.parse_xml()
        # Datos Aceptacion
        self.assertEqual(r1.datos_aceptacion.fecha_aceptacion, u'2016-06-06')
        self.assertEqual(r1.datos_aceptacion.codigo_reclamacion_distribuidora, u'1234')

    def test_r103(self):
        r1 = R1(self.xml_r103)
        r1.parse_xml()
        # Datos Informacion
        di = r1.datos_informacion
        self.assertEqual(di.codigo_reclamacion_distribuidora, u'12345678')
        self.assertEqual(di.num_expediente_acometida, u'1111122222')
        self.assertEqual(di.tipo_comunicacion, u'01')
        # Informacion Intermedia
        info = r1.informacion_intermedia
        self.assertEqual(info.desc_informacion_intermedia, u'Descripcion de la informacion intermedia aportada.')
        self.assertEqual(len(info.intervenciones), 0)
        # Retipificacion
        ret = r1.retipificacion
        self.assertEqual(ret.desc_retipificacion, u'descripcio de la retipificacio.')
        self.assertEqual(ret.subtipo, u'003')
        self.assertEqual(ret.tipo, u'02')
        # Solicitudes Informacion Adicional
        sol = r1.solicitudes_informacion_adicional
        self.assertEqual(len(sol), 2)
        sol1 = sol[0]
        sol2 = sol[1]
        self.assertEqual(sol1.desc_peticion_informacion, u'Descripcion de la peticion.')
        self.assertEqual(sol1.fecha_limite_envio, u'2016-07-10')
        self.assertEqual(sol1.tipo_informacion_adicional, u'01')
        self.assertEqual(sol2.desc_peticion_informacion, u'Descripcion de la peticion.')
        self.assertEqual(sol2.fecha_limite_envio, u'2016-07-10')
        self.assertEqual(sol2.tipo_informacion_adicional, u'02')
        sol_ret = r1.solicitud_informacion_adicional_para_retipificacion
        self.assertEqual(sol_ret.fecha_limite_envio, u'2016-08-10')
        self.assertEqual(sol_ret.subtipo, u'003')
        self.assertEqual(sol_ret.tipo, u'03')
        # Comentarios
        self.assertEqual(r1.comentarios, u'R1 03.')
        # Parametros Comunicacion
        self.assertEqual(r1.parametros_comunicacion[0].cod_pm, u'1234567890123456789012')
        self.assertEqual(r1.parametros_comunicacion[0].cod_pm_principal, u'1234567890123456789012')
        self.assertEqual(r1.parametros_comunicacion[0].funcion, u'P')
        self.assertEqual(r1.parametros_comunicacion[0].direccion_enlace, u'a1b2c3d4e5')
        self.assertEqual(r1.parametros_comunicacion[0].num_linea, u'2')
        self.assertEqual(r1.parametros_comunicacion[0].telefono_telemedida, u'999888444333')
        self.assertEqual(r1.parametros_comunicacion[0].telefono_velocidad_comunicacion, u'20')
        self.assertEqual(r1.parametros_comunicacion[0].telefono_bit_datos, u'1')
        self.assertEqual(r1.parametros_comunicacion[0].telefono_paridad, u'0')
        self.assertEqual(r1.parametros_comunicacion[0].telefono_bit_stop, u'1')
        # Intervenciones
        r1_int = R1(self.xml_r103_intervenciones)
        r1_int.parse_xml()
        intv = r1_int.informacion_intermedia.intervenciones
        self.assertEqual(len(intv), 2)
        intv1 = intv[0]
        intv2 = intv[1]
        self.assertEqual(intv1.detalle_resultado, u'Descripcion de los resultados obtenidos.')
        self.assertEqual(intv1.fecha, u'2016-06-10')
        self.assertEqual(intv1.hora_desde, u'08:00:00')
        self.assertEqual(intv1.hora_hasta, u'09:00:00')
        self.assertEqual(intv1.numero_visita, u'10')
        self.assertEqual(intv1.resultado, u'001')
        self.assertEqual(intv1.tipo_intervencion, u'01')
        self.assertEqual(intv2.detalle_resultado, u'Descripcion de los resultados obtenidos.')
        self.assertEqual(intv2.fecha, u'2016-06-10')
        self.assertEqual(intv2.hora_desde, u'08:00:00')
        self.assertEqual(intv2.hora_hasta, u'09:00:00')
        self.assertEqual(intv2.numero_visita, u'10')
        self.assertEqual(intv2.resultado, u'001')
        self.assertEqual(intv2.tipo_intervencion, u'02')

        # Sin Informacion Adicional
        r1_noadd = R1(self.xml_r103_no_add_info)
        r1_noadd.parse_xml()
        dinfo = r1_noadd.datos_informacion
        self.assertEqual(dinfo.tipo_comunicacion, u'04')
        self.assertEqual(dinfo.codigo_reclamacion_distribuidora, u'12345678')
        sols = r1_noadd.solicitudes_informacion_adicional
        self.assertEqual(len(sols), 0)
        retip = r1_noadd.solicitud_informacion_adicional_para_retipificacion
        self.assertEqual(retip.tipo, u'02')
        self.assertEqual(retip.subtipo, u'004')
        self.assertEqual(retip.fecha_limite_envio, u'2019-06-19')
        self.assertEqual(
            r1_noadd.comentarios, u'Solicitud de datos para la retipificación'
        )

    def test_r104(self):
        r1 = R1(self.xml_r104)
        r1.parse_xml()
        # Datos Envio Informacion
        datos_envio = r1.datos_envio_informacion
        self.assertEqual(datos_envio.fecha_informacion, u'2016-01-20')
        self.assertEqual(datos_envio.num_expediente_acometida, u'0123456789ABCD')
        # Variables Aportacion informacion
        varsi = r1.variables_aportacion_informacion
        self.assertEqual(len(varsi), 2)
        vari1 = varsi[0]
        vari2 = varsi[1]
        self.assertEqual(vari1.desc_peticion_informacion, u'Informacio per fer testos.')
        self.assertEqual(vari1.tipo_informacion, u'01')
        self.assertEqual(vari1.valor, u'125')
        self.assertEqual(vari1.variable, u'01')
        self.assertFalse(vari2.desc_peticion_informacion)
        self.assertEqual(vari2.tipo_informacion, u'02')
        self.assertFalse(vari2.valor)
        self.assertFalse(vari2.variable)
        # Variables Aportacion Informacion Para Retipificacion
        varsr = r1.variables_aportacion_informacion_para_retipificacion
        self.assertEqual(len(varsr), 1)
        varr1 = varsr[0]
        self.assertEqual(varr1.codigo_incidencia, u'01')
        self.assertEqual(varr1.codigo_solicitud, u'33333')
        self.assertEqual(varr1.codigo_solicitud_reclamacion, u'11111')
        self.assertEqual(varr1.concepto_disconformidad, u'100')
        self.assertEqual(varr1.fecha_desde, u'2017-02-05')
        self.assertEqual(varr1.fecha_hasta, u'2017-04-05')
        self.assertEqual(varr1.fecha_incidente, u'2016-02-10')
        self.assertEqual(varr1.fecha_lectura, u'2016-01-20')
        self.assertEqual(varr1.iban, u'4444222211113333')
        self.assertEqual(varr1.importe_reclamado, u'5000')
        self.assertEqual(varr1.num_expediente_acometida, u'11111')
        self.assertEqual(varr1.num_expediente_fraude, u'22222')
        self.assertEqual(varr1.num_factura_atr, u'243615')
        self.assertEqual(varr1.parametro_contratacion, u'01')
        self.assertEqual(varr1.tipo_concepto_facturado, u'01')
        self.assertEqual(varr1.tipo_de_atencion_incorrecta, u'05')
        self.assertEqual(varr1.tipo_dhedm, u'1')
        ubi = varr1.ubicacion_incidencia
        self.assertEqual(ubi.des_ubicacion_incidencia, u'Destino')
        self.assertEqual(ubi.cod_postal, u'17001')
        self.assertEqual(ubi.municipio, u'17079')
        self.assertEqual(ubi.poblacion, u'17079000501')
        self.assertEqual(ubi.provincia, u'17')
        cont = varr1.contacto
        self.assertEqual(cont.correo_electronico, u'perico@acme.com')
        self.assertEqual(cont.persona_de_contacto, u'Perico Palotes Largos')
        self.assertEqual(cont.telefonos[1][1], u'55512345')
        self.assertEqual(cont.telefonos[1][0], u'34')
        self.assertEqual(len(varr1.lecturas_aportadas), 2)
        lect1 = varr1.lecturas_aportadas[0]
        self.assertEqual(lect1.codigo_periodo_dh, u'21')
        self.assertEqual(lect1.integrador, u'AE')
        self.assertEqual(lect1.lectura_propuesta, u'0000001162.00')
        # Cliente
        cli = r1.cliente
        self.assertEqual(cli.correo_electronico, u'email@host')
        self.assertEqual(cli.identificador, u'B36385870')
        self.assertEqual(cli.indicador_tipo_direccion, u'F')
        self.assertEqual(cli.razon_social, u'ACC Y COMP DE COCINA MILLAN Y MUÑOZ')
        self.assertEqual(cli.segundo_apellido, u'')
        self.assertEqual(cli.telefonos[0][1], u'666777666')
        self.assertEqual(cli.telefonos[0][0], u'36')
        self.assertEqual(cli.tipo_identificador, u'NI')
        self.assertEqual(cli.tipo_persona, u'J')
        direccion = cli.direccion
        self.assertEqual(direccion.aclarador_finca, u'Bloque de Pisos')
        self.assertEqual(direccion.calle, u'MELA MUTERMILCH')
        self.assertEqual(direccion.cod_postal, u'17001')
        self.assertEqual(direccion.duplicador_finca, u'')
        self.assertEqual(direccion.escalera, u'')
        self.assertEqual(direccion.municipio, u'17079')
        self.assertEqual(direccion.numero_finca, u'2')
        self.assertEqual(direccion.pais, u'España')
        self.assertEqual(direccion.piso, u'001')
        self.assertEqual(direccion.poblacion, u'17079000501')
        self.assertEqual(direccion.provincia, u'17')
        self.assertEqual(direccion.puerta, u'001')
        self.assertEqual(direccion.tipo_aclarador_finca, u'BI')
        self.assertEqual(direccion.tipo_via, u'PZ')
        # Comentarios
        self.assertEqual(r1.comentarios, u'R104 test with VariablesAportacionInformacion.')
        # Registros Documento
        self.assertEqual(len(r1.registros_documento), 3)
        doc1 = r1.registros_documento[0]
        doc2 = r1.registros_documento[1]
        doc3 = r1.registros_documento[2]
        self.assertEqual(doc1.tipo_doc_aportado, u'01')
        self.assertEqual(doc1.direccion_url, u'http://eneracme.com/docs/CIE0100001.pdf')
        self.assertEqual(doc2.tipo_doc_aportado, u'06')
        self.assertEqual(doc2.direccion_url, u'http://eneracme.com/docs/INV201509161234.pdf')
        self.assertEqual(doc3.tipo_doc_aportado, u'08')
        self.assertEqual(doc3.direccion_url, u'http://eneracme.com/docs/NIF11111111H.pdf')

    def test_r105(self):
        r1 = R1(self.xml_r105)
        r1.parse_xml()
        # Datos Cierre
        dc = r1.datos_cierre
        self.assertEqual(dc.codigo_reclamacion_distribuidora, u'3291970')
        self.assertEqual(dc.detalle_resultado, u'0010101')
        self.assertEqual(dc.fecha, u'2016-04-12')
        self.assertEqual(dc.fecha_movimiento, u'2016-04-12')
        self.assertEqual(dc.hora, u'16:02:25')
        self.assertEqual(dc.indemnizacion_abonada, u'0.0')
        self.assertEqual(dc.num_expediente_acometida, u'11111')
        self.assertEqual(dc.num_expediente_anomalia_fraude, u'22222')
        self.assertEqual(dc.observaciones, u'Observaciones generales')
        self.assertEqual(dc.resultado_reclamacion, u'02')
        self.assertEqual(dc.subtipo, u'013')
        self.assertEqual(dc.tipo, u'03')
        self.assertEqual(r1.parametros_comunicacion[0].direccion_enlace, u'a1b2c3d4e5')
        self.assertEqual(r1.parametros_comunicacion[0].num_linea, u'2')
        self.assertEqual(r1.parametros_comunicacion[0].ip_direccion, u'0.0.0.0')
        self.assertEqual(r1.parametros_comunicacion[0].ip_puerto_enlace, u'8080')

        # Cod Contrato
        self.assertEqual(r1.cod_contrato, u'383922379')

    def test_r108(self):
        c = R1(self.xml_r108)
        c.parse_xml()
        self.assertEqual(c.pas, u'08')

    def test_r109(self):
        c = R1(self.xml_r109)
        c.parse_xml()
        self.assertEqual(c.fecha_aceptacion, u'2017-02-03')

    def test_r109_reject(self):
        d1 = R1(self.xml_r109_rej)
        d1.parse_xml()
        self.assertEqual(d1.fecha_rechazo, u'2016-07-20')
        self.assertEqual(len(d1.registros_documento), 2)
        doc1 = d1.registros_documento[0]
        doc2 = d1.registros_documento[1]
        self.assertEqual(doc1.tipo_doc_aportado, u'08')
        self.assertEqual(doc1.direccion_url, u'http://eneracme.com/docs/NIF11111111H.pdf')
        self.assertEqual(doc2.tipo_doc_aportado, u'07')
        self.assertEqual(doc2.direccion_url, u'http://eneracme.com/docs/NIF11111111H.pdf')
        self.assertEqual(len(d1.rechazos), 1)
        rej = d1.rechazos[0]
        self.assertEqual(rej.secuencial, u'1')
        self.assertEqual(rej.codigo_motivo, u'F1')
        self.assertEqual(rej.comentarios, u'Motiu de rebuig F1')


class test_F1(unittest.TestCase):
    def setUp(self):
        with open(get_data("f101_factura_atr.xml"), "r") as f:
            self.xml_f101_atr_invoice = f.read()
        with open(get_data("f101_factura_atr_30A.xml"), "r") as f:
            self.xml_f101_atr_invoice_30A = f.read()
        with open(get_data("f101_factura_atr_61B_exceso.xml"), "r") as f:
            self.xml_f101_atr_invoice_61B = f.read()
        with open(get_data("f101_factura_atr_ajuste.xml"), "r") as f:
            self.xml_f101_atr_invoice_ajuste = f.read()
        with open(get_data("f101_factura_atr_empty_periods.xml"), "r") as f:
            self.xml_f101_atr_invoice_empty_periods = f.read()
        with open(get_data("f101_factura_otros.xml"), "r") as f:
            self.xml_f101_other_invoice = f.read()
        with open(get_data("f101_spaces.xml"), "r") as f:
            self.xml_f101_spaces = f.read()
        with open(get_data("f101_factura_atr_free_interpretation.xml"), "r") as f:
            self.xml_f101_free_interpretation = f.read()
        with open(get_data("f101_factura_empty_rent.xml"), "r") as f:
            self.xml_f101_empty_rent = f.read()
        with open(get_data("F1_periodos_DH.xml"), "r") as f:
            self.xml_f101_integradores_dh = f.read()

    def testATRInvoice(self):
        f1 = F1(self.xml_f101_atr_invoice)
        f1.parse_xml()

        self.assertEqual(f1.otras_facturas, [])
        self.assertEqual(len(f1.facturas_atr), 1)

        fact = f1.facturas_atr[0]

        datos_factura = fact.datos_factura

        direccion_suministro = datos_factura.direccion_suministro

        self.assertEqual(direccion_suministro.pais, u'España')
        self.assertEqual(direccion_suministro.provincia, u'17')
        self.assertEqual(direccion_suministro.municipio, u'17079')
        self.assertEqual(direccion_suministro.cod_postal, u'17003')
        self.assertEqual(direccion_suministro.calle, u'Nom carrer')
        self.assertEqual(direccion_suministro.numero_finca, u'3')
        self.assertEqual(direccion_suministro.escalera, u'1')
        self.assertEqual(direccion_suministro.piso, u'1')
        self.assertEqual(direccion_suministro.puerta, u'1')

        cliente = datos_factura.cliente

        self.assertEqual(cliente.tipo_identificador, u'NI')
        self.assertEqual(cliente.identificador, u'70876712G')
        self.assertEqual(cliente.tipo_persona, u'F')

        self.assertEqual(datos_factura.cod_contrato, u'111111')
        self.assertEqual(datos_factura.codigo_fiscal_factura, u'F0001')
        self.assertEqual(datos_factura.tipo_factura, u'N')
        self.assertEqual(datos_factura.motivo_facturacion, u'01')
        self.assertEqual(datos_factura.fecha_factura, u'2017-05-01')
        self.assertEqual(datos_factura.identificador_emisora, u'B11254455')
        self.assertEqual(datos_factura.comentarios, u'.')
        self.assertEqual(datos_factura.importe_total_factura, 100)
        self.assertEqual(datos_factura.saldo_factura, 100)
        self.assertEqual(datos_factura.tipo_moneda, u'02')
        self.assertEqual(datos_factura.fecha_boe, u'2016-01-01')
        self.assertEqual(datos_factura.tarifa_atr_fact, u'001')
        self.assertEqual(datos_factura.modo_control_potencia, u'1')
        self.assertEqual(datos_factura.marca_medida_con_perdidas, u'N')
        self.assertEqual(datos_factura.indicativo_curva_carga, u'02')
        self.assertEqual(datos_factura.fecha_desde_factura, u'2017-03-31')
        self.assertEqual(datos_factura.fecha_hasta_factura, u'2017-04-30')
        self.assertEqual(datos_factura.numero_dias, 30)

        potencia = fact.potencia

        terminos_potencia = potencia.terminos_potencia
        self.assertEqual(len(terminos_potencia), 1)
        termino_potencia = terminos_potencia[0]

        self.assertEqual(termino_potencia.fecha_desde, u'2017-03-31')
        self.assertEqual(termino_potencia.fecha_hasta, u'2017-04-30')

        periodos_potencia = termino_potencia.periodos
        self.assertEqual(len(periodos_potencia), 1)
        periodo_potencia = periodos_potencia[0]

        self.assertDictEqual(
            termino_potencia.get_contracted_periods_by_period(),
            {'P1': 1000}
        )

        self.assertEqual(periodo_potencia.potencia_contratada, 1000)
        self.assertEqual(periodo_potencia.potencia_max_demandada, 1000)
        self.assertEqual(periodo_potencia.potencia_a_facturar, 1000)
        self.assertEqual(periodo_potencia.cantidad, 1000)
        self.assertEqual(periodo_potencia.precio, 0.05)
        self.assertEqual(periodo_potencia.nombre, u'P1')
        self.assertEqual(periodo_potencia.es_facturable(), True)
        self.assertEqual(periodo_potencia.fecha_desde, u'2017-03-31')
        self.assertEqual(periodo_potencia.fecha_hasta, u'2017-04-30')

        self.assertEqual(potencia.penalizacion_no_icp, u'N')
        self.assertEqual(potencia.importe_total, 50)

        energia_activa = fact.energia_activa

        terminos_energia_activa = energia_activa.terminos_energia_activa
        self.assertEqual(len(terminos_energia_activa), 1)
        termino_energia_activa = terminos_energia_activa[0]

        self.assertEqual(termino_energia_activa.fecha_desde, u'2017-03-31')
        self.assertEqual(termino_energia_activa.fecha_hasta, u'2017-04-30')

        periodos_energia = termino_energia_activa.periodos
        self.assertEqual(len(periodos_energia), 1)
        periodo_energia = periodos_energia[0]

        self.assertEqual(periodo_energia.valor_energia_activa, 300)
        self.assertEqual(periodo_energia.cantidad, 300)
        self.assertEqual(periodo_energia.precio, 0.044027)
        self.assertEqual(periodo_energia.nombre, u'P1')
        self.assertEqual(periodo_energia.es_facturable(), True)
        self.assertEqual(periodo_energia.fecha_desde, u'2017-03-31')
        self.assertEqual(periodo_energia.fecha_hasta, u'2017-04-30')

        self.assertEqual(energia_activa.importe_total, 13.21)

        impuesto_electrico = fact.impuesto_electrico

        self.assertEqual(impuesto_electrico.base, 0)
        self.assertEqual(impuesto_electrico.porcentaje, 0)
        self.assertEqual(impuesto_electrico.importe, 0)

        # TODO: ConceptoRepercutible

        ivas = fact.ivas
        self.assertEqual(len(ivas), 1)
        iva = ivas[0]

        self.assertEqual(iva.base, 63.21)
        self.assertEqual(iva.porcentaje, 21)
        self.assertEqual(iva.importe, 13.27)

        # TODO: IVAReducido

        medidas = fact.medidas
        self.assertEqual(len(medidas), 1)
        medida = medidas[0]

        self.assertEqual(medida.cod_pm, u'ES1234000000000001JN0F')

        modelos_aparatos = medida.modelos_aparatos
        self.assertEqual(len(modelos_aparatos), 1)
        modelo_aparato = modelos_aparatos[0]

        self.assertEqual(modelo_aparato.tipo_aparato, u'CC')
        self.assertEqual(modelo_aparato.marca_aparato, u'199')
        self.assertEqual(modelo_aparato.numero_serie, u'C99999')
        self.assertEqual(modelo_aparato.tipo_dhedm, u'1')
        self.assertEqual(modelo_aparato.gir_comptador, 10 ** 5)

        integradores = modelo_aparato.integradores
        self.assertEqual(len(integradores), 1)
        integrador = integradores[0]

        self.assertEqual(integrador.magnitud, u'AE')
        self.assertEqual(integrador.codigo_periodo, u'10')
        self.assertEqual(integrador.constante_multiplicadora, 1)
        self.assertEqual(integrador.numero_ruedas_enteras, 5)
        self.assertEqual(integrador.numero_ruedas_decimales, 0)
        self.assertEqual(integrador.consumo_calculado, 300)
        self.assertEqual(integrador.tipus, u'A')
        self.assertEqual(integrador.periode, u'P1')
        self.assertEqual(integrador.gir_comptador, 10 ** 5)
        self.assertEqual(integrador.ometre, False)

        lectura_desde = integrador.lectura_desde

        self.assertEqual(lectura_desde.fecha, u'2017-03-31')
        self.assertEqual(lectura_desde.procedencia, u'30')
        self.assertEqual(lectura_desde.lectura, 100)

        lectura_hasta = integrador.lectura_hasta

        ajuste = integrador.ajuste

        self.assertEqual(ajuste, None)

        self.assertEqual(lectura_hasta.fecha, u'2017-04-30')
        self.assertEqual(lectura_hasta.procedencia, u'30')
        self.assertEqual(lectura_hasta.lectura, 400)

        registro = f1.registro

        self.assertEqual(registro.importe_total, 76.48)
        self.assertEqual(registro.saldo_total, 76.48)
        self.assertEqual(registro.total_recibos, 1)
        self.assertEqual(registro.tipo_moneda, u'02')
        self.assertEqual(registro.fecha_valor, u'2017-05-01')
        self.assertEqual(registro.fecha_limite_pago, u'2017-06-01')
        self.assertEqual(registro.iban, u'ES7712341234161234567890')
        self.assertEqual(registro.id_remesa, u'0')

        self.assertDictEqual(
            fact.get_create_invoice_params(),
            {
                'tipo_rectificadora': 'N',
                'tipo_factura': '01',
                'date_invoice': '2017-05-01',
                'check_total': 100,
                'origin': 'F0001',
                'origin_date_invoice': '2017-05-01',
                'reference': 'F0001',
            }
        )

        self.assertEqual(fact.get_info_facturacio_potencia(), u'icp')

    def test_integradores_DH(self):
        f1 = F1(self.xml_f101_integradores_dh)
        f1.parse_xml()

        self.assertEqual(f1.otras_facturas, [])
        self.assertEqual(len(f1.facturas_atr), 1)

        fact = f1.facturas_atr[0]
        comptador = fact.get_comptadors()[0]
        integradors_pm = comptador.get_lectures_maximetre()
        self.assertEqual(len(integradors_pm), 1)
        self.assertEqual(integradors_pm[0].codigo_periodo, '21')
        self.assertEqual(integradors_pm[0].lectura_hasta.lectura, 100)

    def test_factura_atr_30A(self):
        f1 = F1(self.xml_f101_atr_invoice_30A)
        f1.parse_xml()

        self.assertEqual(len(f1.facturas_atr), 1)

        fact = f1.facturas_atr[0]

        potencia = fact.potencia

        self.assertEqual(len(potencia.terminos_potencia), 1)

        termino_potencia = potencia.terminos_potencia[0]

        self.assertDictEqual(
            termino_potencia.get_contracted_periods_by_period(),
            {
                'P1': 35000,
                'P2': 35000,
                'P3': 35000,
            }
        )

        energia_reactiva = fact.energia_reactiva

        terminos_energia_reactiva = energia_reactiva.terminos_energia_reactiva
        self.assertEqual(len(terminos_energia_reactiva), 2)
        termino_energia_reactiva0 = terminos_energia_reactiva[0]
        termino_energia_reactiva1 = terminos_energia_reactiva[1]

        self.assertEqual(termino_energia_reactiva0.fecha_desde, u'2017-03-31')
        self.assertEqual(termino_energia_reactiva0.fecha_hasta, u'2017-04-17')

        periodos_reactiva0 = termino_energia_reactiva0.periodos
        self.assertEqual(len(periodos_reactiva0), 1)
        periodo_reactiva0 = periodos_reactiva0[0]

        self.assertEqual(periodo_reactiva0.valor_energia_reactiva, 15.55)
        self.assertEqual(periodo_reactiva0.cantidad, 15.55)
        self.assertEqual(periodo_reactiva0.precio, 0.041554)
        self.assertEqual(periodo_reactiva0.fecha_desde, u'2017-03-31')
        self.assertEqual(periodo_reactiva0.fecha_hasta, u'2017-04-17')

        self.assertEqual(termino_energia_reactiva1.fecha_desde, u'2017-03-31')
        self.assertEqual(termino_energia_reactiva1.fecha_hasta, u'2017-04-30')

        periodos_reactiva1 = termino_energia_reactiva1.periodos
        self.assertEqual(len(periodos_reactiva1), 1)
        periodo_reactiva1 = periodos_reactiva1[0]

        self.assertEqual(periodo_reactiva1.valor_energia_reactiva, 714.46)
        self.assertEqual(periodo_reactiva1.cantidad, 714.46)
        self.assertEqual(periodo_reactiva1.precio, 0.041554)
        self.assertEqual(periodo_reactiva1.fecha_desde, u'2017-03-31')
        self.assertEqual(periodo_reactiva1.fecha_hasta, u'2017-04-30')

        self.assertEqual(energia_reactiva.importe_total, 30.34)

        alquiler = fact.alquiler

        precios_alquileres = alquiler.precios_alquiler
        self.assertEqual(len(precios_alquileres), 2)
        alquiler0 = precios_alquileres[0]
        alquiler1 = precios_alquileres[1]

        self.assertEqual(alquiler0.precio_dia, 0.345205)
        self.assertEqual(alquiler0.numero_dias, 17)

        self.assertEqual(alquiler1.precio_dia, 0.345205)
        self.assertEqual(alquiler1.numero_dias, 13)

        self.assertEqual(alquiler.importe_total, 10.36)

        self.assertEqual(fact.get_info_facturacio_potencia(), u'max')

    def test_factura_atr_61B(self):
        f1 = F1(self.xml_f101_atr_invoice_61B)
        f1.parse_xml()

        self.assertEqual(len(f1.facturas_atr), 1)

        fact = f1.facturas_atr[0]

        potencia = fact.potencia

        self.assertEqual(len(potencia.terminos_potencia), 1)

        termino_potencia = potencia.terminos_potencia[0]

        self.assertDictEqual(
            termino_potencia.get_contracted_periods_by_period(),
            {
                'P1': 450000,
                'P2': 500000,
                'P3': 500000,
                'P4': 500000,
                'P5': 500000,
                'P6': 725000,
            }
        )

        exceso_potencia = fact.exceso_potencia

        periodos_exceso_potencia = exceso_potencia.periodos
        self.assertEqual(len(periodos_exceso_potencia), 1)
        periodo_exceso_potencia = periodos_exceso_potencia[0]

        self.assertEqual(periodo_exceso_potencia.valor_exceso_potencia, 186.29)
        self.assertEqual(periodo_exceso_potencia.name, u'P1')
        self.assertEqual(periodo_exceso_potencia.nombre, u'P1')

        self.assertEqual(exceso_potencia.importe_total, 186.29)

    def test_factura_atr_ajuste(self):
        f1 = F1(self.xml_f101_atr_invoice_ajuste)
        f1.parse_xml()

        self.assertEqual(len(f1.facturas_atr), 1)

        fact = f1.facturas_atr[0]

        self.assertEqual(len(fact.medidas), 1)

        medida = fact.medidas[0]

        self.assertEqual(len(medida.modelos_aparatos), 1)

        modelo_aparato = medida.modelos_aparatos[0]

        self.assertEqual(len(modelo_aparato.integradores), 1)

        integrador = modelo_aparato.integradores[0]

        ajuste = integrador.ajuste

        self.assertEqual(ajuste.codigo_motivo, u'01')
        self.assertEqual(ajuste.ajuste_por_integrador, 12.0)
        self.assertEqual(ajuste.comentario, u'Ajuste')

    def testOtherInvoice(self):
        f1 = F1(self.xml_f101_other_invoice)
        f1.parse_xml()

        self.assertEqual(f1.facturas_atr, [])
        self.assertEqual(len(f1.otras_facturas), 1)

        fact = f1.otras_facturas[0]

        datos_factura = fact.datos_factura

        direccion_suministro = datos_factura.direccion_suministro

        self.assertEqual(direccion_suministro.pais, u'España')
        self.assertEqual(direccion_suministro.provincia, u'17')
        self.assertEqual(direccion_suministro.municipio, u'17079')
        self.assertEqual(direccion_suministro.cod_postal, u'17003')
        self.assertEqual(direccion_suministro.calle, u'Nom carrer')
        self.assertEqual(direccion_suministro.numero_finca, u'3')
        self.assertEqual(direccion_suministro.escalera, u'1')
        self.assertEqual(direccion_suministro.piso, u'1')
        self.assertEqual(direccion_suministro.puerta, u'1')

        cliente = datos_factura.cliente

        self.assertEqual(cliente.tipo_identificador, u'NI')
        self.assertEqual(cliente.identificador, u'70876712G')
        self.assertEqual(cliente.tipo_persona, u'F')

        self.assertEqual(datos_factura.cod_contrato, u'111111')
        self.assertEqual(datos_factura.codigo_fiscal_factura, u'F0001')
        self.assertEqual(datos_factura.tipo_factura, u'N')
        self.assertEqual(datos_factura.motivo_facturacion, u'01')
        self.assertEqual(datos_factura.fecha_factura, u'2017-05-01')
        self.assertEqual(datos_factura.identificador_emisora, u'B11254455')
        self.assertEqual(datos_factura.comentarios, u'.')
        self.assertEqual(datos_factura.importe_total_factura, 21.84)
        self.assertEqual(datos_factura.saldo_factura, 21.84)
        self.assertEqual(datos_factura.tipo_moneda, u'02')
        self.assertEqual(datos_factura.fecha_boe, u'2016-01-01')

        conceptos_repercutibles = fact.conceptos_repercutibles
        self.assertEqual(len(conceptos_repercutibles), 3)
        concepto_enganche = conceptos_repercutibles[0]
        concepto_verificacion = conceptos_repercutibles[1]
        concepto_demora = conceptos_repercutibles[2]

        self.assertEqual(concepto_enganche.concepto_repercutible, u'04')
        self.assertEqual(concepto_enganche.tipo_impositivo, u'1')
        self.assertEqual(concepto_enganche.fecha_operacion, u'2016-09-01')
        self.assertEqual(concepto_enganche.unidades, 1)
        self.assertEqual(concepto_enganche.precio_unidad, 9.04476)
        self.assertEqual(concepto_enganche.importe, 9.04)
        self.assertEqual(
            concepto_enganche.comentarios,
            'Cuota de enganche / Act. en equipos BT'
        )

        self.assertEqual(concepto_verificacion.concepto_repercutible, u'05')
        self.assertEqual(concepto_verificacion.tipo_impositivo, u'1')
        self.assertEqual(concepto_verificacion.fecha_operacion, u'2016-09-01')
        self.assertEqual(concepto_verificacion.unidades, 1)
        self.assertEqual(concepto_verificacion.precio_unidad, 8.011716)
        self.assertEqual(concepto_verificacion.importe, 8.01)
        self.assertEqual(
            concepto_verificacion.comentarios, u'Cuota de verificación BT'
        )

        self.assertEqual(concepto_demora.concepto_repercutible, u'11')
        self.assertEqual(concepto_demora.tipo_impositivo, u'1')
        self.assertEqual(concepto_demora.fecha_desde, u'2016-09-01')
        self.assertEqual(concepto_demora.fecha_hasta, u'2016-10-01')
        self.assertEqual(concepto_demora.unidades, 1)
        self.assertEqual(concepto_demora.precio_unidad, 1.0)
        self.assertEqual(concepto_demora.importe, 1.0)
        self.assertEqual(
            concepto_demora.comentarios, u'Intereses de demora'
        )

        ivas = fact.ivas
        self.assertEqual(len(ivas), 1)
        iva = ivas[0]

        self.assertEqual(iva.base, 18.05)
        self.assertEqual(iva.porcentaje, 21)
        self.assertEqual(iva.importe, 3.79)

        registro = f1.registro

        self.assertEqual(registro.importe_total, 21.84)
        self.assertEqual(registro.saldo_total, 21.84)
        self.assertEqual(registro.total_recibos, 1)
        self.assertEqual(registro.tipo_moneda, u'02')
        self.assertEqual(registro.fecha_valor, u'2016-11-01')
        self.assertEqual(registro.fecha_limite_pago, u'2016-11-21')
        self.assertEqual(registro.iban, u'ES7712341234161234567890')
        self.assertEqual(registro.id_remesa, u'0')

    def test_get_remesa(self):
        f1 = F1(self.xml_f101_atr_invoice)
        f1.parse_xml()

        self.assertEqual(
            f1.registro.get_remesa(),
            {
                'id_remesa': '0',
                'fecha_valor_remesa': '2017-05-01',
                'data_limit_pagament': '2017-06-01',
                'total_importe_remesa': 76.48,
                'total_recibos_remesa': 1,
            }
        )

    def test_get_comptadors(self):
        f1 = F1(self.xml_f101_atr_invoice)
        f1.parse_xml()

        fact = f1.facturas_atr[0]

        comptadors = fact.get_comptadors()
        self.assertEqual(len(comptadors), 1)
        comptador = comptadors[0]

        self.assertEqual(comptador.tipo_aparato, u'CC')
        self.assertEqual(comptador.marca_aparato, u'199')
        self.assertEqual(comptador.numero_serie, u'C99999')
        self.assertEqual(comptador.tipo_dhedm, u'1')

        integradores = comptador.integradores
        self.assertEqual(len(integradores), 1)
        integrador = integradores[0]

        self.assertEqual(integrador.magnitud, u'AE')
        self.assertEqual(integrador.codigo_periodo, u'10')
        self.assertEqual(integrador.constante_multiplicadora, 1)
        self.assertEqual(integrador.numero_ruedas_enteras, 5)
        self.assertEqual(integrador.numero_ruedas_decimales, 0)
        self.assertEqual(integrador.consumo_calculado, 300)
        self.assertEqual(integrador.tipus, u'A')
        self.assertEqual(integrador.periode, u'P1')
        self.assertEqual(integrador.gir_comptador, 10 ** 5)

        lectura_desde = integrador.lectura_desde

        self.assertEqual(lectura_desde.fecha, u'2017-03-31')
        self.assertEqual(lectura_desde.procedencia, u'30')
        self.assertEqual(lectura_desde.lectura, 100)

        lectura_hasta = integrador.lectura_hasta

        self.assertEqual(lectura_hasta.fecha, u'2017-04-30')
        self.assertEqual(lectura_hasta.procedencia, u'30')
        self.assertEqual(lectura_hasta.lectura, 400)

    def test_specific_get_lectures_returns_correct_readings(self):
        f1 = F1(self.xml_f101_atr_invoice_30A)
        f1.set_xsd()
        f1.parse_xml()

        invoice = f1.facturas_atr[0]
        meter = invoice.get_comptadors()[0]
        readings = meter.get_lectures()
        expected_lectures_activa = {
            read.integrador for read in readings if read.tipus == 'A'
        }
        expected_lectures_reactiva = {
            read.integrador for read in readings if read.tipus == 'R'
        }
        expected_lectures_max = {
            read.integrador for read in readings if read.tipus == 'M'
        }
        expected_lectures_energia = {
            read.integrador for read in readings if read.tipus in ('A', u'R')
        }

        lectures_activa = {
            read.integrador for read in meter.get_lectures_activa()
        }
        lectures_reactiva = {
            read.integrador for read in meter.get_lectures_reactiva()
        }
        lectures_max = {
            read.integrador for read in meter.get_lectures_maximetre()
        }
        lectures_energia = {
            read.integrador for read in meter.get_lectures_energia()
        }

        self.assertEqual(expected_lectures_activa, lectures_activa)
        self.assertEqual(expected_lectures_reactiva, lectures_reactiva)
        self.assertEqual(expected_lectures_max, lectures_max)
        self.assertEqual(expected_lectures_energia, lectures_energia)

    def test_get_periods_ignores_empty_periods(self):
        f1 = F1(self.xml_f101_atr_invoice_empty_periods)
        f1.parse_xml()

        fact = f1.facturas_atr[0]

        self.assertEqual(len(fact.potencia.terminos_potencia[0].periodos), 1)
        self.assertEqual(
            len(fact.energia_activa.terminos_energia_activa[0].periodos), 1
        )

    def test_sin_base_imponible(self):
        f1_atr = F1(self.xml_f101_atr_invoice)
        f1_atr.parse_xml()

        f1_otros = F1(self.xml_f101_other_invoice)
        f1_otros.parse_xml()

        f1_sin_base = F1(
            self.xml_f101_atr_invoice.replace(
                '<BaseImponible>63.21</BaseImponible>',
                '<BaseImponible>0.0</BaseImponible>'
            )
        )
        f1_sin_base.parse_xml()

        fact_atr = f1_atr.facturas_atr[0]
        fact_oth = f1_otros.otras_facturas[0]
        fact_sin = f1_sin_base.facturas_atr[0]

        self.assertEqual(fact_atr.sin_base_imponible(), False)
        self.assertEqual(fact_oth.sin_base_imponible(), False)
        self.assertEqual(fact_sin.sin_base_imponible(), True)

    def test_get_linies_factura_on_atr(self):
        f1_atr = F1(self.xml_f101_atr_invoice_30A)
        f1_atr.parse_xml()

        lines_atr = f1_atr.facturas_atr[0].get_linies_factura_by_type()

        self.assertItemsEqual(
            lines_atr.keys(), ['potencia', u'energia', u'reactiva', u'lloguer']
        )

        lines_pot = lines_atr['potencia']
        lines_act = lines_atr['energia']
        lines_rea = lines_atr['reactiva']
        lines_llo = lines_atr['lloguer']

        self.assertEqual(lines_pot['total'], 245.95)
        self.assertEqual(lines_act['total'], 124.25)
        self.assertEqual(lines_rea['total'], 30.34)
        self.assertEqual(lines_llo['total'], 10.36)

        self.assertEqual(len(lines_pot['lines']), 3)
        self.assertEqual(len(lines_act['lines']), 3)
        self.assertEqual(len(lines_rea['lines']), 2)
        self.assertEqual(len(lines_llo['lines']), 2)

    def test_get_linies_factura_on_atr_with_exces(self):
        f1_atr = F1(self.xml_f101_atr_invoice_61B)
        f1_atr.parse_xml()

        lines_atr = f1_atr.facturas_atr[0].get_linies_factura_by_type()

        self.assertItemsEqual(
            lines_atr.keys(),
            ['potencia', u'exces_potencia', u'energia', u'lloguer']
        )

        lines_pot = lines_atr['potencia']
        lines_exc = lines_atr['exces_potencia']
        lines_act = lines_atr['energia']
        lines_llo = lines_atr['lloguer']

        self.assertEqual(lines_pot['total'], 3611.37)
        self.assertEqual(lines_exc['total'], 186.29)
        self.assertEqual(lines_act['total'], 535.64)
        self.assertEqual(lines_llo['total'], 41.25)

        self.assertEqual(len(lines_pot['lines']), 6)
        self.assertEqual(len(lines_exc['lines']), 1)
        self.assertEqual(len(lines_act['lines']), 6)
        self.assertEqual(len(lines_llo['lines']), 1)

    def test_get_linies_factura_on_other(self):
        f1_oth = F1(self.xml_f101_other_invoice)
        f1_oth.parse_xml()

        lines_oth = f1_oth.otras_facturas[0].get_linies_factura_by_type()

        self.assertItemsEqual(
            lines_oth.keys(), ['altres']
        )
        line_oth = lines_oth['altres']

        self.assertEqual(len(line_oth['lines']), 3)
        self.assertEqual(line_oth['total'], 18.05)

        line_eng = line_oth['lines'][0]
        line_ver = line_oth['lines'][1]
        line_dem = line_oth['lines'][2]

        self.assertEqual(line_eng.concepto_repercutible, u'04')
        self.assertEqual(line_eng.tipo_impositivo, u'1')
        self.assertEqual(line_eng.fecha_operacion, u'2016-09-01')
        self.assertEqual(line_eng.unidades, 1)
        self.assertEqual(line_eng.precio_unidad, 9.04476)
        self.assertEqual(line_eng.importe, 9.04)
        self.assertEqual(
            line_eng.comentarios,
            'Cuota de enganche / Act. en equipos BT'
        )

        self.assertEqual(line_ver.concepto_repercutible, u'05')
        self.assertEqual(line_ver.tipo_impositivo, u'1')
        self.assertEqual(line_ver.fecha_operacion, u'2016-09-01')
        self.assertEqual(line_ver.unidades, 1)
        self.assertEqual(line_ver.precio_unidad, 8.011716)
        self.assertEqual(line_ver.importe, 8.01)
        self.assertEqual(
            line_ver.comentarios, u'Cuota de verificación BT'
        )

        self.assertEqual(line_dem.concepto_repercutible, u'11')
        self.assertEqual(line_dem.tipo_impositivo, u'1')
        self.assertEqual(line_dem.fecha_desde, u'2016-09-01')
        self.assertEqual(line_dem.fecha_hasta, u'2016-10-01')
        self.assertEqual(line_dem.unidades, 1)
        self.assertEqual(line_dem.precio_unidad, 1.0)
        self.assertEqual(line_dem.importe, 1.0)
        self.assertEqual(
            line_dem.comentarios, u'Intereses de demora'
        )

    def test_agrupar_i_obtenir_dates(self):
        f1 = F1(self.xml_f101_atr_invoice)
        f1.parse_xml()

        fact = f1.facturas_atr[0]
        compt = fact.get_comptadors()[0]
        lectures = compt.get_lectures()

        lectures_agrupades = agrupar_lectures_per_data(lectures)

        lectura = lectures[0]

        self.assertDictEqual(
            lectures_agrupades,
            {
                ('2017-03-31', u'2017-04-30'):
                    [lectura]
            }
        )

        data_inici, data_fi = obtenir_data_inici_i_final(lectures_agrupades)
        self.assertEqual(data_inici, u'2017-03-31')
        self.assertEqual(data_fi, u'2017-04-30')

    def test_agrupar_i_obtenir_dates_maximetre(self):
        f1 = F1(self.xml_f101_atr_invoice_30A)
        f1.parse_xml()

        fact = f1.facturas_atr[0]
        compt = fact.get_comptadors()[0]
        lectures = compt.get_lectures()

        lectures_agrupades = agrupar_lectures_per_data(lectures)

        self.assertEqual(
            lectures_agrupades.keys(),
            [
                ('2017-03-31', u'2017-04-17'),  # Energy readings
                ('2017-04-30', u'2017-04-30')   # Maximeter readings
            ]
        )

        data_inici, data_fi = obtenir_data_inici_i_final(lectures_agrupades)
        self.assertEqual(data_inici, u'2017-03-31')
        self.assertEqual(data_fi, u'2017-04-30')

    def test_spaces_are_deleted(self):
        f1 = F1(self.xml_f101_spaces)
        f1.parse_xml()

        # Everything should work just as where we don't have spaces

        self.assertEqual(f1.otras_facturas, [])
        self.assertEqual(len(f1.facturas_atr), 1)

        fact = f1.facturas_atr[0]

        datos_factura = fact.datos_factura

        direccion_suministro = datos_factura.direccion_suministro

        self.assertEqual(direccion_suministro.pais, u'España')
        self.assertEqual(direccion_suministro.provincia, u'17')
        self.assertEqual(direccion_suministro.municipio, u'17079')
        self.assertEqual(direccion_suministro.cod_postal, u'17003')
        self.assertEqual(direccion_suministro.calle, u'Nom carrer')
        self.assertEqual(direccion_suministro.numero_finca, u'3')
        self.assertEqual(direccion_suministro.escalera, u'1')
        self.assertEqual(direccion_suministro.piso, u'1')
        self.assertEqual(direccion_suministro.puerta, u'1')

        cliente = datos_factura.cliente

        self.assertEqual(cliente.tipo_identificador, u'NI')
        self.assertEqual(cliente.identificador, u'70876712G')
        self.assertEqual(cliente.tipo_persona, u'F')

        self.assertEqual(datos_factura.cod_contrato, u'111111')
        self.assertEqual(datos_factura.codigo_fiscal_factura, u'F0001')
        self.assertEqual(datos_factura.tipo_factura, u'N')
        self.assertEqual(datos_factura.motivo_facturacion, u'01')
        self.assertEqual(datos_factura.fecha_factura, u'2017-05-01')
        self.assertEqual(datos_factura.identificador_emisora, u'B11254455')
        self.assertEqual(datos_factura.comentarios, u'.')
        self.assertEqual(datos_factura.importe_total_factura, 100)
        self.assertEqual(datos_factura.saldo_factura, 100)
        self.assertEqual(datos_factura.tipo_moneda, u'02')
        self.assertEqual(datos_factura.fecha_boe, u'2016-01-01')
        self.assertEqual(datos_factura.tarifa_atr_fact, u'001')
        self.assertEqual(datos_factura.modo_control_potencia, u'1')
        self.assertEqual(datos_factura.marca_medida_con_perdidas, u'N')
        self.assertEqual(datos_factura.indicativo_curva_carga, u'02')
        self.assertEqual(datos_factura.fecha_desde_factura, u'2017-03-31')
        self.assertEqual(datos_factura.fecha_hasta_factura, u'2017-04-30')
        self.assertEqual(datos_factura.numero_dias, 30)

        potencia = fact.potencia

        terminos_potencia = potencia.terminos_potencia
        self.assertEqual(len(terminos_potencia), 1)
        termino_potencia = terminos_potencia[0]

        self.assertEqual(termino_potencia.fecha_desde, u'2017-03-31')
        self.assertEqual(termino_potencia.fecha_hasta, u'2017-04-30')

        periodos_potencia = termino_potencia.periodos
        self.assertEqual(len(periodos_potencia), 1)
        periodo_potencia = periodos_potencia[0]

        self.assertDictEqual(
            termino_potencia.get_contracted_periods_by_period(),
            {'P1': 1000}
        )

        self.assertEqual(periodo_potencia.potencia_contratada, 1000)
        self.assertEqual(periodo_potencia.potencia_max_demandada, 1000)
        self.assertEqual(periodo_potencia.potencia_a_facturar, 1000)
        self.assertEqual(periodo_potencia.cantidad, 1000)
        self.assertEqual(periodo_potencia.precio, 0.05)
        self.assertEqual(periodo_potencia.nombre, u'P1')
        self.assertEqual(periodo_potencia.es_facturable(), True)
        self.assertEqual(periodo_potencia.fecha_desde, u'2017-03-31')
        self.assertEqual(periodo_potencia.fecha_hasta, u'2017-04-30')

        self.assertEqual(potencia.penalizacion_no_icp, u'N')
        self.assertEqual(potencia.importe_total, 50)

        energia_activa = fact.energia_activa

        terminos_energia_activa = energia_activa.terminos_energia_activa
        self.assertEqual(len(terminos_energia_activa), 1)
        termino_energia_activa = terminos_energia_activa[0]

        self.assertEqual(termino_energia_activa.fecha_desde, u'2017-03-31')
        self.assertEqual(termino_energia_activa.fecha_hasta, u'2017-04-30')

        periodos_energia = termino_energia_activa.periodos
        self.assertEqual(len(periodos_energia), 1)
        periodo_energia = periodos_energia[0]

        self.assertEqual(periodo_energia.valor_energia_activa, 300)
        self.assertEqual(periodo_energia.cantidad, 300)
        self.assertEqual(periodo_energia.precio, 0.044027)
        self.assertEqual(periodo_energia.nombre, u'P1')
        self.assertEqual(periodo_energia.es_facturable(), True)
        self.assertEqual(periodo_energia.fecha_desde, u'2017-03-31')
        self.assertEqual(periodo_energia.fecha_hasta, u'2017-04-30')

        self.assertEqual(energia_activa.importe_total, 13.21)

        impuesto_electrico = fact.impuesto_electrico

        self.assertEqual(impuesto_electrico.base, 0)
        self.assertEqual(impuesto_electrico.porcentaje, 0)
        self.assertEqual(impuesto_electrico.importe, 0)

        # TODO: ConceptoRepercutible

        ivas = fact.ivas
        self.assertEqual(len(ivas), 1)
        iva = ivas[0]

        self.assertEqual(iva.base, 63.21)
        self.assertEqual(iva.porcentaje, 21)
        self.assertEqual(iva.importe, 13.27)

        # TODO: IVAReducido

        medidas = fact.medidas
        self.assertEqual(len(medidas), 1)
        medida = medidas[0]

        self.assertEqual(medida.cod_pm, u'ES1234000000000001JN0F')

        modelos_aparatos = medida.modelos_aparatos
        self.assertEqual(len(modelos_aparatos), 1)
        modelo_aparato = modelos_aparatos[0]

        self.assertEqual(modelo_aparato.tipo_aparato, u'CC')
        self.assertEqual(modelo_aparato.marca_aparato, u'199')
        self.assertEqual(modelo_aparato.numero_serie, u'C99999')
        self.assertEqual(modelo_aparato.tipo_dhedm, u'1')
        self.assertEqual(modelo_aparato.gir_comptador, 10 ** 5)

        integradores = modelo_aparato.integradores
        self.assertEqual(len(integradores), 1)
        integrador = integradores[0]

        self.assertEqual(integrador.magnitud, u'AE')
        self.assertEqual(integrador.codigo_periodo, u'10')
        self.assertEqual(integrador.constante_multiplicadora, 1)
        self.assertEqual(integrador.numero_ruedas_enteras, 5)
        self.assertEqual(integrador.numero_ruedas_decimales, 0)
        self.assertEqual(integrador.consumo_calculado, 300)
        self.assertEqual(integrador.tipus, u'A')
        self.assertEqual(integrador.periode, u'P1')
        self.assertEqual(integrador.gir_comptador, 10 ** 5)
        self.assertEqual(integrador.ometre, False)

        lectura_desde = integrador.lectura_desde

        self.assertEqual(lectura_desde.fecha, u'2017-03-31')
        self.assertEqual(lectura_desde.procedencia, u'30')
        self.assertEqual(lectura_desde.lectura, 100)

        lectura_hasta = integrador.lectura_hasta

        ajuste = integrador.ajuste

        self.assertEqual(ajuste, None)

        self.assertEqual(lectura_hasta.fecha, u'2017-04-30')
        self.assertEqual(lectura_hasta.procedencia, u'30')
        self.assertEqual(lectura_hasta.lectura, 400)

        registro = f1.registro

        self.assertEqual(registro.importe_total, 76.48)
        self.assertEqual(registro.saldo_total, 76.48)
        self.assertEqual(registro.total_recibos, 1)
        self.assertEqual(registro.tipo_moneda, u'02')
        self.assertEqual(registro.fecha_valor, u'2017-05-01')
        self.assertEqual(registro.fecha_limite_pago, u'2017-06-01')
        self.assertEqual(registro.iban, u'ES7712341234161234567890')
        self.assertEqual(registro.id_remesa, u'0')

        self.assertDictEqual(
            fact.get_create_invoice_params(),
            {
                'tipo_rectificadora': 'N',
                'tipo_factura': '01',
                'date_invoice': '2017-05-01',
                'check_total': 100,
                'origin': 'F0001',
                'origin_date_invoice': '2017-05-01',
                'reference': 'F0001',
            }
        )

        self.assertEqual(fact.get_info_facturacio_potencia(), u'icp')

    def test_free_interpretation(self):
        f1 = F1(self.xml_f101_free_interpretation)
        f1.parse_xml()

        # We should be able to input free interpretations as well...

        fact = f1.facturas_atr[0]

        comptadors = fact.get_comptadors()
        self.assertEqual(len(comptadors), 1)
        comptador = comptadors[0]

        # We will assume that the correct values for the meter are the first one
        self.assertEqual(comptador.tipo_aparato, u'TG')
        self.assertEqual(comptador.marca_aparato, u'199')
        self.assertEqual(comptador.numero_serie, u'202459701')
        self.assertEqual(comptador.tipo_dhedm, u'2')

        # If we get "integradores" we should be getting all of them though
        integradores = comptador.integradores
        self.assertEqual(len(integradores), 2)
        integrador_p1 = integradores[0]
        integrador_p2 = integradores[1]

        self.assertEqual(integrador_p1.magnitud, u'AE')
        self.assertEqual(integrador_p1.codigo_periodo, u'21')
        self.assertEqual(integrador_p1.constante_multiplicadora, 1)
        self.assertEqual(integrador_p1.numero_ruedas_enteras, 6)
        self.assertEqual(integrador_p1.numero_ruedas_decimales, 0)
        self.assertEqual(integrador_p1.consumo_calculado, 259)
        self.assertEqual(integrador_p1.tipus, u'A')
        self.assertEqual(integrador_p1.periode, u'P1')
        self.assertEqual(integrador_p1.gir_comptador, 10 ** 6)

        lectura_desde_p1 = integrador_p1.lectura_desde

        self.assertEqual(lectura_desde_p1.fecha, u'2017-06-29')
        self.assertEqual(lectura_desde_p1.procedencia, u'60')
        self.assertEqual(lectura_desde_p1.lectura, 5730)

        lectura_hasta_p1 = integrador_p1.lectura_hasta

        self.assertEqual(lectura_hasta_p1.fecha, u'2017-07-27')
        self.assertEqual(lectura_hasta_p1.procedencia, u'60')
        self.assertEqual(lectura_hasta_p1.lectura, 5989)

        self.assertEqual(integrador_p2.magnitud, u'AE')
        self.assertEqual(integrador_p2.codigo_periodo, u'22')
        self.assertEqual(integrador_p2.constante_multiplicadora, 1)
        self.assertEqual(integrador_p2.numero_ruedas_enteras, 6)
        self.assertEqual(integrador_p2.numero_ruedas_decimales, 0)
        self.assertEqual(integrador_p2.consumo_calculado, 153)
        self.assertEqual(integrador_p2.tipus, u'A')
        self.assertEqual(integrador_p2.periode, u'P2')
        self.assertEqual(integrador_p2.gir_comptador, 10 ** 6)

        lectura_desde_p2 = integrador_p2.lectura_desde

        self.assertEqual(lectura_desde_p2.fecha, u'2017-06-29')
        self.assertEqual(lectura_desde_p2.procedencia, u'60')
        self.assertEqual(lectura_desde_p2.lectura, 3656)

        lectura_hasta_p2 = integrador_p2.lectura_hasta

        self.assertEqual(lectura_hasta_p2.fecha, u'2017-07-27')
        self.assertEqual(lectura_hasta_p2.procedencia, u'60')
        self.assertEqual(lectura_hasta_p2.lectura, 3809)

    def test_empty_rents_dont_return(self):
        f1 = F1(self.xml_f101_empty_rent)
        f1.parse_xml()

        # We should be able to input free interpretations as well...

        fact = f1.facturas_atr[0]

        llog, total = fact.get_info_lloguer()

        # Despite having lines with 0 they shouldn't be returned since they
        # are empty
        self.assertEqual(llog, [])
        self.assertEqual(total, 0)


class test_P0(unittest.TestCase):

    def setUp(self):
        self.xml_p001 = open(get_data("p001.xml"), "r")
        self.xml_p002_accept = open(get_data("p002_accept.xml"), "r")
        self.xml_p002_accept_min = open(get_data("p002_accept_min.xml"), "r")
        self.xml_p002_reject = open(get_data("p002_reject.xml"), "r")

    def tearDown(self):
        self.xml_p001.close()
        self.xml_p002_accept.close()
        self.xml_p002_reject.close()

    def test_p001(self):
        p0 = P0(self.xml_p001)
        p0.parse_xml()
        self.assertEqual(p0.tipo_identificador, u'NI')
        self.assertEqual(p0.identificador, u'11111111H')

    def test_p002_accept(self):
        p0 = P0(self.xml_p002_accept)
        p0.parse_xml()
        # Datos Aceptacion
        self.assertEqual(p0.expediente_acometida.expediente_abierto, 'S')

    def test_p002_accept_min(self):
        p0 = P0(self.xml_p002_accept_min)
        p0.parse_xml()
        # Datos Aceptacion
        self.assertEqual(p0.en_vigor, 'N')

    def test_p002_reject(self):
        p0 = P0(self.xml_p002_reject)
        p0.parse_xml()
        self.assertEqual(p0.fecha_rechazo, u'2016-07-20')


class test_E1(unittest.TestCase):

    def setUp(self):
        self.xml_e101 = open(get_data("e101.xml"), "r")
        self.xml_e102_accept = open(get_data("e102_accept.xml"), "r")
        self.xml_e102_reject = open(get_data("e102_reject.xml"), "r")
        self.xml_e103 = open(get_data("e103.xml"), "r")
        self.xml_e104 = open(get_data("e104.xml"), "r")
        self.xml_e105 = open(get_data("e105.xml"), "r")
        self.xml_e106 = open(get_data("e106.xml"), "r")
        self.xml_e112 = open(get_data("e112.xml"), "r")
        self.xml_e113 = open(get_data("e113.xml"), "r")

    def tearDown(self):
        self.xml_e101.close()
        self.xml_e102_accept.close()
        self.xml_e102_reject.close()
        self.xml_e103.close()
        self.xml_e104.close()
        self.xml_e105.close()
        self.xml_e106.close()
        self.xml_e112.close()
        self.xml_e113.close()

    def test_e101(self):
        e1 = E1(self.xml_e101)
        e1.parse_xml()
        self.assertEqual(e1.codigo_de_solicitud_ref, u'201605219400')
        self.assertEqual(e1.tipo_de_solicitud, u'01')
        self.assertEqual(e1.id_cliente.tipo_identificador, u'NI')
        self.assertEqual(e1.id_cliente.identificador, u'11111111H')
        self.assertEqual(e1.id_cliente.tipo_persona, u'F')

    def test_e102_accept(self):
        e1 = E1(self.xml_e102_accept)
        e1.parse_xml()
        self.assertEqual(e1.fecha_aceptacion, u'2020-05-01')
        self.assertEqual(e1.ind_anulable, u'S')
        self.assertEqual(e1.actuacion_campo, u'S')
        self.assertEqual(e1.fecha_activacion_prevista, u'2020-05-06')

    def test_e102_reject(self):
        e1 = E1(self.xml_e102_reject)
        e1.parse_xml()

        self.assertEqual(e1.fecha_rechazo, u'2016-07-20')
        self.assertEqual(len(e1.registros_documento), 2)
        self.assertEqual(len(e1.rechazos), 2)
        rej1 = e1.rechazos[0]
        rej2 = e1.rechazos[1]
        self.assertEqual(rej1.secuencial, u'1')
        self.assertEqual(rej1.codigo_motivo, u'01')
        self.assertEqual(rej1.comentarios, u'Motiu de rebuig 01: No existe Punto de Suministro asociado al CUPS')
        self.assertEqual(rej2.secuencial, u'2')
        self.assertEqual(rej2.codigo_motivo, u'03')
        self.assertEqual(rej2.comentarios,
                         u'Cuando el CIF-NIF no coincide con el que figura en la base de datos del Distribuidor')
        doc1 = e1.registros_documento[0]
        doc2 = e1.registros_documento[1]
        self.assertEqual(doc1.tipo_doc_aportado, u'08')
        self.assertEqual(doc1.direccion_url, u'http://eneracme.com/docs/NIF11111111H.pdf')
        self.assertEqual(doc2.tipo_doc_aportado, u'07')
        self.assertEqual(doc2.direccion_url, u'http://eneracme.com/docs/NIF11111111H.pdf')

    def test_e103(self):
        e1 = E1(self.xml_e103)
        e1.parse_xml()
        self.assertEqual(e1.fecha_incidencia, u'2016-07-21')
        self.assertEqual(e1.fecha_prevista_accion, u'2016-07-22')
        incidencies = e1.incidencias
        self.assertEqual(len(incidencies), 2)
        i1 = incidencies[0]
        i2 = incidencies[1]
        self.assertEqual(i1.codigo_motivo, u'01')
        self.assertEqual(i1.secuencial, u'1')
        self.assertEqual(i1.comentarios, u'Com 1')
        self.assertEqual(i2.codigo_motivo, u'08')
        self.assertEqual(i2.secuencial, u'2')
        self.assertEqual(i2.comentarios, u'Com 2')

    def test_e104(self):
        e1 = E1(self.xml_e104)
        e1.parse_xml()

        self.assertEqual(e1.fecha_rechazo, u'2016-07-20')
        self.assertEqual(len(e1.registros_documento), 2)
        self.assertEqual(len(e1.rechazos), 2)
        rej1 = e1.rechazos[0]
        rej2 = e1.rechazos[1]
        self.assertEqual(rej1.secuencial, u'1')
        self.assertEqual(rej1.codigo_motivo, u'01')
        self.assertEqual(rej1.comentarios, u'Motiu de rebuig 01: No existe Punto de Suministro asociado al CUPS')
        self.assertEqual(rej2.secuencial, u'2')
        self.assertEqual(rej2.codigo_motivo, u'03')
        self.assertEqual(rej2.comentarios,
                         u'Cuando el CIF-NIF no coincide con el que figura en la base de datos del Distribuidor')
        doc1 = e1.registros_documento[0]
        doc2 = e1.registros_documento[1]
        self.assertEqual(doc1.tipo_doc_aportado, u'08')
        self.assertEqual(doc1.direccion_url, u'http://eneracme.com/docs/NIF11111111H.pdf')
        self.assertEqual(doc2.tipo_doc_aportado, u'07')
        self.assertEqual(doc2.direccion_url, u'http://eneracme.com/docs/NIF11111111H.pdf')

    def test_e105(self):
        e1 = E1(self.xml_e105)
        e1.parse_xml()
        self.assertEqual(e1.datos_notificacion.fecha_activacion, u'2016-08-21')
        self.assertEqual(e1.datos_notificacion.resultado_activacion, u'01')
        self.assertEqual(e1.datos_notificacion.ind_anulable, u'S')
        # Contrato
        self.assertEqual(e1.contrato.cod_contrato, u'00001')
        # Puntos Medida
        self.assertEqual(len(e1.puntos_medida), 1)
        pm = e1.puntos_medida[0]
        self.assertEqual(pm.cod_pm, u'ES1234000000000001JN0F')
        self.assertEqual(pm.tipo_movimiento, u'A')
        self.assertEqual(pm.tipo_pm, u'03')
        self.assertEqual(pm.cod_pm_principal, u'ES1234000000000002JN0F')
        self.assertEqual(pm.modo_lectura, u'1')
        self.assertEqual(pm.funcion, u'P')
        self.assertEqual(pm.direccion_enlace, u'39522')
        self.assertEqual(pm.direccion_punto_medida, u'000000001')
        self.assertEqual(pm.num_linea, u'12')
        self.assertEqual(pm.telefono_telemedida, u'987654321')
        self.assertEqual(pm.estado_telefono, u'1')
        self.assertEqual(pm.clave_acceso, u'0000000007')
        self.assertEqual(pm.tension_pm, u'0')
        self.assertEqual(pm.fecha_vigor, u'2003-01-01')
        self.assertEqual(pm.fecha_alta, u'2003-01-01')
        self.assertEqual(pm.fecha_baja, u'2003-02-01')
        self.assertEqual(pm.comentarios, u'Comentarios Varios')
        # Aparatos
        self.assertEqual(len(pm.aparatos), 1)
        ap = pm.aparatos[0]
        self.assertEqual(ap.cod_precinto, u'02')
        self.assertEqual(ap.constante_energia, u'1.000')
        self.assertEqual(ap.constante_maximetro, u'1.000')
        self.assertEqual(ap.funcion_aparato, u'M')
        self.assertEqual(ap.lectura_directa, u'N')
        self.assertEqual(ap.marca_aparato, u'132')
        self.assertEqual(ap.modelo_marca, u'011')
        self.assertEqual(ap.modo_medida_potencia, u'1')
        self.assertEqual(ap.num_integradores, u'18')
        self.assertEqual(ap.numero_serie, u'0000539522')
        self.assertEqual(ap.periodo_fabricacion, u'2005')
        self.assertEqual(ap.propietario, u'Desc. Propietario')
        self.assertEqual(ap.ruedas_decimales, u'02')
        self.assertEqual(ap.ruedas_enteras, u'08')
        self.assertEqual(ap.tipo_aparato, u'CG')
        self.assertEqual(ap.tipo_dhedm, u'6')
        self.assertEqual(ap.tipo_equipo_medida, u'L03')
        self.assertEqual(ap.tipo_movimiento, u'CX')
        self.assertEqual(ap.tipo_propiedad_aparato, u'1')
        # Medidas
        self.assertEqual(len(ap.medidas), 2)
        md = ap.medidas[0]
        self.assertEqual(md.anomalia, u'01')
        self.assertEqual(md.comentarios, u'Comentario sobre anomalia')
        self.assertEqual(md.fecha_lectura_firme, u'2003-01-02')
        self.assertEqual(md.magnitud_medida, u'PM')
        self.assertEqual(md.periodo, u'65')
        self.assertEqual(md.procedencia, u'30')
        self.assertEqual(md.tipo_dhedm, u'6')
        self.assertEqual(md.ultima_lectura_firme, u'0.00')
        md2 = ap.medidas[1]
        self.assertFalse(md2.anomalia)
        self.assertFalse(md2.comentarios)
        self.assertEqual(md2.fecha_lectura_firme, u'2003-01-03')

    def test_e106(self):
        e1 = E1(self.xml_e106)
        e1.parse_xml()
        self.assertEqual(e1.datos_activacion.fecha, u'2016-08-21')
        self.assertEqual(e1.datos_activacion.en_servicio, u'S')
        self.assertEqual(e1.datos_activacion.ind_anulable, u'S')
        # Contrato
        self.assertEqual(e1.contrato.cod_contrato, u'00001')
        # Puntos Medida
        self.assertEqual(len(e1.puntos_medida), 1)
        pm = e1.puntos_medida[0]
        self.assertEqual(pm.cod_pm, u'ES1234000000000001JN0F')
        self.assertEqual(pm.tipo_movimiento, u'A')
        self.assertEqual(pm.tipo_pm, u'03')
        self.assertEqual(pm.cod_pm_principal, u'ES1234000000000002JN0F')
        self.assertEqual(pm.modo_lectura, u'1')
        self.assertEqual(pm.funcion, u'P')
        self.assertEqual(pm.direccion_enlace, u'39522')
        self.assertEqual(pm.direccion_punto_medida, u'000000001')
        self.assertEqual(pm.num_linea, u'12')
        self.assertEqual(pm.telefono_telemedida, u'987654321')
        self.assertEqual(pm.estado_telefono, u'1')
        self.assertEqual(pm.clave_acceso, u'0000000007')
        self.assertEqual(pm.tension_pm, u'0')
        self.assertEqual(pm.fecha_vigor, u'2003-01-01')
        self.assertEqual(pm.fecha_alta, u'2003-01-01')
        self.assertEqual(pm.fecha_baja, u'2003-02-01')
        self.assertEqual(pm.comentarios, u'Comentarios Varios')
        # Aparatos
        self.assertEqual(len(pm.aparatos), 1)
        ap = pm.aparatos[0]
        self.assertEqual(ap.cod_precinto, u'02')
        self.assertEqual(ap.constante_energia, u'1.000')
        self.assertEqual(ap.constante_maximetro, u'1.000')
        self.assertEqual(ap.funcion_aparato, u'M')
        self.assertEqual(ap.lectura_directa, u'N')
        self.assertEqual(ap.marca_aparato, u'132')
        self.assertEqual(ap.modelo_marca, u'011')
        self.assertEqual(ap.modo_medida_potencia, u'1')
        self.assertEqual(ap.num_integradores, u'18')
        self.assertEqual(ap.numero_serie, u'0000539522')
        self.assertEqual(ap.periodo_fabricacion, u'2005')
        self.assertEqual(ap.propietario, u'Desc. Propietario')
        self.assertEqual(ap.ruedas_decimales, u'02')
        self.assertEqual(ap.ruedas_enteras, u'08')
        self.assertEqual(ap.tipo_aparato, u'CG')
        self.assertEqual(ap.tipo_dhedm, u'6')
        self.assertEqual(ap.tipo_equipo_medida, u'L03')
        self.assertEqual(ap.tipo_movimiento, u'CX')
        self.assertEqual(ap.tipo_propiedad_aparato, u'1')
        # Medidas
        self.assertEqual(len(ap.medidas), 2)
        md = ap.medidas[0]
        self.assertEqual(md.anomalia, u'01')
        self.assertEqual(md.comentarios, u'Comentario sobre anomalia')
        self.assertEqual(md.fecha_lectura_firme, u'2003-01-02')
        self.assertEqual(md.magnitud_medida, u'PM')
        self.assertEqual(md.periodo, u'65')
        self.assertEqual(md.procedencia, u'30')
        self.assertEqual(md.tipo_dhedm, u'6')
        self.assertEqual(md.ultima_lectura_firme, u'0.00')
        md2 = ap.medidas[1]
        self.assertFalse(md2.anomalia)
        self.assertFalse(md2.comentarios)
        self.assertEqual(md2.fecha_lectura_firme, u'2003-01-03')

    def test_e112(self):
        e1 = E1(self.xml_e112)
        e1.parse_xml()
        self.assertEqual(e1.fecha_rechazo, u'2020-05-01')

    def test_e113(self):
        e1 = E1(self.xml_e113)
        e1.parse_xml()
        self.assertEqual(e1.contestacion_incidencia, u'02')


class test_T1(unittest.TestCase):

    def setUp(self):
        self.xml_t101 = open(get_data("t101.xml"), "r")
        self.xml_t102_accept = open(get_data("t102_accept.xml"), "r")
        self.xml_t102_reject = open(get_data("t102_reject.xml"), "r")
        self.xml_t105 = open(get_data("t105.xml"), "r")
        self.xml_t106 = open(get_data("t106.xml"), "r")
        self.xml_t110 = open(get_data("t110.xml"), "r")

    def tearDown(self):
        self.xml_t101.close()
        self.xml_t102_accept.close()
        self.xml_t102_reject.close()
        self.xml_t105.close()
        self.xml_t106.close()
        self.xml_t110.close()

    def test_t101(self):
        t1 = T1(self.xml_t101)
        t1.parse_xml()

        self.assertEqual(t1.datos_solicitud.motivo_traspaso, u'03')
        self.assertEqual(t1.datos_solicitud.fecha_prevista_accion, u'2020-05-01')
        self.assertEqual(t1.datos_solicitud.cnae, u'9820')
        self.assertEqual(t1.datos_solicitud.ind_esencial, u'S')
        self.assertEqual(t1.datos_solicitud.susp_baja_impago_en_curso, u'S')
        # Contrato
        self.assertEqual(t1.contrato.contacto.persona_de_contacto, u'Nombre Inventado')
        self.assertEqual(len(t1.contrato.contacto.telefonos), 2)
        self.assertEqual(t1.contrato.contacto.telefonos[1][1], u'666777999')
        self.assertEqual(t1.contrato.contacto.telefonos[1][0], u'34')
        self.assertEqual(t1.contrato.fecha_finalizacion, u'2018-01-01')
        self.assertEqual(t1.contrato.modo_control_potencia, u'1')
        self.assertEqual(len(t1.contrato.potencias_contratadas), 2)
        self.assertEqual(t1.contrato.potencias_contratadas[0][1], 1000)
        self.assertEqual(t1.contrato.potencias_contratadas[1][1], 2000)
        self.assertEqual(t1.contrato.tarifa_atr, u'003')
        self.assertEqual(t1.contrato.tipo_autoconsumo, u'00')
        self.assertEqual(t1.contrato.tipo_contrato_atr, u'02')
        self.assertEqual(t1.contrato.consumo_anual_estimado, u'5000')
        # Cliente
        self.assertEqual(t1.cliente.correo_electronico, u'email@host')
        self.assertEqual(t1.cliente.identificador, u'B36385870')
        self.assertEqual(t1.cliente.indicador_tipo_direccion, u'F')
        self.assertEqual(t1.cliente.nombre, u'ACC Y COMP DE COCINA MILLAN Y MUÑOZ')
        self.assertEqual(t1.cliente.razon_social, u'ACC Y COMP DE COCINA MILLAN Y MUÑOZ')
        self.assertEqual(len(t1.cliente.telefonos), 3)
        self.assertEqual(t1.cliente.telefonos[0][1], u'666777666')
        self.assertEqual(t1.cliente.telefonos[0][0], u'36')
        self.assertEqual(t1.cliente.telefonos[2][1], u'666777888')
        self.assertEqual(t1.cliente.telefonos[2][0], u'38')
        self.assertEqual(t1.cliente.tipo_identificador, u'NI')
        self.assertEqual(t1.cliente.tipo_persona, u'J')
        self.assertEqual(t1.cliente.direccion.aclarador_finca, u'Bloque de Pisos')
        self.assertEqual(t1.cliente.direccion.calle, u'MELA MUTERMILCH')
        self.assertEqual(t1.cliente.direccion.cod_postal, u'17001')
        self.assertEqual(t1.cliente.direccion.duplicador_finca, u'')
        self.assertEqual(t1.cliente.direccion.escalera, u'')
        self.assertEqual(t1.cliente.direccion.municipio, u'17079')
        self.assertEqual(t1.cliente.direccion.numero_finca, u'2')
        self.assertEqual(t1.cliente.direccion.pais, u'España')
        self.assertEqual(t1.cliente.direccion.piso, u'001')
        self.assertEqual(t1.cliente.direccion.poblacion, u'17079000501')
        self.assertEqual(t1.cliente.direccion.provincia, u'17')
        self.assertEqual(t1.cliente.direccion.puerta, u'001')
        self.assertEqual(t1.cliente.direccion.tipo_aclarador_finca, u'BI')
        self.assertEqual(t1.cliente.direccion.tipo_via, u'PZ')
        # DireccionPS
        self.assertEqual(t1.direccion_ps.pais, u'España')
        self.assertEqual(t1.direccion_ps.provincia, u'17')
        self.assertEqual(t1.direccion_ps.municipio, u'17079')
        self.assertEqual(t1.direccion_ps.cod_postal, u'17003')
        self.assertEqual(t1.direccion_ps.calle, u'Nom carrer')
        self.assertEqual(t1.direccion_ps.numero_finca, u'3')
        self.assertEqual(t1.direccion_ps.escalera, u'1')
        self.assertEqual(t1.direccion_ps.piso, u'1')
        self.assertEqual(t1.direccion_ps.puerta, u'1')
        # RegistrosDocumento
        self.assertEqual(len(t1.registros_documento), 2)
        self.assertEqual(t1.registros_documento[0].tipo_doc_aportado, u'08')
        self.assertEqual(t1.registros_documento[0].direccion_url, u'http://eneracme.com/docs/NIF11111111H.pdf')
        self.assertEqual(t1.registros_documento[1].tipo_doc_aportado, u'07')
        self.assertEqual(t1.registros_documento[1].direccion_url, u'http://eneracme.com/docs/NIF11111111H.pdf')

    def test_t102_accept(self):
        t1 = T1(self.xml_t102_accept)
        t1.parse_xml()
        self.assertEqual(t1.datos_aceptacion.fecha_aceptacion, u'2016-06-06')

    def test_t102_reject(self):
        t1 = T1(self.xml_t102_reject)
        t1.parse_xml()

        self.assertEqual(t1.fecha_rechazo, u'2016-07-20')
        self.assertEqual(len(t1.registros_documento), 2)
        self.assertEqual(len(t1.rechazos), 2)
        rej1 = t1.rechazos[0]
        rej2 = t1.rechazos[1]
        self.assertEqual(rej1.secuencial, u'1')
        self.assertEqual(rej1.codigo_motivo, u'08')
        self.assertEqual(rej1.comentarios, u'Fecha de finalización del Contrato sin informar o no válida')
        self.assertEqual(rej2.secuencial, u'2')
        self.assertEqual(rej2.codigo_motivo, u'E4')
        self.assertEqual(rej2.comentarios,u'Impago Previo')
        doc1 = t1.registros_documento[0]
        doc2 = t1.registros_documento[1]
        self.assertEqual(doc1.tipo_doc_aportado, u'08')
        self.assertEqual(doc1.direccion_url, u'http://eneracme.com/docs/NIF11111111H.pdf')
        self.assertEqual(doc2.tipo_doc_aportado, u'07')
        self.assertEqual(doc2.direccion_url, u'http://eneracme.com/docs/NIF11111111H.pdf')

    def test_t105(self):
        t1 = T1(self.xml_t105)
        t1.parse_xml()
        self.assertEqual(t1.datos_activacion.fecha_activacion, u'2016-08-21')
        self.assertEqual(t1.datos_activacion.en_servicio, u'S')
        # Contrato
        self.assertEqual(t1.contrato.cod_contrato, u'00001')
        self.assertEqual(t1.contrato.tipo_autoconsumo, u'00')
        self.assertEqual(t1.contrato.tipo_contrato_atr, u'02')
        self.assertEqual(t1.contrato.tarifa_atr, u'003')
        self.assertEqual(t1.contrato.periodicidad_facturacion, u'01')
        self.assertEqual(t1.contrato.tipo_de_telegestion, u'01')
        self.assertEqual(t1.contrato.modo_control_potencia, u'1')
        self.assertEqual(t1.contrato.marca_medida_con_perdidas, u'S')
        self.assertEqual(t1.contrato.tension_del_suministro, u'10')
        self.assertEqual(t1.contrato.vas_trafo, u'50')
        self.assertEqual(t1.contrato.porcentaje_perdidas, u'05')
        self.assertEqual(len(t1.contrato.potencias_contratadas), 2)
        pot1 = t1.contrato.potencias_contratadas[0]
        pot2 = t1.contrato.potencias_contratadas[1]
        self.assertEqual(pot1[1], 1000)
        self.assertEqual(pot2[1], 2000)
        # Puntos Medida
        self.assertEqual(len(t1.puntos_medida), 1)
        pm = t1.puntos_medida[0]
        self.assertEqual(pm.cod_pm, u'ES1234000000000001JN0F')
        self.assertEqual(pm.tipo_movimiento, u'A')
        self.assertEqual(pm.tipo_pm, u'03')
        self.assertEqual(pm.cod_pm_principal, u'ES1234000000000002JN0F')
        self.assertEqual(pm.modo_lectura, u'1')
        self.assertEqual(pm.funcion, u'P')
        self.assertEqual(pm.direccion_enlace, u'39522')
        self.assertEqual(pm.direccion_punto_medida, u'000000001')
        self.assertEqual(pm.num_linea, u'12')
        self.assertEqual(pm.telefono_telemedida, u'987654321')
        self.assertEqual(pm.estado_telefono, u'1')
        self.assertEqual(pm.clave_acceso, u'0000000007')
        self.assertEqual(pm.tension_pm, u'0')
        self.assertEqual(pm.fecha_vigor, u'2003-01-01')
        self.assertEqual(pm.fecha_alta, u'2003-01-01')
        self.assertEqual(pm.fecha_baja, u'2003-02-01')
        self.assertEqual(pm.comentarios, u'Comentarios Varios')
        # Aparatos
        self.assertEqual(len(pm.aparatos), 1)
        ap = pm.aparatos[0]
        self.assertEqual(ap.cod_precinto, u'02')
        self.assertEqual(ap.constante_energia, u'1.000')
        self.assertEqual(ap.constante_maximetro, u'1.000')
        self.assertEqual(ap.funcion_aparato, u'M')
        self.assertEqual(ap.lectura_directa, u'N')
        self.assertEqual(ap.marca_aparato, u'132')
        self.assertEqual(ap.modelo_marca, u'011')
        self.assertEqual(ap.modo_medida_potencia, u'1')
        self.assertEqual(ap.num_integradores, u'18')
        self.assertEqual(ap.numero_serie, u'0000539522')
        self.assertEqual(ap.periodo_fabricacion, u'2005')
        self.assertEqual(ap.propietario, u'Desc. Propietario')
        self.assertEqual(ap.ruedas_decimales, u'02')
        self.assertEqual(ap.ruedas_enteras, u'08')
        self.assertEqual(ap.tipo_aparato, u'CG')
        self.assertEqual(ap.tipo_dhedm, u'6')
        self.assertEqual(ap.tipo_equipo_medida, u'L03')
        self.assertEqual(ap.tipo_movimiento, u'CX')
        self.assertEqual(ap.tipo_propiedad_aparato, u'1')
        # Medidas
        self.assertEqual(len(ap.medidas), 2)
        md = ap.medidas[0]
        self.assertEqual(md.anomalia, u'01')
        self.assertEqual(md.comentarios, u'Comentario sobre anomalia')
        self.assertEqual(md.fecha_lectura_firme, u'2003-01-02')
        self.assertEqual(md.magnitud_medida, u'PM')
        self.assertEqual(md.periodo, u'65')
        self.assertEqual(md.procedencia, u'30')
        self.assertEqual(md.tipo_dhedm, u'6')
        self.assertEqual(md.ultima_lectura_firme, u'0.00')
        md2 = ap.medidas[1]
        self.assertFalse(md2.anomalia)
        self.assertFalse(md2.comentarios)
        self.assertEqual(md2.fecha_lectura_firme, u'2003-01-03')

    def test_t106(self):
        t1 = T1(self.xml_t106)
        t1.parse_xml()
        self.assertEqual(t1.datos_notificacion.fecha_activacion, u'2016-08-21')
        # Contrato
        self.assertEqual(t1.contrato.cod_contrato, u'00001')
        # Puntos Medida
        self.assertEqual(len(t1.puntos_medida), 1)
        pm = t1.puntos_medida[0]
        self.assertEqual(pm.cod_pm, u'ES1234000000000001JN0F')
        self.assertEqual(pm.tipo_movimiento, u'A')
        self.assertEqual(pm.tipo_pm, u'03')
        self.assertEqual(pm.cod_pm_principal, u'ES1234000000000002JN0F')
        self.assertEqual(pm.modo_lectura, u'1')
        self.assertEqual(pm.funcion, u'P')
        self.assertEqual(pm.direccion_enlace, u'39522')
        self.assertEqual(pm.direccion_punto_medida, u'000000001')
        self.assertEqual(pm.num_linea, u'12')
        self.assertEqual(pm.telefono_telemedida, u'987654321')
        self.assertEqual(pm.estado_telefono, u'1')
        self.assertEqual(pm.clave_acceso, u'0000000007')
        self.assertEqual(pm.tension_pm, u'0')
        self.assertEqual(pm.fecha_vigor, u'2003-01-01')
        self.assertEqual(pm.fecha_alta, u'2003-01-01')
        self.assertEqual(pm.fecha_baja, u'2003-02-01')
        self.assertEqual(pm.comentarios, u'Comentarios Varios')
        # Aparatos
        self.assertEqual(len(pm.aparatos), 1)
        ap = pm.aparatos[0]
        self.assertEqual(ap.cod_precinto, u'02')
        self.assertEqual(ap.constante_energia, u'1.000')
        self.assertEqual(ap.constante_maximetro, u'1.000')
        self.assertEqual(ap.funcion_aparato, u'M')
        self.assertEqual(ap.lectura_directa, u'N')
        self.assertEqual(ap.marca_aparato, u'132')
        self.assertEqual(ap.modelo_marca, u'011')
        self.assertEqual(ap.modo_medida_potencia, u'1')
        self.assertEqual(ap.num_integradores, u'18')
        self.assertEqual(ap.numero_serie, u'0000539522')
        self.assertEqual(ap.periodo_fabricacion, u'2005')
        self.assertEqual(ap.propietario, u'Desc. Propietario')
        self.assertEqual(ap.ruedas_decimales, u'02')
        self.assertEqual(ap.ruedas_enteras, u'08')
        self.assertEqual(ap.tipo_aparato, u'CG')
        self.assertEqual(ap.tipo_dhedm, u'6')
        self.assertEqual(ap.tipo_equipo_medida, u'L03')
        self.assertEqual(ap.tipo_movimiento, u'CX')
        self.assertEqual(ap.tipo_propiedad_aparato, u'1')
        # Medidas
        self.assertEqual(len(ap.medidas), 2)
        md = ap.medidas[0]
        self.assertEqual(md.anomalia, u'01')
        self.assertEqual(md.comentarios, u'Comentario sobre anomalia')
        self.assertEqual(md.fecha_lectura_firme, u'2003-01-02')
        self.assertEqual(md.magnitud_medida, u'PM')
        self.assertEqual(md.periodo, u'65')
        self.assertEqual(md.procedencia, u'30')
        self.assertEqual(md.tipo_dhedm, u'6')
        self.assertEqual(md.ultima_lectura_firme, u'0.00')
        md2 = ap.medidas[1]
        self.assertFalse(md2.anomalia)
        self.assertFalse(md2.comentarios)
        self.assertEqual(md2.fecha_lectura_firme, u'2003-01-03')

    def test_t110(self):
        t1 = T1(self.xml_t110)
        t1.parse_xml()
        self.assertEqual(t1.fecha_aceptacion, u'2016-06-06')


class test_MessageGas(unittest.TestCase):
    def setUp(self):
        self.xml_a241 = open(get_data("a241.xml"), "r")

    def tearDown(self):
        self.xml_a241.close()

    def test_gas_header(self):
        a1_41 = A1_41(self.xml_a241)
        a1_41.parse_xml()
        self.assertEqual(a1_41.get_codi_emisor, u'1234')
        self.assertEqual(a1_41.get_codi_destinatari, u'4321')
        self.assertEqual(a1_41.cups, u'ES1234000000000001JN')
        self.assertEqual(a1_41.codi_sollicitud, u'000123456789')
        self.assertEqual(a1_41.data_sollicitud, u'2018-05-01 12:00:00')


class test_A1_41(unittest.TestCase):

    def setUp(self):
        self.xml_a241 = open(get_data("a241.xml"), "r")
        self.xml_a341 = open(get_data("a341.xml"), "r")
        self.xml_a441 = open(get_data("a441.xml"), "r")
        self.xml_a3s41 = open(get_data("a3s41.xml"), "r")

    def tearDown(self):
        self.xml_a241.close()
        self.xml_a341.close()
        self.xml_a441.close()
        self.xml_a3s41.close()

    def test_a241(self):
        a1_41 = A1_41(self.xml_a241)
        a1_41.parse_xml()
        self.assertEqual(a1_41.StatusPS, u'1')
        self.assertEqual(a1_41.comreferencenum, u'000123456789')
        self.assertEqual(a1_41.cups, u'ES1234000000000001JN')
        self.assertEqual(a1_41.documentnum, u'11111111H')
        self.assertEqual(a1_41.documenttype, u'01')
        self.assertEqual(a1_41.extrainfo, u'comentarios extras')
        self.assertEqual(a1_41.foreseentransferdate, u'2018-06-01')
        self.assertEqual(a1_41.nationality, u'ES')
        self.assertEqual(a1_41.netsituation, u'red municipio')
        self.assertEqual(a1_41.newmodeffectdate, u'04')
        self.assertEqual(a1_41.qdgranted, u'987654321.1234567')
        self.assertEqual(a1_41.reqcode, u'0123456789')
        self.assertEqual(a1_41.reqestimatedqa, u'665544332211')
        self.assertEqual(a1_41.reqoutgoingpressure, u'54321.123')
        self.assertEqual(a1_41.reqqd, u'987654321.1234567')
        self.assertEqual(a1_41.reqqh, u'987654321')
        self.assertEqual(a1_41.responsedate, u'2018-05-01')
        self.assertEqual(a1_41.responsehour, u'13:00:00')
        self.assertEqual(a1_41.result, u'01')
        self.assertEqual(a1_41.resultdesc, u'Aceptada')
        self.assertEqual(a1_41.resultreason, u'R32')
        self.assertEqual(a1_41.resultreasondesc, u'Fecha efecto solicitada anterior al día actual.')
        self.assertEqual(a1_41.singlenomination, u'S')
        self.assertEqual(a1_41.tolltype, u'31')
        self.assertEqual(a1_41.updatereason, u'01')

        self.assertEqual(a1_41.productlist[0].productcode, u'TESTCODE1')
        self.assertEqual(a1_41.productlist[0].producttype, u'03')
        self.assertEqual(a1_41.productlist[0].producttolltype, u'31')
        self.assertEqual(a1_41.productlist[0].productqd, u'23.6')
        self.assertEqual(a1_41.productlist[0].productqa, u'12345')
        self.assertEqual(a1_41.productlist[0].productstartdate, u'2020-01-01')
        self.assertEqual(a1_41.productlist[0].productenddate, u'2020-02-01')

        self.assertEqual(a1_41.productlist[1].productcode, u'TESTCODE2')
        self.assertEqual(a1_41.productlist[1].producttype, u'02')
        self.assertEqual(a1_41.productlist[1].producttolltype, u'32')
        self.assertEqual(a1_41.productlist[1].productqd, u'23.5')
        self.assertEqual(a1_41.productlist[1].productqa, u'1234')
        self.assertEqual(a1_41.productlist[1].productstartdate, u'2020-01-02')
        self.assertEqual(a1_41.productlist[1].productenddate, u'2020-02-02')

    def test_a341(self):
        a1_41 = A1_41(self.xml_a341)
        a1_41.parse_xml()
        self.assertEqual(a1_41.StatusPS, u'1')
        self.assertEqual(a1_41.activationtype, u'001')
        self.assertEqual(a1_41.activationtypedesc, u'Realizada puesta en servicio')
        self.assertEqual(a1_41.atrcode, u'000111222333444555666777')
        self.assertEqual(a1_41.canonircperiodicity, u'01')
        self.assertEqual(a1_41.cityowner, u'17001')
        self.assertEqual(a1_41.closingtype, u'001')
        self.assertEqual(a1_41.closingtypedesc, u'La Actualización de Datos se ha realizado correctamente')
        self.assertEqual(a1_41.comreferencenum, u'000123456789')
        self.assertEqual(a1_41.cups, u'ES1234000000000001JN')
        self.assertEqual(a1_41.documentnum, u'11111111H')
        self.assertEqual(a1_41.documenttype, u'01')
        self.assertEqual(a1_41.doorowner, u'v')
        self.assertEqual(a1_41.email, u'gasalmatalas@atr.cat')
        self.assertEqual(a1_41.extrainfo, u'comentarios extras')
        self.assertEqual(a1_41.familyname1, u'Al')
        self.assertEqual(a1_41.familyname2, u'Matalas')
        self.assertEqual(a1_41.finalclientyearlyconsumption, u'665544332211')
        self.assertEqual(a1_41.finalqdgranted, u'987654321.1234567')
        self.assertEqual(a1_41.finalqhgranted, u'987654321')
        self.assertEqual(a1_41.firstname, u'Gas')
        self.assertEqual(a1_41.floorowner, u'4')
        self.assertEqual(a1_41.gasusetype, u'01')
        self.assertEqual(a1_41.interventiondate, u'2016-01-01')
        self.assertEqual(a1_41.interventionhourfrom, u'09:00:00')
        self.assertEqual(a1_41.interventionhourto, u'12:00:00')
        self.assertEqual(a1_41.language, u'01')
        self.assertEqual(a1_41.lastinspectionsdate, u'2017-01-01')
        self.assertEqual(a1_41.lastinspectionsresult, u'01')
        self.assertEqual(a1_41.lectureperiodicity, u'02')
        self.assertEqual(a1_41.nationality, u'ES')
        self.assertEqual(a1_41.portalowner, u'2')
        self.assertEqual(a1_41.provinceowner, u'17')
        self.assertEqual(a1_41.readingtype, u'1')
        self.assertEqual(a1_41.regularaddress, u'S')
        self.assertEqual(a1_41.reqcode, u'0123456789')
        self.assertEqual(a1_41.responsedate, u'2018-05-01')
        self.assertEqual(a1_41.responsehour, u'13:00:00')
        self.assertEqual(a1_41.result, u'09')
        self.assertEqual(a1_41.resultdesc, u'Realizada')
        self.assertEqual(a1_41.staircaseowner, u'3')
        self.assertEqual(a1_41.streetnumberowner, u'1')
        self.assertEqual(a1_41.streetowner, u'Carrer inventat')
        self.assertEqual(a1_41.streettypeowner, u'ACCE')
        self.assertEqual(a1_41.telemetering, u'S')
        self.assertEqual(a1_41.telephone1, u'999888777')
        self.assertEqual(a1_41.telephone2, u'666555444')
        self.assertEqual(a1_41.titulartype, u'F')
        self.assertEqual(a1_41.transfereffectivedate, u'2018-07-01')
        self.assertEqual(a1_41.updatereason, u'01')
        self.assertEqual(a1_41.visitnumber, u'987')
        self.assertEqual(a1_41.zipcodeowner, u'17002')
        self.assertEqual(len(a1_41.correctorlist), 2)
        corrector = a1_41.correctorlist[0]
        self.assertEqual(corrector.correctedlecture, u'2200')
        self.assertEqual(corrector.correctormodel, u'modelo1')
        self.assertEqual(corrector.correctornumber, u'D123456')
        self.assertEqual(corrector.correctorproperty, u'01')
        self.assertEqual(corrector.correctortype, u'01')
        self.assertEqual(len(a1_41.counterlist), 2)
        counter = a1_41.counterlist[1]
        self.assertEqual(counter.countermodel, u'marca2')
        self.assertEqual(counter.counternumber, u'C123456')
        self.assertEqual(counter.counterpressure, u'13245.321')
        self.assertEqual(counter.counterproperty, u'06')
        self.assertEqual(counter.countertype, u'tipo2')
        self.assertEqual(counter.reallecture, u'3000')

        self.assertEqual(a1_41.productlist[0].productcode, u'TESTCODE1')
        self.assertEqual(a1_41.productlist[0].producttype, u'03')
        self.assertEqual(a1_41.productlist[0].producttolltype, u'31')
        self.assertEqual(a1_41.productlist[0].productqd, u'23.6')
        self.assertEqual(a1_41.productlist[0].productqa, u'12345')
        self.assertEqual(a1_41.productlist[0].productstartdate, u'2020-01-01')
        self.assertEqual(a1_41.productlist[0].productenddate, u'2020-02-01')

        self.assertEqual(a1_41.productlist[1].productcode, u'TESTCODE2')
        self.assertEqual(a1_41.productlist[1].producttype, u'02')
        self.assertEqual(a1_41.productlist[1].producttolltype, u'32')
        self.assertEqual(a1_41.productlist[1].productqd, u'23.5')
        self.assertEqual(a1_41.productlist[1].productqa, u'1234')
        self.assertEqual(a1_41.productlist[1].productstartdate, u'2020-01-02')
        self.assertEqual(a1_41.productlist[1].productenddate, u'2020-02-02')

    def test_a441(self):
        a1_41 = A1_41(self.xml_a441)
        a1_41.parse_xml()
        self.assertEqual(a1_41.codi_sollicitud, u'000123456789')
        self.assertEqual(a1_41.comreferencenum, u'000123456789')
        self.assertEqual(a1_41.cups, u'ES1234000000000001JN')
        self.assertEqual(a1_41.documentnum, u'11111111H')
        self.assertEqual(a1_41.documenttype, u'01')
        self.assertEqual(a1_41.extrainfo, u'comentarios extras')
        self.assertEqual(a1_41.nationality, u'ES')
        self.assertEqual(a1_41.reqcode, u'0123456789')
        self.assertEqual(a1_41.responsedate, u'2018-05-01')
        self.assertEqual(a1_41.responsehour, u'13:00:00')
        self.assertEqual(a1_41.result, u'13')
        self.assertEqual(a1_41.resultdesc, u'No Realizada')
        self.assertEqual(a1_41.resultreason, u'R32')
        self.assertEqual(a1_41.resultreasondesc, u'Fecha efecto solicitada anterior al día actual.')
        self.assertEqual(a1_41.updatereason, u'01')
        self.assertEqual(a1_41.closingtype, u'064')
        self.assertEqual(a1_41.closingtypedesc, u'No quiere gas')
        self.assertEqual(a1_41.interventiondate, u'2016-01-01')
        self.assertEqual(a1_41.interventionhourfrom, u'09:00:00')
        self.assertEqual(a1_41.interventionhourto, u'12:00:00')
        self.assertEqual(a1_41.visitnumber, u'987')

    def test_a3s41(self):
        a1_41 = A1_41(self.xml_a3s41)
        a1_41.parse_xml()
        self.assertEqual(a1_41.previousatrcode, u'000111222333444555666777')
        self.assertEqual(a1_41.nationality, u'ES')
        self.assertEqual(a1_41.readingtype, u'1')
        self.assertEqual(a1_41.cups, u'ES1234000000000001JN')
        self.assertEqual(a1_41.documentnum, u'11111111H')
        self.assertEqual(a1_41.documenttype, u'01')
        self.assertEqual(a1_41.extrainfo, u'comentarios extras')
        self.assertEqual(a1_41.reqcode, u'0123456789')
        self.assertEqual(a1_41.responsedate, u'2018-05-01')
        self.assertEqual(a1_41.responsehour, u'13:00:00')
        self.assertEqual(a1_41.transfereffectivedate, u'2018-07-01')
        self.assertEqual(a1_41.codi_sollicitud, u'0123456789')
        self.assertEqual(len(a1_41.correctorlist), 2)
        corrector = a1_41.correctorlist[0]
        self.assertEqual(corrector.correctedlecture, u'2200')
        self.assertEqual(corrector.correctormodel, u'modelo1')
        self.assertEqual(corrector.correctornumber, u'D123456')
        self.assertEqual(corrector.correctorproperty, u'01')
        self.assertEqual(corrector.correctortype, u'01')
        self.assertEqual(len(a1_41.counterlist), 2)
        counter = a1_41.counterlist[1]
        self.assertEqual(counter.countermodel, u'marca2')
        self.assertEqual(counter.counternumber, u'C123456')
        self.assertEqual(counter.counterpressure, u'13245.321')
        self.assertEqual(counter.counterproperty, u'06')
        self.assertEqual(counter.countertype, u'tipo2')
        self.assertEqual(counter.reallecture, u'3000')


class test_B70(unittest.TestCase):

    def setUp(self):
        self.xml_b7031 = open(get_data("b7031.xml"), "r")
        self.xml_b7032 = open(get_data("b7032.xml"), "r")

    def tearDown(self):
        self.xml_b7031.close()
        self.xml_b7032.close()

    def test_b7031(self):
        b7031 = B7031(self.xml_b7031)
        b7031.parse_xml()

        # cabecera
        self.assertEqual(b7031.get_codi_emisor, u'1234')
        self.assertEqual(b7031.get_codi_destinatari, u'4321')
        self.assertEqual(b7031.cups, u'ES1234000000000001JN')
        self.assertEqual(b7031.codi_sollicitud, u'')
        self.assertEqual(b7031.data_sollicitud, u'2018-01-19 06:49:55')

        dest = b7031.datosempresadestino
        # Datosempresadestino
        self.assertEqual(dest.numdocumento, 'B24291833')
        self.assertEqual(dest.razonsocial, 'Destino, S.L.')
        self.assertEqual(dest.direccion, 'C inventat 1')
        self.assertEqual(dest.municipio, '28290 LAS ROZAS DE MADRID')

        em = b7031.datosempresaemisora
        # Datosempresaemisora
        self.assertEqual(em.numdocumento, 'B11254455')
        self.assertEqual(em.razonsocial, 'Emisora, S.A')
        self.assertEqual(em.direccion, 'C inventat 2')
        self.assertEqual(em.municipio, '28043 MADRID')
        self.assertEqual(em.regmercantil, 'Emisora, S.A. INSCRITA EM EL R. M. DE Coruscant')

        fact = b7031.facturas[0]
        # Factura
        self.assertEqual(fact.cups, 'ES1234000000000001JN')

        self.assertEqual(fact.contratosimultaneo, 'S')
        self.assertEqual(fact.codigoproducto, '123456')
        self.assertEqual(fact.tipoproducto, '01')
        self.assertEqual(fact.arrastrapenalizacion, 'N')

        self.assertEqual(fact.provincia, '22')
        self.assertEqual(fact.municipio, '22158')
        self.assertEqual(fact.codpostal, '22400')
        self.assertEqual(fact.tipovia, 'AV')
        self.assertEqual(fact.descalle, 'LERIDA')
        self.assertEqual(fact.numfinca, '53')
        self.assertEqual(fact.portal, '1')
        self.assertEqual(fact.escalera, '2')
        self.assertEqual(fact.piso, '3')
        self.assertEqual(fact.puerta, '4')
        self.assertEqual(fact.municipio_red, '22158')
        self.assertEqual(fact.tipodocumento, '01')
        self.assertEqual(fact.numdocumento, '11111111H')
        self.assertEqual(fact.nombre, 'Gas')
        self.assertEqual(fact.apellido1, 'Al')
        self.assertEqual(fact.apellido2, 'Matalas')
        self.assertEqual(fact.tipofactura, '01')
        self.assertEqual(fact.clasefact, 'N')
        self.assertEqual(fact.numfactorigen, '20180101')
        self.assertEqual(fact.fecfactura, '2018-01-19')
        self.assertEqual(fact.numfactura, 'RG01A18N00136042')
        self.assertEqual(fact.tipofacturacion, '1')
        self.assertEqual(fact.tipopeaje, '32')
        self.assertEqual(fact.feccontable, '2018-01-01')
        self.assertEqual(fact.fecpago, '2015-02-01')
        self.assertEqual(fact.importetotal, 70.2)
        self.assertEqual(fact.saldo_total_a_cobrar, 60.2)
        self.assertEqual(fact.idremesa, '0035194')
        self.assertEqual(fact.tipopenalizacion, 'N')
        self.assertEqual(fact.observaciones1, 'Obs1')
        self.assertEqual(fact.observaciones2, 'Obs2')
        self.assertEqual(fact.telefurgencias, '900900900')

        boe = fact.listaboe[1]
        # BOE
        self.assertEqual(boe.numboe, 'BOE NQM')
        self.assertEqual(boe.fecboe, '2013-12-31')

        self.assertEqual(len(fact.listaconceptos), 10)
        concepto = fact.listaconceptos[9]
        # Concepto
        self.assertEqual(concepto.fecdesde, '2017-12-01')
        self.assertEqual(concepto.fechasta, '2017-12-31')
        self.assertEqual(concepto.unidad, 1746.48)
        self.assertEqual(concepto.precunidad, 0.022413)
        self.assertEqual(concepto.importe, 39.14)
        self.assertEqual(concepto.codconcepto, '0017')
        self.assertEqual(concepto.desconcepto, 'Termino inventado')
        self.assertEqual(concepto.porcentajeconcepto, 2)
        self.assertEqual(concepto.impuestoconcepto, 'N')
        self.assertEqual(concepto.codtipoimpuesto, '01')
        self.assertEqual(concepto.porcentajeimpcto, 0)
        self.assertEqual(concepto.umconcepto, '02')
        self.assertEqual(concepto.aparatoconcepto, 'CO')
        self.assertEqual(concepto.observaciones, 'ObsCon')
        self.assertEqual(concepto.fec_desde_prorrateo, '2018-01-02')
        self.assertEqual(concepto.tipo_interes_demora, '12')

        self.assertEqual(len(fact.listamedidores), 2)
        medidor = fact.listamedidores[1]
        # Medidor
        self.assertEqual(medidor.um, 'M3')
        self.assertEqual(medidor.feclecant, '2017-12-01')
        self.assertEqual(medidor.horalecant, '20:00:00')
        self.assertEqual(medidor.feclecact, '2018-01-16')
        self.assertEqual(medidor.horalecact, '20:00:00')
        self.assertEqual(medidor.serializada, 'N')
        self.assertEqual(medidor.restadeserializada, '11')
        self.assertEqual(medidor.cupsresta, 'ES1234000000000001JN')
        self.assertEqual(medidor.aparato, 'CO')
        self.assertEqual(medidor.medicion, '06')
        self.assertEqual(medidor.modelomedidor, '20')
        self.assertEqual(medidor.numseriemedidor, '704414207')
        self.assertEqual(medidor.unipres, '2')
        self.assertEqual(medidor.presatm, '100')
        self.assertEqual(medidor.presionsuministro, '0.0500')
        self.assertEqual(medidor.temp, '28')
        self.assertEqual(medidor.factorconver, 11.462870)
        self.assertEqual(medidor.factork, 0.979900)
        self.assertEqual(medidor.pcs, 11.698000)
        self.assertEqual(medidor.zeta, '1')
        self.assertEqual(medidor.densidad, '2')
        self.assertEqual(medidor.n2, '3')
        self.assertEqual(medidor.co2, '4')
        self.assertEqual(medidor.h2, '5')
        self.assertEqual(medidor.consumokwh, 2647.92297)
        self.assertEqual(medidor.consumoereal, 2600)
        self.assertEqual(medidor.consumoreg, 2650)
        self.assertEqual(medidor.codajuste, '01')
        self.assertEqual(medidor.ajuste, 50)
        self.assertEqual(medidor.qdaplicado, 10)
        self.assertEqual(medidor.qdmaximo, 20)
        self.assertEqual(medidor.fecqdmax, '2018-01-03')
        self.assertEqual(medidor.dqmedio, '5')
        self.assertEqual(medidor.qdcontratado, 55)
        self.assertEqual(medidor.motivolec, '02')
        self.assertEqual(medidor.tipo_dh, '01')
        self.assertEqual(medidor.perlec, 'M')
        self.assertEqual(medidor.capacidadcontador, '2000')
        self.assertEqual(medidor.observaciones1, 'Obs1')
        self.assertEqual(medidor.observaciones2, 'Obs2')
        medidor.get_lectures_info()

        self.assertEqual(len(medidor.listanumeradores), 2)
        num = medidor.listanumeradores[1]
        # Numerador
        self.assertEqual(num.num, '2')
        self.assertEqual(num.digmed, '05')
        self.assertEqual(num.digdecmed, '02')
        self.assertEqual(num.factmulmed, '1.00')
        self.assertEqual(num.lectant, '9832.00')
        self.assertEqual(num.lecact, '10063.00')
        self.assertEqual(num.tipolec, '1')
        self.assertEqual(num.consumo, '231.00')
        self.assertEqual(num.tipolecnum, 'BR')
        self.assertEqual(num.aparatorelevante, 'S')
        self.assertEqual(num.observaciones, 'Obs1')

        self.assertEqual(len(fact.listafacturasinspeccion), 2)
        fins = fact.listafacturasinspeccion[1]
        # Facturasinspeccion
        self.assertEqual(fins.numdocumentoinstalador, '20')
        self.assertEqual(fins.razonsocialinstalador, 'Inspectora SA')
        self.assertEqual(fins.numfacturainspeccion, '20155152')

        self.assertEqual(len(fact.lista_contactos), 2)
        cont = fact.lista_contactos[1]
        # Contacto
        self.assertEqual(cont.denominacion, 'GTS')
        self.assertEqual(cont.url, 'WWW.ENAGAS.ES')
        self.assertEqual(cont.email, 'GTS@ENAGAS.ES')
        self.assertEqual(cont.telefono, '902443700')

        self.assertEqual(len(fact.historial_consumos), 2)
        cons = fact.historial_consumos[1]
        # Consumo
        self.assertEqual(cons.fecinicioperiodo, '2017-10-01')
        self.assertEqual(cons.fecfinperiodo, '2017-12-01')
        self.assertEqual(cons.consumoperiodo, '2000.92')

        impc = fact.imputacion_costes
        # Imputacioncostes
        self.assertEqual(impc.pcttasacnmc, '0.140')
        self.assertEqual(impc.pctcuotagts, '0.797')

    def test_b7032(self):
        b7032 = B7032(self.xml_b7032)
        b7032.parse_xml()

        # cabecera
        self.assertEqual(b7032.get_codi_emisor, u'1234')
        self.assertEqual(b7032.get_codi_destinatari, u'4321')
        self.assertEqual(b7032.cups, u'ES1234000000000001JN')
        self.assertEqual(b7032.codi_sollicitud, u'')
        self.assertEqual(b7032.data_sollicitud, u'2018-01-19 06:49:55')

        dest = b7032.datosempresadestino
        # Datosempresadestino
        self.assertEqual(dest.numdocumento, 'B24291833')
        self.assertEqual(dest.razonsocial, 'Destino, S.L.')
        self.assertEqual(dest.direccion, 'C inventat 1')
        self.assertEqual(dest.municipio, '28290 LAS ROZAS DE MADRID')

        em = b7032.datosempresaemisora
        # Datosempresaemisora
        self.assertEqual(em.numdocumento, 'B11254455')
        self.assertEqual(em.razonsocial, 'Emisora, S.A')
        self.assertEqual(em.direccion, 'C inventat 2')
        self.assertEqual(em.municipio, '28043 MADRID')
        self.assertEqual(em.regmercantil, 'Emisora, S.A. INSCRITA EM EL R. M. DE Coruscant')

        fact = b7032.facturas[0]
        # Factura
        self.assertEqual(fact.cups, 'ES1234000000000001JN')
        self.assertEqual(fact.provincia, '22')
        self.assertEqual(fact.municipio, '22158')
        self.assertEqual(fact.codpostal, '22400')
        self.assertEqual(fact.tipovia, 'AV')
        self.assertEqual(fact.descalle, 'LERIDA')
        self.assertEqual(fact.numfinca, '53')
        self.assertEqual(fact.portal, '1')
        self.assertEqual(fact.escalera, '2')
        self.assertEqual(fact.piso, '3')
        self.assertEqual(fact.puerta, '4')
        self.assertEqual(fact.municipio_red, '22158')
        self.assertEqual(fact.tipodocumento, '01')
        self.assertEqual(fact.numdocumento, '11111111H')
        self.assertEqual(fact.nombre, 'Gas')
        self.assertEqual(fact.apellido1, 'Al')
        self.assertEqual(fact.apellido2, 'Matalas')
        self.assertEqual(fact.tipofactura, '01')
        self.assertEqual(fact.clasefact, 'N')
        self.assertEqual(fact.numfactorigen, '20180101')
        self.assertEqual(fact.numpseudofactura, '222111')
        self.assertEqual(fact.fecfactura, '2018-01-19')
        self.assertEqual(fact.numfactura, 'RG01A18N00136042')
        self.assertEqual(fact.tipofacturacion, '1')
        self.assertEqual(fact.tipopeaje, '32')
        self.assertEqual(fact.importetotal, 70.2)
        self.assertEqual(fact.saldo_total_a_cobrar, 60.2)
        self.assertEqual(fact.tipopenalizacion, 'N')
        self.assertEqual(fact.observaciones1, 'Obs1')
        self.assertEqual(fact.observaciones2, 'Obs2')
        self.assertEqual(fact.telefurgencias, '900900900')

        boe = fact.listaboe[1]
        # BOE
        self.assertEqual(boe.numboe, 'BOE NQM')
        self.assertEqual(boe.fecboe, '2013-12-31')

        self.assertEqual(len(fact.listaconceptos), 10)
        concepto = fact.listaconceptos[9]
        # Concepto
        self.assertEqual(concepto.fecdesde, '2017-12-01')
        self.assertEqual(concepto.fechasta, '2017-12-31')
        self.assertEqual(concepto.unidad, 1746.48)
        self.assertEqual(concepto.precunidad, 0.022413)
        self.assertEqual(concepto.importe, 39.14)
        self.assertEqual(concepto.codconcepto, '0017')
        self.assertEqual(concepto.desconcepto, 'Termino inventado')
        self.assertEqual(concepto.porcentajeconcepto, 2)
        self.assertEqual(concepto.impuestoconcepto, 'N')
        self.assertEqual(concepto.codtipoimpuesto, '01')
        self.assertEqual(concepto.porcentajeimpcto, 0)
        self.assertEqual(concepto.umconcepto, '02')
        self.assertEqual(concepto.aparatoconcepto, 'CO')
        self.assertEqual(concepto.observaciones, 'ObsCon')
        self.assertEqual(concepto.fec_desde_prorrateo, '2018-01-02')
        self.assertEqual(concepto.tipo_interes_demora, '12')

        self.assertEqual(len(fact.listamedidores), 2)
        medidor = fact.listamedidores[1]
        # Medidor
        self.assertEqual(medidor.um, 'M3')
        self.assertEqual(medidor.feclecant, '2017-12-01')
        self.assertEqual(medidor.horalecant, '20:00:00')
        self.assertEqual(medidor.feclecact, '2018-01-16')
        self.assertEqual(medidor.horalecact, '20:00:00')
        self.assertEqual(medidor.serializada, 'N')
        self.assertEqual(medidor.restadeserializada, '11')
        self.assertEqual(medidor.cupsresta, 'ES1234000000000001JN')
        self.assertEqual(medidor.aparato, 'CO')
        self.assertEqual(medidor.medicion, '06')
        self.assertEqual(medidor.modelomedidor, '20')
        self.assertEqual(medidor.numseriemedidor, '704414207')
        self.assertEqual(medidor.unipres, '2')
        self.assertEqual(medidor.presatm, '100')
        self.assertEqual(medidor.presionsuministro, '0.0500')
        self.assertEqual(medidor.temp, '28')
        self.assertEqual(medidor.factorconver, 11.462870)
        self.assertEqual(medidor.factork, 0.979900)
        self.assertEqual(medidor.pcs, 11.698000)
        self.assertEqual(medidor.zeta, '1')
        self.assertEqual(medidor.densidad, '2')
        self.assertEqual(medidor.n2, '3')
        self.assertEqual(medidor.co2, '4')
        self.assertEqual(medidor.h2, '5')
        self.assertEqual(medidor.consumokwh, 2647.92297)
        self.assertEqual(medidor.consumoereal, 2600)
        self.assertEqual(medidor.consumoreg, 2650)
        self.assertEqual(medidor.codajuste, '01')
        self.assertEqual(medidor.ajuste, 50)
        self.assertEqual(medidor.qdaplicado, 10)
        self.assertEqual(medidor.qdmaximo, 20)
        self.assertEqual(medidor.fecqdmax, '2018-01-03')
        self.assertEqual(medidor.dqmedio, '5')
        self.assertEqual(medidor.qdcontratado, 55)
        self.assertEqual(medidor.motivolec, '02')
        self.assertEqual(medidor.tipo_dh, '01')
        self.assertEqual(medidor.perlec, 'M')
        self.assertEqual(medidor.capacidadcontador, '2000')
        self.assertEqual(medidor.observaciones1, 'Obs1')
        self.assertEqual(medidor.observaciones2, 'Obs2')

        self.assertEqual(len(medidor.listanumeradores), 2)
        num = medidor.listanumeradores[1]
        # Numerador
        self.assertEqual(num.num, '2')
        self.assertEqual(num.digmed, '05')
        self.assertEqual(num.digdecmed, '02')
        self.assertEqual(num.factmulmed, '1.00')
        self.assertEqual(num.lectant, '9832.00')
        self.assertEqual(num.lecact, '10063.00')
        self.assertEqual(num.tipolec, '1')
        self.assertEqual(num.consumo, '231.00')
        self.assertEqual(num.tipolecnum, 'BR')
        self.assertEqual(num.aparatorelevante, 'S')
        self.assertEqual(num.observaciones, 'Obs1')

        self.assertEqual(len(fact.listafacturasinspeccion), 2)
        fins = fact.listafacturasinspeccion[1]
        # Facturasinspeccion
        self.assertEqual(fins.numdocumentoinstalador, '20')
        self.assertEqual(fins.razonsocialinstalador, 'Inspectora SA')
        self.assertEqual(fins.numfacturainspeccion, '20155152')

        self.assertEqual(len(fact.lista_contactos), 2)
        cont = fact.lista_contactos[1]
        # Contacto
        self.assertEqual(cont.denominacion, 'GTS')
        self.assertEqual(cont.url, 'WWW.ENAGAS.ES')
        self.assertEqual(cont.email, 'GTS@ENAGAS.ES')
        self.assertEqual(cont.telefono, '902443700')

        self.assertEqual(len(fact.historial_consumos), 2)
        cons = fact.historial_consumos[1]
        # Consumo
        self.assertEqual(cons.fecinicioperiodo, '2017-10-01')
        self.assertEqual(cons.fecfinperiodo, '2017-12-01')
        self.assertEqual(cons.consumoperiodo, '2000.92')

        impc = fact.imputacion_costes
        # Imputacioncostes
        self.assertEqual(impc.pcttasacnmc, '0.140')
        self.assertEqual(impc.pctcuotagts, '0.797')


class test_A1_02(unittest.TestCase):

    def setUp(self):
        self.xml_a202 = open(get_data("a202.xml"), "r")
        self.xml_a302 = open(get_data("a302.xml"), "r")
        self.xml_a3s02 = open(get_data("a3s02.xml"), "r")
        self.xml_a402 = open(get_data("a402.xml"), "r")

    def tearDown(self):
        self.xml_a202.close()
        self.xml_a302.close()
        self.xml_a3s02.close()
        self.xml_a402.close()

    def test_a202(self):
        a202 = A1_02(self.xml_a202)
        a202.parse_xml()
        self.assertEqual(a202.reqcode, u'0123456789')
        self.assertEqual(a202.comreferencenum, u'000123456789')
        self.assertEqual(a202.responsedate, u'2018-05-01')
        self.assertEqual(a202.responsehour, u'13:00:00')
        self.assertEqual(a202.result, u'01')
        self.assertEqual(a202.resultdesc, u'Aceptada')
        self.assertEqual(a202.resultreason, u'R32')
        self.assertEqual(a202.resultreasondesc, u'Fecha efecto solicitada anterior al día actual.')
        self.assertEqual(a202.documentnum, u'11111111H')
        self.assertEqual(a202.nationality, u'ES')
        self.assertEqual(a202.documenttype, u'01')
        self.assertEqual(a202.cups, u'ES1234000000000001JN')
        self.assertEqual(a202.tolltype, u'31')
        self.assertEqual(a202.qdgranted, u'654321.1234')
        self.assertEqual(a202.outgoingpressuregranted, u'12345.123')
        self.assertEqual(a202.singlenomination, u'S')
        self.assertEqual(a202.netsituation, u'red municipio')
        self.assertEqual(a202.newmodeffectdate, u'04')
        self.assertEqual(a202.foreseentransferdate, u'2018-06-01')
        self.assertEqual(a202.StatusPS, u'1')
        self.assertEqual(a202.extrainfo, u'comentarios extras')
        producto = a202.productlist[0]
        self.assertEqual(producto.productcode, u'TESTCODE1')
        self.assertEqual(producto.producttype, u'03')
        self.assertEqual(producto.producttolltype, u'31')
        self.assertEqual(producto.productqd, u'23.6')
        self.assertEqual(producto.productqa, u'12345')
        self.assertEqual(producto.productstartdate, u'2020-01-01')
        self.assertEqual(producto.productenddate, u'2020-02-01')
        producto = a202.productlist[1]
        self.assertEqual(producto.productcode, u'TESTCODE2')
        self.assertEqual(producto.producttype, u'02')
        self.assertEqual(producto.producttolltype, u'32')
        self.assertEqual(producto.productqd, u'23.5')
        self.assertEqual(producto.productqa, u'1234')
        self.assertEqual(producto.productstartdate, u'2020-01-02')
        self.assertEqual(producto.productenddate, u'2020-02-02')

    def test_a302(self):
        a302 = A1_02(self.xml_a302)
        a302.parse_xml()
        self.assertEqual(a302.reqcode, u'0123456789')
        self.assertEqual(a302.comreferencenum, u'000123456789')
        self.assertEqual(a302.responsedate, u'2018-05-01')
        self.assertEqual(a302.responsehour, u'13:00:00')
        self.assertEqual(a302.titulartype, u'F')
        self.assertEqual(a302.nationality, u'ES')
        self.assertEqual(a302.documenttype, u'01')
        self.assertEqual(a302.documentnum, u'11111111H')
        self.assertEqual(a302.cups, u'ES1234000000000001JN')
        self.assertEqual(a302.lastinspectionsdate, u'2017-01-01')
        self.assertEqual(a302.lastinspectionsresult, u'01')
        self.assertEqual(a302.atrcode, u'000111222333444555666777')
        self.assertEqual(a302.transfereffectivedate, u'2018-07-01')
        self.assertEqual(a302.telemetering, u'S')
        self.assertEqual(a302.finalclientyearlyconsumption, u'665544332211')
        self.assertEqual(a302.readingtype, u'1')
        self.assertEqual(a302.gasusetype, u'01')
        self.assertEqual(a302.caecode, u'123456')
        self.assertEqual(a302.canonircperiodicity, u'01')
        self.assertEqual(a302.StatusPS, u'1')
        self.assertEqual(a302.lectureperiodicity, u'02')
        self.assertEqual(a302.extrainfo, u'comentarios extras')
        self.assertEqual(len(a302.correctorlist), 2)
        corrector = a302.correctorlist[0]
        self.assertEqual(corrector.correctedlecture, u'2200')
        self.assertEqual(corrector.correctormodel, u'modelo1')
        self.assertEqual(corrector.correctornumber, u'D123456')
        self.assertEqual(corrector.correctorproperty, u'01')
        self.assertEqual(corrector.correctortype, u'01')
        self.assertEqual(len(a302.counterlist), 2)
        counter = a302.counterlist[1]
        self.assertEqual(counter.countermodel, u'marca2')
        self.assertEqual(counter.counternumber, u'C123456')
        self.assertEqual(counter.counterpressure, u'13245.321')
        self.assertEqual(counter.counterproperty, u'06')
        self.assertEqual(counter.countertype, u'tipo2')
        self.assertEqual(counter.reallecture, u'3000')
        producto = a302.productlist[0]
        self.assertEqual(producto.productcode, u'TESTCODE1')
        self.assertEqual(producto.producttype, u'03')
        self.assertEqual(producto.producttolltype, u'31')
        self.assertEqual(producto.productqd, u'23.6')
        self.assertEqual(producto.productqa, u'12345')
        self.assertEqual(producto.productstartdate, u'2020-01-01')
        self.assertEqual(producto.productenddate, u'2020-02-01')
        producto = a302.productlist[1]
        self.assertEqual(producto.productcode, u'TESTCODE2')
        self.assertEqual(producto.producttype, u'02')
        self.assertEqual(producto.producttolltype, u'32')
        self.assertEqual(producto.productqd, u'23.5')
        self.assertEqual(producto.productqa, u'1234')
        self.assertEqual(producto.productstartdate, u'2020-01-02')
        self.assertEqual(producto.productenddate, u'2020-02-02')

    def test_a3s02(self):
        a3s02 = A1_02(self.xml_a3s02)
        a3s02.parse_xml()
        self.assertEqual(a3s02.previousatrcode, u'000111222333444555666777')
        self.assertEqual(a3s02.nationality, u'ES')
        self.assertEqual(a3s02.readingtype, u'1')
        self.assertEqual(a3s02.cups, u'ES1234000000000001JN')
        self.assertEqual(a3s02.documentnum, u'11111111H')
        self.assertEqual(a3s02.documenttype, u'01')
        self.assertEqual(a3s02.extrainfo, u'comentarios extras')
        self.assertEqual(a3s02.reqcode, u'0123456789')
        self.assertEqual(a3s02.responsedate, u'2018-05-01')
        self.assertEqual(a3s02.responsehour, u'13:00:00')
        self.assertEqual(a3s02.transfereffectivedate, u'2018-07-01')
        self.assertEqual(a3s02.codi_sollicitud, u'0123456789')
        self.assertEqual(len(a3s02.correctorlist), 2)
        corrector = a3s02.correctorlist[0]
        self.assertEqual(corrector.correctedlecture, u'2200')
        self.assertEqual(corrector.correctormodel, u'modelo1')
        self.assertEqual(corrector.correctornumber, u'D123456')
        self.assertEqual(corrector.correctorproperty, u'01')
        self.assertEqual(corrector.correctortype, u'01')
        self.assertEqual(len(a3s02.counterlist), 2)
        counter = a3s02.counterlist[1]
        self.assertEqual(counter.countermodel, u'marca2')
        self.assertEqual(counter.counternumber, u'C123456')
        self.assertEqual(counter.counterpressure, u'13245.321')
        self.assertEqual(counter.counterproperty, u'06')
        self.assertEqual(counter.countertype, u'tipo2')
        self.assertEqual(counter.reallecture, u'3000')

    def test_a402(self):
        a402 = A1_02(self.xml_a402)
        a402.parse_xml()
        self.assertEqual(a402.reqcode, u'0123456789')
        self.assertEqual(a402.comreferencenum, u'000123456789')
        self.assertEqual(a402.responsedate, u'2018-05-01')
        self.assertEqual(a402.responsehour, u'13:00:00')
        self.assertEqual(a402.result, u'13')
        self.assertEqual(a402.resultdesc, u'No Realizada')
        self.assertEqual(a402.resultreason, u'R32')
        self.assertEqual(a402.resultreasondesc, u'Fecha efecto solicitada anterior al día actual.')
        self.assertEqual(a402.titulartype, u'F')
        self.assertEqual(a402.nationality, u'ES')
        self.assertEqual(a402.documenttype, u'01')
        self.assertEqual(a402.documentnum, u'11111111H')
        self.assertEqual(a402.cups, u'ES1234000000000001JN')
        self.assertEqual(a402.extrainfo, u'comentarios extras')


class test_A1_05(unittest.TestCase):

    def setUp(self):
        self.xml_a205 = open(get_data("a205.xml"), "r")
        self.xml_a305 = open(get_data("a305.xml"), "r")
        self.xml_a405 = open(get_data("a405.xml"), "r")

    def tearDown(self):
        self.xml_a205.close()
        self.xml_a305.close()
        self.xml_a405.close()

    def test_a205(self):
        a205 = A1_05(self.xml_a205)
        a205.parse_xml()
        self.assertEqual(a205.reqcode, u'0123456789')
        self.assertEqual(a205.comreferencenum, u'000123456789')
        self.assertEqual(a205.responsedate, u'2018-05-01')
        self.assertEqual(a205.responsehour, u'13:00:00')
        self.assertEqual(a205.result, u'01')
        self.assertEqual(a205.resultdesc, u'Aceptada')
        self.assertEqual(a205.resultreason, u'R32')
        self.assertEqual(a205.resultreasondesc, u'Fecha efecto solicitada anterior al día actual.')
        self.assertEqual(a205.nationality, u'ES')
        self.assertEqual(a205.documentnum, u'11111111H')
        self.assertEqual(a205.documenttype, u'01')
        self.assertEqual(a205.cups, u'ES1234000000000001JN')
        self.assertEqual(a205.updatereason, u'01')
        self.assertEqual(a205.finaltolltypegranted, u'31')
        self.assertEqual(a205.qdgranted, u'987654321.1234567')
        self.assertEqual(a205.newmodeffectdate, u'04')
        self.assertEqual(a205.foreseentransferdate, u'2018-06-01')
        self.assertEqual(a205.extrainfo, u'comentarios extras')

    def test_a305(self):
        a305 = A1_05(self.xml_a305)
        a305.parse_xml()
        self.assertEqual(a305.tolltype, u'31')
        self.assertEqual(a305.caecode, u'9988')
        self.assertEqual(a305.atrcode, u'000111222333444555666777')
        self.assertEqual(a305.cityowner, u'17001')
        self.assertEqual(a305.comreferencenum, u'000123456789')
        self.assertEqual(a305.cups, u'ES1234000000000001JN')
        self.assertEqual(a305.documentnum, u'11111111H')
        self.assertEqual(a305.documenttype, u'01')
        self.assertEqual(a305.doorowner, u'v')
        self.assertEqual(a305.email, u'gasalmatalas@atr.cat')
        self.assertEqual(a305.extrainfo, u'comentarios extras')
        self.assertEqual(a305.familyname1, u'Al')
        self.assertEqual(a305.familyname2, u'Matalas')
        self.assertEqual(a305.qdgranted, u'987654321.1234567')
        self.assertEqual(a305.firstname, u'Gas')
        self.assertEqual(a305.floorowner, u'4')
        self.assertEqual(a305.nationality, u'ES')
        self.assertEqual(a305.portalowner, u'2')
        self.assertEqual(a305.provinceowner, u'17')
        self.assertEqual(a305.regularaddress, u'S')
        self.assertEqual(a305.reqcode, u'0123456789')
        self.assertEqual(a305.responsedate, u'2018-05-01')
        self.assertEqual(a305.responsehour, u'13:00:00')
        self.assertEqual(a305.result, u'09')
        self.assertEqual(a305.resultdesc, u'Realizada')
        self.assertEqual(a305.staircaseowner, u'3')
        self.assertEqual(a305.streetnumberowner, u'1')
        self.assertEqual(a305.streetowner, u'Carrer inventat')
        self.assertEqual(a305.streettypeowner, u'ACCE')
        self.assertEqual(a305.telephone, u'999888777')
        self.assertEqual(a305.fax, u'666555444')
        self.assertEqual(a305.titulartype, u'F')
        self.assertEqual(a305.transfereffectivedate, u'2018-07-01')
        self.assertEqual(a305.updatereason, u'01')
        self.assertEqual(a305.zipcodeowner, u'17002')
        self.assertEqual(len(a305.correctorlist), 2)
        corrector = a305.correctorlist[0]
        self.assertEqual(corrector.correctedlecture, u'2200')
        self.assertEqual(corrector.correctormodel, u'modelo1')
        self.assertEqual(corrector.correctornumber, u'D123456')
        self.assertEqual(corrector.correctorproperty, u'01')
        self.assertEqual(corrector.correctortype, u'01')
        self.assertEqual(len(a305.counterlist), 2)
        counter = a305.counterlist[1]
        self.assertEqual(counter.countermodel, u'marca2')
        self.assertEqual(counter.counternumber, u'C123456')
        self.assertEqual(counter.counterpressure, u'13245.321')
        self.assertEqual(counter.counterproperty, u'06')
        self.assertEqual(counter.countertype, u'tipo2')
        self.assertEqual(counter.reallecture, u'3000')

    def test_a405(self):
        a405 = A1_05(self.xml_a405)
        a405.parse_xml()
        self.assertEqual(a405.codi_sollicitud, u'000123456789')
        self.assertEqual(a405.comreferencenum, u'000123456789')
        self.assertEqual(a405.cups, u'ES1234000000000001JN')
        self.assertEqual(a405.extrainfo, u'comentarios extras')
        self.assertEqual(a405.reqcode, u'0123456789')
        self.assertEqual(a405.responsedate, u'2018-05-01')
        self.assertEqual(a405.responsehour, u'13:00:00')
        self.assertEqual(a405.result, u'13')
        self.assertEqual(a405.resultdesc, u'No Realizada')
        self.assertEqual(a405.resultreason, u'R32')
        self.assertEqual(a405.resultreasondesc, u'Fecha efecto solicitada anterior al día actual.')
        self.assertEqual(a405.updatereason, u'01')


class test_A1_44(unittest.TestCase):

    def setUp(self):
        self.xml_a244 = open(get_data("a244.xml"), "r")
        self.xml_a344 = open(get_data("a344.xml"), "r")
        self.xml_a444 = open(get_data("a444.xml"), "r")

    def tearDown(self):
        self.xml_a244.close()
        self.xml_a344.close()
        self.xml_a444.close()

    def test_a244(self):
        a244 = A1_44(self.xml_a244)
        a244.parse_xml()
        self.assertEqual(a244.reqcode, u'0123456789')
        self.assertEqual(a244.reqdate, u'2018-05-01')
        self.assertEqual(a244.reqhour, u'13:00:00')
        self.assertEqual(a244.comreferencenum, u'000123456789')
        self.assertEqual(a244.cups, u'ES1234000000000001JN')
        self.assertEqual(a244.operationtype, u'A10011')
        self.assertEqual(a244.responsedate, u'2018-05-01')
        self.assertEqual(a244.responsehour, u'13:00:00')
        self.assertEqual(a244.result, u'01')
        self.assertEqual(a244.resultdesc, u'Aceptada')
        self.assertEqual(a244.resultreason, u'R32')
        self.assertEqual(a244.resultreasondesc, u'Fecha efecto solicitada anterior al día actual.')
        self.assertEqual(a244.srcode, u'998877665544332211')
        self.assertEqual(a244.extrainfo, u'Coments')

    def test_a344(self):
        a344 = A1_44(self.xml_a344)
        a344.parse_xml()
        self.assertEqual(a344.reqcode, u'0123456789')
        self.assertEqual(a344.reqdate, u'2018-05-01')
        self.assertEqual(a344.reqhour, u'13:00:00')
        self.assertEqual(a344.comreferencenum, u'000123456789')
        self.assertEqual(a344.cups, u'ES1234000000000001JN')
        self.assertEqual(a344.operationtype, u'A10011')
        self.assertEqual(a344.responsedate, u'2018-05-01')
        self.assertEqual(a344.responsehour, u'13:00:00')
        self.assertEqual(a344.result, u'09')
        self.assertEqual(a344.resultdesc, u'Realizada')
        self.assertEqual(a344.activationtype, u'001')
        self.assertEqual(a344.activationtypedesc, u'Realizada puesta en servicio')
        self.assertEqual(a344.closingtype, u'001')
        self.assertEqual(a344.closingtypedesc, u'La Actualización de Datos se ha realizado correctamente')
        self.assertEqual(a344.reqdescription, u'Desc')
        self.assertEqual(a344.interventiondate, u'2016-01-01')
        self.assertEqual(a344.interventionhour, u'09:00:00')
        self.assertEqual(a344.resultinspection, u'01')
        self.assertEqual(a344.resultinspectiondesc, u'Correcto')
        self.assertEqual(a344.operationnum, u'9874')
        self.assertEqual(a344.visitnumber, u'0000')
        self.assertEqual(a344.counterchange, u'S')
        self.assertEqual(a344.removallecture, u'56')
        self.assertEqual(a344.supplystatus, u'05')
        self.assertEqual(a344.supplystatusdesc, u'CORTE POR FALTA DE PAGO')
        self.assertEqual(a344.servicestatus, u'00')
        self.assertEqual(a344.servicestatusdesc, u'EN SERVICIO')
        self.assertEqual(a344.extrainfo, u'Coment')
        self.assertEqual(a344.conceptnumber, u'2')
        self.assertEqual(len(a344.conceptlist), 2)
        concept = a344.conceptlist[1]
        self.assertEqual(concept.level, u'1')
        self.assertEqual(concept.code, u'0002')
        self.assertEqual(concept.description, u'Desc')
        self.assertEqual(concept.periodicity, u'03')
        self.assertEqual(concept.units, u'1')
        self.assertEqual(concept.unitimport, u'23.8')
        self.assertEqual(concept.import_, u'23.8')
        self.assertEqual(len(a344.counterlist), 2)
        counter = a344.counterlist[1]
        self.assertEqual(counter.countermodel, u'marca2')
        self.assertEqual(counter.counternumber, u'C123456')
        self.assertEqual(counter.counterpressure, u'13245.321')
        self.assertEqual(counter.counterproperty, u'06')
        self.assertEqual(counter.countertype, u'tipo2')
        self.assertEqual(counter.reallecture, u'3000')
        self.assertEqual(len(a344.defectlist), 2)
        defect = a344.defectlist[1]
        self.assertEqual(defect.code, u'002')
        self.assertEqual(defect.description, u'Desc2')
        self.assertEqual(len(a344.registerdoclist), 2)
        registerdoc = a344.registerdoclist[1]
        self.assertEqual(registerdoc.date, u'2018-01-01')
        self.assertEqual(registerdoc.doctype, u'02')
        self.assertEqual(registerdoc.url, u'http://gasalmatalas.com')
        self.assertEqual(registerdoc.extrainfo, u'Comments')

    def test_a444(self):
        a444 = A1_44(self.xml_a444)
        a444.parse_xml()
        self.assertEqual(a444.reqcode, u"10_Aql6Crc")
        self.assertEqual(a444.reqdate, u"2018-09-03")
        self.assertEqual(a444.reqhour, u"15:53:48")
        self.assertEqual(a444.comreferencenum, u"123456789")
        self.assertEqual(a444.cups, u"20aXn4jOtXkA8PF9JCHH")
        self.assertEqual(a444.operationtype, u"A10001")
        self.assertEqual(a444.responsedate, u"2018-09-03")
        self.assertEqual(a444.responsehour, u"15:53:48")
        self.assertEqual(a444.result, u"13")
        self.assertEqual(a444.resultdesc, u"No Realizada")
        self.assertEqual(a444.resultreason, u"R01")
        self.assertEqual(a444.resultreasondesc, u"Cliente suministrado desde planta satélite.")
        self.assertEqual(a444.closingtype, u"001")
        self.assertEqual(a444.closingtypedesc, u"La Actualización de Datos se ha realizado correctamente")
        self.assertEqual(a444.reqdescription, u"255_jK4VNLI9yGHM2iXotIhngmDIbQsVCh")
        self.assertEqual(a444.interventiondate, u"2018-09-03")
        self.assertEqual(a444.interventionhour, u"15:53:48")
        self.assertEqual(a444.resultinspection, u"01")
        self.assertEqual(a444.resultinspectiondesc, u"CORRECTO")
        self.assertEqual(a444.operationnum, u"40_Q6UldWk39wNRX5s2uSkVIponc3dAVu")
        self.assertEqual(a444.visitnumber, u"324")
        self.assertEqual(a444.counterchange, u"S")
        self.assertEqual(a444.removallecture, u"15065352")
        self.assertEqual(a444.supplystatus, u"00")
        self.assertEqual(a444.supplystatusdesc, u"PENDIENTE COMUNICACION DE OBRA CORRIENTE")
        self.assertEqual(a444.servicestatus, u"00")
        self.assertEqual(a444.servicestatusdesc, u"EN SERVICIO")
        self.assertEqual(a444.extrainfo, u"400_iicHtFZt43x9GRffBbuEvZACvCUGr4")
        self.assertEqual(a444.conceptnumber, u"95")
        concept = a444.conceptlist[0]
        self.assertEqual(concept.level, u"1")
        self.assertEqual(concept.code, u"0000")
        self.assertEqual(concept.description, u"Importe Total Factura")
        self.assertEqual(concept.periodicity, u"01")
        self.assertEqual(concept.units, u"66")
        self.assertEqual(concept.unitimport, u"55445.71")
        self.assertEqual(concept.import_, u"4016102.9")
        counter = a444.counterlist[0]
        self.assertEqual(counter.countermodel, u"50_jr23Qy5fvVmQ2FtjhwovVAY8mxigTk")
        self.assertEqual(counter.countertype, u"7_UbbtS")
        self.assertEqual(counter.counternumber, u"18_KbFpIkwTRIBDnU6")
        self.assertEqual(counter.counterproperty, u"04")
        self.assertEqual(counter.reallecture, u"36119625759")
        self.assertEqual(counter.counterpressure, u"18000.079")
        defect = a444.defectlist[0]
        self.assertEqual(defect.code, u"001")
        self.assertEqual(defect.description, u"FUGA DE GAS")
        registerdoc = a444.registerdoclist[0]
        self.assertEqual(registerdoc.date, u"2018-09-03")
        self.assertEqual(registerdoc.doctype, u"CC")
        self.assertEqual(registerdoc.url, u"255_fNTPLw5NQGEdAC6TzZrLSetqW7K6PY")
        self.assertEqual(registerdoc.extrainfo, u"255_ieYyI19A1KmTmbsNs5i3ycsbRc01Rx")


class test_A1_03(unittest.TestCase):

    def setUp(self):
        self.xml_a203 = open(get_data("a203.xml"), "r")
        self.xml_a2s03 = open(get_data("a2s03.xml"), "r")

    def tearDown(self):
        self.xml_a203.close()
        self.xml_a2s03.close()

    def test_a203(self):
        a203 = A1_03(self.xml_a203)
        a203.parse_xml()
        self.assertEqual(a203.reqcode, u'0123456789')
        self.assertEqual(a203.comreferencenum, u'000123456789')
        self.assertEqual(a203.cups, u'ES1234000000000001JN')
        self.assertEqual(a203.responsedate, u'2018-05-01')
        self.assertEqual(a203.responsehour, u'13:00:00')
        self.assertEqual(a203.result, u'01')
        self.assertEqual(a203.resultdesc, u'Aceptada')
        self.assertEqual(a203.resultreason, u'R32')
        self.assertEqual(a203.resultreasondesc, u'Fecha efecto solicitada anterior al día actual.')
        self.assertEqual(a203.extrainfo, u'Coments')
        self.assertEqual(a203.nationality, u"ES")
        self.assertEqual(a203.documenttype, u"01")
        self.assertEqual(a203.documentnum, u"ES11111111H")
        self.assertEqual(a203.annulmentreason, u"002")

    def test_a2s03(self):
        a203 = A1_03(self.xml_a2s03)
        a203.parse_xml()
        self.assertEqual(a203.reqcode, u'0123456789')
        self.assertEqual(a203.cups, u'ES1234000000000001JN')
        self.assertEqual(a203.responsedate, u'2018-05-01')
        self.assertEqual(a203.responsehour, u'13:00:00')
        self.assertEqual(a203.result, u'01')
        self.assertEqual(a203.resultdesc, u'Aceptada')
        self.assertEqual(a203.extrainfo, u'Coments')
        self.assertEqual(a203.nationality, u"ES")
        self.assertEqual(a203.documenttype, u"01")
        self.assertEqual(a203.documentnum, u"ES11111111H")
        self.assertEqual(a203.annulmentreason, u"002")


class test_A1_04(unittest.TestCase):

    def setUp(self):
        self.xml_a204 = open(get_data("a204.xml"), "r")
        self.xml_a304 = open(get_data("a304.xml"), "r")
        self.xml_a404 = open(get_data("a404.xml"), "r")

    def tearDown(self):
        self.xml_a204.close()
        self.xml_a304.close()
        self.xml_a404.close()

    def test_a204(self):
        a204 = A1_04(self.xml_a204)
        a204.parse_xml()

        self.assertEqual(a204.reqcode, '0123456789')
        self.assertEqual(a204.comreferencenum, '000123456789')
        self.assertEqual(a204.responsedate, '2018-05-01')
        self.assertEqual(a204.responsehour, '13:00:00')
        self.assertEqual(a204.result, '01')
        self.assertEqual(a204.resultdesc, 'Aceptada')
        self.assertEqual(a204.nationality, 'ES')
        self.assertEqual(a204.documenttype, '01')
        self.assertEqual(a204.documentnum, '11111111H')
        self.assertEqual(a204.cups, 'ES1234000000000001JN')
        self.assertEqual(a204.cancelreason, '04')
        self.assertEqual(a204.newmodeffectdate, '04')
        self.assertEqual(a204.foreseentransferdate, '2018-06-01')
        self.assertEqual(
            a204.extrainfo,
            u'Información adicional con la ubicación del tesoro de Mary Read'
        )

    def test_a304(self):
        a304 = A1_04(self.xml_a304)
        a304.parse_xml()

        self.assertEqual(a304.reqcode, '0123456789')
        self.assertEqual(a304.comreferencenum, '000123456789')
        self.assertEqual(a304.responsedate, '2018-05-01')
        self.assertEqual(a304.responsehour, '13:00:00')
        self.assertEqual(a304.titulartype, 'F')
        self.assertEqual(a304.nationality, 'ES')
        self.assertEqual(a304.documenttype, '01')
        self.assertEqual(a304.documentnum, '11111111H')
        self.assertEqual(a304.result, '09')
        self.assertEqual(a304.resultdesc, 'Realizada')
        self.assertEqual(a304.activationtype, '001')
        self.assertEqual(a304.activationtypedesc, 'Realizada puesta en servicio')
        self.assertEqual(a304.cups, 'ES1234000000000001JN')
        self.assertEqual(a304.atrcode, '000111222333444555666777')

        self.assertEqual(a304.operationnum, '4444448877787879894898189881848844894894')
        self.assertEqual(a304.moreinformation, 'N')
        self.assertEqual(a304.transfereffectivedate, '2018-07-01')
        self.assertEqual(
            a304.extrainfo,
            u'Información adicional con la ubicación del tesoro de Mary Read'
        )

        counter = a304.counterlist[0]

        self.assertEqual(counter.countermodel, u"marca1")
        self.assertEqual(counter.countertype, u"tipo1")
        self.assertEqual(counter.counternumber, u"B123456")
        self.assertEqual(counter.counterproperty, u"04")
        self.assertEqual(counter.reallecture, u"2000")
        self.assertEqual(counter.counterpressure, u"54321.123")

        counter2 = a304.counterlist[1]

        self.assertEqual(counter2.countermodel, u"marca2")
        self.assertEqual(counter2.countertype, u"tipo2")
        self.assertEqual(counter2.counternumber, u"C123456")
        self.assertEqual(counter2.counterproperty, u"06")
        self.assertEqual(counter2.reallecture, u"3000")
        self.assertEqual(counter2.counterpressure, u"13245.321")

        corrector = a304.correctorlist[0]
        self.assertEqual(corrector.correctedlecture, u'2200')
        self.assertEqual(corrector.correctormodel, u'modelo1')
        self.assertEqual(corrector.correctornumber, u'D123456')
        self.assertEqual(corrector.correctorproperty, u'01')
        self.assertEqual(corrector.correctortype, u'01')

        corrector2 = a304.correctorlist[1]
        self.assertEqual(corrector2.correctedlecture, u'3300')
        self.assertEqual(corrector2.correctormodel, u'modelo2')
        self.assertEqual(corrector2.correctornumber, u'E654321')
        self.assertEqual(corrector2.correctorproperty, u'02')
        self.assertEqual(corrector2.correctortype, u'02')

        self.assertEqual(len(a304.counterlist), 2)

    def test_a404(self):
        a404 = A1_04(self.xml_a404)
        a404.parse_xml()

        self.assertEqual(a404.reqcode, '0123456789')
        self.assertEqual(a404.comreferencenum, '000123456789')
        self.assertEqual(a404.responsedate, '2018-05-01')
        self.assertEqual(a404.responsehour, '13:00:00')
        self.assertEqual(a404.titulartype, 'F')
        self.assertEqual(a404.nationality, 'ES')
        self.assertEqual(a404.documenttype, '01')
        self.assertEqual(a404.documentnum, '11111111H')
        self.assertEqual(a404.result, '13')
        self.assertEqual(a404.resultdesc, 'No Realizada')


class test_A1_48(unittest.TestCase):

    def setUp(self):
        self.xml_a148 = open(get_data("a148.xml"), "r")
        self.xml_a248 = open(get_data("a248.xml"), "r")
        self.xml_a2548 = open(get_data("a2548.xml"), "r")
        self.xml_a2648 = open(get_data("a2648.xml"), "r")
        self.xml_a348 = open(get_data("a348.xml"), "r")

    def tearDown(self):
        self.xml_a148.close()
        self.xml_a248.close()
        self.xml_a2548.close()
        self.xml_a2648.close()
        self.xml_a348.close()

    def test_a148(self):
        a148 = A1_48(self.xml_a148)
        a148.parse_xml()
        self.assertEqual(a148.comreferencenum, u'000123456789')
        self.assertEqual(a148.cups, u'ES1234000000000001JN')

        self.assertEqual(a148.claimertype, u"01")
        claimer = a148.claimer
        claimerid = claimer.claimerid
        self.assertEqual(claimerid.claimerdocumenttype, u"01")
        self.assertEqual(claimerid.claimerdocumentnum, u"ES00000000T")
        claimername = claimer.claimername
        self.assertEqual(claimername.claimerfirstname, u"gas")
        self.assertEqual(claimername.claimerlastname, u"al")
        self.assertEqual(claimername.claimersecondname, u"matalas")
        claimertelephone = claimer.claimertelephone
        self.assertEqual(claimertelephone.claimerprefixtel1, u"34")
        self.assertEqual(claimertelephone.claimertelephone1, u"999888777")
        self.assertEqual(claimer.claimeremail, u"gas@matalas")
        self.assertEqual(a148.claimtype, u"01")
        self.assertEqual(a148.claimsubtype, u"001")
        self.assertEqual(a148.originreference, u"AB999888")
        claimreference = a148.claimreferencelist[0]
        self.assertEqual(claimreference.wrongattentiontype, u"01")
        self.assertEqual(claimreference.comreferencenum, u"0000001")
        self.assertEqual(claimreference.targetclaimcomreferencenum, u"9999998")
        self.assertEqual(claimreference.conceptcontract, u"01")
        self.assertEqual(claimreference.conceptfacturation, u"02")
        contact = claimreference.contact
        self.assertEqual(contact.contactname, u"mortdegana")
        contacttelephone = contact.contacttelephone
        self.assertEqual(contacttelephone.telephoneprefix, u"+34")
        self.assertEqual(contacttelephone.telephonenumber, u"666555444")
        self.assertEqual(contact.contactemail, u"matalas@gas")
        self.assertEqual(claimreference.nnssexpedient, u"45666666")
        self.assertEqual(claimreference.fraudrecordnum, u"888888888")
        incidentperiod = claimreference.incidentperiod
        self.assertEqual(incidentperiod.datefrom, u"2018-09-21")
        self.assertEqual(incidentperiod.dateto, u"2018-09-21")
        self.assertEqual(claimreference.invoicenumber, u"F5555")
        incidentlocation = claimreference.incidentlocation
        self.assertEqual(incidentlocation.incidentlocationdesc, u"calle pequeña")
        self.assertEqual(incidentlocation.incidentlocationprovince, u"01")
        self.assertEqual(incidentlocation.incidentlocationcity, u"000001")
        self.assertEqual(incidentlocation.incidentlocationcitysubdivision, u"17079000503")
        self.assertEqual(incidentlocation.incidentlocationzipcode, u"17888")
        reading = claimreference.reading
        self.assertEqual(reading.readingdate, u"2018-09-21")
        self.assertEqual(reading.readingvalue, u"4.89")
        incident = claimreference.incident
        self.assertEqual(incident.incidentdate, u"2018-09-21")
        client = claimreference.client
        document = client.document
        self.assertEqual(document.documenttype, u"01")
        self.assertEqual(document.documentnum, u"ES11111111T")
        self.assertEqual(client.titulartype, u"F")
        name = client.name
        self.assertEqual(name.firstname, u"nom")
        self.assertEqual(name.familyname1, u"cognom")
        self.assertEqual(name.familyname2, u"cognom 2")
        telephone = client.telephone
        self.assertEqual(telephone.telephoneprefix, u"34")
        self.assertEqual(telephone.telephonenumber, u"999111222")
        self.assertEqual(client.email, u"a@a")
        clientaddress = client.clientaddress
        self.assertEqual(clientaddress.province, u"01")
        self.assertEqual(clientaddress.city, u"000001")
        self.assertEqual(clientaddress.zipcode, u"16001")
        self.assertEqual(clientaddress.streettype, u"ACCE")
        self.assertEqual(clientaddress.street, u"inventat")
        self.assertEqual(clientaddress.streetnumber, u"4_ce")
        self.assertEqual(clientaddress.portal, u"5_TE2")
        self.assertEqual(clientaddress.staircase, u"5_mIh")
        self.assertEqual(clientaddress.floor, u"5_e6A")
        self.assertEqual(clientaddress.door, u"5_40T")
        self.assertEqual(claimreference.claimedcompensation, u"520176666.24")
        self.assertEqual(claimreference.iban, u"ES0000000000000000000000000000000")
        self.assertEqual(a148.cups, u"ES1234000000000001JN")
        self.assertEqual(a148.legallimitdate, u"2018-09-21")
        self.assertEqual(a148.priority, u"1")
        self.assertEqual(a148.extrainfo, u"comentarios extra")
        self.assertEqual(len(a148.registerdoclist), 2)
        registerdoc = a148.registerdoclist[1]
        self.assertEqual(registerdoc.date, u'2018-05-03')
        self.assertEqual(registerdoc.doctype, u'01')
        self.assertEqual(registerdoc.url, u'http://www.gasalmatalas.com')
        self.assertEqual(registerdoc.extrainfo, u'Comments')

    def test_a248(self):
        a248 = A1_48(self.xml_a248)
        a248.parse_xml()
        self.assertEqual(a248.comreferencenum, u'000123456789')
        self.assertEqual(a248.cups, u'ES1234000000000001JN')
        self.assertEqual(a248.reqcode, u"0123456789")
        self.assertEqual(a248.reqdate, u"2018-09-24")
        self.assertEqual(a248.reqhour, u"15:01:41")
        self.assertEqual(a248.responsedate, u"2018-05-01")
        self.assertEqual(a248.responsehour, u"13:00:00")
        self.assertEqual(a248.comreferencenum, u"000123456789")
        self.assertEqual(a248.claimtype, u"01")
        self.assertEqual(a248.claimsubtype, u"001")
        self.assertEqual(a248.cups, u"ES1234000000000001JN")
        self.assertEqual(a248.result, u"01")
        self.assertEqual(a248.resultdesc, u"Aceptada")
        self.assertEqual(a248.resultreason, u"R01")
        self.assertEqual(a248.resultreasondesc, u"Cliente suministrado desde planta satélite.")
        self.assertEqual(a248.srcode, u"00010")
        self.assertEqual(a248.extrainfo, u"comentarios extras")

    def test_a2548(self):
        a2548 = A1_48(self.xml_a2548)
        a2548.parse_xml()
        self.assertEqual(a2548.reqcode, u"123456789")
        self.assertEqual(a2548.responsedate, u"2018-09-24")
        self.assertEqual(a2548.responsehour, u"15:25:18")
        self.assertEqual(a2548.comreferencenum, u"987654321")
        self.assertEqual(a2548.sequential, u"01")
        self.assertEqual(a2548.claimtype, u"01")
        self.assertEqual(a2548.claimsubtype, u"001")
        self.assertEqual(a2548.cups, u"ES1234000000000001JN")
        self.assertEqual(a2548.srcode, u"99988")
        self.assertEqual(a2548.interventiontype, u"01")
        self.assertEqual(a2548.newclaimtype, u"01")
        self.assertEqual(a2548.newclaimsubtype, u"001")
        self.assertEqual(a2548.operationnum, u"741")
        self.assertEqual(a2548.visitdate, u"2018-09-24")
        self.assertEqual(a2548.visithour, u"15:25:18")
        self.assertEqual(a2548.informationtype, u"002")
        self.assertEqual(a2548.resultreasonintervention, u"R01")
        self.assertEqual(a2548.interventiondate, u"2018-09-24")
        self.assertEqual(a2548.interventionhourfrom, u"15:25:18")
        self.assertEqual(a2548.interventionhourto, u"15:25:18")
        self.assertEqual(a2548.resultinspection, u"01")
        self.assertEqual(a2548.visitnumber, u"590")
        self.assertEqual(a2548.extrainfo, u"coments")
        counter = a2548.counterlist[0]
        self.assertEqual(counter.countermodel, u"model")
        self.assertEqual(counter.countertype, u"55")
        self.assertEqual(counter.counternumber, u"9999")
        self.assertEqual(counter.counterproperty, u"04")
        self.assertEqual(counter.reallecture, u"68104264290")
        self.assertEqual(counter.counterpressure, u"83819.042")
        defect = a2548.defectlist[0]
        self.assertEqual(defect.code, u"001")
        self.assertEqual(defect.description, u"FUGA DE GAS")
        registerdoc = a2548.registerdoclist[0]
        self.assertEqual(registerdoc.date, u"2018-09-24")
        self.assertEqual(registerdoc.doctype, u"CC")
        self.assertEqual(registerdoc.url, u"gasalatalas.com")
        self.assertEqual(registerdoc.extrainfo, u"extra")
        information = a2548.informationlist[0]
        self.assertEqual(information.moreinformation, u"moer information")
        self.assertEqual(information.moreinformationtype, u"01")
        self.assertEqual(information.limitsenddate, u"2018-09-24")

    def test_a2648(self):
        a2648 = A1_48(self.xml_a2648)
        a2648.parse_xml()
        self.assertEqual(a2648.reqcode, u'7777')
        self.assertEqual(a2648.reqdate, u"2018-05-01")
        self.assertEqual(a2648.reqhour, u"13:00:00")
        self.assertEqual(a2648.comreferencenum, u'000123456789')
        self.assertEqual(a2648.sequential, u'01')
        self.assertEqual(a2648.cups, u'ES1234000000000001JN')
        self.assertEqual(a2648.informationdate, u"2018-09-24")
        self.assertEqual(a2648.informationtype, u"01")

        claimreference = a2648.claimreferencelist[0]
        self.assertEqual(claimreference.wrongattentiontype, u"01")
        self.assertEqual(claimreference.comreferencenum, u"0000001")
        self.assertEqual(claimreference.targetclaimcomreferencenum, u"9999998")
        self.assertEqual(claimreference.conceptcontract, u"01")
        self.assertEqual(claimreference.conceptfacturation, u"02")
        contact = claimreference.contact
        self.assertEqual(contact.contactname, u"mortdegana")
        contacttelephone = contact.contacttelephone
        self.assertEqual(contacttelephone.telephoneprefix, u"+34")
        self.assertEqual(contacttelephone.telephonenumber, u"666555444")
        self.assertEqual(contact.contactemail, u"matalas@gas")
        self.assertEqual(claimreference.nnssexpedient, u"45666666")
        self.assertEqual(claimreference.fraudrecordnum, u"888888888")
        incidentperiod = claimreference.incidentperiod
        self.assertEqual(incidentperiod.datefrom, u"2018-09-21")
        self.assertEqual(incidentperiod.dateto, u"2018-09-21")
        self.assertEqual(claimreference.invoicenumber, u"F5555")
        incidentlocation = claimreference.incidentlocation
        self.assertEqual(incidentlocation.incidentlocationdesc, u"calle pequeña")
        self.assertEqual(incidentlocation.incidentlocationprovince, u"01")
        self.assertEqual(incidentlocation.incidentlocationcity, u"000001")
        self.assertEqual(incidentlocation.incidentlocationcitysubdivision, u"17079000503")
        self.assertEqual(incidentlocation.incidentlocationzipcode, u"17888")
        reading = claimreference.reading
        self.assertEqual(reading.readingdate, u"2018-09-21")
        self.assertEqual(reading.readingvalue, u"4.89")
        incident = claimreference.incident
        self.assertEqual(incident.incidentdate, u"2018-09-21")
        client = claimreference.client
        document = client.document
        self.assertEqual(document.documenttype, u"01")
        self.assertEqual(document.documentnum, u"ES11111111T")
        self.assertEqual(client.titulartype, u"F")
        name = client.name
        self.assertEqual(name.firstname, u"nom")
        self.assertEqual(name.familyname1, u"cognom")
        self.assertEqual(name.familyname2, u"cognom 2")
        telephone = client.telephone
        self.assertEqual(telephone.telephoneprefix, u"34")
        self.assertEqual(telephone.telephonenumber, u"999111222")
        self.assertEqual(client.email, u"a@a")
        clientaddress = client.clientaddress
        self.assertEqual(clientaddress.province, u"01")
        self.assertEqual(clientaddress.city, u"000001")
        self.assertEqual(clientaddress.zipcode, u"16001")
        self.assertEqual(clientaddress.streettype, u"ACCE")
        self.assertEqual(clientaddress.street, u"inventat")
        self.assertEqual(clientaddress.streetnumber, u"4_ce")
        self.assertEqual(clientaddress.portal, u"5_TE2")
        self.assertEqual(clientaddress.staircase, u"5_mIh")
        self.assertEqual(clientaddress.floor, u"5_e6A")
        self.assertEqual(clientaddress.door, u"5_40T")
        self.assertEqual(claimreference.claimedcompensation, u"520176666.24")
        self.assertEqual(claimreference.iban, u"ES0000000000000000000000000000000")
        self.assertEqual(a2648.extrainfo, u"comentarios extra")
        variableinf = a2648.variableinflist[0]
        self.assertEqual(variableinf.moreinformationtype, u"01")
        self.assertEqual(variableinf.description, u"desc")
        self.assertEqual(variableinf.variabletype, u"01")
        self.assertEqual(variableinf.variablevalue, u"val")
        self.assertEqual(len(a2648.registerdoclist), 2)
        registerdoc = a2648.registerdoclist[1]
        self.assertEqual(registerdoc.date, u'2018-05-03')
        self.assertEqual(registerdoc.doctype, u'01')
        self.assertEqual(registerdoc.url, u'http://www.gasalmatalas.com')
        self.assertEqual(registerdoc.extrainfo, u'Comments')

    def test_a348(self):
        a348 = A1_48(self.xml_a348)
        a348.parse_xml()
        self.assertEqual(a348.reqdate, u"2018-09-24")
        self.assertEqual(a348.reqhour, u"17:04:56")
        self.assertEqual(a348.responsedate, u"2018-09-24")
        self.assertEqual(a348.responsehour, u"17:04:56")
        self.assertEqual(a348.comreferencenum, u"123456789")
        self.assertEqual(a348.claimtype, u"01")
        self.assertEqual(a348.claimsubtype, u"001")
        self.assertEqual(a348.cups, u"ES1234000000000001JN")
        self.assertEqual(a348.srcode, u"55")
        self.assertEqual(a348.result, u"01")
        self.assertEqual(a348.resultdesc, u"Procedente / Favorable")
        self.assertEqual(a348.resolutiondetail, u"0010101")
        self.assertEqual(a348.resolutiondetaildesc, u"Se piden disculpas")
        self.assertEqual(a348.reqdescription, u"rdesc")
        self.assertEqual(a348.creditedcompensation, u"88.02")
        self.assertEqual(a348.anomalyfraudrecordnum, u"885522")
        self.assertEqual(a348.movementdate, u"2018-09-24")
        self.assertEqual(a348.extrainfo, u"extra")
        registerdoc = a348.registerdoclist[0]
        self.assertEqual(registerdoc.date, u"2018-09-24")
        self.assertEqual(registerdoc.doctype, u"CC")
        self.assertEqual(registerdoc.url, u"gasal@matalas")
        self.assertEqual(registerdoc.extrainfo, u"coments")


class test_A1_46(unittest.TestCase):

    def setUp(self):
        self.xml_a246 = open(get_data("a246.xml"), "r")

    def tearDown(self):
        self.xml_a246.close()

    def test_a246(self):
        a246 = A1_46(self.xml_a246)
        a246.parse_xml()
        self.assertEqual(a246.responsedate, u"2018-05-01")
        self.assertEqual(a246.responsehour, u"13:00:00")
        self.assertEqual(a246.comreferencenum, u"000123456789")
        self.assertEqual(a246.operationtype, u"A20002")
        self.assertEqual(a246.annulmentreason, u"101")
        self.assertEqual(a246.cups, u"ES1234000000000001JN")
        self.assertEqual(a246.reqcodetoanul, u"0123456790")
        self.assertEqual(a246.claimtype, u"01")
        self.assertEqual(a246.claimsubtype, u"001")
        self.assertEqual(a246.result, u"01")
        self.assertEqual(a246.resultdesc, u"Aceptada")
        self.assertEqual(a246.resultreason, u"R01")
        self.assertEqual(a246.resultreasondesc, u"Cliente suministrado desde planta satélite.")
        self.assertEqual(a246.extrainfo, u"comentarios extras")


class test_A12_26(unittest.TestCase):

    def setUp(self):
        self.xml_a1226 = open(get_data("a1226.xml"), "r")

    def tearDown(self):
        self.xml_a1226.close()

    def test_a246(self):
        a1226 = A12_26(self.xml_a1226)
        a1226.parse_xml()
        self.assertEqual(a1226.reqhour, u"12:57:59")
        self.assertEqual(a1226.atrcode, u"24_0mVgXP2mQWbjDIW3Y7DFf")
        self.assertEqual(a1226.cups, u"ES1234000000000001JN")
        self.assertEqual(a1226.nationality, u"SB")
        self.assertEqual(a1226.documenttype, u"01")
        self.assertEqual(a1226.documentnum, u"20_ikhOXhfYkJDE8GXdS")
        self.assertEqual(a1226.firstname, u"40_F6S6mwa91ebOPvu1lRDhPV2aRTjRic")
        self.assertEqual(a1226.familyname1, u"30_ghUjt3ZyeoBellwhPI3g99zFDyB")
        self.assertEqual(a1226.familyname2, u"30_Sv2t9Zg4JuKhOMPAk0CWygkBw85")
        self.assertEqual(a1226.telephone, u"20_fO2z6JBpmivuOeG3a")
        self.assertEqual(a1226.fax, u"20_qXZjH8iiAc2bsH1It")
        self.assertEqual(a1226.newcustomer, u"S")
        self.assertEqual(a1226.email, u"60_EUMoY071vBip1qmYVxuJ1TGmJihWmM")
        self.assertEqual(a1226.streettype, u"ACCE")
        self.assertEqual(a1226.street, u"60_vdL9HZyoO6RyPRQnmirjeDxoLX0Uej")
        self.assertEqual(a1226.streetnumber, u"4_tS")
        self.assertEqual(a1226.portal, u"5_PUQ")
        self.assertEqual(a1226.staircase, u"5_7bv")
        self.assertEqual(a1226.floor, u"5_DLx")
        self.assertEqual(a1226.door, u"5_mmC")
        self.assertEqual(a1226.province, u"01")
        self.assertEqual(a1226.city, u"00001")
        self.assertEqual(a1226.zipcode, u"5_MLU")
        self.assertEqual(a1226.tolltype, u"11")
        self.assertEqual(a1226.qdgranted, u"5.8689")
        self.assertEqual(a1226.qhgranted, u"88")
        self.assertEqual(a1226.singlenomination, u"S")
        self.assertEqual(a1226.transfereffectivedate, u"2019-05-16")
        self.assertEqual(a1226.finalclientyearlyconsumption, u"878")
        self.assertEqual(a1226.netsituation, u"14_bdrdvx3064I")
        self.assertEqual(a1226.outgoingpressuregranted, u"72012.464")
        self.assertEqual(a1226.lastinspectionsdate, u"2019-05-16")
        self.assertEqual(a1226.lastinspectionsresult, u"01")
        self.assertEqual(a1226.readingtype, u"0")
        self.assertEqual(a1226.rentingamount, u"40770.27")
        self.assertEqual(a1226.rentingperiodicity, u"01")
        self.assertEqual(a1226.canonircamount, u"62529.35")
        self.assertEqual(a1226.canonircperiodicity, u"01")
        self.assertEqual(a1226.canonircforlife, u"S")
        self.assertEqual(a1226.canonircdate, u"2019-05-16")
        self.assertEqual(a1226.canonircmonth, u"01")
        self.assertEqual(a1226.othersamount, u"51589.82")
        self.assertEqual(a1226.othersperiodicity, u"01")
        self.assertEqual(a1226.readingperiodicitycode, u"01")
        self.assertEqual(a1226.transporter, u"0001")
        self.assertEqual(a1226.transnet, u"14_0jldeS2u13Y")
        self.assertEqual(a1226.gasusetype, u"01")
        self.assertEqual(a1226.caecode, u"13_h1c6VEDs7V")
        self.assertEqual(a1226.communicationreason, u"01")
        self.assertEqual(a1226.titulartype, u"F")
        self.assertEqual(a1226.regularaddress, u"S")
        counter = a1226.counterlist[0]
        self.assertEqual(counter.countermodel, u"50_gKM9uwusZjqsf9bWbLEvzf9LhZGq17")
        self.assertEqual(counter.countertype, u"7_OC85P")
        self.assertEqual(counter.counternumber, u"18_KcbwQ2vdOKAR0nQ")
        self.assertEqual(counter.counterproperty, u"04")
        self.assertEqual(counter.reallecture, u"53749846509")
        self.assertEqual(counter.counterpressure, u"72241.495")
        self.assertEqual(len(a1226.correctorlist), 2)
        corrector = a1226.correctorlist[0]
        self.assertEqual(corrector.correctedlecture, u'2200')
        self.assertEqual(corrector.correctormodel, u'modelo1')
        self.assertEqual(corrector.correctornumber, u'D123456')
        self.assertEqual(corrector.correctorproperty, u'01')
        self.assertEqual(corrector.correctortype, u'01')


class test_A12_24(unittest.TestCase):

    def setUp(self):
        self.xml_a1224 = open(get_data("a1224.xml"), "r")

    def tearDown(self):
        self.xml_a1224.close()

    def test_a1224(self):
        a1224 = A12_24(self.xml_a1224)
        a1224.parse_xml()

        self.assertEqual(a1224.reqdate, u"2018-05-01")
        self.assertEqual(a1224.reqhour, u"12:00:00")

        self.assertEqual(a1224.productcode, u"12345")

        self.assertEqual(a1224.nationality, u"ES")
        self.assertEqual(a1224.documenttype, u"01")
        self.assertEqual(a1224.documentnum, u"11111111H")
        self.assertEqual(a1224.cups, u"ES1234000000000001JN")

        self.assertEqual(a1224.operationnum, u"4444448877787879894898189881848844894894")
        self.assertEqual(a1224.communicationreason, u"01")
        self.assertEqual(a1224.transfereffectivedate, u"2018-07-01")
        self.assertEqual(a1224.readingtype, u"1")

        counter = a1224.counterlist[0]
        self.assertEqual(counter.countermodel, u"marca1")
        self.assertEqual(counter.countertype, u"tipo1")
        self.assertEqual(counter.counternumber, u"B123456")
        self.assertEqual(counter.counterproperty, u"04")
        self.assertEqual(counter.reallecture, u"2000")
        self.assertEqual(counter.counterpressure, u"54321.123")

        counter2 = a1224.counterlist[1]

        self.assertEqual(counter2.countermodel, u"marca2")
        self.assertEqual(counter2.countertype, u"tipo2")
        self.assertEqual(counter2.counternumber, u"C123456")
        self.assertEqual(counter2.counterproperty, u"06")
        self.assertEqual(counter2.reallecture, u"3000")
        self.assertEqual(counter2.counterpressure, u"13245.321")

        corrector = a1224.correctorlist[0]
        self.assertEqual(corrector.correctedlecture, u'2200')
        self.assertEqual(corrector.correctormodel, u'modelo1')
        self.assertEqual(corrector.correctornumber, u'D123456')
        self.assertEqual(corrector.correctorproperty, u'01')
        self.assertEqual(corrector.correctortype, u'01')

        corrector2 = a1224.correctorlist[1]
        self.assertEqual(corrector2.correctedlecture, u'3300')
        self.assertEqual(corrector2.correctormodel, u'modelo2')
        self.assertEqual(corrector2.correctornumber, u'E654321')
        self.assertEqual(corrector2.correctorproperty, u'02')
        self.assertEqual(corrector2.correctortype, u'02')

        self.assertEqual(len(a1224.counterlist), 2)


class test_A19_45(unittest.TestCase):

    def setUp(self):
        self.xml_a1945 = open(get_data("a1945.xml"), "r")

    def tearDown(self):
        self.xml_a1945.close()

    def test_a246(self):
        a1945 = A19_45(self.xml_a1945)
        a1945.parse_xml()
        self.assertEqual(a1945.reqcode, '0014296514')
        self.assertEqual(a1945.reqdate, '2019-01-02')
        self.assertEqual(a1945.reqhour, '15:28:54')
        self.assertEqual(a1945.cups, 'ES0217010143209335YG')
        self.assertEqual(a1945.operationtype, 'A10009')
        self.assertEqual(a1945.operationnum, '5838204')
        self.assertEqual(a1945.responsedate, '2019-01-02')
        self.assertEqual(a1945.responsehour, '15:28:55')
        self.assertEqual(a1945.result, '13')
        self.assertEqual(a1945.resultdesc, 'No Realizada')
        self.assertEqual(a1945.closingtype, '028')
        self.assertEqual(a1945.closingtypedesc, 'No realizada por causas imputables al cliente')
        self.assertEqual(a1945.activationtype, '001')
        self.assertEqual(a1945.activationtypedesc, 'Descripcion')
        self.assertEqual(a1945.interventiondate, '2018-12-11')
        self.assertEqual(a1945.interventionhour, '07:44:32')
        self.assertEqual(a1945.resultinspection, '03')
        self.assertEqual(a1945.resultinspectiondesc, 'AUSENTE')
        self.assertEqual(a1945.visitnumber, '1')
        self.assertEqual(a1945.counterchange, 'N')
        self.assertEqual(a1945.removallecture, '50')
        self.assertEqual(a1945.supplystatus, '01')
        self.assertEqual(a1945.supplystatusdesc, 'Desc.Suply')
        self.assertEqual(a1945.servicestatus, '00')
        self.assertEqual(a1945.servicestatusdesc, 'EN SERVICIO')
        self.assertEqual(a1945.extrainfo, 'COMENTARIIIS')
        self.assertEqual(a1945.communicationreason, '08')
        self.assertEqual(a1945.conceptnumber, u'2')
        self.assertEqual(len(a1945.conceptlist), 2)
        concept = a1945.conceptlist[1]
        self.assertEqual(concept.level, u'1')
        self.assertEqual(concept.code, u'0002')
        self.assertEqual(concept.description, u'Desc')
        self.assertEqual(concept.periodicity, u'03')
        self.assertEqual(concept.units, u'1')
        self.assertEqual(concept.unitimport, u'23.8')
        self.assertEqual(concept.import_, u'23.8')
        self.assertEqual(len(a1945.counterlist), 2)
        counter = a1945.counterlist[1]
        self.assertEqual(counter.countermodel, u'marca2')
        self.assertEqual(counter.counternumber, u'C123456')
        self.assertEqual(counter.counterpressure, u'13245.321')
        self.assertEqual(counter.counterproperty, u'06')
        self.assertEqual(counter.countertype, u'tipo2')
        self.assertEqual(counter.reallecture, u'3000')
        self.assertEqual(len(a1945.defectlist), 2)
        defect = a1945.defectlist[1]
        self.assertEqual(defect.code, u'002')
        self.assertEqual(defect.description, u'Desc2')
        self.assertEqual(len(a1945.registerdoclist), 2)
        registerdoc = a1945.registerdoclist[1]
        self.assertEqual(registerdoc.date, u'2018-01-01')
        self.assertEqual(registerdoc.doctype, u'02')
        self.assertEqual(registerdoc.url, u'http://gasalmatalas.com')
        self.assertEqual(registerdoc.extrainfo, u'Comments')


class test_A1_38(unittest.TestCase):

    def setUp(self):
        self.xml_a238 = open(get_data("a238.xml"), "r")
        self.xml_a2538 = open(get_data("a2538.xml"), "r")
        self.xml_a338 = open(get_data("a338.xml"), "r")
        self.xml_a438 = open(get_data("a438.xml"), "r")

    def tearDown(self):
        self.xml_a238.close()
        self.xml_a2538.close()
        self.xml_a338.close()
        self.xml_a438.close()

    def test_a238(self):
        a238 = A1_38(self.xml_a238)
        a238.parse_xml()
        self.assertEqual(a238.reqcode, u"10_4E4mh15")
        self.assertEqual(a238.comreferencenum, u"123456789123")
        self.assertEqual(a238.responsedate, u"2020-03-13")
        self.assertEqual(a238.responsehour, u"13:52:14")
        self.assertEqual(a238.result, u"01")
        self.assertEqual(a238.resultdesc, u"Aceptada")
        self.assertEqual(a238.resultreason, u"R01")
        self.assertEqual(a238.resultreasondesc, u"Cliente suministrado desde planta satélite.")
        self.assertEqual(a238.nationality, u"SB")
        self.assertEqual(a238.documenttype, u"01")
        self.assertEqual(a238.documentnum, u"20_f8aQW2mqoLv4GLJ8M")
        self.assertEqual(a238.cups, u"20ai6Nmki1j8m5qCDmuG")
        self.assertEqual(a238.qdgranted, u"481479688.216")
        self.assertEqual(a238.qhgranted, u"397959673")
        self.assertEqual(a238.outgoingpressuregranted, u"87952.239")
        self.assertEqual(a238.clientyearlyconsumption, u"445325674084")
        self.assertEqual(a238.tolltype, u"11")
        self.assertEqual(a238.newmodeffectdate, u"01")
        self.assertEqual(a238.foreseentransferdate, u"2020-03-13")
        self.assertEqual(a238.extrainfo, u"400_Y1cLoMJo2SXTeCdHmJCodtnOvEsmDn")
        self.assertEqual(a238.conceptnumber, u"4")
        self.assertEqual(len(a238.conceptlist), 2)
        concept = a238.conceptlist[1]
        self.assertEqual(concept.level, u'1')
        self.assertEqual(concept.code, u'0002')
        self.assertEqual(concept.description, u'Desc')
        self.assertEqual(concept.periodicity, u'03')
        self.assertEqual(concept.units, u'1')
        self.assertEqual(concept.unitimport, u'23.8')
        self.assertEqual(concept.import_, u'23.8')

        self.assertEqual(a238.productlist[0].productcode, u'TESTCODE1')
        self.assertEqual(a238.productlist[0].producttype, u'03')
        self.assertEqual(a238.productlist[0].producttolltype, u'31')
        self.assertEqual(a238.productlist[0].productqd, u'23.6')
        self.assertEqual(a238.productlist[0].productqa, u'12345')
        self.assertEqual(a238.productlist[0].productstartdate, u'2020-01-01')
        self.assertEqual(a238.productlist[0].productenddate, u'2020-02-01')

        self.assertEqual(a238.productlist[1].productcode, u'TESTCODE2')
        self.assertEqual(a238.productlist[1].producttype, u'02')
        self.assertEqual(a238.productlist[1].producttolltype, u'32')
        self.assertEqual(a238.productlist[1].productqd, u'23.5')
        self.assertEqual(a238.productlist[1].productqa, u'1234')
        self.assertEqual(a238.productlist[1].productstartdate, u'2020-01-02')
        self.assertEqual(a238.productlist[1].productenddate, u'2020-02-02')

    def test_a2538(self):
        a2538 = A1_38(self.xml_a2538)
        a2538.parse_xml()
        self.assertEqual(a2538.reqcode, u"10_p62j9fh")
        self.assertEqual(a2538.visitdate, u"2020-03-13")
        self.assertEqual(a2538.visithour, u"14:26:35")
        self.assertEqual(a2538.comreferencenum, u"123456789")
        self.assertEqual(a2538.informationtype, u"002")
        self.assertEqual(a2538.informationtypedesc, u"0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001")
        self.assertEqual(a2538.interventiondate, u"2020-03-13")
        self.assertEqual(a2538.interventionhourfrom, u"14:26:35")
        self.assertEqual(a2538.interventionhourto, u"14:26:35")
        self.assertEqual(a2538.cups, u"20alzDPKUDB5HhZDhn5X")
        self.assertEqual(a2538.visitnumber, u"228")
        self.assertEqual(a2538.operationnum, u"40_tQzwG5OT6YTye1UiYVtoV3r9VymR5B")
        self.assertEqual(a2538.extrainfo, u"400_C9BEFQSmU4c7fJcqlXEYL79KyKwcZ9")
        self.assertEqual(len(a2538.defectlist), 2)
        defect = a2538.defectlist[1]
        self.assertEqual(defect.code, u'002')
        self.assertEqual(defect.description, u'Desc2')

    def test_a338(self):
        a338 = A1_38(self.xml_a338)
        a338.parse_xml()
        self.assertEqual(a338.reqcode, u"10_Qb9POo4")
        self.assertEqual(a338.comreferencenum, u"987654")
        self.assertEqual(a338.responsedate, u"2020-03-13")
        self.assertEqual(a338.responsehour, u"14:48:40")
        self.assertEqual(a338.result, u"09")
        self.assertEqual(a338.resultdesc, u"Aceptada")
        self.assertEqual(a338.activationtype, u"001")
        self.assertEqual(a338.activationtypedesc, u"Realizada puesta en servicio")
        self.assertEqual(a338.interventiondate, u"2020-03-13")
        self.assertEqual(a338.interventionhour, u"14:48:40")
        self.assertEqual(a338.canonircperiodicity, u"01")
        self.assertEqual(a338.nationality, u"SB")
        self.assertEqual(a338.documenttype, u"01")
        self.assertEqual(a338.documentnum, u"20_lhGlhEgKWo4lNBRTV")
        self.assertEqual(a338.titulartype, u"F")
        self.assertEqual(a338.firstname, u"40_QQofyiQEv44lbt60GpvTRKfZvFesdN")
        self.assertEqual(a338.familyname1, u"30_Nou0DMJw9Heqd4kANMhTAbqb4QN")
        self.assertEqual(a338.familyname2, u"30_J10jWjwENZvnk4O9gqDrxjoC5y1")
        self.assertEqual(a338.province, u"01")
        self.assertEqual(a338.city, u"00001")
        self.assertEqual(a338.zipcode, u"5_oDV")
        self.assertEqual(a338.streettype, u"ACCE")
        self.assertEqual(a338.street, u"60_9Kl8rg7zlaDCIvLbP3FNaOpIPGvWDv")
        self.assertEqual(a338.streetnumber, u"4_LZ")
        self.assertEqual(a338.portal, u"5_Z7w")
        self.assertEqual(a338.staircase, u"5_XdF")
        self.assertEqual(a338.floor, u"5_48N")
        self.assertEqual(a338.door, u"5_PFm")
        self.assertEqual(a338.cups, u"20amkKAzgAypslzxvpoB")
        self.assertEqual(a338.atr, u"24_d0xPA3by9PW02qjoQpI0j")
        self.assertEqual(a338.operationnum, u"40_a5ZVA49iVRlW0ivVoh7VXeQOa9bxLr")
        self.assertEqual(a338.netsituation, u"14_m8MEzzq0q3f")
        self.assertEqual(a338.lectureperiodicity, u"01")
        self.assertEqual(a338.visitnumber, u"521")
        self.assertEqual(a338.tolltype, u"11")
        self.assertEqual(a338.finalqdgranted, u"210355200.787")
        self.assertEqual(a338.finalqhgranted, u"654846713")
        self.assertEqual(a338.finalclientyearlyconsumption, u"252744160122")
        self.assertEqual(a338.extrainfo, u"400_ylDyrpjutezfQ2ojWqcyjdpQqN7UG7")
        self.assertEqual(a338.conceptnumber, u"29")
        self.assertEqual(len(a338.conceptlist), 2)
        concept = a338.conceptlist[1]
        self.assertEqual(concept.level, u'1')
        self.assertEqual(concept.code, u'0002')
        self.assertEqual(concept.description, u'Desc')
        self.assertEqual(concept.periodicity, u'03')
        self.assertEqual(concept.units, u'1')
        self.assertEqual(concept.unitimport, u'23.8')
        self.assertEqual(concept.import_, u'23.8')
        self.assertEqual(len(a338.counterlist), 2)
        counter = a338.counterlist[1]
        self.assertEqual(counter.countermodel, u'marca2')
        self.assertEqual(counter.counternumber, u'C123456')
        self.assertEqual(counter.counterpressure, u'13245.321')
        self.assertEqual(counter.counterproperty, u'06')
        self.assertEqual(counter.countertype, u'tipo2')
        self.assertEqual(counter.reallecture, u'3000')
        self.assertEqual(len(a338.correctorlist), 2)
        corrector = a338.correctorlist[0]
        self.assertEqual(corrector.correctedlecture, u'2200')
        self.assertEqual(corrector.correctormodel, u'modelo1')
        self.assertEqual(corrector.correctornumber, u'D123456')
        self.assertEqual(corrector.correctorproperty, u'01')
        self.assertEqual(corrector.correctortype, u'01')

        self.assertEqual(a338.productlist[0].productcode, u'TESTCODE1')
        self.assertEqual(a338.productlist[0].producttype, u'03')
        self.assertEqual(a338.productlist[0].producttolltype, u'31')
        self.assertEqual(a338.productlist[0].productqd, u'23.6')
        self.assertEqual(a338.productlist[0].productqa, u'12345')
        self.assertEqual(a338.productlist[0].productstartdate, u'2020-01-01')
        self.assertEqual(a338.productlist[0].productenddate, u'2020-02-01')

        self.assertEqual(a338.productlist[1].productcode, u'TESTCODE2')
        self.assertEqual(a338.productlist[1].producttype, u'02')
        self.assertEqual(a338.productlist[1].producttolltype, u'32')
        self.assertEqual(a338.productlist[1].productqd, u'23.5')
        self.assertEqual(a338.productlist[1].productqa, u'1234')
        self.assertEqual(a338.productlist[1].productstartdate, u'2020-01-02')
        self.assertEqual(a338.productlist[1].productenddate, u'2020-02-02')

    def test_a438(self):
        a438 = A1_38(self.xml_a438)
        a438.parse_xml()
        self.assertEqual(a438.reqcode, u"10_z9f2k6S")
        self.assertEqual(a438.comreferencenum, u"123456789")
        self.assertEqual(a438.responsedate, u"2020-03-13")
        self.assertEqual(a438.responsehour, u"15:09:09")
        self.assertEqual(a438.result, u"13")
        self.assertEqual(a438.resultdesc, u"Aceptada")
        self.assertEqual(a438.resultreason, u"R01")
        self.assertEqual(a438.resultreasondesc, u"Cliente suministrado desde planta satélite.")
        self.assertEqual(a438.interventiondate, u"2020-03-13")
        self.assertEqual(a438.interventionhour, u"15:09:09")
        self.assertEqual(a438.cups, u"20aXn4jOtXkA8PF9JCHH")
        self.assertEqual(a438.nationality, u"SB")
        self.assertEqual(a438.documenttype, u"01")
        self.assertEqual(a438.documentnum, u"20_IebsHNeRmZxuEPuXi")
        self.assertEqual(a438.operationnum, u"40_PFC7QxHLQmOOoIp6PGjE13LnU2cqsI")
        self.assertEqual(a438.visitnumber, u"987")
        self.assertEqual(a438.extrainfo, u"400_ssYcpvXKXUF3DuQzltLLSTHWo2SDsC")
        self.assertEqual(len(a438.defectlist), 2)
        defect = a438.defectlist[1]
        self.assertEqual(defect.code, u'002')
        self.assertEqual(defect.description, u'Desc2')


class test_A1_49(unittest.TestCase):

    def setUp(self):
        self.xml_a249 = open(get_data("a249.xml"), "r")
        self.xml_a2s49 = open(get_data("a2s49.xml"), "r")
        self.xml_a2549 = open(get_data("a2549.xml"), "r")
        self.xml_a349 = open(get_data("a349.xml"), "r")
        self.xml_a3s49 = open(get_data("a3s49.xml"), "r")
        self.xml_a449 = open(get_data("a449.xml"), "r")
        self.xml_a4s49 = open(get_data("a4s49.xml"), "r")

    def tearDown(self):
        self.xml_a249.close()
        self.xml_a2s49.close()
        self.xml_a2549.close()
        self.xml_a349.close()
        self.xml_a3s49.close()
        self.xml_a449.close()
        self.xml_a4s49.close()

    def test_a249(self):
        a249 = A1_49(self.xml_a249)
        a249.parse_xml()
        self.assertEqual(a249.reqcode, '1234567890')
        self.assertEqual(a249.reqdate, '2020-03-01')
        self.assertEqual(a249.reqhour, '08:00:00')
        self.assertEqual(a249.responsedate, '2020-03-01')
        self.assertEqual(a249.responsehour, '08:00:00')
        self.assertEqual(a249.comreferencenum, '12345')
        self.assertEqual(a249.cups, 'ES1234000000000001JN')
        self.assertEqual(a249.result, '01')
        self.assertEqual(a249.resultdesc, 'Aceptada')
        self.assertEqual(a249.resultreason, 'R01')
        self.assertEqual(a249.resultreasondesc, u'Cliente suministrado desde planta satélite.')
        self.assertEqual(a249.indanulable, 'S')
        self.assertEqual(a249.indactcampo, 'S')
        self.assertEqual(a249.foreseentransferdate, '2020-05-01')
        self.assertEqual(a249.extrainfo, 'EXTRA EXTRA! EL GAS NO TE SENTIT!')

    def test_a2s49(self):
        a2s49 = A1_49(self.xml_a2s49)
        a2s49.parse_xml()
        self.assertEqual(a2s49.reqcode, '1234567890')
        self.assertEqual(a2s49.responsedate, '2020-03-01')
        self.assertEqual(a2s49.responsehour, '08:00:00')
        self.assertEqual(a2s49.cups, 'ES1234000000000001JN')
        self.assertEqual(a2s49.indanulable, 'S')
        self.assertEqual(a2s49.indactcampo, 'S')
        self.assertEqual(a2s49.foreseentransferdate, '2020-05-01')
        self.assertEqual(a2s49.extrainfo, 'EXTRA EXTRA! EL GAS NO TE SENTIT!')

    def test_a2549(self):
        a2549 = A1_49(self.xml_a2549)
        a2549.parse_xml()
        self.assertEqual(a2549.reqcode, '123456789')
        self.assertEqual(a2549.cups, 'ES1234000000000001JN')
        self.assertEqual(a2549.visitdate, '2018-09-24')
        self.assertEqual(a2549.visithour, '15:25:18')
        self.assertEqual(a2549.comreferencenum, '987654321')
        self.assertEqual(a2549.informationtype, '002')
        self.assertEqual(a2549.informationtypedesc, 'Orden de Trabajo pendiente')
        self.assertEqual(a2549.interventiondate, '2018-09-24')
        self.assertEqual(a2549.interventionhourfrom, '15:25:18')
        self.assertEqual(a2549.interventionhourto, '15:25:18')
        self.assertEqual(a2549.visitnumber, '590')
        self.assertEqual(a2549.operationnum, '741')
        self.assertEqual(a2549.extrainfo, 'coments')
        defect = a2549.defectlist[0]
        self.assertEqual(defect.code, u"001")
        self.assertEqual(defect.description, u"FUGA DE GAS")

    def test_a349(self):
        a349 = A1_49(self.xml_a349)
        a349.parse_xml()
        self.assertEqual(a349.reqcode, '10_Qb9POo4')
        self.assertEqual(a349.comreferencenum, '987654')
        self.assertEqual(a349.responsedate, '2020-03-13')
        self.assertEqual(a349.responsehour, '14:48:40')
        self.assertEqual(a349.cups, 'ES1234000000000001JN')
        self.assertEqual(a349.atrcode, '000111222333444555666777')
        self.assertEqual(a349.resactivacion, '01')
        self.assertEqual(a349.transfereffectivedate, '2020-05-01')
        self.assertEqual(a349.enservicio, 'S')
        self.assertEqual(a349.telemetering, 'S')
        self.assertEqual(a349.finalqdgranted, '210355200.787')
        self.assertEqual(a349.finalqhgranted, '654846713')
        self.assertEqual(a349.finalclientyearlyconsumption, '252744160122')
        self.assertEqual(a349.gasusetype, '01')
        self.assertEqual(a349.result, '09')
        self.assertEqual(a349.resultdesc, 'Aceptada')
        self.assertEqual(a349.indanulable, 'S')
        self.assertEqual(a349.interventiondate, '2020-03-13')
        self.assertEqual(a349.interventionhourfrom, '14:48:40')
        self.assertEqual(a349.interventionhourto, '15:48:40')
        self.assertEqual(a349.visitnumber, '521')
        self.assertEqual(a349.canonircperiodicity, '01')
        self.assertEqual(a349.lastinspectionsdate, '2019-01-01')
        self.assertEqual(a349.lastinspectionsresult, '01')
        self.assertEqual(a349.StatusPS, '1')
        self.assertEqual(a349.readingtype, '1')
        self.assertEqual(a349.lectureperiodicity, '01')
        self.assertEqual(a349.extrainfo, '400_ylDyrpjutezfQ2ojWqcyjdpQqN7UG7')

        counter = a349.counterlist[0]

        self.assertEqual(counter.countermodel, u"marca1")
        self.assertEqual(counter.countertype, u"tipo1")
        self.assertEqual(counter.counternumber, u"B123456")
        self.assertEqual(counter.counterproperty, u"04")
        self.assertEqual(counter.reallecture, u"2000")
        self.assertEqual(counter.counterpressure, u"54321.123")

        counter2 = a349.counterlist[1]

        self.assertEqual(counter2.countermodel, u"marca2")
        self.assertEqual(counter2.countertype, u"tipo2")
        self.assertEqual(counter2.counternumber, u"C123456")
        self.assertEqual(counter2.counterproperty, u"06")
        self.assertEqual(counter2.reallecture, u"3000")
        self.assertEqual(counter2.counterpressure, u"13245.321")

    def test_a3s49(self):
        a3s49 = A1_49(self.xml_a3s49)
        a3s49.parse_xml()
        self.assertEqual(a3s49.reqcode, '0123456789')
        self.assertEqual(a3s49.comreferencenum, '123456789')
        self.assertEqual(a3s49.responsedate, '2018-05-01')
        self.assertEqual(a3s49.responsehour, '13:00:00')
        self.assertEqual(a3s49.cups, 'ES1234000000000001JN')
        self.assertEqual(a3s49.atrcode, '000111222333444555666777')
        self.assertEqual(a3s49.resactivacion, '01')
        self.assertEqual(a3s49.transfereffectivedate, '2020-05-01')
        self.assertEqual(a3s49.enservicio, 'S')
        self.assertEqual(a3s49.telemetering, 'S')
        self.assertEqual(a3s49.finalqdgranted, '210355200.787')
        self.assertEqual(a3s49.finalqhgranted, '654846713')
        self.assertEqual(a3s49.finalclientyearlyconsumption, '252744160122')
        self.assertEqual(a3s49.gasusetype, '01')
        self.assertEqual(a3s49.result, '09')
        self.assertEqual(a3s49.resultdesc, 'Aceptada')
        self.assertEqual(a3s49.indanulable, 'S')
        self.assertEqual(a3s49.interventiondate, '2020-03-13')
        self.assertEqual(a3s49.interventionhourfrom, '14:48:40')
        self.assertEqual(a3s49.interventionhourto, '15:48:40')
        self.assertEqual(a3s49.visitnumber, '521')
        self.assertEqual(a3s49.firstname, 'Gas')
        self.assertEqual(a3s49.familyname1, 'Al')
        self.assertEqual(a3s49.familyname2, 'Matalas')
        self.assertEqual(a3s49.telephone1, '999888777')
        self.assertEqual(a3s49.telephone2, '666555444')
        self.assertEqual(a3s49.email, 'gasalmatalas@atr')
        self.assertEqual(a3s49.language, '02')
        self.assertEqual(a3s49.provinceowner, '16')
        self.assertEqual(a3s49.cityowner, '17000')
        self.assertEqual(a3s49.zipcodeowner, '17001')
        self.assertEqual(a3s49.streettypeowner, 'ACCE')
        self.assertEqual(a3s49.streetowner, 'Carrer inventat 2')
        self.assertEqual(a3s49.streetnumberowner, '12')
        self.assertEqual(a3s49.portalowner, '22')
        self.assertEqual(a3s49.staircaseowner, '32')
        self.assertEqual(a3s49.floorowner, '42')
        self.assertEqual(a3s49.doorowner, '52')
        self.assertEqual(a3s49.canonircperiodicity, '01')
        self.assertEqual(a3s49.lastinspectionsdate, '2017-01-01')
        self.assertEqual(a3s49.lastinspectionsresult, '01')
        self.assertEqual(a3s49.StatusPS, '1')
        self.assertEqual(a3s49.readingtype, '1')
        self.assertEqual(a3s49.lectureperiodicity, '02')
        self.assertEqual(a3s49.extrainfo, 'comentarios extras')

        counter = a3s49.counterlist[0]

        self.assertEqual(counter.countermodel, u"marca1")
        self.assertEqual(counter.countertype, u"tipo1")
        self.assertEqual(counter.counternumber, u"B123456")
        self.assertEqual(counter.counterproperty, u"04")
        self.assertEqual(counter.reallecture, u"2000")
        self.assertEqual(counter.counterpressure, u"54321.123")

        counter2 = a3s49.counterlist[1]

        self.assertEqual(counter2.countermodel, u"marca2")
        self.assertEqual(counter2.countertype, u"tipo2")
        self.assertEqual(counter2.counternumber, u"C123456")
        self.assertEqual(counter2.counterproperty, u"06")
        self.assertEqual(counter2.reallecture, u"3000")
        self.assertEqual(counter2.counterpressure, u"13245.321")

        corrector = a3s49.correctorlist[0]

        self.assertEqual(corrector.correctedlecture, u'2200')
        self.assertEqual(corrector.correctormodel, u'modelo1')
        self.assertEqual(corrector.correctornumber, u'D123456')
        self.assertEqual(corrector.correctorproperty, u'01')
        self.assertEqual(corrector.correctortype, u'01')

        corrector2 = a3s49.correctorlist[1]

        self.assertEqual(corrector2.correctedlecture, u'3300')
        self.assertEqual(corrector2.correctormodel, u'modelo2')
        self.assertEqual(corrector2.correctornumber, u'E654321')
        self.assertEqual(corrector2.correctorproperty, u'02')
        self.assertEqual(corrector2.correctortype, u'02')

    def test_a449(self):
        a449 = A1_49(self.xml_a449)
        a449.parse_xml()
        self.assertEqual(a449.reqcode, '10_z9f2k6S')
        self.assertEqual(a449.comreferencenum, '123456789')
        self.assertEqual(a449.responsedate, '2020-03-13')
        self.assertEqual(a449.responsehour, '15:09:09')
        self.assertEqual(a449.cups, '20aXn4jOtXkA8PF9JCHH')
        self.assertEqual(a449.resultreason, 'R01')
        self.assertEqual(a449.interventiondate, '2020-03-13')
        self.assertEqual(a449.interventionhourfrom, '15:09:09')
        self.assertEqual(a449.interventionhourto, '15:09:09')
        self.assertEqual(a449.visitnumber, '987')
        self.assertEqual(a449.extrainfo, '400_ssYcpvXKXUF3DuQzltLLSTHWo2SDsC')

    def test_a4s49(self):
        a4s49 = A1_49(self.xml_a4s49)
        a4s49.parse_xml()
        self.assertEqual(a4s49.reqcode, '10_z9f2k6S')
        self.assertEqual(a4s49.responsedate, '2020-03-13')
        self.assertEqual(a4s49.responsehour, '15:09:09')
        self.assertEqual(a4s49.nationality, 'ES')
        self.assertEqual(a4s49.documenttype, '01')
        self.assertEqual(a4s49.documentnum, '11111111H')
        self.assertEqual(a4s49.cups, '20aXn4jOtXkA8PF9JCHH')
        self.assertEqual(a4s49.previousatrcode, '000111222333444555666777')
        self.assertEqual(a4s49.result, '13')
        self.assertEqual(a4s49.resultdesc, 'Aceptada')
        self.assertEqual(a4s49.resultreason, 'R01')
        self.assertEqual(a4s49.resultreasondesc, u'Cliente suministrado desde planta satélite.')
        self.assertEqual(a4s49.extrainfo, '400_ssYcpvXKXUF3DuQzltLLSTHWo2SDsC')


class test_A13_50(unittest.TestCase):

    def setUp(self):
        self.xml_a15s50 = open(get_data("a15s50.xml"), "r")

    def tearDown(self):
        self.xml_a15s50.close()

    def test_a15s50(self):
        a15s50 = A13_50(self.xml_a15s50)
        a15s50.parse_xml()
        self.assertEqual(a15s50.reqcode, '0123456789')
        self.assertEqual(a15s50.responsedate, '2018-05-01')
        self.assertEqual(a15s50.responsehour, '13:00:00')
        self.assertEqual(a15s50.nationality, 'ES')
        self.assertEqual(a15s50.documenttype, '07')
        self.assertEqual(a15s50.documentnum, '11111111H')
        self.assertEqual(a15s50.cups, 'ES1234000000000001JN')
        self.assertEqual(a15s50.previousatrcode, '000111222333444555666777')
        self.assertEqual(a15s50.transfereffectivedate, '2018-07-01')
        self.assertEqual(a15s50.readingtype, '1')
        self.assertEqual(a15s50.extrainfo, 'comentarios extras')
        self.assertEqual(len(a15s50.correctorlist), 2)
        corrector = a15s50.correctorlist[0]
        self.assertEqual(corrector.correctedlecture, u'2200')
        self.assertEqual(corrector.correctormodel, u'modelo1')
        self.assertEqual(corrector.correctornumber, u'D123456')
        self.assertEqual(corrector.correctorproperty, u'01')
        self.assertEqual(corrector.correctortype, u'01')
        self.assertEqual(len(a15s50.counterlist), 2)
        counter = a15s50.counterlist[1]
        self.assertEqual(counter.countermodel, u'marca2')
        self.assertEqual(counter.counternumber, u'C123456')
        self.assertEqual(counter.counterpressure, u'13245.321')
        self.assertEqual(counter.counterproperty, u'06')
        self.assertEqual(counter.countertype, u'tipo2')
        self.assertEqual(counter.reallecture, u'3000')


class test_A21_36(unittest.TestCase):

    def setUp(self):
        self.xml_a2136 = open(get_data("a2136.xml"), "r")

    def tearDown(self):
        self.xml_a2136.close()

    def test_a2136(self):
        a2136 = A20_36(self.xml_a2136)
        a2136.parse_xml()
        self.assertEqual(a2136.solcode, '1234567890')
        self.assertEqual(a2136.reqdate, '2020-03-01')
        self.assertEqual(a2136.reqhour, '08:00:00')
        self.assertEqual(a2136.cups, 'ES1234000000000001JN')
        self.assertEqual(a2136.result, '01')
        self.assertEqual(a2136.resultdescr, 'Aceptada')
        self.assertEqual(a2136.reason, 'R01')
        self.assertEqual(a2136.reasondescr, u'Cliente suministrado desde planta satélite.')
        self.assertEqual(a2136.permissionreq, 'S')
        self.assertEqual(a2136.expecteddate, '2020-04-30')
        self.assertEqual(a2136.infraestructurestatus, '01')
        self.assertEqual(a2136.province, '17')
        self.assertEqual(a2136.city, '17001')
        self.assertEqual(a2136.zipcode, '17001')
        self.assertEqual(a2136.streettype, 'ACCE')
        self.assertEqual(a2136.street, 'Carrer inventat')
        self.assertEqual(a2136.streetnumber, '1')
        self.assertEqual(a2136.portal, '2')
        self.assertEqual(a2136.staircase, '3')
        self.assertEqual(a2136.floor, '4')
        self.assertEqual(a2136.door, '5')
        self.assertEqual(a2136.zipcode, '17001')
        self.assertEqual(a2136.comunitypressure, 'B5')
        self.assertEqual(a2136.aptransind, 'S')
        self.assertEqual(a2136.aptransnumber, '1234')
        self.assertEqual(a2136.reig, '123456')
        self.assertEqual(a2136.iricertificateneeded, 'S')
        self.assertEqual(a2136.iricertificatedate, '2020-01-01')
        self.assertEqual(a2136.designpower, '10000')
        self.assertEqual(a2136.terminstexist, 'S')


class test_A1_42(unittest.TestCase):

    def setUp(self):
        self.xml_a242 = open(get_data("a242.xml"), "r")
        self.xml_a342 = open(get_data("a342.xml"), "r")
        self.xml_a442 = open(get_data("a442.xml"), "r")
        self.xml_a2542 = open(get_data("a2542.xml"), "r")
        self.xml_a2s42 = open(get_data("a2s42.xml"), "r")
        self.xml_a3s42 = open(get_data("a3s42.xml"), "r")
        self.xml_a4s42 = open(get_data("a4s42.xml"), "r")

    def tearDown(self):
        self.xml_a242.close()
        self.xml_a342.close()
        self.xml_a442.close()
        self.xml_a2542.close()
        self.xml_a2s42.close()
        self.xml_a3s42.close()
        self.xml_a4s42.close()

    def test_a242(self):
        a242 = A1_42(self.xml_a242)
        a242.parse_xml()
        self.assertEqual(a242.reqcode, u'10_4E4mh15')
        self.assertEqual(a242.comreferencenum, u'123456789123')
        self.assertEqual(a242.responsedate, u'2020-03-13')
        self.assertEqual(a242.responsehour, u'13:52:14')
        self.assertEqual(a242.result, u'01')
        self.assertEqual(a242.resultdesc, u'Aceptada')
        self.assertEqual(a242.resultreason, u'R01')
        self.assertEqual(a242.resultreasondesc, u'Cliente suministrado desde planta satélite.')
        self.assertEqual(a242.nationality, u'SB')
        self.assertEqual(a242.documenttype, u'01')
        self.assertEqual(a242.documentnum, u'20_f8aQW2mqoLv4GLJ8M')
        self.assertEqual(a242.cups, u'20ai6Nmki1j8m5qCDmuG')
        self.assertEqual(a242.updatereason, u'01')
        self.assertEqual(a242.outgoingpressuregranted, u'87952.239')
        self.assertEqual(a242.singlenomination, u'S')
        self.assertEqual(a242.netsituation, u'Girona')
        self.assertEqual(a242.newmodeffectdate, u'01')
        self.assertEqual(a242.foreseentransferdate, u'2020-03-13')
        self.assertEqual(a242.StatusPS, u'1')
        self.assertEqual(a242.extrainfo, u'400_Y1cLoMJo2SXTeCdHmJCodtnOvEsmDn')

        self.assertEqual(a242.productlist[0].productcode, u'TESTCODE1')
        self.assertEqual(a242.productlist[0].producttype, u'03')
        self.assertEqual(a242.productlist[0].producttolltype, u'31')
        self.assertEqual(a242.productlist[0].productqd, u'23.6')
        self.assertEqual(a242.productlist[0].productqa, u'12345')
        self.assertEqual(a242.productlist[0].productstartdate, u'2020-01-01')
        self.assertEqual(a242.productlist[0].productenddate, u'2020-02-01')

        self.assertEqual(a242.productlist[1].productcode, u'TESTCODE2')
        self.assertEqual(a242.productlist[1].producttype, u'02')
        self.assertEqual(a242.productlist[1].producttolltype, u'32')
        self.assertEqual(a242.productlist[1].productqd, u'23.5')
        self.assertEqual(a242.productlist[1].productqa, u'1234')
        self.assertEqual(a242.productlist[1].productstartdate, u'2020-01-02')
        self.assertEqual(a242.productlist[1].productenddate, u'2020-02-02')

    def test_a342(self):
        a342 = A1_42(self.xml_a342)
        a342.parse_xml()
        self.assertEqual(a342.reqcode, '0123456789')
        self.assertEqual(a342.comreferencenum, '000123456789')
        self.assertEqual(a342.responsedate, '2018-05-01')
        self.assertEqual(a342.responsehour, '13:00:00')
        self.assertEqual(a342.nationality, 'ES')
        self.assertEqual(a342.documenttype, '01')
        self.assertEqual(a342.documentnum, '11111111H')
        self.assertEqual(a342.cups, 'ES1234000000000001JN')
        self.assertEqual(a342.lastinspectionsdate, '2018-07-01')
        self.assertEqual(a342.lastinspectionsresult, '01')
        self.assertEqual(a342.transfereffectivedate, '2018-07-02')
        self.assertEqual(a342.telemetering, 'S')
        self.assertEqual(a342.readingtype, '1')
        self.assertEqual(a342.gasusetype, '01')
        self.assertEqual(a342.updatereason, '01')
        self.assertEqual(a342.activationtype, '001')
        self.assertEqual(a342.closingtype, '001')
        self.assertEqual(a342.canonircperiodicity, '01')
        self.assertEqual(a342.StatusPS, '1')
        self.assertEqual(a342.lectureperiodicity, '02')
        self.assertEqual(a342.extrainfo, 'comentarios extras')

        self.assertEqual(len(a342.correctorlist), 2)
        corrector = a342.correctorlist[0]
        self.assertEqual(corrector.correctedlecture, u'2200')
        self.assertEqual(corrector.correctormodel, u'modelo1')
        self.assertEqual(corrector.correctornumber, u'D123456')
        self.assertEqual(corrector.correctorproperty, u'01')
        self.assertEqual(corrector.correctortype, u'01')
        self.assertEqual(len(a342.counterlist), 2)
        counter = a342.counterlist[1]
        self.assertEqual(counter.countermodel, u'marca2')
        self.assertEqual(counter.counternumber, u'C123456')
        self.assertEqual(counter.counterpressure, u'13245.321')
        self.assertEqual(counter.counterproperty, u'06')
        self.assertEqual(counter.countertype, u'tipo2')
        self.assertEqual(counter.reallecture, u'3000')

        self.assertEqual(a342.productlist[0].productcode, u'TESTCODE1')
        self.assertEqual(a342.productlist[0].producttype, u'03')
        self.assertEqual(a342.productlist[0].producttolltype, u'31')
        self.assertEqual(a342.productlist[0].productqd, u'23.6')
        self.assertEqual(a342.productlist[0].productqa, u'12345')
        self.assertEqual(a342.productlist[0].productstartdate, u'2020-01-01')
        self.assertEqual(a342.productlist[0].productenddate, u'2020-02-01')

        self.assertEqual(a342.productlist[1].productcode, u'TESTCODE2')
        self.assertEqual(a342.productlist[1].producttype, u'02')
        self.assertEqual(a342.productlist[1].producttolltype, u'32')
        self.assertEqual(a342.productlist[1].productqd, u'23.5')
        self.assertEqual(a342.productlist[1].productqa, u'1234')
        self.assertEqual(a342.productlist[1].productstartdate, u'2020-01-02')
        self.assertEqual(a342.productlist[1].productenddate, u'2020-02-02')

    def test_a442(self):
        a4_42 = A1_42(self.xml_a442)
        a4_42.parse_xml()
        self.assertEqual(a4_42.codi_sollicitud, u'000123456789')
        self.assertEqual(a4_42.comreferencenum, u'000123456789')
        self.assertEqual(a4_42.cups, u'ES1234000000000001JN')
        self.assertEqual(a4_42.documentnum, u'11111111H')
        self.assertEqual(a4_42.documenttype, u'01')
        self.assertEqual(a4_42.extrainfo, u'comentarios extras')
        self.assertEqual(a4_42.nationality, u'ES')
        self.assertEqual(a4_42.reqcode, u'0123456789')
        self.assertEqual(a4_42.responsedate, u'2018-05-01')
        self.assertEqual(a4_42.responsehour, u'13:00:00')
        self.assertEqual(a4_42.resultreason, u'R32')
        self.assertEqual(a4_42.resultreasondesc, u'Fecha efecto solicitada anterior al día actual.')
        self.assertEqual(a4_42.updatereason, u'01')
        self.assertEqual(a4_42.closingtype, u'064')
        self.assertEqual(a4_42.closingtypedesc, u'No quiere gas')
        self.assertEqual(a4_42.interventiondate, u'2016-01-01')
        self.assertEqual(a4_42.interventionhourfrom, u'09:00:00')
        self.assertEqual(a4_42.interventionhourto, u'12:00:00')
        self.assertEqual(a4_42.visitnumber, u'987')

    def test_a2542(self):
        a25_42 = A1_42(self.xml_a2542)
        a25_42.parse_xml()
        self.assertEqual(a25_42.reqcode, u"10_p62j9fh")
        self.assertEqual(a25_42.visitdate, u"2020-03-13")
        self.assertEqual(a25_42.visithour, u"14:26:35")
        self.assertEqual(a25_42.comreferencenum, u"123456789")
        self.assertEqual(a25_42.informationtype, u"002")
        self.assertEqual(a25_42.informationtypedesc,
                         u"0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001")
        self.assertEqual(a25_42.interventiondate, u"2020-03-13")
        self.assertEqual(a25_42.interventionhourfrom, u"14:26:35")
        self.assertEqual(a25_42.interventionhourto, u"14:26:35")
        self.assertEqual(a25_42.cups, u"20alzDPKUDB5HhZDhn5X")
        self.assertEqual(a25_42.visitnumber, u"228")
        self.assertEqual(a25_42.operationnum, u"40_tQzwG5OT6YTye1UiYVtoV3r9VymR5B")
        self.assertEqual(a25_42.extrainfo, u"400_C9BEFQSmU4c7fJcqlXEYL79KyKwcZ9")
        self.assertEqual(len(a25_42.defectlist), 2)
        defect = a25_42.defectlist[1]
        self.assertEqual(defect.code, u'002')
        self.assertEqual(defect.description, u'Desc2')

    def test_a2s42(self):
        a2s42 = A1_42(self.xml_a2s42)
        a2s42.parse_xml()
        self.assertEqual(a2s42.reqcode, u'0123456789')
        self.assertEqual(a2s42.responsedate, u'2018-05-01')
        self.assertEqual(a2s42.responsehour, u'13:00:00')
        self.assertEqual(a2s42.nationality, u"ES")
        self.assertEqual(a2s42.documenttype, u"01")
        self.assertEqual(a2s42.documentnum, u"ES11111111H")
        self.assertEqual(a2s42.cups, u'ES1234000000000001JN')
        self.assertEqual(a2s42.foreseentransferdate, u'2018-05-09')
        self.assertEqual(a2s42.extrainfo, u'Coments')

    def test_a3s42(self):
        a1_42 = A1_42(self.xml_a3s42)
        a1_42.parse_xml()
        self.assertEqual(a1_42.nationality, u'ES')
        self.assertEqual(a1_42.readingtype, u'1')
        self.assertEqual(a1_42.cups, u'ES1234000000000001JN')
        self.assertEqual(a1_42.documentnum, u'11111111H')
        self.assertEqual(a1_42.documenttype, u'01')
        self.assertEqual(a1_42.extrainfo, u'comentarios extras')
        self.assertEqual(a1_42.reqcode, u'0123456789')
        self.assertEqual(a1_42.responsedate, u'2018-05-01')
        self.assertEqual(a1_42.responsehour, u'13:00:00')
        self.assertEqual(a1_42.transfereffectivedate, u'2018-07-01')
        self.assertEqual(len(a1_42.correctorlist), 2)
        corrector = a1_42.correctorlist[0]
        self.assertEqual(corrector.correctedlecture, u'2200')
        self.assertEqual(corrector.correctormodel, u'modelo1')
        self.assertEqual(corrector.correctornumber, u'D123456')
        self.assertEqual(corrector.correctorproperty, u'01')
        self.assertEqual(corrector.correctortype, u'01')
        self.assertEqual(len(a1_42.counterlist), 2)
        counter = a1_42.counterlist[1]
        self.assertEqual(counter.countermodel, u'marca2')
        self.assertEqual(counter.counternumber, u'C123456')
        self.assertEqual(counter.counterpressure, u'13245.321')
        self.assertEqual(counter.counterproperty, u'06')
        self.assertEqual(counter.countertype, u'tipo2')
        self.assertEqual(counter.reallecture, u'3000')

    def test_a4s42(self):
        a4s42 = A1_42(self.xml_a4s42)
        a4s42.parse_xml()
        self.assertEqual(a4s42.reqcode, '10_z9f2k6S')
        self.assertEqual(a4s42.responsedate, '2020-03-13')
        self.assertEqual(a4s42.responsehour, '15:09:09')
        self.assertEqual(a4s42.nationality, 'ES')
        self.assertEqual(a4s42.documenttype, '01')
        self.assertEqual(a4s42.documentnum, '11111111H')
        self.assertEqual(a4s42.cups, '20aXn4jOtXkA8PF9JCHH')
        self.assertEqual(a4s42.previousatrcode, '000111222333444555666777')
        self.assertEqual(a4s42.resultreason, 'R01')
        self.assertEqual(a4s42.resultreasondesc, u'Cliente suministrado desde planta satélite.')
        self.assertEqual(a4s42.extrainfo, '400_ssYcpvXKXUF3DuQzltLLSTHWo2SDsC')


class test_A1_43(unittest.TestCase):

    def setUp(self):
        self.xml_a243 = open(get_data("a243.xml"), "r")
        self.xml_a343 = open(get_data("a343.xml"), "r")
        self.xml_a443 = open(get_data("a443.xml"), "r")
        self.xml_a2543 = open(get_data("a2543.xml"), "r")
        self.xml_a2643 = open(get_data("a2643.xml"), "r")

    def tearDown(self):
        self.xml_a243.close()
        self.xml_a343.close()
        self.xml_a443.close()
        self.xml_a2543.close()
        self.xml_a2643.close()

    def test_a243(self):
        a243 = A1_43(self.xml_a243)
        a243.parse_xml()
        self.assertEqual(a243.reqcode, u'10_4E4mh15')
        self.assertEqual(a243.comreferencenum, u'123456789123')
        self.assertEqual(a243.responsedate, u'2020-03-13')
        self.assertEqual(a243.responsehour, u'13:52:14')
        self.assertEqual(a243.result, u'01')
        self.assertEqual(a243.resultdesc, u'Aceptada')
        self.assertEqual(a243.resultreason, u'R01')
        self.assertEqual(a243.resultreasondesc, u'Cliente suministrado desde planta satélite.')
        self.assertEqual(a243.nationality, u'SB')
        self.assertEqual(a243.documenttype, u'01')
        self.assertEqual(a243.documentnum, u'20_f8aQW2mqoLv4GLJ8M')
        self.assertEqual(a243.cups, u'20ai6Nmki1j8m5qCDmuG')
        self.assertEqual(a243.extrainfo, u'400_Y1cLoMJo2SXTeCdHmJCodtnOvEsmDn')

        self.assertEqual(a243.productlist[0].productcode, u'TESTCODE1')
        self.assertEqual(a243.productlist[0].producttype, u'03')
        self.assertEqual(a243.productlist[0].producttolltype, u'31')
        self.assertEqual(a243.productlist[0].productqd, u'23.6')
        self.assertEqual(a243.productlist[0].productqa, u'12345')
        self.assertEqual(a243.productlist[0].productstartdate, u'2020-01-01')
        self.assertEqual(a243.productlist[0].productenddate, u'2020-02-01')

        self.assertEqual(a243.productlist[1].productcode, u'TESTCODE2')
        self.assertEqual(a243.productlist[1].producttype, u'02')
        self.assertEqual(a243.productlist[1].producttolltype, u'32')
        self.assertEqual(a243.productlist[1].productqd, u'23.5')
        self.assertEqual(a243.productlist[1].productqa, u'1234')
        self.assertEqual(a243.productlist[1].productstartdate, u'2020-01-02')
        self.assertEqual(a243.productlist[1].productenddate, u'2020-02-02')



    def test_a343(self):
        a343 = A1_43(self.xml_a343)
        a343.parse_xml()
        self.assertEqual(a343.reqcode, '0123456789')
        self.assertEqual(a343.comreferencenum, '000123456789')

        self.assertEqual(a343.responsedate, '2020-01-01')
        self.assertEqual(a343.responsehour, '13:37:00')
        self.assertEqual(a343.result, '09')
        self.assertEqual(a343.resultdesc, 'Correcto')

        self.assertEqual(a343.cups, 'ES1234000000000001JN')
        self.assertEqual(a343.extrainfo, 'comentarios extras')

        self.assertEqual(a343.productlist[0].productcode, u'TESTCODE1')
        self.assertEqual(a343.productlist[0].producttype, u'03')
        self.assertEqual(a343.productlist[0].producttolltype, u'31')
        self.assertEqual(a343.productlist[0].productqd, u'23.6')
        self.assertEqual(a343.productlist[0].productqa, u'12345')
        self.assertEqual(a343.productlist[0].productstartdate, u'2020-01-01')
        self.assertEqual(a343.productlist[0].productenddate, u'2020-02-01')

        self.assertEqual(a343.productlist[1].productcode, u'TESTCODE2')
        self.assertEqual(a343.productlist[1].producttype, u'02')
        self.assertEqual(a343.productlist[1].producttolltype, u'32')
        self.assertEqual(a343.productlist[1].productqd, u'23.5')
        self.assertEqual(a343.productlist[1].productqa, u'1234')
        self.assertEqual(a343.productlist[1].productstartdate, u'2020-01-02')
        self.assertEqual(a343.productlist[1].productenddate, u'2020-02-02')

    def test_a443(self):
        a4_43 = A1_43(self.xml_a443)
        a4_43.parse_xml()

        self.assertEqual(a4_43.reqcode, u'0123456789')
        self.assertEqual(a4_43.comreferencenum, u'000123456789')
        self.assertEqual(a4_43.responsedate, u'2018-05-01')
        self.assertEqual(a4_43.responsehour, u'13:00:00')
        self.assertEqual(a4_43.nationality, u'ES')
        self.assertEqual(a4_43.documenttype, u'01')
        self.assertEqual(a4_43.documentnum, u'11111111H')
        self.assertEqual(a4_43.cups, u'ES1234000000000001JN')

        self.assertEqual(a4_43.result, '13')
        self.assertEqual(a4_43.resultdesc, 'Correcto')
        self.assertEqual(a4_43.resultreason, u'R32')
        self.assertEqual(a4_43.resultreasondesc, u'Fecha efecto solicitada anterior al día actual.')

        self.assertEqual(a4_43.closingtype, u'064')
        self.assertEqual(a4_43.closingtypedesc, u'No quiere gas')
        self.assertEqual(a4_43.interventiondate, u'2016-01-01')
        self.assertEqual(a4_43.interventionhourfrom, u'09:00:00')
        self.assertEqual(a4_43.interventionhourto, u'12:00:00')
        self.assertEqual(a4_43.visitnumber, u'987')

        self.assertEqual(a4_43.extrainfo, u'comentarios extras')

    def test_a2543(self):
        a25_43 = A1_43(self.xml_a2543)
        a25_43.parse_xml()
        self.assertEqual(a25_43.reqcode, u"10_p62j9fh")
        self.assertEqual(a25_43.visitdate, u"2020-03-13")
        self.assertEqual(a25_43.visithour, u"14:26:35")
        self.assertEqual(a25_43.comreferencenum, u"123456789")
        self.assertEqual(a25_43.informationtype, u"002")
        self.assertEqual(a25_43.informationtypedesc,
                         u"0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001")
        self.assertEqual(a25_43.interventiondate, u"2020-03-13")
        self.assertEqual(a25_43.interventionhourfrom, u"14:26:35")
        self.assertEqual(a25_43.interventionhourto, u"14:26:35")
        self.assertEqual(a25_43.cups, u"20alzDPKUDB5HhZDhn5X")
        self.assertEqual(a25_43.visitnumber, u"228")
        self.assertEqual(a25_43.operationnum, u"40_tQzwG5OT6YTye1UiYVtoV3r9VymR5B")
        self.assertEqual(a25_43.extrainfo, u"400_C9BEFQSmU4c7fJcqlXEYL79KyKwcZ9")
        self.assertEqual(len(a25_43.defectlist), 2)
        defect = a25_43.defectlist[1]
        self.assertEqual(defect.code, u'002')
        self.assertEqual(defect.description, u'Desc2')

    def test_a2643(self):
        a26_43 = A1_43(self.xml_a2643)
        a26_43.parse_xml()
        self.assertEqual(a26_43.reqcode, u"7777")
        self.assertEqual(a26_43.cups, u"ES1234000000000001JN")
        self.assertEqual(a26_43.comreferencenum, u'000123456789')

        self.assertEqual(a26_43.stateincidence, u'01') ######
        self.assertEqual(a26_43.contact.contactname, u'mortdegana')
        self.assertEqual(a26_43.contact.contacttelephone1, u'+34666555444')
        self.assertEqual(a26_43.contact.contacttelephone2, u'+34666555444')
        self.assertEqual(a26_43.contact.contacttelephone3, u'+34666555444')
        self.assertEqual(a26_43.contact.contactemail, u'matalas@gas')

        self.assertEqual(a26_43.extrainfo, u"comentarios extra")


