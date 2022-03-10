# -*- coding: utf-8 -*-
from lxml import objectify, etree
from gestionatr import utils

XSD_DATA = {'F1': {'01': 'Facturacion.xsd'},
            'Q1': {'01': 'SaldoLecturasFacturacion.xsd'},
            'A1': {'01': 'A101.xsd',
                   '02': 'A102e.xsd'},
            'A3': {'01': 'Alta.xsd',
                   '02': ('AceptacionAlta.xsd',
                          'Rechazo.xsd'),
                   '03': 'IncidenciasATRDistribuidor.xsd',
                   '04': 'Rechazo.xsd',
                   '05': 'ActivacionAlta.xsd',
                   '06': 'AnulacionSolicitud.xsd',
                   '07': ('AceptacionAnulacion.xsd',
                          'Rechazo.xsd'),
                   '13': 'ContestacionIncidencia.xsd'
                   },
            'B1': {'01': 'BajaSuspension.xsd',
                   '02': ('AceptacionBajaSuspension.xsd',
                          'Rechazo.xsd'),
                   '03': 'AnulacionSolicitud.xsd',
                   '04': ('AceptacionAnulacionBaja.xsd',
                          'Rechazo.xsd'),
                   '05': 'ActivacionBajaSuspension.xsd',
                   '06': 'IncidenciasATRDistribuidor.xsd',
                   '07': 'Rechazo.xsd',
                   '16': 'ContestacionIncidencia.xsd'},
            'B2': {'05': 'ActivacionBaja.xsd'},
            'C1': {'01': 'CambiodeComercializadorSinCambios.xsd',
                   '02': ('AceptacionCambiodeComercializadorSinCambios.xsd',
                          'Rechazo.xsd'),
                   '04': 'Rechazo.xsd',
                   '05': 'ActivacionCambiodeComercializadorSinCambios.xsd',
                   '06': 'ActivacionComercializadorSaliente.xsd',
                   '08': 'AnulacionSolicitud.xsd',
                   '09': ('AceptacionAnulacion.xsd',
                          'Rechazo.xsd'),
                   '10': 'AceptacionAnulacion.xsd',
                   '11': 'AceptacionCambiodeComercializadorSaliente.xsd',
                   '12': 'RechazoCambiodeComercializadorSaliente.xsd'},
            'C2': {'01': 'CambiodeComercializadorConCambios.xsd',
                   '02': ('AceptacionCambiodeComercializadorConCambios.xsd',
                          'Rechazo.xsd'),
                   '03': 'IncidenciasATRDistribuidor.xsd',
                   '04': 'Rechazo.xsd',
                   '05': 'ActivacionCambiodeComercializadorConCambios.xsd',
                   '06': 'ActivacionComercializadorSaliente.xsd',
                   '08': 'AnulacionSolicitud.xsd',
                   '09': ('AceptacionAnulacion.xsd',
                          'Rechazo.xsd'),
                   '10': 'AceptacionAnulacion.xsd',
                   '11': 'AceptacionCambiodeComercializadorSaliente.xsd',
                   '12': 'RechazoCambiodeComercializadorSaliente.xsd',
                   '13': 'ContestacionIncidencia.xsd'
                   },
            'D1': {'01': 'NotificacionCambiosATRDesdeDistribuidor.xsd',
                   '02': ('AceptacionNotificacionCambiosATRDesdeDistribuidor.xsd', 'RechazoD1.xsd'),
                   },
            'E1': {'01': 'SolicitudDesistimiento.xsd',
                   '02': ('AceptacionDesistimiento.xsd', 'Rechazo.xsd'),
                   '03': 'IncidenciasATRDistribuidor.xsd',
                   '04': 'Rechazo.xsd',
                   '05': 'ActivacionDesistimiento.xsd',
                   '06': 'NotificacionActivacionPorDesistimiento.xsd',
                   '08': 'AnulacionSolicitud.xsd',
                   '09': ('AceptacionAnulacion.xsd',
                          'Rechazo.xsd'),
                   '10': 'AceptacionAnulacion.xsd',
                   '11': 'AceptacionDesistimiento.xsd',
                   '12': 'RechazoDesistimiento.xsd',
                   '13': 'ContestacionIncidencia.xsd'
                   },
            'M1': {'01': 'ModificacionDeATR.xsd',
                   '02': ('AceptacionModificacionDeATR.xsd',
                          'Rechazo.xsd'),
                   '03': 'IncidenciasATRDistribuidor.xsd',
                   '04': 'Rechazo.xsd',
                   '05': 'ActivacionModificacionDeATR.xsd',
                   '06': 'AnulacionSolicitud.xsd',
                   '07': ('AceptacionAnulacion.xsd',
                          'Rechazo.xsd'),
                   '13': 'ContestacionIncidencia.xsd',
                   },
            'P0': {'01': 'SolicitudInformacionAlRegistroDePS.xsd',
                   '02': ('EnvioInformacionPS.xsd',
                          'RechazoPeticion.xsd'),
                   },
            'R1': {'01': 'ReclamacionPeticion.xsd',
                   '02': ('AceptacionReclamacion.xsd',
                          'RechazoReclamacion.xsd'),
                   '03': 'PeticionInformacionAdicionalReclamacion.xsd',
                   '04': 'EnvioInformacionReclamacion.xsd',
                   '05': 'CierreReclamacion.xsd',
                   '08': 'AnulacionSolicitudReclamacion.xsd',
                   '09': ('AceptacionAnulacionReclamacion.xsd', 'RechazoReclamacion.xsd'),
                   },
            'T1': {
                '01': 'SolicitudTraspasoCOR.xsd',
                '02': ('AceptacionTraspasoCOR.xsd',
                       'RechazoTraspasoCOR.xsd'),
                '05': 'ActivacionTraspasoCOR.xsd',
                '06': 'ActivacionTraspasoCORSaliente.xsd',
                '10': 'AceptacionAnulacion.xsd',
            },
            'W1': {'01': 'SolicitudAportacionLectura.xsd',
                   '02': ('AceptacionAportacionLectura.xsd',
                          'Rechazo.xsd'),
                   },
            }

