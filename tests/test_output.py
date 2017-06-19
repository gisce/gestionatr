#!/usr/bin/env python
# -*- coding: utf-8 -*-
from . import unittest
from .utils import get_data, assertXmlEqual, get_header, get_cliente, get_contacto, get_medida
from gestionatr.output.messages import sw_c1 as c1
from gestionatr.output.messages import sw_c2 as c2
from gestionatr.output.messages import sw_a3 as a3
from gestionatr.output.messages import sw_m1 as m1
from gestionatr.output.messages import sw_d1 as d1
from gestionatr.output.messages import sw_q1 as q1
from gestionatr.output.messages import sw_w1 as w1
from gestionatr.output.messages import sw_b1 as b1
from gestionatr.output.messages import sw_r1 as r1
from gestionatr.output.messages import sw_f1 as f1


class test_C1(unittest.TestCase):

    def setUp(self):
        self.xml_c101_completo = open(get_data("c101.xml"), "r")
        self.xml_c102_accept = open(get_data("c102_accept.xml"), "r")
        self.xml_c102_reject = open(get_data("c102_reject.xml"), "r")
        self.xml_c105 = open(get_data("c105.xml"), "r")
        self.xml_c106 = open(get_data("c106.xml"), "r")
        self.xml_c109 = open(get_data("c109.xml"), "r")
        self.xml_c111 = open(get_data("c111.xml"), "r")
        self.xml_c112 = open(get_data("c112.xml"), "r")

        # RegistrosDocumento
        self.registros_documento = c1.RegistrosDocumento()
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
        self.registros_documento.feed(registros_documento_fields)

        self.cliente = get_cliente()

        # PuntosDeMedida
        self.puntos_de_medida = c1.PuntosDeMedida()
        # PuntoDeMedida
        punto_de_medida = c1.PuntoDeMedida()
        # Aparatos
        aparatos = c1.Aparatos()
        # Aparato
        aparato = c1.Aparato()

        # ModeloAparato
        modelo_aparato = c1.ModeloAparato()
        modelo_aparato_fields = {
            'tipo_aparato': 'CG',
            'marca_aparato': '132',
            'modelo_marca': '011',
        }
        modelo_aparato.feed(modelo_aparato_fields)

        # DatosAparato
        datos_aparato = c1.DatosAparato()
        datos_aparato_fields = {
            'periodo_fabricacion': '2005',
            'numero_serie': '0000539522',
            'funcion_aparato': 'M',
            'num_integradores': '18',
            'constante_energia': '1.000',
            'constante_maximetro': '1.000',
            'ruedas_enteras': '08',
            'ruedas_decimales': '02',
        }
        datos_aparato.feed(datos_aparato_fields)

        # Medidas
        medidas = c1.Medidas()
        # Medida 1
        medida1 = c1.Medida()
        medida_fields = {
            'tipo_dhedm': '6',
            'periodo': '65',
            'magnitud_medida': 'PM',
            'procedencia': '30',
            'ultima_lectura_firme': '6.00',
            'fecha_lectura_firme': '2003-01-02',
            'anomalia': '01',
            'comentarios': 'Comentario sobre anomalia',
        }
        medida1.feed(medida_fields)
        # Medida 2
        medida2 = c1.Medida()
        medida_fields = {
            'tipo_dhedm': '6',
            'periodo': '66',
            'magnitud_medida': 'PM',
            'procedencia': '30',
            'ultima_lectura_firme': '6.00',
            'fecha_lectura_firme': '2003-01-03',
        }
        medida2.feed(medida_fields)
        medidas_fields = {
            'medida_list': [medida1, medida2],
        }
        medidas.feed(medidas_fields)

        aparato_fields = {
            'modelo_aparato': modelo_aparato,
            'tipo_movimiento': 'CX',
            'tipo_equipo_medida': 'L03',
            'tipo_propiedad_aparato': '1',
            'propietario': 'Desc. Propietario',
            'tipo_dhedm': '6',
            'modo_medida_potencia': '1',
            'lectura_directa': 'N',
            'cod_precinto': '02',
            'datos_aparato': datos_aparato,
            'medidas': medidas
        }

        aparato.feed(aparato_fields)
        aparatos_fields = {
            'aparato_list': [aparato],
        }
        aparatos.feed(aparatos_fields)

        punto_de_medida_fields = {
            'cod_pm': 'ES1234000000000001JN0F',
            'tipo_movimiento': 'A',
            'tipo_pm': '03',
            'cod_pm_principal': 'ES1234000000000002JN0F',
            'modo_lectura': '1',
            'funcion': 'P',
            'direccion_enlace': '39522',
            'direccion_punto_medida': '000000001',
            'num_linea': '12',
            'telefono_telemedida': '987654321',
            'estado_telefono': '1',
            'clave_acceso': '0000000007',
            'tension_pm': '0',
            'fecha_vigor': '2003-01-01',
            'fecha_alta': '2003-01-01',
            'fecha_baja': '2003-02-01',
            'aparatos': aparatos,
            'comentarios': 'Comentarios Varios',
        }
        punto_de_medida.feed(punto_de_medida_fields)

        puntos_de_medida_fields = {
            'punto_de_medida_list': [punto_de_medida],
        }
        self.puntos_de_medida.feed(puntos_de_medida_fields)

    def tearDown(self):
        self.xml_c101_completo.close()
        self.xml_c102_accept.close()
        self.xml_c102_reject.close()
        self.xml_c105.close()
        self.xml_c106.close()
        self.xml_c109.close()
        self.xml_c111.close()
        self.xml_c112.close()

    def test_create_pas01(self):
        # MensajeCambiodeComercializadorSinCambios
        mensaje = c1.MensajeCambiodeComercializadorSinCambios()

        # Cabecera
        cabecera = get_header(step='01')

        # CambiodeComercializadorSinCambios
        cambio_comer = c1.CambiodeComercializadorSinCambios()

        # DatosSolicitud
        datos_solicitud = c1.DatosSolicitud()
        datos_solicitud_fields = {
            'ind_activacion': 'L',
            'fecha_prevista_accion': '2016-06-06',
            'contratacion_incondicional_ps': 'S',
        }
        datos_solicitud.feed(datos_solicitud_fields)

        # Cliente
        cliente = self.cliente

        # RegistrosDocumento
        registros_documento = self.registros_documento

        cambiode_comercializador_sin_cambios_fields = {
            'datos_solicitud': datos_solicitud,
            'cliente': cliente,
            'registros_documento': registros_documento,
        }
        cambio_comer.feed(
            cambiode_comercializador_sin_cambios_fields)

        mensaje_cambiode_comercializador_sin_cambios_fields = {
            'cabecera': cabecera,
            'cambiode_comercializador_sin_cambios': cambio_comer,
        }
        mensaje.feed(
            mensaje_cambiode_comercializador_sin_cambios_fields)

        mensaje.build_tree()
        xml = str(mensaje)
        assertXmlEqual(xml, self.xml_c101_completo.read())

    def test_create_pas02(self):
        # MensajeAceptacionCambiodeComercializadorSinCambios
        mensaje = c1.MensajeAceptacionCambiodeComercializadorSinCambios()

        # Cabecera
        cabecera = get_header(step='02')

        # AceptacionCambiodeComercializadorSinCambios
        acept_cambio = c1.AceptacionCambiodeComercializadorSinCambios()

        # DatosAceptacion
        datos_aceptacion = c1.DatosAceptacion()
        datos_aceptacion_fields = {
            'fecha_aceptacion': '2016-06-06',
            'actuacion_campo': 'S',
            'fecha_ultima_lectura_firme': '2016-06-01',
        }
        datos_aceptacion.feed(datos_aceptacion_fields)

        # Contrato
        contrato = c1.Contrato()

        # CondicionesContractuales
        condiciones_contractuales = c1.CondicionesContractuales()
        potencias_contratadas = c1.PotenciasContratadas()
        potencias_contratadas.feed({'p1': 1000, 'p2': 2000})
        condiciones_contractuales_fields = {
            'tarifa_atr': '003',
            'potencias_contratadas': potencias_contratadas,
        }
        condiciones_contractuales.feed(condiciones_contractuales_fields)

        contrato_fields = {
            'tipo_contrato_atr': '02',
            'condiciones_contractuales': condiciones_contractuales,
            'tipo_activacion_prevista': 'C0',
            'fecha_activacion_prevista': '2016-07-06',
        }
        contrato.feed(contrato_fields)

        aceptacion_cambiode_comercializador_sin_cambios_fields = {
            'datos_aceptacion': datos_aceptacion,
            'contrato': contrato,
        }
        acept_cambio.feed(
            aceptacion_cambiode_comercializador_sin_cambios_fields)

        mensaje_aceptacion_cambiode_comercializador_sin_cambios_fields = {
            'cabecera': cabecera,
            'aceptacion_cambiode_comercializador_sin_cambios': acept_cambio,
        }
        mensaje.feed(
            mensaje_aceptacion_cambiode_comercializador_sin_cambios_fields)

        mensaje.build_tree()
        xml = str(mensaje)
        assertXmlEqual(xml, self.xml_c102_accept.read())

    def test_create_pas02_rej(self):
        # MensajeRechazo
        mensaje_rechazo = c1.MensajeRechazo()

        # Cabecera
        cabecera = get_header(step='02')

        # MensageRechazos
        rechazos = c1.Rechazos()

        # Rechazos
        r1 = c1.Rechazo()
        r1.feed({
            'secuencial': '1',
            'codigo_motivo': '01',
            'comentarios': 'Motiu de rebuig 01: No existe Punto de Suministro asociado al CUPS'
        })
        r2 = c1.Rechazo()
        r2.feed({
            'secuencial': '2',
            'codigo_motivo': '03',
            'comentarios': 'Cuando el CIF-NIF no coincide con el que figura en la base de datos del Distribuidor'
        })

        # RegistrosDocumento
        registros_documento = self.registros_documento

        rechazos_fields = {
            'fecha_rechazo': '2016-07-20',
            'rechazo_list': [r1, r2],
            'registros_documento': registros_documento,
        }
        rechazos.feed(rechazos_fields)

        mensaje_rechazo_fields = {
            'cabecera': cabecera,
            'rechazos': rechazos,
        }
        mensaje_rechazo.feed(mensaje_rechazo_fields)
        mensaje_rechazo.build_tree()
        xml = str(mensaje_rechazo)
        assertXmlEqual(xml, self.xml_c102_reject.read())

    def test_create_pas05(self):
        # MensajeActivacionCambiodeComercializadorSinCambios
        mensaje = c1.MensajeActivacionCambiodeComercializadorSinCambios()

        # Cabecera
        cabecera = get_header(step='05')

        # ActivacionCambiodeComercializadorSinCambios
        act_cambio = c1.ActivacionCambiodeComercializadorSinCambios()

        # DatosActivacion
        datos_activacion = c1.DatosActivacion()
        datos_activacion_fields = {
            'fecha': '2016-08-21',
        }
        datos_activacion.feed(datos_activacion_fields)

        # Contrato
        contrato = c1.Contrato()

        # IdContrato
        id_contrato = c1.IdContrato()
        id_contrato_fields = {
            'cod_contrato': '00001',
        }
        id_contrato.feed(id_contrato_fields)

        # CondicionesContractuales
        condiciones_contractuales = c1.CondicionesContractuales()

        # PotenciasContratadas
        potencias_contratadas = c1.PotenciasContratadas()
        potencias_contratadas.feed({'p1': 1000, 'p2': 2000})

        condiciones_contractuales_fields = {
            'tarifa_atr': '003',
            'periodicidad_facturacion': '01',
            'tipode_telegestion': '01',
            'potencias_contratadas': potencias_contratadas,
            'modo_control_potencia': '1',
            'marca_medida_con_perdidas': 'S',
            'tension_del_suministro': '10',
            'vas_trafo': '50',
            'porcentaje_perdidas': '05',
        }
        condiciones_contractuales.feed(condiciones_contractuales_fields)

        contrato_fields = {
            'id_contrato': id_contrato,
            'tipo_autoconsumo': '00',
            'tipo_contrato_atr': '02',
            'condiciones_contractuales': condiciones_contractuales,
        }
        contrato.feed(contrato_fields)

        # Puntos de Medida
        puntos_de_medida = self.puntos_de_medida

        activacion_cambiode_comercializador_sin_cambios_fields = {
            'datos_activacion': datos_activacion,
            'contrato': contrato,
            'puntos_de_medida': puntos_de_medida,
        }
        act_cambio.feed(
            activacion_cambiode_comercializador_sin_cambios_fields)

        mensaje_activacion_cambiode_comercializador_sin_cambios_fields = {
            'cabecera': cabecera,
            'activacion_cambiode_comercializador_sin_cambios': act_cambio,
        }
        mensaje.feed(mensaje_activacion_cambiode_comercializador_sin_cambios_fields)
        mensaje.build_tree()
        xml = str(mensaje)
        assertXmlEqual(xml, self.xml_c105.read())

    def test_create_pas06(self):
        # MensajeActivacionComercializadorSaliente
        mensaje_activacion_comercializador_saliente = c1.MensajeActivacionComercializadorSaliente()

        # Cabecera
        cabecera = get_header(step='06')

        # NotificacionComercializadoraSaliente
        notificacion_comercializadora_saliente = c1.NotificacionComercializadorSaliente()

        # DatosNotificacion
        datos_notificacion = c1.DatosNotificacion()
        datos_notificacion_fields = {
            'fecha_activacion': '2016-08-21',
        }
        datos_notificacion.feed(datos_notificacion_fields)

        # Contrato
        contrato = c1.Contrato()
        id_contrato = c1.IdContrato()
        id_contrato.feed({'cod_contrato': '00001'})
        contrato.feed({'id_contrato': id_contrato})

        # PuntosDeMedida
        puntos_de_medida = self.puntos_de_medida

        notificacion_comercializadora_saliente_fields = {
            'datos_notificacion': datos_notificacion,
            'contrato': contrato,
            'puntos_de_medida': puntos_de_medida,
        }
        notificacion_comercializadora_saliente.feed(
            notificacion_comercializadora_saliente_fields)

        mensaje_activacion_comercializador_saliente_fields = {
            'cabecera': cabecera,
            'notificacion_comercializador_saliente': notificacion_comercializadora_saliente,
        }
        mensaje_activacion_comercializador_saliente.feed(
            mensaje_activacion_comercializador_saliente_fields)
        mensaje_activacion_comercializador_saliente.build_tree()
        xml = str(mensaje_activacion_comercializador_saliente)
        assertXmlEqual(xml, self.xml_c106.read())

    def test_create_pas09(self):
        # MensajeAceptacionAnulacion
        mensaje_aceptacion_anulacion = c1.MensajeAceptacionAnulacion()

        # Cabecera
        cabecera = get_header(step='09')

        # AceptacionAnulacion
        aceptacion_anulacion = c1.AceptacionAnulacion()
        aceptacion_anulacion_fields = {
            'fecha_aceptacion': '2017-02-02',
        }
        aceptacion_anulacion.feed(aceptacion_anulacion_fields)

        mensaje_aceptacion_anulacion_fields = {
            'cabecera': cabecera,
            'aceptacion_anulacion': aceptacion_anulacion,
        }
        mensaje_aceptacion_anulacion.feed(mensaje_aceptacion_anulacion_fields)
        mensaje_aceptacion_anulacion.build_tree()
        xml = str(mensaje_aceptacion_anulacion)
        assertXmlEqual(xml, self.xml_c109.read())

    def test_create_pas11(self):
        # MensajeAceptacionCambiodeComercializadorSaliente
        mensaje_aceptacion_cambiode_comercializador_saliente = c1.MensajeAceptacionCambiodeComercializadorSaliente()

        # Cabecera
        cabecera = get_header(step='11')

        # AceptacionCambioComercializadorSaliente
        aceptacion_cambio_comercializador_saliente = c1.AceptacionCambioComercializadorSaliente()
        aceptacion_cambio_comercializador_saliente_fields = {
            'fecha_activacion_prevista': '2017-02-02',
        }
        aceptacion_cambio_comercializador_saliente.feed(aceptacion_cambio_comercializador_saliente_fields)

        mensaje_aceptacion_cambiode_comercializador_saliente_fields = {
            'cabecera': cabecera,
            'aceptacion_cambio_comercializador_saliente': aceptacion_cambio_comercializador_saliente,
        }
        mensaje_aceptacion_cambiode_comercializador_saliente.feed(mensaje_aceptacion_cambiode_comercializador_saliente_fields)
        mensaje_aceptacion_cambiode_comercializador_saliente.build_tree()
        xml = str(mensaje_aceptacion_cambiode_comercializador_saliente)
        assertXmlEqual(xml, self.xml_c111.read())

    def test_create_pas12(self):
        # MensajeRechazoCambiodeComercializadorSaliente
        mensaje_rechazo_cambiode_comercializador_saliente = c1.MensajeRechazoCambiodeComercializadorSaliente()

        # Cabecera
        cabecera = get_header(step='12')

        # RechazoCambioComercializadorSaliente
        rechazo_cambio_comercializador_saliente = c1.RechazoCambioComercializadorSaliente()
        rechazo_cambio_comercializador_saliente_fields = {
            'fecha_rechazo': '2017-02-02',
        }
        rechazo_cambio_comercializador_saliente.feed(
            rechazo_cambio_comercializador_saliente_fields)

        mensaje_rechazo_cambiode_comercializador_saliente_fields = {
            'cabecera': cabecera,
            'rechazo_cambio_comercializador_saliente': rechazo_cambio_comercializador_saliente,
        }
        mensaje_rechazo_cambiode_comercializador_saliente.feed(
            mensaje_rechazo_cambiode_comercializador_saliente_fields)
        mensaje_rechazo_cambiode_comercializador_saliente.build_tree()
        xml = str(mensaje_rechazo_cambiode_comercializador_saliente)
        assertXmlEqual(xml, self.xml_c112.read())


