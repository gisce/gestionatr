# -*- coding: utf-8 -*-
from message_gas import MessageGas
from gestionatr.utils import get_rec_attr


class B7031(MessageGas):

    @property
    def datosempresaemisora(self):
        tree = 'datosempresaemisora'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return Datosempresaemisora(data)
        else:
            return False

    @property
    def datosempresadestino(self):
        tree = 'datosempresadestino'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return Datosempresadestino(data)
        else:
            return False

    @property
    def facturas(self):
        data = []
        for d in get_rec_attr(self.obj, 'factura', []):
            data.append(Factura(d))
        return data

    def get_datosempresaemisora(self):
        tree = 'datosempresaemisora'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            aux = Datosempresaemisora(data)
            return {
                'numdocumento': aux.numdocumento,
                'razonsocial': aux.razonsocial,
                'direccion': aux.direccion,
                'municipio': aux.municipio,
                'regmercantil': aux.regmercantil,
            }
        else:
            return False

    def get_datosempresadestino(self):
        tree = 'datosempresaemisora'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            aux = Datosempresadestino(data)
            return {
                'numdocumento': aux.numdocumento,
                'razonsocial': aux.razonsocial,
                'direccion': aux.direccion,
                'municipio': aux.municipio,
            }
        else:
            return False


class Datosempresadestino(object):
    def __init__(self, data):
        self.obj = data

    @property
    def numdocumento(self):
        tree = 'numdocumento'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def razonsocial(self):
        tree = 'razonsocial'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def direccion(self):
        tree = 'direccion'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def municipio(self):
        tree = 'municipio'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False


class Datosempresaemisora(Datosempresadestino):

    @property
    def regmercantil(self):
        tree = 'regmercantil'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False


class Factura(object):
    def __init__(self, data):
        self.obj = data

    @property
    def cups(self):
        tree = 'cups'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def provincia(self):
        tree = 'provincia'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def municipio(self):
        tree = 'municipio'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def codpostal(self):
        tree = 'codpostal'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def tipovia(self):
        tree = 'tipovia'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def descalle(self):
        tree = 'descalle'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def numfinca(self):
        tree = 'numfinca'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def portal(self):
        tree = 'portal'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def escalera(self):
        tree = 'escalera'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def piso(self):
        tree = 'piso'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def puerta(self):
        tree = 'puerta'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def municipio_red(self):
        tree = 'municipioRed'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def tipodocumento(self):
        tree = 'tipodocumento'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def numdocumento(self):
        tree = 'numdocumento'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def nombre(self):
        tree = 'nombre'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def apellido1(self):
        tree = 'apellido1'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def apellido2(self):
        tree = 'apellido2'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def tipofactura(self):
        tree = 'tipofactura'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def clasefact(self):
        tree = 'clasefact'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def numfactorigen(self):
        tree = 'numfactorigen'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def fecfactura(self):
        tree = 'fecfactura'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def numfactura(self):
        tree = 'numfactura'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def tipofacturacion(self):
        tree = 'tipofacturacion'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def tipopeaje(self):
        tree = 'tipopeaje'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def feccontable(self):
        tree = 'feccontable'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def fecpago(self):
        tree = 'fecpago'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def importetotal(self):
        tree = 'importetotal'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def saldo_total_a_cobrar(self):
        tree = 'SaldoTotalACobrar'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def idremesa(self):
        tree = 'idremesa'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def tipopenalizacion(self):
        tree = 'tipopenalizacion'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def observaciones1(self):
        tree = 'observaciones1'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def observaciones2(self):
        tree = 'observaciones2'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def telefurgencias(self):
        tree = 'telefurgencias'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def listaboe(self):
        data = []
        obj = self.obj
        if (hasattr(obj, 'listaboe') and
                hasattr(obj.listaboe, 'boe')):
            for d in obj.listaboe.boe:
                data.append(Boe(d))
        return data

    @property
    def listaconceptos(self):
        data = []
        obj = self.obj
        if (hasattr(obj, 'listaconceptos') and
                hasattr(obj.listaconceptos, 'concepto')):
            for d in obj.listaconceptos.concepto:
                data.append(Concepto(d))
        return data

    @property
    def listamedidores(self):
        data = []
        obj = self.obj
        if (hasattr(obj, 'listamedidores') and
                hasattr(obj.listamedidores, 'medidor')):
            for d in obj.listamedidores.medidor:
                data.append(Medidor(d))
        return data

    @property
    def listafacturasinspeccion(self):
        data = []
        obj = self.obj
        if (hasattr(obj, 'listafacturasinspeccion') and
                hasattr(obj.listafacturasinspeccion, 'facturainspeccion')):
            for d in obj.listafacturasinspeccion.facturainspeccion:
                data.append(Facturasinspeccion(d))
        return data

    @property
    def lista_contactos(self):
        data = []
        obj = self.obj
        if (hasattr(obj, 'listaContactos') and
                hasattr(obj.listaContactos, 'contacto')):
            for d in obj.listaContactos.contacto:
                data.append(Contacto(d))
        return data

    @property
    def historial_consumos(self):
        data = []
        obj = self.obj
        if (hasattr(obj, 'historialConsumos') and
                hasattr(obj.historialConsumos, 'consumo')):
            for d in obj.historialConsumos.consumo:
                data.append(Consumo(d))
        return data

    @property
    def imputacion_costes(self):
        tree = 'imputacionCostes'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return Imputacioncostes(data)
        else:
            return False


