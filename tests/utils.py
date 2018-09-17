# -*- coding: utf-8 -*-
import os
from gestionatr.output.messages.base import Cabecera
from gestionatr.output.messages import sw_c1 as c1
from gestionatr.output.messages import sw_c2 as c2
from . import unittest

_ROOT = os.path.abspath(os.path.dirname(__file__))


def get_data(path):
    filename = isinstance(path, (list, tuple)) and path[0] or path
    return os.path.join(_ROOT, 'data', filename)


def get_header(process='C1', step='01', code='201607211259', date='2016-07-21T12:59:47'):
    header = Cabecera()
    vals = {
        'codigo_del_proceso': process,
        'codigo_del_paso': step,
        'codigo_de_solicitud': code,
        'secuencial_de_solicitud': '01',
        'cups': 'ES1234000000000001JN0F',
        'codigo_ree_empresa_emisora': '1234',
        'codigo_ree_empresa_destino': '4321',
        'fecha': date,
    }
    header.feed(vals)
    return header


def get_cliente(dir=False, tipo_dir=None):
    # Cliente
    cliente = c2.Cliente()

    # IdCliente
    id_cliente = c2.IdCliente()
    id_cliente_fields = {
        'tipo_identificador': 'NI',
        'identificador': 'B36385870',
        'tipo_persona': 'J',
    }
    id_cliente.feed(id_cliente_fields)

    # Nombre
    nombre = c2.Nombre()
    nombre_fields = {
        'nombre_de_pila': '',
        'primer_apellido': '',
        'segundo_apellido': '',
        'razon_social': u'ACC Y COMP DE COCINA MILLAN Y MUÑOZ',
    }
    nombre.feed(nombre_fields)

    # Telefono
    telefono1 = c2.Telefono()
    telefono_fields = {
        'prefijo_pais': '36',
        'numero': '666777666',
    }
    telefono1.feed(telefono_fields)
    telefono2 = c2.Telefono()
    telefono_fields = {
        'prefijo_pais': '37',
        'numero': '666777777',
    }
    telefono2.feed(telefono_fields)
    telefono3 = c2.Telefono()
    telefono_fields = {
        'prefijo_pais': '38',
        'numero': '666777888',
    }
    telefono3.feed(telefono_fields)
    telefonos = [telefono1, telefono2, telefono3]

    indicador_tipo_direccion = None
    if tipo_dir:
        indicador_tipo_direccion = tipo_dir
    direccion = None
    if dir:
        # Direccion
        direccion = c2.Direccion()
        direccion_fields = {
            'pais': 'España',
            'provincia': '17',
            'municipio': '17079',
            'poblacion': '17079',
            'tipo_via': 'PZ',
            'cod_postal': '17001',
            'calle': 'MELA MUTERMILCH',
            'numero_finca': '2',
            'piso': '001',
            'puerta': '001',
            'tipo_aclarador_finca': 'BI',
            'aclarador_finca': 'Bloque de Pisos',
        }
        direccion.feed(direccion_fields)

    cliente_fields = {
        'id_cliente': id_cliente,
        'nombre': nombre,
        'telefonos': telefonos,
        'correo_electronico': 'email@host',
        'indicador_tipo_direccion': indicador_tipo_direccion,
        'direccion': direccion
    }
    cliente.feed(cliente_fields)
    return cliente


def get_contacto(email=True):
    # Contacto
    contacto = c2.Contacto()

    # Telefono
    telefono = c2.Telefono()
    telefono_fields = {
        'prefijo_pais': '34',
        'numero': '666777888',
    }
    telefono.feed(telefono_fields)
    telefono2 = c2.Telefono()
    telefono_fields = {
        'prefijo_pais': '34',
        'numero': '666777999',
    }
    telefono2.feed(telefono_fields)
    telefonos = [telefono, telefono2]

    correo = None
    if email:
        correo = 'email@host'
    contacto_fields = {
        'persona_de_contacto': 'Nombre Inventado',
        'telefonos': telefonos,
        'correo_electronico': correo,
    }
    contacto.feed(contacto_fields)
    return contacto


def get_medida():
    # Medida
    medida = c2.Medida()

    # ModelosAparato
    md1 = c2.ModeloAparato()
    modelo_aparato_fields = {
        'tipo_aparato': 'CG',
        'marca_aparato': '132',
        'modelo_marca': '011',
    }
    md1.feed(modelo_aparato_fields)
    md2 = c2.ModeloAparato()
    modelo_aparato_fields = {
        'tipo_aparato': 'CG',
        'marca_aparato': '132',
        'modelo_marca': '012',
    }
    md2.feed(modelo_aparato_fields)

    modelos_aparato = c2.ModelosAparato()
    modelos_aparato_fields = {
        'modelo_aparato_list': [md1, md2],
    }
    modelos_aparato.feed(modelos_aparato_fields)

    medida_fields = {
        'propiedad_equipo': 'C',
        'tipo_equipo_medida': 'L00',
        'modelos_aparato': modelos_aparato,
    }
    medida.feed(medida_fields)
    return medida


def assertXmlEqual(got, want):
    from lxml.doctestcompare import LXMLOutputChecker
    from doctest import Example

    checker = LXMLOutputChecker()
    if checker.check_output(want, got, 0):
        return
    message = checker.output_difference(Example("", want), got, 0)
    raise AssertionError(message)

unittest.TestCase.assertXmlEqual = assertXmlEqual
unittest.TestCase.__str__ = unittest.TestCase.id