class test_C2(unittest.TestCase):

    def setUp(self):
        self.xml_c201_completo = open(get_data("c201.xml"), "r")
        self.xml_c202_accept = open(get_data("c202_accept.xml"), "r")
        self.xml_c203 = open(get_data("c203.xml"), "r")

    def tearDown(self):
        self.xml_c201_completo.close()
        self.xml_c202_accept.close()
        self.xml_c203.close()

    def test_create_pas01(self):
        # MensajeCambiodeComercializadorConCambios
        mensage = c2.MensajeCambiodeComercializadorConCambios()

        # Cabecera
        cabecera = get_header(process='C2', step='01', date='2014-04-16T22:13:37', code='201412111009')

        # CambiodeComercializadorConCambios
        cambiode_comercializador_con_cambios = c2.CambiodeComercializadorConCambios()

        # DatosSolicitud
        datos_solicitud = c2.DatosSolicitud()
        datos_solicitud_fields = {
            'tipo_modificacion': 'S',
            'tipo_solicitud_administrativa': 'S',
            'cnae': '2222',
            'ind_activacion': 'L',
            'fecha_prevista_accion': '2016-06-06',
            'contratacion_incondicional_ps': 'S',
        }
        datos_solicitud.feed(datos_solicitud_fields)

        # Contrato
        contrato = c2.Contrato()

        # CondicionesContractuales
        condiciones_contractuales = c2.CondicionesContractuales()

        # PotenciasContratadas
        potencias_contratadas = c2.PotenciasContratadas()
        potencias_contratadas.feed({'p1': 1000, 'p2': 2000})

        condiciones_contractuales_fields = {
            'tarifa_atr': '003',
            'potencias_contratadas': potencias_contratadas,
            'modo_control_potencia': '1',
        }
        condiciones_contractuales.feed(condiciones_contractuales_fields)

        # Contacto
        contacto = get_contacto()

        contrato_fields = {
            'fecha_finalizacion': '2018-01-01',
            'tipo_autoconsumo': '00',
            'tipo_contrato_atr': '02',
            'condiciones_contractuales': condiciones_contractuales,
            'periodicidad_facturacion': '01',
            'consumo_anual_estimado': '5000',
            'contacto': contacto,
        }
        contrato.feed(contrato_fields)

        # Cliente
        cliente = get_cliente(dir=True, tipo_dir='F')

        # Medida
        medida = get_medida()

        # DocTecnica
        doc_tecnica = c2.DocTecnica()

        # DatosCie
        datos_cie = c2.DatosCie()

        # CIEPapel
        cie_papel = c2.CIEPapel()
        cie_papel_fields = {
            'codigo_cie': '1234567',
            'potencia_inst_bt': '3500',
            'potencia_no_interrumpible': '2000',
            'fecha_emision_cie': '2015-06-04',
            'fecha_caducidad_cie': '',
            'nif_instalador': '12345678Z',
            'tension_suministro_cie': '10',
            'tipo_suministro': 'VI',
        }
        cie_papel.feed(cie_papel_fields)

        datos_cie_fields = {
            'cie_papel': cie_papel,
            'validez_cie': 'ES',
        }
        datos_cie.feed(datos_cie_fields)

        # DatosAPM
        datos_apm = c2.DatosAPM()
        datos_apm_fields = {
            'codigo_apm': '1111111111',
            'potencia_inst_at': '5000',
            'fecha_emision_apm': '2015-06-04',
            'fecha_caducidad_apm': '2016-06-04',
            'tension_suministro_apm': '20',
            'codigo_instalador': '0550',
        }
        datos_apm.feed(datos_apm_fields)

        doc_tecnica_fields = {
            'datos_cie': datos_cie,
            'datos_apm': datos_apm,
        }
        doc_tecnica.feed(doc_tecnica_fields)

        cambiode_comercializador_con_cambios_fields = {
            'datos_solicitud': datos_solicitud,
            'contrato': contrato,
            'cliente': cliente,
            'medida': medida,
            'doc_tecnica': doc_tecnica,
            'comentarios': 'Comentario',
        }
        cambiode_comercializador_con_cambios.feed(
            cambiode_comercializador_con_cambios_fields)

        mensaje_fields = {
            'cabecera': cabecera,
            'cambiode_comercializador_con_cambios': cambiode_comercializador_con_cambios,
        }
        mensage.feed(mensaje_fields)
        mensage.build_tree()
        xml = str(mensage)
        assertXmlEqual(xml, self.xml_c201_completo.read())

    def test_create_pas02(self):
        # MensajeAceptacionCambiodeComercializadorConCambios
        mensaje_aceptacion_cambiode_comercializador_con_cambios = c2.MensajeAceptacionCambiodeComercializadorConCambios()

        # Cabecera
        cabecera = get_header(process='C2', step='02')

        # AceptacionCambiodeComercializadorConCambios
        aceptacion_cambiode_comercializador_con_cambios = c2.AceptacionCambiodeComercializadorConCambios()

        # DatosAceptacion
        datos_aceptacion = c2.DatosAceptacion()
        datos_aceptacion_fields = {
            'fecha_aceptacion': '2016-06-06',
            'potencia_actual': '5000',
            'actuacion_campo': 'S',
            'fecha_ultima_lectura_firme': '2016-06-01',
        }
        datos_aceptacion.feed(datos_aceptacion_fields)

        # Contrato
        contrato = c2.Contrato()

        # CondicionesContractuales
        condiciones_contractuales = c2.CondicionesContractuales()

        # PotenciasContratadas
        potencias_contratadas = c2.PotenciasContratadas()
        potencias_contratadas.feed({'p1': 1000, 'p2': 2000})

        condiciones_contractuales_fields = {
            'tarifa_atr': '003',
            'potencias_contratadas': potencias_contratadas,
            'modo_control_potencia': '1',
        }
        condiciones_contractuales.feed(condiciones_contractuales_fields)

        contrato_fields = {
            'tipo_contrato_atr': '02',
            'condiciones_contractuales': condiciones_contractuales,
            'tipo_activacion_prevista': 'C0',
            'fecha_activacion_prevista': '2016-07-06',
        }
        contrato.feed(contrato_fields)

        aceptacion_cambiode_comercializador_con_cambios_fields = {
            'datos_aceptacion': datos_aceptacion,
            'contrato': contrato,
        }
        aceptacion_cambiode_comercializador_con_cambios.feed(
            aceptacion_cambiode_comercializador_con_cambios_fields)

        mensaje_aceptacion_cambiode_comercializador_con_cambios_fields = {
            'cabecera': cabecera,
            'aceptacion_cambiode_comercializador_con_cambios': aceptacion_cambiode_comercializador_con_cambios,
        }
        mensaje_aceptacion_cambiode_comercializador_con_cambios.feed(
            mensaje_aceptacion_cambiode_comercializador_con_cambios_fields)
        mensaje_aceptacion_cambiode_comercializador_con_cambios.build_tree()
        xml = str(mensaje_aceptacion_cambiode_comercializador_con_cambios)
        assertXmlEqual(xml, self.xml_c202_accept.read())

    def test_create_pas03(self):
        # MensajeIncidenciasATRDistribuidor
        mensaje = c2.MensajeIncidenciasATRDistribuidor()

        # Cabecera
        cabecera = get_header(process='C2', step='03')

        # IncidenciasATRDistribuidor
        incidencias_atr_distribuidor = c2.IncidenciasATRDistribuidor()
        i1 = c2.Incidencia()
        incidencia_fields = {
            'secuencial': '1',
            'codigo_motivo': '01',
            'comentarios': 'Com 1',
        }
        i1.feed(incidencia_fields)
        i2 = c2.Incidencia()
        incidencia_fields = {
            'secuencial': '2',
            'codigo_motivo': '08',
            'comentarios': 'Com 2',
        }
        i2.feed(incidencia_fields)

        incidencias_atr_distribuidor_fields = {
            'fecha_incidencia': '2016-07-21',
            'fecha_prevista_accion': '2016-07-22',
            'incidencia_list': [i1, i2],
        }
        incidencias_atr_distribuidor.feed(incidencias_atr_distribuidor_fields)

        mensaje_incidencias_atr_distribuidor_fields = {
            'cabecera': cabecera,
            'incidencias_atr_distribuidor': incidencias_atr_distribuidor,
        }
        mensaje.feed(mensaje_incidencias_atr_distribuidor_fields)
        mensaje.build_tree()
        xml = str(mensaje)
        assertXmlEqual(xml, self.xml_c203.read())


