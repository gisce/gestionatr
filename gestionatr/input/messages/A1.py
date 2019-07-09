# -*- coding: utf-8 -*-
from message import Message
from Deadlines import ProcessDeadline
from gestionatr.input.messages import except_f1
from D1 import DatosInstGen, DatosSuministro, Autoconsumo
from gestionatr.utils import get_rec_attr


class A1(Message, ProcessDeadline):
    """Clase que implementa A1."""

    # Sobreescribim funcions relacionades amb la capçalera del XML
    @property
    def get_codi_emisor(self):
        if self.tipus == 'A1' and self.pas == '01':
            ref = self.head.CodigoEmpresaEmisora.text
        else:
            ref = self.head.CodigoREEEmpresaEmisora.text
        if not ref:
            raise except_f1('Error', u'Documento sin emisor')
        return ref

    @property
    def get_codi_destinatari(self):
        if self.tipus == 'A1' and self.pas == '02':
            ref = self.head.CodigoEmpresaDestino.text
        else:
            ref = self.head.CodigoREEEmpresaDestino.text
        if not ref:
            raise except_f1('Error', u'Documento sin emisor')
        return ref

    @property
    def cups(self):
        # El tipus A1 no informa CUPS a la capçalera
        return ''

    # Datos paso 01
    @property
    def movimiento(self):
        tree = '{0}.Movimiento'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data:
            return data.text
        else:
            return False

    @property
    def autoconsumo(self):
        tree = '{0}.Autoconsumo'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data not in [None, False]:
            return Autoconsumo(data)
        else:
            return False

    @property
    def datos_suministro(self):
        tree = '{0}.DatosSuministro'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data not in [None, False]:
            return DatosSuministro(data)
        else:
            return False

    @property
    def datos_inst_gen(self):
        data = []
        tree = get_rec_attr(self.obj, self._header, False)
        if hasattr(tree, 'DatosInstGen'):
            for datos in tree.DatosInstGen:
                data.append(DatosInstGen(datos))
            return data
        else:
            return False

    @property
    def comentarios(self):
        tree = '{0}.Comentarios'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data:
            return data.text
        else:
            return False

    # Datos paso 02 aceptacion / rechazo
    @property
    def cau(self):
        tree = '{0}.CAU'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data:
            return data.text
        else:
            return False

    @property
    def actualizacion_datos_registro(self):
        tree = '{0}.ActualizacionDatosRegistro'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data not in [None, False]:
            return ActualizacionDatosRegistro(data)
        else:
            return False

    @property
    def rechazos(self):
        data = []
        obj = get_rec_attr(self.obj, self._header, False)
        if (hasattr(obj, 'Rechazos') and
                hasattr(obj.Rechazos, 'Rechazo')):
            for d in obj.Rechazos.Rechazo:
                data.append(Rechazo(d))
        return data

    @property
    def comentarios(self):
        tree = '{0}.Comentarios'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data:
            return data.text
        else:
            return False


class ActualizacionDatosRegistro(object):

    def __init__(self, data):
        self.actualizacion_datos_registro = data

    @property
    def sub_seccion(self):
        data = ''
        try:
            data = self.actualizacion_datos_registro.SubSeccion.text
        except AttributeError:
            pass
        return data


class Rechazo(object):

    def __init__(self, data):
        self.rechazo = data

    @property
    def fecha_rechazo(self):
        data = ''
        try:
            data = self.rechazo.FechaRechazo.text
        except AttributeError:
            pass
        return data

    @property
    def secuencial(self):
        data = ''
        try:
            data = self.rechazo.Secuencial.text
        except AttributeError:
            pass
        return data

    @property
    def codigo_motivo(self):
        data = ''
        try:
            data = self.rechazo.CodigoMotivo.text
        except AttributeError:
            pass
        return data

    @property
    def cups(self):
        data = ''
        try:
            data = self.rechazo.CUPS.text
        except AttributeError:
            pass
        return data

    @property
    def comentarios(self):
        data = ''
        try:
            data = self.rechazo.Comentarios.text
        except AttributeError:
            pass
        return data