MAIN_MESSAGE_XSD = {
    'SaldoLecturasFacturacion': 'Medidas',
    'Alta': 'Alta',
    'AceptacionAlta': 'AceptacionAlta',
    'Rechazo': 'Rechazos',
    'IncidenciasATRDistribuidor': 'IncidenciasATRDistribuidor',
    'ActivacionAlta': 'ActivacionAlta',
    'AnulacionSolicitud': '',
    'AceptacionAnulacion': 'AceptacionAnulacion',
    'BajaSuspension': 'BajaSuspension',
    'AceptacionBajaSuspension': 'AceptacionBajaSuspension',
    'AceptacionAnulacionBaja': 'AceptacionAnulacion',
    'ActivacionBajaSuspension': 'ActivacionBaja',
    'ActivacionBajaUnidireccional': 'ActivacionBaja',
    'CambiodeComercializadorSinCambios': 'CambiodeComercializadorSinCambios',
    'AceptacionCambiodeComercializadorSinCambios': 'AceptacionCambiodeComercializadorSinCambios',
    'ActivacionCambiodeComercializadorSinCambios': 'ActivacionCambiodeComercializadorSinCambios',
    'ActivacionComercializadorSaliente': 'NotificacionComercializadorSaliente',
    'AceptacionCambiodeComercializadorSaliente': 'AceptacionCambioComercializadorSaliente',
    'RechazoCambiodeComercializadorSaliente': 'RechazoCambioComercializadorSaliente',
    'NotificacionCambiosATRDesdeDistribuidor': 'NotificacionCambiosATRDesdeDistribuidor',
    'AceptacionD1': 'AceptacionNotificacionCambiosATRDesdeDistribuidor',
    'RechazoD1': 'Rechazos',
    'A101': 'A101',
    'A102e': 'A102',
    'SolicitudInformacionAlRegistroDePS': 'ValidacionCliente',
    'SolicitudDesistimiento': 'SolicitudDesistimiento',
    'AceptacionDesistimiento': 'AceptacionDesistimiento',
    'RechazoDesistimiento': 'RechazoDesistimiento',
    'ActivacionDesistimiento': 'ActivacionDesistimiento',
    'NotificacionActivacionDesistimiento': 'NotificacionActivacionDesistimiento',
    'ContestacionIncidencia': 'ContestacionIncidencia',
    'SolicitudTraspasoCOR': 'SolicitudTraspasoCOR',
    'AceptacionTraspasoCOR': 'AceptacionTraspasoCOR',
    'RechazoTraspasoCOR': 'Rechazos',
    'ActivacionTraspasoCOR': 'ActivacionTraspasoCOR',
    'ActivacionTraspasoCORSaliente': 'NotificacionComercializadorSalienteT1',
    'EnvioInformacionPS': 'EnvioInformacionPS',
    'RechazoPeticion': 'RechazosPeticion',
    'ModificacionDeATR': 'ModificacionDeATR',
    'AceptacionModificacionDeATR': 'AceptacionModificacionDeATR',
    'ActivacionModificacionDeATR': 'ActivacionModificaciones',
    'ReclamacionPeticion': 'SolicitudReclamacion',
    'AceptacionReclamacion': 'AceptacionReclamacion',
    'RechazoReclamacion': 'Rechazos',
    'PeticionInformacionAdicionalReclamacion': 'InformacionAdicional',
    'EnvioInformacionReclamacion': 'EnvioInformacionReclamacion',
    'CierreReclamacion': 'CierreReclamacion',
    'AceptacionAnulacionReclamacion': 'AceptacionAnulacion',
    'MensajeSolicitudAportacionLectura': ['DatosSolicitudAportacionLectura', 'LecturaAportada'],
    'AceptacionAportacionLectura': 'DatosAceptacionLectura',
    'Facturacion': ['Facturas',  'OtrosDatosFactura'],
}