class test_A3(unittest.TestCase):
    def setUp(self):
        self.xml_a301 = open(get_data("a301.xml"), "r")

    def tearDown(self):
        self.xml_a301.close()

    def test_create_pas01(self):
        # MensajeAlta
        mensaje_alta = a3.MensajeAlta()

        # Cabecera
        cabecera = get_header(process='A3', step='01', date='2014-04-16T22:13:37', code='201412111009')

        # Alta
        alta = a3.Alta()

        # DatosSolicitud
        datos_solicitud = a3.DatosSolicitud()
        datos_solicitud_fields = {
            'cnae': '2222',
            'ind_activacion': 'L',
            'fecha_prevista_accion': '2016-06-06',
        }
        datos_solicitud.feed(datos_solicitud_fields)


        # Contrato
        contrato = a3.Contrato()

        # CondicionesContractuales
        condiciones_contractuales = a3.CondicionesContractuales()

        # PotenciasContratadas
        potencias_contratadas = a3.PotenciasContratadas()
        potencias_contratadas.feed({'p1': 1000, 'p2': 2000})

        condiciones_contractuales_fields = {
            'tarifa_atr': '003',
            'potencias_contratadas': potencias_contratadas,
            'modo_control_potencia': '1'
        }
        condiciones_contractuales.feed(condiciones_contractuales_fields)

        # Contacto
        contacto = get_contacto(email=False)

        contrato_fields = {
            'fecha_finalizacion': '2018-01-01',
            'tipo_autoconsumo': '00',
            'tipo_contrato_atr': '02',
            'condiciones_contractuales': condiciones_contractuales,
            'consumo_anual_estimado': '5000',
            'contacto': contacto,
        }
        contrato.feed(contrato_fields)

        # Cliente
        cliente = get_cliente(dir=True, tipo_dir='F')

        # Medida
        medida = get_medida()

        # DocTecnica
        doc_tecnica = a3.DocTecnica()

        # DatosCie
        datos_cie = a3.DatosCie()

        # CIEElectronico
        cie_electronico = a3.CIEElectronico()
        cie_electronico_fields = {
            'codigo_cie': '1234567',
            'sello_electronico': '11111',
        }
        cie_electronico.feed(cie_electronico_fields)

        datos_cie_fields = {
            'cie_electronico': cie_electronico,
            'validez_cie': 'ES',
        }
        datos_cie.feed(datos_cie_fields)


        # DatosAPM
        datos_apm = a3.DatosAPM()
        datos_apm_fields = {
            'codigo_apm': '1111111111',
            'potencia_inst_at': '5000',
            'fecha_emision_apm': '2015-06-04',
            'fecha_caducidad_apm': '2016-06-04',
            'tension_suministro_apm': '20',
            'codigo_instalador': '0550',
        }
        datos_apm.feed(datos_apm_fields)

        doc_tecnica_fields = {
            'datos_cie': datos_cie,
            'datos_apm': datos_apm,
        }
        doc_tecnica.feed(doc_tecnica_fields)

        alta_fields = {
            'datos_solicitud': datos_solicitud,
            'contrato': contrato,
            'cliente': cliente,
            'medida': medida,
            'doc_tecnica': doc_tecnica,
            'comentarios': 'Comentario',
        }
        alta.feed(alta_fields)

        mensaje_alta_fields = {
            'cabecera': cabecera,
            'alta': alta,
        }
        mensaje_alta.feed(mensaje_alta_fields)
        mensaje_alta.build_tree()
        xml = str(mensaje_alta)
        assertXmlEqual(xml, self.xml_a301.read())


class test_M1(unittest.TestCase):
    def setUp(self):
        self.xml_m101 = open(get_data("m101.xml"), "r")

    def tearDown(self):
        self.xml_m101.close()

    def test_create_pas01(self):
        # MensajeModificacionDeATR
        mensaje_modificacion_de_atr = m1.MensajeModificacionDeATR()

        # Cabecera
        cabecera = get_header(process='M1', step='01', date='2014-04-16T22:13:37', code='201412111009')

        # ModificacionDeATR
        modificacion_de_atr = m1.ModificacionDeATR()

        # DatosSolicitud
        datos_solicitud = m1.DatosSolicitud()
        datos_solicitud_fields = {
            'tipo_modificacion': 'S',
            'tipo_solicitud_administrativa': 'S',
            'periodicidad_facturacion': '01',
            'ind_activacion': 'L',
            'fecha_prevista_accion': '2016-06-06',
            'cnae': '2222',
        }
        datos_solicitud.feed(datos_solicitud_fields)

        # Contrato
        contrato = m1.Contrato()

        # CondicionesContractuales
        condiciones_contractuales = m1.CondicionesContractuales()

        # PotenciasContratadas
        potencias_contratadas = a3.PotenciasContratadas()
        potencias_contratadas.feed({'p1': 1000, 'p2': 2000})

        condiciones_contractuales_fields = {
            'tarifa_atr': '003',
            'potencias_contratadas': potencias_contratadas,
            'modo_control_potencia': '1',
        }
        condiciones_contractuales.feed(condiciones_contractuales_fields)


        # Contacto
        contacto = get_contacto(email=False)

        contrato_fields = {
            'fecha_finalizacion': '2018-01-01',
            'tipo_autoconsumo': '00',
            'tipo_contrato_atr': '02',
            'condiciones_contractuales': condiciones_contractuales,
            'contacto': contacto,
        }
        contrato.feed(contrato_fields)

        # Cliente
        cliente = get_cliente(dir=False, tipo_dir='S')

        # Medida
        medida = m1.Medida()
        medida_fields = {
            'propiedad_equipo': 'C',
            'tipo_equipo_medida': 'L00',
        }
        medida.feed(medida_fields)

        modificacion_de_atr_fields = {
            'datos_solicitud': datos_solicitud,
            'contrato': contrato,
            'cliente': cliente,
            'medida': medida,
        }
        modificacion_de_atr.feed(modificacion_de_atr_fields)

        mensaje_modificacion_de_atr_fields = {
            'cabecera': cabecera,
            'modificacion_de_atr': modificacion_de_atr,
        }
        mensaje_modificacion_de_atr.feed(mensaje_modificacion_de_atr_fields)
        mensaje_modificacion_de_atr.build_tree()
        xml = str(mensaje_modificacion_de_atr)
        assertXmlEqual(xml, self.xml_m101.read())


