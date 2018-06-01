#!/usr/bin/env python
# -*- coding: utf-8 -*-
from . import unittest
from .utils import get_data
from gestionatr.input.messages \
    import C1, C2, A3, B1, M1, D1, W1, Q1, R1, F1, Deadlines, A1_41
from gestionatr.input.messages.F1 \
    import agrupar_lectures_per_data, obtenir_data_inici_i_final


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

    def tearDown(self):
        self.xml_c201_completo.close()
        self.xml_c202_accept.close()
        self.xml_c203.close()

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
        self.assertEqual(direccion.poblacion, u'17079')
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


class test_A3(unittest.TestCase):

    def setUp(self):
        self.xml_a301 = open(get_data("a301.xml"), "r")

    def tearDown(self):
        self.xml_a301.close()

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
        self.assertEqual(direccion.poblacion, u'17079')
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


class test_B1(unittest.TestCase):

    def setUp(self):
        self.xml_b101 = open(get_data("b101.xml"), "r")
        self.xml_b102_accept = open(get_data("b102_accept.xml"), "r")
        self.xml_b104_accept = open(get_data("b104_accept.xml"), "r")
        self.xml_b105 = open(get_data("b105.xml"), "r")

    def tearDown(self):
        self.xml_b101.close()
        self.xml_b102_accept.close()
        self.xml_b104_accept.close()
        self.xml_b105.close()

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

    def tearDown(self):
        self.xml_d101.close()

    def test_d101(self):
        d1 = D1(self.xml_d101)
        d1.parse_xml()
        self.assertEqual(d1.periodicidad_facturacion, u'01')
        self.assertEqual(d1.fecha_prevista_aplicacion_cambio_atr, u'2016-06-09')
        self.assertEqual(d1.motivo_cambio_atr_desde_distribuidora, u'01')


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
        self.xml_r104 = open(get_data("r104.xml"), "r")
        self.xml_r105 = open(get_data("r105.xml"), "r")

    def tearDown(self):
        self.xml_r101.close()
        self.xml_r102_accept.close()
        self.xml_r103.close()
        self.xml_r103_intervenciones.close()
        self.xml_r104.close()
        self.xml_r105.close()

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
        self.assertEqual(ubi.poblacion, u'17079')
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
        self.assertEqual(direccion.poblacion, u'17079')
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
        self.assertEqual(ubi.poblacion, u'17079')
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
        self.assertEqual(direccion.poblacion, u'17079')
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
        # Cod Contrato
        self.assertEqual(r1.cod_contrato, u'383922379')


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