class MessageBase(object):
    """Classe base"""
    def __init__(self, xml, force_tipus=None):
        """Construir mensaje base."""
        self.obj = None
        self.error = None
        if isinstance(xml, file):
            self.check_fpos(xml)
            xml = xml.read()
        self.xml_orig = xml
        try:
            root = etree.fromstring(xml)
        except etree.XMLSyntaxError:
            raise except_f1('Error', u'Fichero XML erróneo')
        uxml = etree.tostring(root).decode('iso-8859-1')
        self.str_xml = uxml
        self.tipus = ''
        self.head = ''
        self._header = ''
        self.pas = ''
        self.f_xsd = ''
        self.set_head()
        self.set_tipus()
        if force_tipus and self.tipus != force_tipus:
            msg = u'El XML no se corresponde con el tipo {0}'.format(force_tipus)
            raise except_f1('Error', msg)
        self.set_xsd()

    @staticmethod
    def check_fpos(f_obj):
        """Setejar la posició actual dels fixers"""
        if isinstance(f_obj, file) and f_obj.tell() != 0:
            f_obj.seek(0)

    def set_tipus(self):
        """Set type of message. To implement in child classes"""
        raise NotImplementedError('This method is not implemented!')

    def set_xsd(self):
        """Set xsd. To implement in child classes"""
        raise NotImplementedError('This method is not implemented!')

    def set_head(self):
        """Set header of message. To implement in child classes"""
        raise NotImplementedError('This method is not implemented!')

    @property
    def valid(self):
        if self.obj is None:
            return None
        else:
            return not bool(self.error)

    def get_tipus_xml(self):
        """Obtenir el tipus de missatge"""
        return self.tipus

    def get_xml(self):
        """Obtenir el fitxer"""
        return self.xml_orig

    def parse_xml(self):
        """Import xml content. To implement in child classes"""
        raise NotImplementedError('This method is not implemented!')