class test_D1(unittest.TestCase):

    def setUp(self):
        self.xml_d101 = open(get_data("d101.xml"), "r")

    def tearDown(self):
        self.xml_d101.close()

    def test_create_pas01(self):
        # MensajeNotificacionCambiosATRDesdeDistribuidor
        mensaje = d1.MensajeNotificacionCambiosATRDesdeDistribuidor()

        # Cabecera
        cabecera = d1.Cabecera()
        cabecera_fields = {
            'codigo_ree_empresa_emisora': '1234',
            'codigo_ree_empresa_destino': '4321',
            'codigo_del_proceso': 'D1',
            'codigo_del_paso': '01',
            'codigo_de_solicitud': '201605219497',
            'secuencial_de_solicitud': '00',
            'fecha': '2016-06-08T04:24:09',
            'cups': 'ES0116000000011531LK0F',
        }
        cabecera.feed(cabecera_fields)

        # NotificacionCambiosATRDesdeDistribuidor
        notificacion = d1.NotificacionCambiosATRDesdeDistribuidor()
        notificacion_cambios_atr_desde_distribuidor_fields = {
            'motivo_cambio_atr_desde_distribuidora': '01',
            'fecha_prevista_aplicacion_cambio_atr': '2016-06-09',
            'periodicidad_facturacion': '01',
        }
        notificacion.feed(notificacion_cambios_atr_desde_distribuidor_fields)

        mensaje_notificacion_cambios_atr_desde_distribuidor_fields = {
            'cabecera': cabecera,
            'notificacion_cambios_atr_desde_distribuidor': notificacion,
        }
        mensaje.feed(mensaje_notificacion_cambios_atr_desde_distribuidor_fields)
        mensaje.build_tree()
        xml = str(mensaje)
        assertXmlEqual(xml, self.xml_d101.read())


class test_Q1(unittest.TestCase):

    def setUp(self):
        self.xml_q101 = open(get_data("q101.xml"), "r")

    def tearDown(self):
        self.xml_q101.close()

    def test_create_pas01(self):
        # MensajeSaldoLecturasFacturacion
        mensaje = q1.MensajeSaldoLecturasFacturacion()

        # Cabecera
        cabecera = get_header(process='Q1', step='01', date='2014-04-16T22:13:37', code='201412111009')

        # Medidas
        medidas = q1.Medidas()

        # ModeloAparato 1
        ma1 = q1.ModeloAparato()

        # Integrador 1
        i1 = q1.Integrador()

        # LecturaDesde
        lectura_desde = q1.LecturaDesde()
        lectura_desde_fields = {
            'fecha': '2014-04-18',
            'procedencia': '20',
            'lectura': '500',
        }
        lectura_desde.feed(lectura_desde_fields)

        # LecturaHasta
        lectura_hasta = q1.LecturaHasta()
        lectura_hasta_fields = {
            'fecha': '2014-05-18',
            'procedencia': '20',
            'lectura': '1500',
        }
        lectura_hasta.feed(lectura_hasta_fields)

        integrador_fields = {
            'magnitud': 'R2',
            'codigo_periodo': '20',
            'constante_multiplicadora': '1',
            'numero_ruedas_enteras': '10',
            'numero_ruedas_decimales': '20',
            'consumo_calculado': '5000',
            'lectura_desde': lectura_desde,
            'lectura_hasta': lectura_hasta,
        }
        i1.feed(integrador_fields)

        modelo_aparato_fields = {
            'tipo_aparato': 'CG',
            'marca_aparato': '135',
            'numero_serie': '012',
            'tipo_dhedm': '2',
            'integrador_list': [i1],
        }
        ma1.feed(modelo_aparato_fields)

        # ModeloAparato 2
        ma2 = q1.ModeloAparato()
        # Integrador 1
        i1 = q1.Integrador()

        # LecturaDesde
        lectura_desde = q1.LecturaDesde()
        lectura_desde_fields = {
            'fecha': '2014-04-18',
            'procedencia': '30',
            'lectura': '500',
        }
        lectura_desde.feed(lectura_desde_fields)

        # LecturaHasta
        lectura_hasta = q1.LecturaHasta()
        lectura_hasta_fields = {
            'fecha': '2014-05-18',
            'procedencia': '30',
            'lectura': '1500',
        }
        lectura_hasta.feed(lectura_hasta_fields)

        integrador_fields = {
            'magnitud': 'R3',
            'codigo_periodo': '30',
            'constante_multiplicadora': '1',
            'numero_ruedas_enteras': '10',
            'numero_ruedas_decimales': '20',
            'consumo_calculado': '5000',
            'lectura_desde': lectura_desde,
            'lectura_hasta': lectura_hasta,
        }
        i1.feed(integrador_fields)

        # Integrador 2
        i2 = q1.Integrador()

        # LecturaDesde
        lectura_desde = q1.LecturaDesde()
        lectura_desde_fields = {
            'fecha': '2014-04-18',
            'procedencia': '30',
            'lectura': '500',
        }
        lectura_desde.feed(lectura_desde_fields)

        # LecturaHasta
        lectura_hasta = q1.LecturaHasta()
        lectura_hasta_fields = {
            'fecha': '2014-05-18',
            'procedencia': '40',
            'lectura': '1500',
        }
        lectura_hasta.feed(lectura_hasta_fields)

        # Ajuste
        ajuste = q1.Ajuste()
        ajuste_fields = {
            'codigo_motivo_ajuste': '01',
            'ajuste_por_integrador': '1500',
            'comentarios': 'Comentario Ajuste',
        }
        ajuste.feed(ajuste_fields)

        # Anomalia
        anomalia = q1.Anomalia()
        anomalia_fields = {
            'tipo_anomalia': '05',
            'comentarios': 'Comentarios Anomalia',
        }
        anomalia.feed(anomalia_fields)

        integrador_fields = {
            'magnitud': 'R3',
            'codigo_periodo': '30',
            'constante_multiplicadora': '1',
            'numero_ruedas_enteras': '10',
            'numero_ruedas_decimales': '20',
            'consumo_calculado': '5000',
            'lectura_desde': lectura_desde,
            'lectura_hasta': lectura_hasta,
            'ajuste': ajuste,
            'anomalia': anomalia,
            'fecha_hora_maximetro': '2014-05-18T22:13:37',
        }
        i2.feed(integrador_fields)

        modelo_aparato_fields = {
            'tipo_aparato': 'CG',
            'marca_aparato': '136',
            'numero_serie': '012',
            'tipo_dhedm': '3',
            'integrador_list': [i1, i2],
        }
        ma2.feed(modelo_aparato_fields)

        medidas_fields = {
            'cod_pm': '1112223334445556667779',
            'modelo_aparato_list': [ma1, ma2],
        }
        medidas.feed(medidas_fields)

        mensaje_saldo_lecturas_facturacion_fields = {
            'cabecera': cabecera,
            'medidas': medidas,
        }
        mensaje.feed(mensaje_saldo_lecturas_facturacion_fields)
        mensaje.build_tree()
        xml = str(mensaje)
        assertXmlEqual(xml, self.xml_q101.read())


