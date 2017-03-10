#!/usr/bin/env python
# -*- coding: utf-8 -*-
from . import unittest
from .utils import get_data, assertXmlEqual, get_header, get_cliente, get_contacto
from gestionatr.output.messages import sw_c1 as c1
from gestionatr.output.messages import sw_c2 as c2


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
        }
        aparato.feed(aparato_fields)
        aparatos_fields = {
            'aparato_list': [aparato],
        }
        aparatos.feed(aparatos_fields)

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
            'medidas': medidas,
            'comentarios': 'Comentarios Varios',
        }
        punto_de_medida.feed(punto_de_medida_fields)

        puntos_de_medida = c1.PuntosDeMedida()
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
        cliente = get_cliente(dir=True)

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