class Message(MessageBase):
    """Clase base intercambio información comer-distri"""

    def set_head(self):
        obj = objectify.fromstring(self.str_xml)
        try:
            self.head = obj.Cabecera
        except Exception:
            self.head = obj.CabeceraReclamacion

    def set_tipus(self):
        """Definir tipo del mensaje"""
        try:
            self.tipus = self.head.CodigoDelProceso.text
            self.pas = self.head.CodigoDePaso.text
        except:
            msg = u'No se puede identificar el código de proceso ' \
                  u'o código de paso'
            raise except_f1('Error', msg)

    def set_xsd(self):
        """Definir fichero xsd"""
        if self.tipus not in XSD_DATA:
            msg = u"Código de proceso '{0}' no soportado".format(self.tipus)
            raise except_f1('Error', msg)
        if self.pas not in XSD_DATA[self.tipus]:
            msg = u"Código de paso '{0}' no soportado".format(self.pas)
            raise except_f1('Error', msg)
        try:
            if isinstance(XSD_DATA[self.tipus][self.pas], tuple):
                trobat = False
                root = objectify.fromstring(self.str_xml)
                for fitxer in XSD_DATA[self.tipus][self.pas]:
                    if 'MensajeRechazoP0' in root.tag:
                        fitxer = "RechazoPeticion.xsd"
                        trobat = True
                        break
                    if fitxer.split(".xsd")[0] in root.tag:
                        trobat = True
                        break
                if not trobat:
                    msg = u"Tipo de fichero '{0}' no soportado".format(root.tag)
                    raise except_f1('Error', msg)
            else:
                fitxer = XSD_DATA[self.tipus][self.pas]
            try:
                self._header = MAIN_MESSAGE_XSD[fitxer.split(".xsd")[0]]
            except:
                self._header = fitxer.split(".xsd")[0]
            if not isinstance(self._header, (list, tuple)):
                if "<"+self._header+">" not in self.str_xml:
                    aux = self._header.replace("s", "S")
                    if "<" + aux + ">" in self.str_xml:
                        self._header = aux

            xsd = utils.get_data(fitxer)
            self.f_xsd = open(xsd, 'r')
        except except_f1, e:
            raise e
        except:
            msg = u"Fichero '{0}' corrupto".format(
                utils.get_data(XSD_DATA[self.tipus])
            )
            raise except_f1('Error', msg)

    def get_pas_xml(self):
        """Obtener paso del missatge"""
        return self.pas

    def parse_xml(self, validate=True):
        """Importar contenido del xml"""
        self.check_fpos(self.f_xsd)
        schema = etree.XMLSchema(file=self.f_xsd)
        parser = objectify.makeparser(schema=schema)
        try:
            self.obj = objectify.fromstring(self.str_xml, parser)
        except Exception as e:
            self.error = e.message
            if validate:
                raise except_f1('Error', u'Documento inválido: {0}'.format(e))
            else:
                parser = objectify.makeparser(schema=None)
                self.obj = objectify.fromstring(self.str_xml, parser)

    # Funcions relacionades amb la capçalera del XML
    @property
    def get_codi_emisor(self):
        ref = self.head.CodigoREEEmpresaEmisora.text
        if not ref:
            raise except_f1('Error', u'Documento sin emisor')
        return ref

    @property
    def get_codi_destinatari(self):
        ref = self.head.CodigoREEEmpresaDestino.text
        if not ref:
            raise except_f1('Error', u'Documento sin destinatario')
        return ref

    @property
    def get_codi_ccaa_emissora(self):
        ref = self.head.CodigoEmpresaEmisora.text
        if not ref:
            raise except_f1('Error', u'Documento sin emisor')
        return ref

    @property
    def get_codi_ccaa_desti(self):
        ref = self.head.CodigoEmpresaDestino.text
        if not ref:
            raise except_f1('Error', u'Documento sin destinatario')
        return ref

    @property
    def cups(self):
        if self.tipus == 'R1':
            if utils.get_rec_attr(self, "head.CUPS", False):
                return utils.get_rec_attr(self, "head.CUPS", "").text.strip()
            else:
                return False

        ref = self.head.CUPS.text.strip()
        if not ref:
            raise except_f1('Error', u'Documento sin código')
        return ref

    @property
    def codi_sollicitud(self):
        ref = self.head.CodigoDeSolicitud.text
        if not ref:
            raise except_f1('Error', u'Documento sin código de solicitud')
        return ref

    @property
    def seq_sollicitud(self):
        ref = self.head.SecuencialDeSolicitud.text
        if not ref:
            raise except_f1('Error', u'Documento sin código de secuencial de '
                                     u'solicitud')
        return ref

    @property
    def data_sollicitud(self):
        ref = self.head.FechaSolicitud.text
        if not ref:
            raise except_f1('Error', u'Documento sin fecha de solicitud')
        return ' '.join(ref.split('T')).split('.')[0]


class except_f1(Exception):
    def __init__(self, name, value, values_dict=None):
        self.name = name
        self.value = value
        self.values_dict = values_dict or {}