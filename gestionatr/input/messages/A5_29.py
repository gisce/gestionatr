# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from .message_gas import MessageGas
from .Deadlines import ProcessDeadline
from gestionatr.utils import get_rec_attr


class A5_29(MessageGas, ProcessDeadline):

    # Datos paso a529
    # TODO

    # Datos paso a629

    @property
    def codrpds(self):
        tree = '{0}.codrpds'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def fechacreacion(self):
        tree = '{0}.fechacreacion'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def horacreacion(self):
        tree = '{0}.horacreacion'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def codresultado(self):
        tree = '{0}.codresultado'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def descresultado(self):
        tree = '{0}.descresultado'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def codmotivo(self):
        tree = '{0}.codmotivo'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def descmotresultado(self):
        tree = '{0}.descmotresultado'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def resvalidacioncliente(self):
        tree = '{0}.resvalidacioncliente'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def datosdis(self):
        tree = '{0}.datosdis'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data not in [None, False]:
            return DatosDis(data)
        else:
            return False

    @property
    def datoscom(self):
        tree = '{0}.datoscom'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data not in [None, False]:
            return DatosCom(data)
        else:
            return False


class DatosDis(object):
    def __init__(self, data):
        self.datosdis = data

    @property
    def cups(self):
        data = False
        try:
            data = self.datosdis.cups.text
        except AttributeError:
            pass
        return data

    @property
    def distribuidor(self):
        data = False
        try:
            data = self.datosdis.distribuidor.text
        except AttributeError:
            pass
        return data

    @property
    def razonsocial(self):
        data = False
        try:
            data = self.datosdis.razonsocial.text
        except AttributeError:
            pass
        return data

    @property
    def codprovincia(self):
        data = False
        try:
            data = self.datosdis.codprovincia.text
        except AttributeError:
            pass
        return data

    @property
    def descprovincia(self):
        data = False
        try:
            data = self.datosdis.descprovincia.text
        except AttributeError:
            pass
        return data

    @property
    def codpostal(self):
        data = False
        try:
            data = self.datosdis.codpostal.text
        except AttributeError:
            pass
        return data

    @property
    def codmunicipio(self):
        data = False
        try:
            data = self.datosdis.codmunicipio.text
        except AttributeError:
            pass
        return data

    @property
    def descmunicipio(self):
        data = False
        try:
            data = self.datosdis.descmunicipio.text
        except AttributeError:
            pass
        return data

    @property
    def tipovia(self):
        data = False
        try:
            data = self.datosdis.tipovia.text
        except AttributeError:
            pass
        return data

    @property
    def via(self):
        data = False
        try:
            data = self.datosdis.via.text
        except AttributeError:
            pass
        return data

    @property
    def numfinca(self):
        data = False
        try:
            data = self.datosdis.numfinca.text
        except AttributeError:
            pass
        return data

    @property
    def restodireccion(self):
        data = False
        try:
            data = self.datosdis.restodireccion.text
        except AttributeError:
            pass
        return data

    @property
    def viviendahabitual(self):
        data = False
        try:
            data = self.datosdis.viviendahabitual.text
        except AttributeError:
            pass
        return data

    @property
    def fechaalta(self):
        data = False
        try:
            data = self.datosdis.fechaalta.text
        except AttributeError:
            pass
        return data

    @property
    def fechaultimalectura(self):
        data = False
        try:
            data = self.datosdis.fechaultimalectura.text
        except AttributeError:
            pass
        return data

    @property
    def puntocortado(self):
        data = False
        try:
            data = self.datosdis.puntocortado.text
        except AttributeError:
            pass
        return data

    @property
    def rangopresiondiseno(self):
        data = False
        try:
            data = self.datosdis.rangopresiondiseno.text
        except AttributeError:
            pass
        return data

    @property
    def qh(self):
        data = False
        try:
            data = self.datosdis.qh.text
        except AttributeError:
            pass
        return data

    @property
    def qmax(self):
        data = False
        try:
            data = self.datosdis.qmax.text
        except AttributeError:
            pass
        return data

    @property
    def derechotur(self):
        data = False
        try:
            data = self.datosdis.derechotur.text
        except AttributeError:
            pass
        return data

    @property
    def tarifapeaje(self):
        data = False
        try:
            data = self.datosdis.tarifapeaje.text
        except AttributeError:
            pass
        return data

    @property
    def fechaultimainspeccion(self):
        data = False
        try:
            data = self.datosdis.fechaultimainspeccion.text
        except AttributeError:
            pass
        return data

    @property
    def resultimainspeccion(self):
        data = False
        try:
            data = self.datosdis.resultimainspeccion.text
        except AttributeError:
            pass
        return data

    @property
    def fechaultimarevision(self):
        data = False
        try:
            data = self.datosdis.fechaultimarevision.text
        except AttributeError:
            pass
        return data

    @property
    def resultimarevision(self):
        data = False
        try:
            data = self.datosdis.resultimarevision.text
        except AttributeError:
            pass
        return data

    @property
    def historicoConsumo(self):
        data = []
        obj = get_rec_attr(self.obj, self._header, False)
        if hasattr(obj, 'historicoConsumo'):
            for i in self.datosdis.historicoConsumo:
                data.append(HistoricoConsumo(i))
            return data
        return data

    @property
    def pctjeconsumonoct(self):
        data = False
        try:
            data = self.datosdis.pctjeconsumonoct.text
        except AttributeError:
            pass
        return data

    @property
    def codequipo(self):
        data = False
        try:
            data = self.datosdis.codequipo.text
        except AttributeError:
            pass
        return data

    @property
    def contelemedida(self):
        data = False
        try:
            data = self.datosdis.contelemedida.text
        except AttributeError:
            pass
        return data

    @property
    def marcamodelocont(self):
        data = False
        try:
            data = self.datosdis.marcamodelocont.text
        except AttributeError:
            pass
        return data

    @property
    def marcamodelocorr(self):
        data = False
        try:
            data = self.datosdis.marcamodelocorr.text
        except AttributeError:
            pass
        return data

    @property
    def propiedad(self):
        data = False
        try:
            data = self.datosdis.propiedad.text
        except AttributeError:
            pass
        return data

    @property
    def tipocorrector(self):
        data = False
        try:
            data = self.datosdis.tipocorrector.text
        except AttributeError:
            pass
        return data

    @property
    def fecultcambiotarifa(self):
        data = False
        try:
            data = self.datosdis.fecultcambiotarifa.text
        except AttributeError:
            pass
        return data

    @property
    def fecultcontrato(self):
        data = False
        try:
            data = self.datosdis.fecultcontrato.text
        except AttributeError:
            pass
        return data

    @property
    def fecultcambiocom(self):
        data = False
        try:
            data = self.datosdis.fecultcambiocom.text
        except AttributeError:
            pass
        return data

    @property
    def perfil(self):
        data = False
        try:
            data = self.datosdis.perfil.text
        except AttributeError:
            pass
        return data

    @property
    def indconectadoplantasatelite(self):
        data = False
        try:
            data = self.datosdis.indconectadoplantasatelite.text
        except AttributeError:
            pass
        return data

    @property
    def fecactdist(self):
        data = False
        try:
            data = self.datosdis.fecactdist.text
        except AttributeError:
            pass
        return data

    @property
    def listaproductos(self):
        data = []
        obj = get_rec_attr(self.obj, self._header, False)
        if (hasattr(obj, 'listaproductos') and
                hasattr(obj.listaproductos, 'producto')):
            for i in self.datosdis.listaproductos:
                data.append(Producto(i))
        return data

