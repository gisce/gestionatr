#!/usr/bin/env python
# -*- coding: utf-8 -*-
from . import unittest
from .utils import get_data, assertXmlEqual
from gestionatr.output.messages import sw_c1 as c1


class test_C1(unittest.TestCase):

    def setUp(self):
        self.xml_c101_completo = open(get_data("c101.xml"), "r")
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
        self.xml_c102_accept.close()
        self.xml_c102_reject.close()
        self.xml_c104.close()
        self.xml_c105.close()
        self.xml_c106.close()
        self.xml_c108.close()
        self.xml_c109.close()
        self.xml_c111.close()
        self.xml_c112.close()

    def test_create_pas01(self):
        # MensajeCambiodeComercializadorSinCambios
        mensaje_cambiode_comercializador_sin_cambios = c1.MensajeCambiodeComercializadorSinCambios()

        # Cabecera
        cabecera = c1.Cabecera()
        cabecera_fields = {
            'codigo_ree_empresa_emisora': '1234',
            'codigo_ree_empresa_destino': '4321',
            'codigo_del_proceso': 'C1',
            'codigo_del_paso': '01',
            'codigo_de_solicitud': '201607211259',
            'secuencial_de_solicitud': '01',
            'fecha': '2016-07-21T12:59:47',
            'cups': 'ES1234000000000001JN0F',
        }
        cabecera.feed(cabecera_fields)

        # CambiodeComercializadorSinCambios
        cambiode_comercializador_sin_cambios = c1.CambiodeComercializadorSinCambios()

        # DatosSolicitud
        datos_solicitud = c1.DatosSolicitud()
        datos_solicitud_fields = {
            'ind_activacion': 'L',
            'fecha_prevista_accion': '2016-06-06',
            'contratacion_incondicional_ps': 'S',
        }
        datos_solicitud.feed(datos_solicitud_fields)

        # Cliente
        cliente = c1.Cliente()

        # IdCliente
        id_cliente = c1.IdCliente()
        id_cliente_fields = {
            'tipo_identificador': 'NI',
            'identificador': 'B36385870',
            'tipo_persona': 'J',
        }
        id_cliente.feed(id_cliente_fields)

        # Nombre
        nombre = c1.Nombre()
        nombre_fields = {
            'nombre_de_pila': '',
            'primer_apellido': '',
            'segundo_apellido': '',
            'razon_social': 'ACC Y COMP DE COCINA MILLAN Y MUÑOZ',
        }
        nombre.feed(nombre_fields)

        # Telefono
        telefono = c1.Telefono()
        telefono_fields = {
            'prefijo_pais': '34',
            'numero': '666777888',
        }
        telefono.feed(telefono_fields)

        cliente_fields = {
            'id_cliente': id_cliente,
            'nombre': nombre,
            'telefono': telefono,
            'correo_electronico': 'email@host',
        }
        cliente.feed(cliente_fields)

        # RegistrosDocumento
        registros_documento = c1.RegistrosDocumento()
        # RegistroDoc
        registro_doc1 = c1.RegistroDoc()
        registro_doc_fields1 = {
            'tipo_doc_aportado': '08',
            'direccion_url': 'http://eneracme.com/docs/NIF11111111H.pdf'
        }
        registro_doc1.feed(registro_doc_fields1)

        registro_doc2 = c1.RegistroDoc()
        registro_doc_fields2 = {
            'tipo_doc_aportado': '07',
            'direccion_url': 'http://eneracme.com/docs/NIF11111111H.pdf'
        }
        registro_doc2.feed(registro_doc_fields2)
        registros_documento_fields = {
            'registro_doc_list': [registro_doc1, registro_doc2],
        }
        registros_documento.feed(registros_documento_fields)

        cambiode_comercializador_sin_cambios_fields = {
            'datos_solicitud': datos_solicitud,
            'cliente': cliente,
            'comentarios': '',
            'registros_documento': registros_documento,
        }
        cambiode_comercializador_sin_cambios.feed(
            cambiode_comercializador_sin_cambios_fields)

        mensaje_cambiode_comercializador_sin_cambios_fields = {
            'cabecera': cabecera,
            'cambiode_comercializador_sin_cambios': cambiode_comercializador_sin_cambios,
        }
        mensaje_cambiode_comercializador_sin_cambios.feed(
            mensaje_cambiode_comercializador_sin_cambios_fields)

        mensaje_cambiode_comercializador_sin_cambios.build_tree()
        xml = str(mensaje_cambiode_comercializador_sin_cambios)
        assertXmlEqual(xml, self.xml_c101_completo.read())