class test_W1(unittest.TestCase):

    def setUp(self):
        self.xml_w101 = open(get_data("w101.xml"), "r")
        self.xml_w102_accept = open(get_data("w102_accept.xml"), "r")
        self.xml_w102_reject = open(get_data("w102_reject.xml"), "r")

    def tearDown(self):
        self.xml_w101.close()
        self.xml_w102_accept.close()
        self.xml_w102_reject.close()

    def test_create_pas01(self):
        # MensajeSolicitudAportacionLectura
        mensaje_aportacion_lectura = w1.MensajeSolicitudAportacionLectura()

        # Cabecera
        cabecera = get_header(process='W1', step='01',  date='2014-04-16T22:13:37', code='201412111009')

        # DatosSolicitudAportacionLectura
        datos_solicitud = w1.DatosSolicitudAportacionLectura()
        datos_solicitud_aportacion_lectura_fields = {
            'fecha_lectura': '2015-02-18',
            'tipo_dhedm': '2',
        }
        datos_solicitud.feed(datos_solicitud_aportacion_lectura_fields)

        # LecturaAportada
        la1 = w1.LecturaAportada()
        lectura_aportada_fields = {
            'integrador': 'AE',
            'tipo_codigo_periodo_dh': '21',
            'lectura_propuesta': '0000001162.00',
        }
        la1.feed(lectura_aportada_fields)

        la2 = w1.LecturaAportada()
        lectura_aportada_fields = {
            'integrador': 'AE',
            'tipo_codigo_periodo_dh': '22',
            'lectura_propuesta': '0000003106.00',
        }
        la2.feed(lectura_aportada_fields)

        mensaje_aportacion_lectura_fields = {
            'cabecera': cabecera,
            'datos_solicitud_aportacion_lectura': datos_solicitud,
            'lectura_aportada_list': [la1, la2],
        }
        mensaje_aportacion_lectura.feed(mensaje_aportacion_lectura_fields)
        mensaje_aportacion_lectura.build_tree()
        xml = str(mensaje_aportacion_lectura)
        assertXmlEqual(xml, self.xml_w101.read())

    def test_create_pas02(self):
        # AceptacionAportacionLectura
        mensaje = w1.AceptacionAportacionLectura()

        # Cabecera
        cabecera = get_header(process='W1', step='02',
                              date='2014-04-16T22:13:37', code='201412111009')
        # DatosAceptacionLectura
        datos_aceptacion_lectura = w1.DatosAceptacionLectura()
        datos_aceptacion_lectura_fields = {
            'fecha_aceptacion': '2016-06-06',
        }
        datos_aceptacion_lectura.feed(datos_aceptacion_lectura_fields)

        aceptacion_aportacion_lectura_fields = {
            'cabecera': cabecera,
            'datos_aceptacion_lectura': datos_aceptacion_lectura,
        }
        mensaje.feed(aceptacion_aportacion_lectura_fields)
        mensaje.build_tree()
        xml = str(mensaje)
        assertXmlEqual(xml, self.xml_w102_accept.read())

    def test_create_pas02_rej(self):
        # MensajeRechazo
        mensaje_rechazo = w1.MensajeRechazo()

        # Cabecera
        cabecera = get_header(process='W1', step='02')

        # Rechazos
        rechazos = w1.Rechazos()

        # Rechazo
        r1 = w1.Rechazo()
        rechazo_fields = {
            'secuencial': '1',
            'codigo_motivo': '01',
            'comentarios': 'Motiu de rebuig 01: No existe Punto de Suministro asociado al CUPS',
        }
        r1.feed(rechazo_fields)

        # RegistrosDocumento
        registros_documento = w1.RegistrosDocumento()

        # RegistroDoc
        rd1 = w1.RegistroDoc()
        registro_doc_fields = {
            'tipo_doc_aportado': '08',
            'direccion_url': 'http://eneracme.com/docs/NIF11111111H.pdf',
        }
        rd1.feed(registro_doc_fields)

        registros_documento_fields = {
            'registro_doc_list': [rd1],
        }
        registros_documento.feed(registros_documento_fields)

        rechazos_fields = {
            'fecha_rechazo': '2016-07-20',
            'rechazo_list': [r1],
            'registros_documento': registros_documento,
        }
        rechazos.feed(rechazos_fields)

        mensaje_rechazo_fields = {
            'cabecera': cabecera,
            'rechazos': rechazos,
        }
        mensaje_rechazo.feed(mensaje_rechazo_fields)
        mensaje_rechazo.build_tree()
        xml = str(mensaje_rechazo)
        assertXmlEqual(xml, self.xml_w102_reject.read())


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

    def test_create_pas01(self):
        # MensajeBajaSuspension
        mensaje_baja_suspension = b1.MensajeBajaSuspension()

        # Cabecera
        cabecera = d1.Cabecera()
        cabecera_fields = {
            'codigo_ree_empresa_emisora': '1234',
            'codigo_ree_empresa_destino': '4321',
            'codigo_del_proceso': 'B1',
            'codigo_del_paso': '01',
            'codigo_de_solicitud': '201605219497',
            'secuencial_de_solicitud': '00',
            'fecha': '2016-06-08T04:24:09',
            'cups': 'ES0116000000011531LK0F',
        }
        cabecera.feed(cabecera_fields)

        # BajaSuspension
        baja_suspension = b1.BajaSuspension()

        # DatosSolicitud
        datos_solicitud = b1.DatosSolicitud()
        datos_solicitud_fields = {
            'ind_activacion': 'L',
            'motivo': '03',
        }
        datos_solicitud.feed(datos_solicitud_fields)

        # Cliente
        cliente = get_cliente()

        baja_suspension_fields = {
            'datos_solicitud': datos_solicitud,
            'cliente': cliente,
            'iban': '444555666',
        }
        baja_suspension.feed(baja_suspension_fields)

        mensaje_baja_suspension_fields = {
            'cabecera': cabecera,
            'baja_suspension': baja_suspension,
        }
        mensaje_baja_suspension.feed(mensaje_baja_suspension_fields)
        mensaje_baja_suspension.build_tree()
        xml = str(mensaje_baja_suspension)
        assertXmlEqual(xml, self.xml_b101.read())

    def test_create_pas02(self):
        # MensajeAceptacionBajaSuspension
        mensaje_aceptacion_baja_suspension = b1.MensajeAceptacionBajaSuspension()

        # Cabecera
        cabecera = get_header(process='B1', step='02')

        # AceptacionBajaSuspension
        aceptacion_baja_suspension = b1.AceptacionBajaSuspension()

        # DatosAceptacion
        datos_aceptacion = b1.DatosAceptacion()
        datos_aceptacion_fields = {
            'fecha_aceptacion': '2016-06-06',
            'actuacion_campo': 'S',
            'fecha_ultima_lectura_firme': '2016-06-01',
            'tipo_activacion_prevista': 'B1',
            'fecha_activacion_prevista': '2016-06-08',
        }
        datos_aceptacion.feed(datos_aceptacion_fields)

        aceptacion_baja_suspension_fields = {
            'datos_aceptacion': datos_aceptacion,
        }
        aceptacion_baja_suspension.feed(aceptacion_baja_suspension_fields)

        mensaje_aceptacion_baja_suspension_fields = {
            'cabecera': cabecera,
            'aceptacion_baja_suspension': aceptacion_baja_suspension,
        }
        mensaje_aceptacion_baja_suspension.feed(mensaje_aceptacion_baja_suspension_fields)
        mensaje_aceptacion_baja_suspension.build_tree()
        xml = str(mensaje_aceptacion_baja_suspension)
        assertXmlEqual(xml, self.xml_b102_accept.read())

    def test_create_pas04(self):
        # MensajeAceptacionAnulacionBaja
        mensaje = b1.MensajeAceptacionAnulacionBaja()

        # Cabecera
        cabecera = get_header(process='B1', step='04')

        # AceptacionAnulacion
        aceptacion_anulacion = b1.AceptacionAnulacion()
        aceptacion_anulacion_fields = {
            'fecha_aceptacion': '2017-02-02',
            'hora_aceptacion': '20:05:10',
        }
        aceptacion_anulacion.feed(aceptacion_anulacion_fields)

        mensaje_aceptacion_anulacion_baja_fields = {
            'cabecera': cabecera,
            'aceptacion_anulacion': aceptacion_anulacion,
        }
        mensaje.feed(mensaje_aceptacion_anulacion_baja_fields)
        mensaje.build_tree()
        xml = str(mensaje)
        assertXmlEqual(xml, self.xml_b104_accept.read())

    def test_create_pas05(self):
        # MensajeActivacionBajaSuspension
        mensaje = b1.MensajeActivacionBajaSuspension()

        # Cabecera
        cabecera = get_header(process='B1', step='05')

        # ActivacionBaja
        activacion_baja = b1.ActivacionBaja()

        # DatosActivacionBaja
        datos_activacion_baja = b1.DatosActivacionBaja()
        datos_activacion_baja_fields = {
            'fecha_activacion': '2016-08-21',
        }
        datos_activacion_baja.feed(datos_activacion_baja_fields)

        # Contrato
        contrato = b1.Contrato()

        # IdContrato
        id_contrato = b1.IdContrato()
        id_contrato.feed({'cod_contrato': '00001'})
        contrato.feed({'id_contrato': id_contrato})

        # PuntosDeMedida
        puntos_de_medida = c1.PuntosDeMedida()
        # PuntoDeMedida
        punto_de_medida = c1.PuntoDeMedida()
        # Aparatos
        aparatos = c1.Aparatos()
        # Aparato
        aparato = c1.Aparato()

        # ModeloAparato
        modelo_aparato = c1.ModeloAparato()
        modelo_aparato_fields = {
            'tipo_aparato': 'CG',
            'marca_aparato': '132',
            'modelo_marca': '011',
        }
        modelo_aparato.feed(modelo_aparato_fields)

        # DatosAparato
        datos_aparato = c1.DatosAparato()
        datos_aparato_fields = {
            'periodo_fabricacion': '2005',
            'numero_serie': '0000539522',
            'funcion_aparato': 'M',
            'num_integradores': '18',
            'constante_energia': '1.000',
            'constante_maximetro': '1.000',
            'ruedas_enteras': '08',
            'ruedas_decimales': '02',
        }
        datos_aparato.feed(datos_aparato_fields)

        # Medidas
        medidas = c1.Medidas()
        # Medida 1
        medida1 = c1.Medida()
        medida_fields = {
            'tipo_dhedm': '6',
            'periodo': '65',
            'magnitud_medida': 'PM',
            'procedencia': '30',
            'ultima_lectura_firme': '6.00',
            'fecha_lectura_firme': '2003-01-02',
            'anomalia': '01',
            'comentarios': 'Comentario sobre anomalia',
        }
        medida1.feed(medida_fields)
        # Medida 2
        medida2 = c1.Medida()
        medida_fields = {
            'tipo_dhedm': '6',
            'periodo': '66',
            'magnitud_medida': 'PM',
            'procedencia': '30',
            'ultima_lectura_firme': '6.00',
            'fecha_lectura_firme': '2003-01-03',
        }
        medida2.feed(medida_fields)
        medidas_fields = {
            'medida_list': [medida1, medida2],
        }
        medidas.feed(medidas_fields)

        aparato_fields = {
            'modelo_aparato': modelo_aparato,
            'tipo_movimiento': 'CX',
            'tipo_equipo_medida': 'L03',
            'tipo_propiedad_aparato': '1',
            'propietario': 'Desc. Propietario',
            'tipo_dhedm': '6',
            'modo_medida_potencia': '1',
            'lectura_directa': 'N',
            'cod_precinto': '02',
            'datos_aparato': datos_aparato,
            'medidas': medidas,
        }
        aparato.feed(aparato_fields)
        aparatos_fields = {
            'aparato_list': [aparato],
        }
        aparatos.feed(aparatos_fields)

        punto_de_medida_fields = {
            'cod_pm': 'ES1234000000000001JN0F',
            'tipo_movimiento': 'A',
            'tipo_pm': '03',
            'cod_pm_principal': 'ES1234000000000002JN0F',
            'modo_lectura': '1',
            'funcion': 'P',
            'direccion_enlace': '39522',
            'direccion_punto_medida': '000000001',
            'num_linea': '12',
            'telefono_telemedida': '987654321',
            'estado_telefono': '1',
            'clave_acceso': '0000000007',
            'tension_pm': '0',
            'fecha_vigor': '2003-01-01',
            'fecha_alta': '2003-01-01',
            'fecha_baja': '2003-02-01',
            'aparatos': aparatos,
            'comentarios': 'Comentarios Varios',
        }
        punto_de_medida.feed(punto_de_medida_fields)

        puntos_de_medida_fields = {
            'punto_de_medida_list': [punto_de_medida],
        }
        puntos_de_medida.feed(puntos_de_medida_fields)

        activacion_baja_fields = {
            'datos_activacion_baja': datos_activacion_baja,
            'contrato': contrato,
            'puntos_de_medida': puntos_de_medida,
        }
        activacion_baja.feed(activacion_baja_fields)

        mensaje_activacion_baja_suspension_fields = {
            'cabecera': cabecera,
            'activacion_baja': activacion_baja,
        }
        mensaje.feed(mensaje_activacion_baja_suspension_fields)
        mensaje.build_tree()
        xml = str(mensaje)
        assertXmlEqual(xml, self.xml_b105.read())


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

    def test_create_pas01(self):
        # MensajeReclamacionPeticion
        mensaje_reclamacion_peticion = r1.MensajeReclamacionPeticion()

        # CabeceraReclamacion
        cabecera_reclamacion = r1.CabeceraReclamacion()
        cabecera_reclamacion_fields = {
            'codigo_ree_empresa_emisora': '0321',
            'codigo_ree_empresa_destino': '0123',
            'codigo_del_proceso': 'R1',
            'codigo_del_paso': '01',
            'codigo_de_solicitud': '201650008314',
            'secuencial_de_solicitud': '01',
            'fecha': '2016-01-22T10:09:41',
            'cups': 'ES1234000000000001JN0F',
        }
        cabecera_reclamacion.feed(cabecera_reclamacion_fields)

        # SolicitudReclamacion
        solicitud_reclamacion = r1.SolicitudReclamacion()

        # DatosSolicitud
        datos_solicitud = r1.DatosSolicitud()
        datos_solicitud_fields = {
            'tipo': '02',
            'subtipo': '003',
            'referencia_origen': '01',
            'fecha_limite': '2016-02-22',
            'prioritario': 'S',
        }
        datos_solicitud.feed(datos_solicitud_fields)

        # VariablesDetalleReclamacion
        variables_detalle_reclamacion = r1.VariablesDetalleReclamacion()

        # VariableDetalleReclamacion
        vdr1 = r1.VariableDetalleReclamacion()

        # LecturasAportadas
        lecturas_aportadas = r1.LecturasAportadas()

        # LecturaAportada
        la1 = r1.LecturaAportada()
        lectura_aportada_fields = {
            'integrador': 'AE',
            'codigo_periodo_dh': '21',
            'lectura_propuesta': '0000001162.00',
        }
        la1.feed(lectura_aportada_fields)

        la2 = r1.LecturaAportada()
        lectura_aportada_fields = {
            'integrador': 'AE',
            'codigo_periodo_dh': '22',
            'lectura_propuesta': '0000003106.00',
        }
        la2.feed(lectura_aportada_fields)

        lecturas_aportadas_fields = {
            'lectura_aportada_list': [la1, la2],
        }
        lecturas_aportadas.feed(lecturas_aportadas_fields)

        # Contacto
        contacto = r1.Contacto()

        # Telefono
        telefono = r1.Telefono()
        telefono_fields = {
            'prefijo_pais': '34',
            'numero': '55512345',
        }
        telefono.feed(telefono_fields)

        contacto_fields = {
            'persona_de_contacto': 'Perico Palotes Largos',
            'telefono': telefono,
            'correo_electronico': 'perico@acme.com',
        }
        contacto.feed(contacto_fields)

        # UbicacionIncidencia
        ubicacion_incidencia = r1.UbicacionIncidencia()
        ubicacion_incidencia_fields = {
            'des_ubicacion_incidencia': 'Destino',
            'provincia': '17',
            'municipio': '17079',
            'poblacion': '17079',
            'cod_postal': '17001',
        }
        ubicacion_incidencia.feed(ubicacion_incidencia_fields)

        variable_detalle_reclamacion_fields = {
            'num_expediente_acometida': '11111',
            'num_expediente_fraude': '22222',
            'fecha_incidente': '2016-02-10',
            'num_factura_atr': '243615',
            'tipo_concepto_facturado': '01',
            'fecha_lectura': '2016-01-20',
            'tipo_dhedm': '1',
            'lecturas_aportadas': lecturas_aportadas,
            'codigo_incidencia': '01',
            'codigo_solicitud': '33333',
            'parametro_contratacion': '01',
            'concepto_disconformidad': '100',
            'tipo_de_atencion_incorrecta': '05',
            'iban': '4444222211113333',
            'contacto': contacto,
            'codigo_solicitud_reclamacion': '11111',
            'fecha_desde': '2017-02-05',
            'fecha_hasta': '2017-04-05',
            'importe_reclamado': '5000',
            'ubicacion_incidencia': ubicacion_incidencia,
        }
        vdr1.feed(variable_detalle_reclamacion_fields)

        # VariableDetalleReclamacion 2
        vdr2 = r1.VariableDetalleReclamacion()
        variable_detalle_reclamacion_fields = {
            'num_expediente_acometida': '22222',
        }
        vdr2.feed(variable_detalle_reclamacion_fields)

        variables_detalle_reclamacion_fields = {
            'variable_detalle_reclamacion_list': [vdr1, vdr2],
        }
        variables_detalle_reclamacion.feed(variables_detalle_reclamacion_fields)

        # Cliente
        cliente = get_cliente(dir=True, tipo_dir='F')

        # Reclamante
        reclamante = r1.Reclamante()

        # IdReclamante
        id_reclamante = r1.IdReclamante()
        id_reclamante_fields = {
            'tipo_identificador': 'NI',
            'identificador': 'B36385870',
            'tipo_persona': 'J',
        }
        id_reclamante.feed(id_reclamante_fields)

        # Nombre
        nombre = r1.Nombre()
        nombre_fields = {
            'nombre_de_pila': '',
            'primer_apellido': '',
            'segundo_apellido': '',
            'razon_social': u'ACC Y COMP DE COCINA MILLAN Y MUÑOZ',
        }
        nombre.feed(nombre_fields)

        # Telefono
        telefono = r1.Telefono()
        telefono_fields = {
            'prefijo_pais': '34',
            'numero': '666777888',
        }
        telefono.feed(telefono_fields)

        reclamante_fields = {
            'id_reclamante': id_reclamante,
            'nombre': nombre,
            'telefono': telefono,
            'correo_electronico': 'email@host',
        }
        reclamante.feed(reclamante_fields)

        solicitud_reclamacion_fields = {
            'datos_solicitud': datos_solicitud,
            'variables_detalle_reclamacion': variables_detalle_reclamacion,
            'cliente': cliente,
            'tipo_reclamante': '01',
            'reclamante': reclamante,
            'comentarios': 'no calcula sus consumos desea revisio y facturas',
        }
        solicitud_reclamacion.feed(solicitud_reclamacion_fields)

        mensaje_reclamacion_peticion_fields = {
            'cabecera_reclamacion': cabecera_reclamacion,
            'solicitud_reclamacion': solicitud_reclamacion,
        }
        mensaje_reclamacion_peticion.feed(mensaje_reclamacion_peticion_fields)
        mensaje_reclamacion_peticion.build_tree()
        xml = str(mensaje_reclamacion_peticion)
        assertXmlEqual(xml, self.xml_r101.read())

    def test_create_pas02(self):
        # MensajeAceptacionReclamacion
        mensaje_aceptacion_reclamacion = r1.MensajeAceptacionReclamacion()

        # CabeceraReclamacion
        cabecera_reclamacion = r1.CabeceraReclamacion()
        cabecera_reclamacion_fields = {
            'codigo_del_proceso': 'R1',
            'codigo_del_paso': '02',
            'codigo_de_solicitud': '201607211259',
            'secuencial_de_solicitud': '01',
            'cups': 'ES1234000000000001JN0F',
            'codigo_ree_empresa_emisora': '1234',
            'codigo_ree_empresa_destino': '4321',
            'fecha': '2016-07-21T12:59:47',
        }
        cabecera_reclamacion.feed(cabecera_reclamacion_fields)

        # AceptacionReclamacion
        aceptacion_reclamacion = r1.AceptacionReclamacion()

        # DatosAceptacion
        datos_aceptacion = r1.DatosAceptacion()
        datos_aceptacion_fields = {
            'fecha_aceptacion': '2016-06-06',
            'codigo_reclamacion_distribuidora': '1234',
        }
        datos_aceptacion.feed(datos_aceptacion_fields)

        aceptacion_reclamacion_fields = {
            'datos_aceptacion': datos_aceptacion,
        }
        aceptacion_reclamacion.feed(aceptacion_reclamacion_fields)

        mensaje_aceptacion_reclamacion_fields = {
            'cabecera_reclamacion': cabecera_reclamacion,
            'aceptacion_reclamacion': aceptacion_reclamacion,
        }
        mensaje_aceptacion_reclamacion.feed(
            mensaje_aceptacion_reclamacion_fields)
        mensaje_aceptacion_reclamacion.build_tree()
        xml = str(mensaje_aceptacion_reclamacion)
        assertXmlEqual(xml, self.xml_r102_accept.read())

    def test_create_pas03(self):
        # MensajePeticionInformacionAdicionalReclamacion
        mensaje_peticion_informacion_adicional_reclamacion = r1.MensajePeticionInformacionAdicionalReclamacion()

        # CabeceraReclamacion
        cabecera_reclamacion = r1.CabeceraReclamacion()
        cabecera_reclamacion_fields = {
            'codigo_ree_empresa_emisora': '1234',
            'codigo_ree_empresa_destino': '4321',
            'codigo_del_proceso': 'R1',
            'codigo_del_paso': '03',
            'codigo_de_solicitud': '201412111009',
            'secuencial_de_solicitud': '01',
            'fecha': '2016-06-10T08:50:43',
            'cups': 'ES1234000000000001JN0F',
        }
        cabecera_reclamacion.feed(cabecera_reclamacion_fields)

        # InformacionAdicional
        informacion_adicional = r1.InformacionAdicional()

        # DatosInformacion
        datos_informacion = r1.DatosInformacion()
        datos_informacion_fields = {
            'num_expediente_acometida': '1111122222',
            'tipo_comunicacion': '01',
            'codigo_reclamacion_distribuidora': '12345678',
        }
        datos_informacion.feed(datos_informacion_fields)

        # InformacionIntermedia
        informacion_intermedia = r1.InformacionIntermedia()

        informacion_intermedia_fields = {
            'desc_informacion_intermedia': 'Descripcion de la informacion intermedia aportada.',
        }
        informacion_intermedia.feed(informacion_intermedia_fields)

        # Retipificacion
        retipificacion = r1.Retipificacion()
        retipificacion_fields = {
            'tipo': '02',
            'subtipo': '003',
            'desc_retipificacion': 'descripcio de la retipificacio.',
        }
        retipificacion.feed(retipificacion_fields)

        # SolicitudesInformacionAdicional
        solicitudes_informacion_adicional = r1.SolicitudesInformacionAdicional()

        # SolicitudInformacionAdicional 1
        sia1 = r1.SolicitudInformacionAdicional()
        solicitud_informacion_adicional_fields = {
            'tipo_informacion_adicional': '01',
            'desc_peticion_informacion': 'Descripcion de la peticion.',
            'fecha_limite_envio': '2016-07-10',
        }
        sia1.feed(solicitud_informacion_adicional_fields)

        # SolicitudInformacionAdicional 2
        sia2 = r1.SolicitudInformacionAdicional()
        solicitud_informacion_adicional_fields = {
            'tipo_informacion_adicional': '02',
            'desc_peticion_informacion': 'Descripcion de la peticion.',
            'fecha_limite_envio': '2016-07-10',
        }
        sia2.feed(solicitud_informacion_adicional_fields)

        # SolicitudInformacionAdicionalparaRetipificacion
        siar = r1.SolicitudInformacionAdicionalparaRetipificacion()
        solicitud_informacion_adicionalpara_retipificacion_fields = {
            'tipo': '03',
            'subtipo': '003',
            'fecha_limite_envio': '2016-08-10',
        }
        siar.feed(solicitud_informacion_adicionalpara_retipificacion_fields)

        solicitudes_informacion_adicional_fields = {
            'solicitud_informacion_adicional_list': [sia1, sia2],
            'solicitud_informacion_adicionalpara_retipificacion': siar
        }
        solicitudes_informacion_adicional.feed(solicitudes_informacion_adicional_fields)

        informacion_adicional_fields = {
            'datos_informacion': datos_informacion,
            'informacion_intermedia': informacion_intermedia,
            'retipificacion': retipificacion,
            'solicitudes_informacion_adicional': solicitudes_informacion_adicional,
            'comentarios': 'R1 03.',
        }
        informacion_adicional.feed(informacion_adicional_fields)

        mensaje_peticion_informacion_adicional_reclamacion_fields = {
            'cabecera_reclamacion': cabecera_reclamacion,
            'informacion_adicional': informacion_adicional,
        }
        mensaje_peticion_informacion_adicional_reclamacion.feed(mensaje_peticion_informacion_adicional_reclamacion_fields)
        mensaje_peticion_informacion_adicional_reclamacion.build_tree()
        xml = str(mensaje_peticion_informacion_adicional_reclamacion)
        assertXmlEqual(xml, self.xml_r103.read())

    def test_create_pas03_intervenciones(self):
        # MensajePeticionInformacionAdicionalReclamacion
        mensaje = r1.MensajePeticionInformacionAdicionalReclamacion()

        # CabeceraReclamacion
        cabecera_reclamacion = r1.CabeceraReclamacion()
        cabecera_reclamacion_fields = {
            'codigo_ree_empresa_emisora': '1234',
            'codigo_ree_empresa_destino': '4321',
            'codigo_del_proceso': 'R1',
            'codigo_del_paso': '03',
            'codigo_de_solicitud': '201412111009',
            'secuencial_de_solicitud': '01',
            'fecha': '2016-06-10T08:50:43',
            'cups': 'ES1234000000000001JN0F',
        }
        cabecera_reclamacion.feed(cabecera_reclamacion_fields)

        # InformacionAdicional
        informacion_adicional = r1.InformacionAdicional()

        # DatosInformacion
        datos_informacion = r1.DatosInformacion()
        datos_informacion_fields = {
            'num_expediente_acometida': '1111122222',
            'tipo_comunicacion': '01',
            'codigo_reclamacion_distribuidora': '12345678',
        }
        datos_informacion.feed(datos_informacion_fields)

        # InformacionIntermedia
        informacion_intermedia = r1.InformacionIntermedia()

        # Intervenciones
        intervenciones = r1.Intervenciones()

        # Intervencion
        i1 = r1.Intervencion()
        intervencion_fields = {
            'tipo_intervencion': '01',
            'fecha': '2016-06-10',
            'hora_desde': '08:00:00',
            'hora_hasta': '09:00:00',
            'numero_visita': '10',
            'resultado': '001',
            'detalle_resultado': 'Descripcion de los resultados obtenidos.',
        }
        i1.feed(intervencion_fields)

        i2 = r1.Intervencion()
        intervencion_fields = {
            'tipo_intervencion': '02',
            'fecha': '2016-06-10',
            'hora_desde': '08:00:00',
            'hora_hasta': '09:00:00',
            'numero_visita': '10',
            'resultado': '001',
            'detalle_resultado': 'Descripcion de los resultados obtenidos.',
        }
        i2.feed(intervencion_fields)

        intervenciones_fields = {
            'intervencion_list': [i1, i2],
        }
        intervenciones.feed(intervenciones_fields)

        informacion_intermedia_fields = {
            'intervenciones': intervenciones,
        }
        informacion_intermedia.feed(informacion_intermedia_fields)

        informacion_adicional_fields = {
            'datos_informacion': datos_informacion,
            'informacion_intermedia': informacion_intermedia,
            'comentarios': "R1 03 with 'Intervenciones'.",
        }
        informacion_adicional.feed(informacion_adicional_fields)

        mensaje_peticion_informacion_adicional_reclamacion_fields = {
            'cabecera_reclamacion': cabecera_reclamacion,
            'informacion_adicional': informacion_adicional,
        }
        mensaje.feed(mensaje_peticion_informacion_adicional_reclamacion_fields)
        mensaje.build_tree()
        xml = str(mensaje)
        assertXmlEqual(xml, self.xml_r103_intervenciones.read())

    def test_create_pas04(self):
        # MensajeEnvioInformacionReclamacion
        mensaje = r1.MensajeEnvioInformacionReclamacion()

        # CabeceraReclamacion
        cabecera_reclamacion = r1.CabeceraReclamacion()
        cabecera_reclamacion_fields = {
            'codigo_ree_empresa_emisora': '1234',
            'codigo_ree_empresa_destino': '4321',
            'codigo_del_proceso': 'R1',
            'codigo_del_paso': '04',
            'codigo_de_solicitud': '201650008314',
            'secuencial_de_solicitud': '01',
            'fecha': '2016-01-22T10:09:41',
            'cups': 'ES1234000000000001JN0F',
        }
        cabecera_reclamacion.feed(cabecera_reclamacion_fields)

        # EnvioInformacionReclamacion
        envio_informacion_reclamacion = r1.EnvioInformacionReclamacion()

        # DatosEnvioInformacion
        datos_envio_informacion = r1.DatosEnvioInformacion()
        datos_envio_informacion_fields = {
            'num_expediente_acometida': '0123456789ABCD',
            'fecha_informacion': '2016-01-20',
        }
        datos_envio_informacion.feed(datos_envio_informacion_fields)

        # VariablesAportacionInformacion
        variables_aportacion_informacion = r1.VariablesAportacionInformacion()

        # VariableAportacionInformacion
        vai1 = r1.VariableAportacionInformacion()
        variable_aportacion_informacion_fields = {
            'tipo_informacion': '01',
            'desc_peticion_informacion': 'Informacio per fer testos.',
            'variable': '01',
            'valor': '125',
        }
        vai1.feed(variable_aportacion_informacion_fields)

        vai2 = r1.VariableAportacionInformacion()
        variable_aportacion_informacion_fields = {
            'tipo_informacion': '02',
        }
        vai2.feed(variable_aportacion_informacion_fields)

        variables_aportacion_informacion_fields = {
            'variable_aportacion_informacion_list': [vai1, vai2],
        }
        variables_aportacion_informacion.feed(variables_aportacion_informacion_fields)

        # VariablesAportacionInformacionparaRetipificacion
        variables_retipificacion = r1.VariablesAportacionInformacionparaRetipificacion()

        vair1 = r1.VariableAportacionInformacionparaRetipificacion()

        # LecturasAportadas
        lecturas_aportadas = r1.LecturasAportadas()

        # LecturaAportada
        la1 = r1.LecturaAportada()
        lectura_aportada_fields = {
            'integrador': 'AE',
            'codigo_periodo_dh': '21',
            'lectura_propuesta': '0000001162.00',
        }
        la1.feed(lectura_aportada_fields)

        la2 = r1.LecturaAportada()
        lectura_aportada_fields = {
            'integrador': 'AE',
            'codigo_periodo_dh': '22',
            'lectura_propuesta': '0000003106.00',
        }
        la2.feed(lectura_aportada_fields)

        lecturas_aportadas_fields = {
            'lectura_aportada_list': [la1, la2],
        }
        lecturas_aportadas.feed(lecturas_aportadas_fields)

        # Contacto
        contacto = r1.Contacto()

        # Telefono
        telefono = r1.Telefono()
        telefono_fields = {
            'prefijo_pais': '34',
            'numero': '55512345',
        }
        telefono.feed(telefono_fields)

        contacto_fields = {
            'persona_de_contacto': 'Perico Palotes Largos',
            'telefono': telefono,
            'correo_electronico': 'perico@acme.com',
        }
        contacto.feed(contacto_fields)

        # UbicacionIncidencia
        ubicacion_incidencia = r1.UbicacionIncidencia()
        ubicacion_incidencia_fields = {
            'des_ubicacion_incidencia': 'Destino',
            'provincia': '17',
            'municipio': '17079',
            'poblacion': '17079',
            'cod_postal': '17001',
        }
        ubicacion_incidencia.feed(ubicacion_incidencia_fields)

        vair_fields = {
            'num_expediente_acometida': '11111',
            'num_expediente_fraude': '22222',
            'fecha_incidente': '2016-02-10',
            'num_factura_atr': '243615',
            'tipo_concepto_facturado': '01',
            'fecha_lectura': '2016-01-20',
            'tipo_dhedm': '1',
            'lecturas_aportadas': lecturas_aportadas,
            'codigo_incidencia': '01',
            'codigo_solicitud': '33333',
            'parametro_contratacion': '01',
            'concepto_disconformidad': '100',
            'tipo_de_atencion_incorrecta': '05',
            'iban': '4444222211113333',
            'contacto': contacto,
            'codigo_solicitud_reclamacion': '11111',
            'fecha_desde': '2017-02-05',
            'fecha_hasta': '2017-04-05',
            'importe_reclamado': '5000',
            'ubicacion_incidencia': ubicacion_incidencia,
        }
        vair1.feed(vair_fields)

        variables_retipificacion_fields = {
            'variable_aportacion_informacionpara_retipificacion_list': [vair1],
        }
        variables_retipificacion.feed(variables_retipificacion_fields)

        # Cliente
        cliente = get_cliente(dir=True, tipo_dir='F')

        # RegistrosDocumento
        registros_documento = r1.RegistrosDocumento()
        # RegistroDoc
        rd1 = w1.RegistroDoc()
        registro_doc_fields = {
            'tipo_doc_aportado': '01',
            'direccion_url': 'http://eneracme.com/docs/CIE0100001.pdf',
        }
        rd1.feed(registro_doc_fields)
        rd2 = w1.RegistroDoc()
        registro_doc_fields = {
            'tipo_doc_aportado': '06',
            'direccion_url': 'http://eneracme.com/docs/INV201509161234.pdf',
        }
        rd2.feed(registro_doc_fields)
        rd3 = w1.RegistroDoc()
        registro_doc_fields = {
            'tipo_doc_aportado': '08',
            'direccion_url': 'http://eneracme.com/docs/NIF11111111H.pdf',
        }
        rd3.feed(registro_doc_fields)

        registros_documento_fields = {
            'registro_doc_list': [rd1, rd2, rd3],
        }
        registros_documento.feed(registros_documento_fields)

        envio_informacion_reclamacion_fields = {
            'datos_envio_informacion': datos_envio_informacion,
            'variables_aportacion_informacion': variables_aportacion_informacion,
            'variables_aportacion_informacionpara_retipificacion': variables_retipificacion,
            'cliente': cliente,
            'comentarios': 'R104 test with VariablesAportacionInformacion.',
            'registros_documento': registros_documento,
        }
        envio_informacion_reclamacion.feed(envio_informacion_reclamacion_fields)

        mensaje_envio_informacion_reclamacion_fields = {
            'cabecera_reclamacion': cabecera_reclamacion,
            'envio_informacion_reclamacion': envio_informacion_reclamacion,
        }
        mensaje.feed(mensaje_envio_informacion_reclamacion_fields)
        mensaje.build_tree()
        xml = str(mensaje)
        assertXmlEqual(xml, self.xml_r104.read())


    def test_create_pas05(self):
        # MensajeCierreReclamacion
        mensaje_cierre_reclamacion = r1.MensajeCierreReclamacion()

        # CabeceraReclamacion
        cabecera_reclamacion = r1.CabeceraReclamacion()
        cabecera_reclamacion_fields = {
            'codigo_ree_empresa_emisora': '1234',
            'codigo_ree_empresa_destino': '4321',
            'codigo_del_proceso': 'R1',
            'codigo_del_paso': '05',
            'codigo_de_solicitud': '201604111738',
            'secuencial_de_solicitud': '01',
            'fecha': '2014-04-16T22:13:37',
            'cups': 'ES1234000000000001JN0F',
        }
        cabecera_reclamacion.feed(cabecera_reclamacion_fields)

        # CierreReclamacion
        cierre_reclamacion = r1.CierreReclamacion()

        # DatosCierre
        datos_cierre = r1.DatosCierre()
        datos_cierre_fields = {
            'num_expediente_acometida': '11111',
            'fecha': '2016-04-12',
            'hora': '16:02:25',
            'tipo': '03',
            'subtipo': '013',
            'codigo_reclamacion_distribuidora': '3291970',
            'resultado_reclamacion': '02',
            'detalle_resultado': '0010101',
            'observaciones': 'Observaciones generales',
            'indemnizacion_abonada': '0.0',
            'num_expediente_anomalia_fraude': '22222',
            'fecha_movimiento': '2016-04-12',
        }
        datos_cierre.feed(datos_cierre_fields)

        cierre_reclamacion_fields = {
            'datos_cierre': datos_cierre,
            'cod_contrato': '383922379',
            'comentarios': 'Comentarios generales',
        }
        cierre_reclamacion.feed(cierre_reclamacion_fields)

        mensaje_cierre_reclamacion_fields = {
            'cabecera_reclamacion': cabecera_reclamacion,
            'cierre_reclamacion': cierre_reclamacion,
        }
        mensaje_cierre_reclamacion.feed(mensaje_cierre_reclamacion_fields)
        mensaje_cierre_reclamacion.build_tree()
        xml = str(mensaje_cierre_reclamacion)
        assertXmlEqual(xml, self.xml_r105.read())