class HistoricoConsumo(object):
    def __init__(self, data):
        self.historicoConsumo = data

    @property
    def fecinicioperiodo(self):
        data = False
        try:
            data = self.historicoConsumo.fecinicioperiodo.text
        except AttributeError:
            pass
        return data

    @property
    def fecfinperiodo(self):
        data = False
        try:
            data = self.historicoConsumo.fecfinperiodo.text
        except AttributeError:
            pass
        return data

    @property
    def consumoperiodo(self):
        data = False
        try:
            data = self.historicoConsumo.consumoperiodo.text
        except AttributeError:
            pass
        return data

    @property
    def caudalminperiodo(self):
        data = False
        try:
            data = self.historicoConsumo.caudalminperiodo.text
        except AttributeError:
            pass
        return data

    @property
    def caudalmedperiodo(self):
        data = False
        try:
            data = self.historicoConsumo.caudalmedperiodo.text
        except AttributeError:
            pass
        return data

    @property
    def caudalmaxperiodo(self):
        data = False
        try:
            data = self.historicoConsumo.caudalmaxperiodo.text
        except AttributeError:
            pass
        return data


class Producto(object):
    def __init__(self, data):
        self.prod = data

    @property
    def codigoproducto(self):
        data = False
        try:
            data = self.prod.codigoproducto.text
        except AttributeError:
            pass
        return data

    @property
    def tipoproducto(self):
        data = False
        try:
            data = self.prod.tipoproducto.text
        except AttributeError:
            pass
        return data

    @property
    def tarifaproducto(self):
        data = False
        try:
            data = self.prod.tarifaproducto.text
        except AttributeError:
            pass
        return data

    @property
    def qdproducto(self):
        data = False
        try:
            data = self.prod.qdproducto.text
        except AttributeError:
            pass
        return data

    @property
    def qaproducto(self):
        data = False
        try:
            data = self.prod.qaproducto.text
        except AttributeError:
            pass
        return data

    @property
    def fechainicioproducto(self):
        data = False
        try:
            data = self.prod.fechainicioproducto.text
        except AttributeError:
            pass
        return data

    @property
    def horainicioproducto(self):
        data = False
        try:
            data = self.prod.horainicioproducto.text
        except AttributeError:
            pass
        return data

    @property
    def fechafinproducto(self):
        data = False
        try:
            data = self.prod.fechafinproducto.text
        except AttributeError:
            pass
        return data