class Boe(object):
    def __init__(self, data):
        self.obj = data

    @property
    def numboe(self):
        tree = 'numboe'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def fecboe(self):
        tree = 'fecboe'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False


class Concepto(object):
    def __init__(self, data):
        self.obj = data

    @property
    def fecdesde(self):
        tree = 'fecdesde'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def fechasta(self):
        tree = 'fechasta'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def unidad(self):
        tree = 'unidad'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def precunidad(self):
        tree = 'precunidad'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def importe(self):
        tree = 'importe'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def codconcepto(self):
        tree = 'codconcepto'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def desconcepto(self):
        tree = 'desconcepto'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def porcentajeconcepto(self):
        tree = 'porcentajeconcepto'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def impuestoconcepto(self):
        tree = 'impuestoconcepto'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def codtipoimpuesto(self):
        tree = 'codtipoimpuesto'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def porcentajeimpcto(self):
        tree = 'porcentajeimpcto'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def umconcepto(self):
        tree = 'umconcepto'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def aparatoconcepto(self):
        tree = 'aparatoconcepto'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def observaciones(self):
        tree = 'observaciones'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def fec_desde_prorrateo(self):
        tree = 'fecDesdeProrrateo'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def tipo_interes_demora(self):
        tree = 'tipoInteresDemora'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False


class Medidor(object):
    def __init__(self, data):
        self.obj = data

    @property
    def um(self):
        tree = 'um'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def feclecant(self):
        tree = 'feclecant'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def horalecant(self):
        tree = 'horalecant'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def feclecact(self):
        tree = 'feclecact'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def horalecact(self):
        tree = 'horalecact'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def serializada(self):
        tree = 'serializada'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def restadeserializada(self):
        tree = 'restadeserializada'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def cupsresta(self):
        tree = 'cupsresta'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def aparato(self):
        tree = 'aparato'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def medicion(self):
        tree = 'medicion'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def modelomedidor(self):
        tree = 'modelomedidor'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def numseriemedidor(self):
        tree = 'numseriemedidor'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def unipres(self):
        tree = 'unipres'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def presatm(self):
        tree = 'presatm'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def presionsuministro(self):
        tree = 'presionsuministro'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def temp(self):
        tree = 'temp'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def factorconver(self):
        tree = 'factorconver'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def factork(self):
        tree = 'factork'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def pcs(self):
        tree = 'pcs'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def zeta(self):
        tree = 'zeta'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def densidad(self):
        tree = 'densidad'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def n2(self):
        tree = 'n2'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def co2(self):
        tree = 'co2'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def h2(self):
        tree = 'h2'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def consumokwh(self):
        tree = 'consumokwh'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def consumoereal(self):
        tree = 'consumoereal'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def consumoreg(self):
        tree = 'consumoreg'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def codajuste(self):
        tree = 'codajuste'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def ajuste(self):
        tree = 'ajuste'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def qdaplicado(self):
        tree = 'qdaplicado'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def qdmaximo(self):
        tree = 'qdmaximo'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def fecqdmax(self):
        tree = 'fecqdmax'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def dqmedio(self):
        tree = 'dqmedio'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def qdcontratado(self):
        tree = 'qdcontratado'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def motivolec(self):
        tree = 'motivolec'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def tipo_dh(self):
        tree = 'tipoDH'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def perlec(self):
        tree = 'perlec'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def capacidadcontador(self):
        tree = 'capacidadcontador'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def observaciones1(self):
        tree = 'observaciones1'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def observaciones2(self):
        tree = 'observaciones2'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def listanumeradores(self):
        data = []
        obj = self.obj
        if (hasattr(obj, 'listanumeradores') and
                hasattr(obj.listanumeradores, 'numerador')):
            for d in obj.listanumeradores.numerador:
                data.append(Numerador(d))
        return data


class Numerador(object):
    def __init__(self, data):
        self.obj = data

    @property
    def num(self):
        tree = 'num'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def digmed(self):
        tree = 'digmed'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def digdecmed(self):
        tree = 'digdecmed'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def factmulmed(self):
        tree = 'factmulmed'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def lectant(self):
        tree = 'lectant'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def lecact(self):
        tree = 'lecact'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def tipolec(self):
        tree = 'tipolec'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def consumo(self):
        tree = 'consumo'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def tipolecnum(self):
        tree = 'tipolecnum'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def aparatorelevante(self):
        tree = 'aparatorelevante'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def observaciones(self):
        tree = 'observaciones'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False


class Facturasinspeccion(object):
    def __init__(self, data):
        self.obj = data

    @property
    def numdocumentoinstalador(self):
        tree = 'numdocumentoinstalador'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def razonsocialinstalador(self):
        tree = 'razonsocialinstalador'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def numfacturainspeccion(self):
        tree = 'numfacturainspeccion'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False


class Contacto(object):
    def __init__(self, data):
        self.obj = data

    @property
    def denominacion(self):
        tree = 'denominacion'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def url(self):
        tree = 'url'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def email(self):
        tree = 'email'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def telefono(self):
        tree = 'telefono'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False


class Consumo(object):
    def __init__(self, data):
        self.obj = data

    @property
    def fecinicioperiodo(self):
        tree = 'fecinicioperiodo'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def fecfinperiodo(self):
        tree = 'fecfinperiodo'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def consumoperiodo(self):
        tree = 'consumoperiodo'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False


class Imputacioncostes(object):
    def __init__(self, data):
        self.obj = data

    @property
    def pcttasacnmc(self):
        tree = 'pcttasacnmc'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def pctcuotagts(self):
        tree = 'pctcuotagts'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False
