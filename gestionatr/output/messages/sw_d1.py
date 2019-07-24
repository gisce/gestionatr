# -*- coding: utf-8 -*-
from libcomxml.core import XmlModel, XmlField
from gestionatr.output.messages.base import Cabecera


# Paso 01
class MensajeNotificacionCambiosATRDesdeDistribuidor(XmlModel):

    _sort_order = ('mensaje', 'cabecera', 'notificacion_cambios_atr_desde_distribuidor')

    def __init__(self):
        self.mensaje = XmlField('MensajeNotificacionCambiosATRDesdeDistribuidor',
                                attributes={'xmlns': 'http://localhost/elegibilidad'})
        self.cabecera = Cabecera()
        self.notificacion_cambios_atr_desde_distribuidor = NotificacionCambiosATRDesdeDistribuidor()
        super(MensajeNotificacionCambiosATRDesdeDistribuidor, self) \
            .__init__('MensajeNotificacionCambiosATRDesdeDistribuidor', 'mensaje')


class NotificacionCambiosATRDesdeDistribuidor(XmlModel):

    _sort_order = ('notificacion_cambios_atr_desde_distribuidor', 'motivo_cambio_atr_desde_distribuidora',
                   'fecha_prevista_aplicacion_cambio_atr', 'periodicidad_facturacion', 'info_registro_autocons')

    def __init__(self):
        self.notificacion_cambios_atr_desde_distribuidor = XmlField('NotificacionCambiosATRDesdeDistribuidor')
        self.motivo_cambio_atr_desde_distribuidora = XmlField('MotivoCambioATRDesdeDistribuidora')
        self.fecha_prevista_aplicacion_cambio_atr = XmlField('FechaPrevistaAplicacionCambioATR')
        self.periodicidad_facturacion = XmlField('PeriodicidadFacturacion')
        self.info_registro_autocons = InfoRegistroAutocons()
        super(NotificacionCambiosATRDesdeDistribuidor, self).__init__('NotificacionCambiosATRDesdeDistribuidor',
                                                                      'notificacion_cambios_atr_desde_distribuidor')


class InfoRegistroAutocons(XmlModel):

    _sort_order = ('info_registro_autocons', 'autoconsumo', 'datos_suministro', 'datos_inst_gen',
                   'comentarios')

    def __init__(self):
        self.info_registro_autocons = XmlField('InfoRegistroAutocons')
        self.autoconsumo = Autoconsumo()
        self.datos_suministro = DatosSuministro()
        self.datos_inst_gen = DatosInstGen()
        self.comentarios = XmlField('Comentarios')
        super(InfoRegistroAutocons, self).__init__('InfoRegistroAutocons', 'info_registro_autocons')


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


# Paso 02 accept
class MensajeAceptacionNotificacionCambiosATRDesdeDistribuidor(XmlModel):

    _sort_order = ('mensaje', 'cabecera', 'aceptacion_notificacion_cambios_atr_desde_distribuidor')

    def __init__(self):
        self.mensaje = XmlField('MensajeAceptacionNotificacionCambiosATRDesdeDistribuidor',
                                attributes={'xmlns': 'http://localhost/elegibilidad'})
        self.cabecera = Cabecera()
        self.aceptacion_notificacion_cambios_atr_desde_distribuidor = AceptacionNotificacionCambiosATRDesdeDistribuidor()
        super(MensajeAceptacionNotificacionCambiosATRDesdeDistribuidor, self)\
            .__init__('MensajeAceptacionNotificacionCambiosATRDesdeDistribuidor', 'mensaje')


class AceptacionNotificacionCambiosATRDesdeDistribuidor(XmlModel):

    _sort_order = ('aceptacion_notificacion_cambios_atr_desde_distribuidor', 'datos_aceptacion')

    def __init__(self):
        self.aceptacion_notificacion_cambios_atr_desde_distribuidor = XmlField('AceptacionNotificacionCambiosATRDesdeDistribuidor')
        self.datos_aceptacion = DatosAceptacion()
        super(AceptacionNotificacionCambiosATRDesdeDistribuidor, self)\
            .__init__('AceptacionNotificacionCambiosATRDesdeDistribuidor',
                      'aceptacion_notificacion_cambios_atr_desde_distribuidor')


class DatosAceptacion(XmlModel):

    _sort_order = ('datos_aceptacion', 'fecha_aceptacion')

    def __init__(self):
        self.datos_aceptacion = XmlField('DatosAceptacion')
        self.fecha_aceptacion = XmlField('FechaAceptacion')
        super(DatosAceptacion, self).__init__('DatosAceptacion', 'datos_aceptacion')


# Paso 02 (Rechazo)
class MensajeRechazo(XmlModel):

    _sort_order = ('mensaje_rechazo', 'cabecera', 'rechazos')

    def __init__(self):
        self.mensaje_rechazo = XmlField('MensajeRechazoD1',
                                        attributes={'xmlns': 'http://localhost/elegibilidad'})
        self.cabecera = Cabecera()
        self.rechazos = Rechazos()
        super(MensajeRechazo, self).__init__('MensajeRechazo', 'mensaje_rechazo')


class Rechazos(XmlModel):

    _sort_order = ('rechazos', 'fecha_rechazo', 'rechazo', 'registros_documento')

    def __init__(self):
        self.rechazos = XmlField('Rechazos')
        self.fecha_rechazo = XmlField('FechaRechazo')
        self.rechazo = Rechazo()
        self.registros_documento = RegistrosDocumento()
        super(Rechazos, self).__init__('Rechazos', 'rechazos')


class Rechazo(XmlModel):

    _sort_order = ('rechazo', 'secuencial', 'codigo_motivo', 'comentarios')

    def __init__(self):
        self.rechazo = XmlField('Rechazo')
        self.secuencial = XmlField('Secuencial')
        self.codigo_motivo = XmlField('CodigoMotivo')
        self.comentarios = XmlField('Comentarios')
        super(Rechazo, self).__init__('Rechazo', 'rechazo')


class RegistrosDocumento(XmlModel):

    _sort_order = ('registros_documento', 'registro_doc')

    def __init__(self):
        self.registros_documento = XmlField('RegistrosDocumento')
        self.registro_doc = RegistroDoc()
        super(RegistrosDocumento, self).__init__('RegistrosDocumento', 'registros_documento')


class RegistroDoc(XmlModel):

    _sort_order = ('registro_doc', 'tipo_doc_aportado', 'direccion_url')

    def __init__(self):
        self.registro_doc = XmlField('RegistroDoc')
        self.tipo_doc_aportado = XmlField('TipoDocAportado')
        self.direccion_url = XmlField('DireccionUrl')
        super(RegistroDoc, self).__init__('RegistroDoc', 'registro_doc')