class test_F1(unittest.TestCase):

    def setUp(self):
        self.xml_f101_factura_atr = open(get_data("f101_factura_atr.xml"), "r")
        self.xml_f101_factura_otros = open(
            get_data("f101_factura_otros.xml"), "r"
        )

        direccion_suministro = f1.DireccionSuministro()

        direccion_suministro.feed(
            {
                'pais': u'España',
                'provincia': '17',
                'municipio': '17079',
                'poblacion': None,
                'tipo_via': None,
                'cod_postal': '17003',
                'calle': 'Nom carrer',
                'numero_finca': '3',
                'duplicador_finca': None,
                'escalera': 1,
                'piso': 1,
                'puerta': 1,
                'tipo_aclarador_finca': None,
                'alcarador_finca': None,
            }
        )

        datos_generales_factura_atr = f1.DatosGeneralesFacturaATR()

        cliente = f1.Cliente()

        cliente.feed(
            {
                'tipo_identificador': 'NI',
                'identificador': '70876712G',
                'tipo_persona': 'F',
            }
        )

        datos_generales_factura_for_atr = f1.DatosGeneralesFactura()

        datos_generales_factura_for_atr.feed(
            {
                'codigo_fiscal_factura': 'F0001',
                'tipo_factura': 'N',
                'motivo_facturacion': '01',
                'codigo_factura_rectificada_anulada': None,
                'expediente': None,
                'fecha_factura': '2017-05-01',
                'identificador_emisora': 'B11254455',
                'comentarios': '. ',
                'importe_total_factura': 100,
                'saldo_factura': 100,
                'tipo_moneda': '02',
            }
        )

        datos_generales_factura_for_otros = f1.DatosGeneralesFactura()

        datos_generales_factura_for_otros.feed(
            {
                'codigo_fiscal_factura': 'F0001',
                'tipo_factura': 'N',
                'motivo_facturacion': '01',
                'codigo_factura_rectificada_anulada': None,
                'expediente': None,
                'fecha_factura': '2017-05-01',
                'identificador_emisora': 'B11254455',
                'comentarios': '. ',
                'importe_total_factura': 20.63,
                'saldo_factura': 20.63,
                'tipo_moneda': '02',
            }
        )

        periodo = f1.Periodo()

        periodo.feed(
            {
                'fecha_desde_factura': '2017-03-31',
                'fecha_hasta_factura': '2017-04-30',
                'numero_dias': 30,
            }
        )

        atr_data = f1.DatosFacturaATR()

        atr_data.feed(
            {
                'fecha_boe': '2016-01-01',
                'tarifa_atr_fact': '001',
                'modo_control_potencia': 1,
                'marca_medida_con_perdidas': 'N',
                'vas_trafo': None,
                'porcentaje_perdidas': None,
                'indicativo_curva_carga': '02',
                'periodo_cch': None,
                'periodo': periodo,
            }
        )

        datos_generales_factura_atr.feed(
            {
                'direccion_suministro': direccion_suministro,
                'cliente': cliente,
                'cod_contrato': '111111',
                'datos_generales_factura': datos_generales_factura_for_atr,
                'datos_factura_atr': atr_data,
            }
        )

        periodo_pot = f1.PeriodoPotencia()

        periodo_pot.feed(
            {
                'potencia_contratada': 1000,
                'potencia_max_demandada': 1000,
                'potencia_a_facturar': 1000,
                'precio_potencia': 0.05,
            }
        )

        periodos_potencia = [periodo_pot]

        term_potencia = f1.TerminoPotencia()

        term_potencia.feed(
            {
                'fecha_desde': '2017-03-31',
                'fecha_hasta': '2017-04-30',
                'periodo': periodos_potencia,
            }
        )

        terminos_potencia = [term_potencia]

        power = f1.Potencia()

        power.feed(
            {
                'termino_potencia': terminos_potencia,
                'penalizacion_no_icp': 'N',
                'importe_total_termino_potencia': 50,
            }
        )

        periodo_act = f1.PeriodoEnergiaActiva()

        periodo_act.feed(
            {
                'valor_energia_activa': 300,
                'precio_energia': 0.044027,
            }
        )

        periodos_activa = [periodo_act]

        term_activa = f1.TerminoEnergiaActiva()

        term_activa.feed(
            {
                'fecha_desde': '2017-03-31',
                'fecha_hasta': '2017-04-30',
                'periodos': periodos_activa,
            }
        )

        terminos_activa = [term_activa]

        energia_activa = f1.EnergiaActiva()

        energia_activa.feed(
            {
                'termino_energia_activa': terminos_activa,
                'importe_total_energia_activa': 13.21,
            }
        )

        impuesto_electrico = f1.ImpuestoElectrico()

        impuesto_electrico.feed(
            {
                'base_imponible': 0,
                'porcentaje': 0,
                'importe': 0,
            }
        )

        iva_atr = f1.IVA()

        iva_atr.feed(
            {
                'base_imponible': 63.21,
                'porcentaje': 21,
                'importe': 13.27,
            }
        )

        lectura_desde = f1.LecturaDesde()

        lectura_desde.feed(
            {
                'fecha': '2017-03-31',
                'procedencia': '30',
                'lectura': 100,
            }
        )

        lectura_hasta = f1.LecturaHasta()

        lectura_hasta.feed(
            {
                'fecha': '2017-04-30',
                'procedencia': '30',
                'lectura': 400,
            }
        )

        ivas_atr = [iva_atr]

        integrador = f1.Integrador()

        integrador.feed(
            {
                'magnitud': 'AE',
                'codigo_periodo': '10',
                'constante_multiplicadora': 1.0,
                'numero_ruedas_enteras': 5,
                'numero_ruedas_decimales': 0,
                'consumo_calculado': 300,
                'lectura_desde': lectura_desde,
                'lectura_hasta': lectura_hasta,
                'ajuste': None,
                'anomalia': None,
                'fecha_hora_maximetro': None,
            }
        )

        integradores = [integrador]

        aparato = f1.ModeloAparato()

        aparato.feed(
            {
                'tipo_aparato': 'CC',
                'marca_aparato': 199,
                'numero_serie': 'C99999',
                'tipo_dhedm': 1,
                'integrador': integradores
            }
        )

        aparatos = [aparato]

        medidas = f1.Medidas()

        medidas.feed(
            {
                'cod_pm': 'ES1234000000000001JN0F',
                'modelo_aparato': aparatos
            }
        )

        self.factura_atr = f1.FacturaATR()

        self.factura_atr.feed(
            {
                'datos_generales_factura_atr': datos_generales_factura_atr,
                'potencia': power,
                'exceso_potencia': None,
                'energia_activa': energia_activa,
                'energia_reactiva': None,
                'impuesto_electrico': impuesto_electrico,
                'alquileres': None,
                'importe_intereses': None,
                'concepto_repercutible': None,
                'iva': ivas_atr,
                'iva_reducido': None,
                'medidas': medidas,
            }
        )

        datos_gen_otras_facturas = f1.DatosGeneralesOtrasFacturas()

        datos_gen_otras_facturas.feed(
            {
                'direccion_suministro': direccion_suministro,
                'cliente': cliente,
                'cod_contrato': '111111',
                'datos_generales_factura': datos_generales_factura_for_otros,
                'fecha_boe': '2016-01-01',
            }
        )

        concepto_repercutible_enganche = f1.ConceptoRepercutible()

        concepto_repercutible_enganche.feed(
            {
                'concepto_repercutible': '04',
                'tipo_impositivo_concepto_repercutible': 1,
                'fecha_operacion': '2016-09-01',
                'unidades_concepto_repercutible': 1.0,
                'precio_unidad_concepto_repercutible': 9.04476,
                'importe_total_concepto_repercutible': 9.04,
                'comentarios': 'Cuota de enganche / Act. en equipos BT',
            }
        )

        concepto_repercutible_verificacion = f1.ConceptoRepercutible()

        concepto_repercutible_verificacion.feed(
            {
                'concepto_repercutible': '05',
                'tipo_impositivo_concepto_repercutible': 1,
                'fecha_operacion': '2016-09-01',
                'unidades_concepto_repercutible': 1.0,
                'precio_unidad_concepto_repercutible': 8.011716,
                'importe_total_concepto_repercutible': 8.01,
                'comentarios': 'Cuota de verificación BT',
            }
        )

        conceptos_repercutibles = [
            concepto_repercutible_enganche, concepto_repercutible_verificacion
        ]

        iva_otros = f1.IVA()

        iva_otros.feed(
            {
                'base_imponible': 17.05,
                'porcentaje': 21,
                'importe': 3.58,
            }
        )

        ivas_otros = [iva_otros]

        self.factura_otros = f1.OtrasFacturas()
        self.factura_otros.feed(
            {
                'datos_generales_otras_facturas': datos_gen_otras_facturas,
                'concepto_repercutible': conceptos_repercutibles,
                'iva': ivas_otros,
                'iva_reducido': None,
            }
        )

    def tearDown(self):
        self.xml_f101_factura_atr.close()

    def with_factura_atr(self):
        cabecera = get_header(process='F1', step='01')

        facturacion = f1.Facturacion()

        facturas = f1.Facturas()

        registo_fin = f1.RegistroFin()
        registo_fin.feed(
            {
                'importe_total': 76.48,
                'saldo_total_facturacion': 76.48,
                'total_recibos': 1,
                'tipo_moneda': '02',
                'fecha_valor': '2017-05-01',
                'fecha_limite_pago': '2017-06-01',
                'iban': 'ES7712341234161234567890',
                'id_remesa': '0',
            }
        )

        facturas.feed(
            {
                'factura_atr': self.factura_atr,
                'registro_fin': registo_fin
            }
        )

        facturacion.feed(
            {
                'cabecera': cabecera,
                'facturas': facturas,
            }
        )

        return facturacion

    def with_factura_otros(self):
        cabecera = get_header(process='F1', step='01')

        facturacion = f1.Facturacion()

        facturas = f1.Facturas()

        registo_fin = f1.RegistroFin()
        registo_fin.feed(
            {
                'importe_total': 20.63,
                'saldo_total_facturacion': 20.63,
                'total_recibos': 1,
                'tipo_moneda': '02',
                'fecha_valor': '2016-11-01',
                'fecha_limite_pago': '2016-11-21',
                'iban': 'ES7712341234161234567890',
                'id_remesa': '0',
            }
        )

        facturas.feed(
            {
                'otras_facturas': self.factura_otros,
                'registro_fin': registo_fin
            }
        )

        facturacion.feed(
            {
                'cabecera': cabecera,
                'facturas': facturas,
            }
        )

        return facturacion

    def test_create_pas01_atr_invoice(self):
        mensaje = self.with_factura_atr()

        mensaje.build_tree()

        xml = str(mensaje)
        assertXmlEqual(xml, self.xml_f101_factura_atr.read())

    def test_create_pas01_other_invoice(self):
        mensaje = self.with_factura_otros()

        mensaje.build_tree()

        xml = str(mensaje)
        assertXmlEqual(xml, self.xml_f101_factura_otros.read())