class DatosCom(object):
    def __init__(self, data):
        self.datoscom = data

    @property
    def nombre(self):
        data = False
        try:
            data = self.datoscom.nombre.text
        except AttributeError:
            pass
        return data

    @property
    def apellido1(self):
        data = False
        try:
            data = self.datoscom.apellido1.text
        except AttributeError:
            pass
        return data

    @property
    def apellido2(self):
        data = False
        try:
            data = self.datoscom.apellido2.text
        except AttributeError:
            pass
        return data

    @property
    def codprovincia(self):
        data = False
        try:
            data = self.datoscom.codprovincia.text
        except AttributeError:
            pass
        return data

    @property
    def descprovincia(self):
        data = False
        try:
            data = self.datoscom.descprovincia.text
        except AttributeError:
            pass
        return data

    @property
    def codpostal(self):
        data = False
        try:
            data = self.datoscom.codpostal.text
        except AttributeError:
            pass
        return data

    @property
    def codmunicipio(self):
        data = False
        try:
            data = self.datoscom.codmunicipio.text
        except AttributeError:
            pass
        return data

    @property
    def descmunicipio(self):
        data = False
        try:
            data = self.datoscom.descmunicipio.text
        except AttributeError:
            pass
        return data

    @property
    def tipovia(self):
        data = False
        try:
            data = self.datoscom.tipovia.text
        except AttributeError:
            pass
        return data

    @property
    def via(self):
        data = False
        try:
            data = self.datoscom.via.text
        except AttributeError:
            pass
        return data

    @property
    def numfinca(self):
        data = False
        try:
            data = self.datoscom.numfinca.text
        except AttributeError:
            pass
        return data

    @property
    def portal(self):
        data = False
        try:
            data = self.datoscom.portal.text
        except AttributeError:
            pass
        return data

    @property
    def escalera(self):
        data = False
        try:
            data = self.datoscom.escalera.text
        except AttributeError:
            pass
        return data

    @property
    def piso(self):
        data = False
        try:
            data = self.datoscom.piso.text
        except AttributeError:
            pass
        return data

    @property
    def puerta(self):
        data = False
        try:
            data = self.datoscom.puerta.text
        except AttributeError:
            pass
        return data

    @property
    def tipopersona(self):
        data = False
        try:
            data = self.datoscom.tipopersona.text
        except AttributeError:
            pass
        return data

    @property
    def viviendahabitual(self):
        data = False
        try:
            data = self.datoscom.viviendahabitual.text
        except AttributeError:
            pass
        return data

    @property
    def impagos(self):
        data = False
        try:
            data = self.datoscom.impagos.text
        except AttributeError:
            pass
        return data

    @property
    def fecimpagos(self):
        data = False
        try:
            data = self.datoscom.fecimpagos.text
        except AttributeError:
            pass
        return data

    @property
    def catimpagos(self):
        data = False
        try:
            data = self.datoscom.catimpagos.text
        except AttributeError:
            pass
        return data

    @property
    def usuimpagos(self):
        data = False
        try:
            data = self.datoscom.usuimpagos.text
        except AttributeError:
            pass
        return data

    @property
    def prohibpublicdatcli(self):
        data = False
        try:
            data = self.datoscom.prohibpublicdatcli.text
        except AttributeError:
            pass
        return data

    @property
    def fecactprohibpublic(self):
        data = False
        try:
            data = self.datoscom.fecactprohibpublic.text
        except AttributeError:
            pass
        return data

    @property
    def catactprohibpublic(self):
        data = False
        try:
            data = self.datoscom.catactprohibpublic.text
        except AttributeError:
            pass
        return data

    @property
    def usuactprohibpublic(self):
        data = False
        try:
            data = self.datoscom.usuactprohibpublic.text
        except AttributeError:
            pass
        return data
