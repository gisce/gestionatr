# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from .message_gas import MessageGas
from gestionatr.utils import get_rec_attr
from gestionatr.defs_gas import TIPUS_CONCEPTES, PEAJES_SEMPRE_CAPACIDAD, REFUND_RECTIFICATIVE_TYPES
from datetime import datetime, timedelta


class B7031(MessageGas):
    def __init__(self, xml, force_tipus=None, productes_exclosos=None):
        if productes_exclosos is None:
            productes_exclosos = []
        super(MessageGas, self).__init__(xml, force_tipus=force_tipus)
        self.productes_exclosos = productes_exclosos

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
            data.append(Factura(d, self.productes_exclosos))
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

    def get_facturas_atr(self):
        return [f for f in self.facturas if not f.is_only_conceptes()]

    def get_facturas_otros(self):
        if self.codproceso == '33':
            return []
        return [f for f in self.facturas if f.is_only_conceptes()]


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
    def __init__(self, data, productes_exclosos):
        self.obj = data
        self.productes_exclosos = productes_exclosos

    @property
    def rangopresiondiseno(self):
        tree = 'rangopresiondiseno'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def telemedida(self):
        tree = 'telemedida'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def tipogasinera(self):
        tree = 'tipogasinera'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def metodofacturacion(self):
        tree = 'metodofacturacion'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            # Si no ens el diuen, el calcularem! En base a la tarifa i a la telemedida ho podem saber
            tarifa = self.tipopeaje
            telemedida = self.telemedida
            if not tarifa or not telemedida:  # No hauria de passar ja que son camps obligatoris en les noves tarifes...
                return False
            elif tarifa in PEAJES_SEMPRE_CAPACIDAD:  # A partir de la 7 sempre son capacidad
                return '1'
            elif telemedida == 'N':  # Les mes baixes, si no tenen telemedida segur que son per client
                return '2'
            # Si arribem a aquest punt vol dir que el F1 esta malament ja que si es una tarifa de les baixes i
            # te telemedida, ens han de concretar com es factura sempre
            return False

    @property
    def cups(self):
        tree = 'cups'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def contratosimultaneo(self):
        tree = 'contratosimultaneo'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def codigoproducto(self):
        tree = 'codigoproducto'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def tipoproducto(self):
        tree = 'tipoproducto'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def arrastrapenalizacion(self):
        tree = 'arrastrapenalizacion'
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

    def get_origin(self):
        return self.numfactura

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
            return float(data.text)
        else:
            return False

    @property
    def saldo_total_a_cobrar(self):
        tree = 'SaldoTotalACobrar'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return float(data.text)
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

    def get_coeficientecortoplazo(self):
        for d in self.listaconceptos:
            if d.coeficientecortoplazo and float(d.coeficientecortoplazo):
                return float(d.coeficientecortoplazo)
        return 0.0

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

    @property
    def mediaconsumo(self):
        tree = 'mediaconsumo'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return MediaConsumo(data)
        else:
            return False

    @property
    def codtbai(self):
        tree = 'codtbai'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    def get_periode_factura(self):
        """Retorna tupla amb (data inici,  data fi) de la factura:
            - data inici: la mes antiga de les fecdesde dels conceptes
            - data fi: la mes nova de les fechasta dels conceptes
        """
        return (
            min([x.fecdesde for x in self.listaconceptos if x.codconcepto not in self.productes_exclosos]),
            max([x.fechasta for x in self.listaconceptos if x.codconcepto not in self.productes_exclosos])
        )

    def get_periode_factura_peatges(self):
        """Retorna tupla amb (data inici,  data fi) de la factura:
            - data inici: la mes antiga de les fecdesde dels conceptes
            - data fi: la mes nova de les fechasta dels conceptes
        """
        return (
            min([x.fecdesde for x in self.listaconceptos if
                 "tvariable" in TIPUS_CONCEPTES.get(x.codconcepto, "") or "tfix" in TIPUS_CONCEPTES.get(x.codconcepto, "")]
                ),
            max([x.fechasta for x in self.listaconceptos if
                 "tvariable" in TIPUS_CONCEPTES.get(x.codconcepto, "") or "tfix" in TIPUS_CONCEPTES.get(x.codconcepto, "")]
                )
        )

    def is_only_conceptes(self):
        has_only_conceptes = True
        for type in self.get_linies_factura_by_type():
            if type not in ['informacio', 'altres']:
                has_only_conceptes = False
        return has_only_conceptes

    def get_create_invoice_params(self):
        return {
            'tipo_rectificadora': self.clasefact or self.indfacturarect or 'N',
            'date_invoice': self.fecfactura,
            'check_total': -1 * self.importetotal if self.clasefact in REFUND_RECTIFICATIVE_TYPES else self.importetotal,
            'origin': self.get_origin(),
            'origin_date_invoice': self.fecfactura,
            'reference': self.get_origin(),
            'tipo_factura': self.tipofactura
        }

    def get_linies_factura_by_type(self):
        res = {}
        res_to_join = {}
        to_join = {
            'tfixe_cargos': 'tfixe',
            'tfixe_altres': 'tfixe',
            'tvariable_altres': 'tvariable',
        }
        for concepte in self.listaconceptos:
            tipus = TIPUS_CONCEPTES.get(concepte.codconcepto, "altres")
            if tipus == "impost":
                continue
            if tipus in to_join.keys():
                aux_res = res_to_join
            else:
                aux_res = res
            aux_res.setdefault(tipus, {'total': 0.0, 'lines': []})
            aux_res[tipus]['lines'] += [concepte]
            new_total = aux_res[tipus]['total'] + concepte.importe
            aux_res[tipus]['total'] = round(new_total, 2)

        for tipus, info in res_to_join.items():
            tipus_join = to_join.get(tipus)
            if not res.get(tipus_join):
                res[tipus_join].setdefault(tipus, {'total': 0.0, 'lines': []})
            base = 1.0
            res[tipus_join]['total'] += info['total']
            for l in info['lines']:
                for l2 in res[tipus_join]['lines']:
                    if l2.unidad == l.unidad:
                        l2.precunidad += round(l.precunidad * base, 9)
        return res

    def get_comptadors(self):
        """Retorna totes les lectures en una llista de comptadors"""
        comptadors_agrupats = {}
        for medidor in self.listamedidores:
            comptadors_agrupats.setdefault(
                medidor.numseriemedidor, []
            ).append(medidor)

        comptadors = []
        for llista_aparells in comptadors_agrupats.values():
            aparell_multi = MultiModeloAparato(llista_aparells)

            di, df = aparell_multi.get_dates_inici_i_final()
            comptadors.append((di, df, aparell_multi))
        return [a[2] for a in sorted(comptadors, lambda x,y: cmp(x[0], y[0]))]

    def get_info_lloguer(self):
        lloguers = []
        total = 0
        info = self.get_linies_factura_by_type().get('lloguer', False)
        if info:
            lloguers = info['lines']
            total = info['total']
        return lloguers, total

    def get_remesa(self):
        return {
            'id_remesa': self.idremesa,
            'fecha_valor_remesa': self.fecpago
        }

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
        self._precunidad = 0.0

    @property
    def coeficientecortoplazo(self):
        tree = 'coeficientecortoplazo'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def multexcesocaudal(self):
        tree = 'multexcesocaudal'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def diascapacidadcontratada(self):
        tree = 'diascapacidadcontratada'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def horascapacidadcontratada(self):
        tree = 'horascapacidadcontratada'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

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
            return float(data.text)
        else:
            return False

    @property
    def precunidad(self):
        if self._precunidad:
            return self._precunidad
        tree = 'precunidad'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return float(data.text)
        else:
            return False

    @precunidad.setter
    def precunidad(self, value):
        self._precunidad = value

    @property
    def importe(self):
        tree = 'importe'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return float(data.text)
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
            return float(data.text)
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
            return float(data.text)
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
    def excesocaudal(self):
        tree = 'excesocaudal'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

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
            return float(data.text)
        else:
            return False

    @property
    def factork(self):
        tree = 'factork'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return float(data.text)
        else:
            return False

    @property
    def pcs(self):
        tree = 'pcs'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return float(data.text)
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
            return float(data.text)
        else:
            return False

    @property
    def consumoereal(self):
        tree = 'consumoereal'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return float(data.text)
        else:
            return False

    @property
    def consumoreg(self):
        tree = 'consumoreg'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return float(data.text)
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
            return float(data.text)
        else:
            return False

    @property
    def qdaplicado(self):
        tree = 'qdaplicado'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return float(data.text)
        else:
            return False

    @property
    def qdmaximo(self):
        tree = 'qdmaximo'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return float(data.text)
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
            return float(data.text)
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

    def get_lectures_info(self):
        res = []
        if not hasattr(self, 'meters'):
            self.meters = [self]
        factor_ultima_lectura = False
        for meter in self.meters:
            fecha_desde = meter.feclecant
            fecha_actual = meter.feclecact
            if fecha_desde == fecha_actual and meter.horalecact in ("23:00:00", "24:00:00"):
                # A vegades envien una lectura a les 00 i l'altre a les 23 i son del mateix dia.
                # Es equivalent a enviar una a les 23 del dia anterior i l'altre a les 23 del dia actual. per tant,
                # restem un dia a la lectura desde
                fecha_desde = (datetime.strptime(fecha_desde, "%Y-%m-%d") - timedelta(days=1)).strftime("%Y-%m-%d")
            comptador = meter.numseriemedidor
            periode = meter.tipo_dh
            ajust = float(meter.ajuste)
            motiu = meter.codajuste
            factor_k = float(meter.factork)
            pcs = float(meter.pcs)
            pressio_subministrament = float(meter.presionsuministro)
            qdaplicado = float(meter.qdaplicado)
            qdmaximo = float(meter.qdmaximo)
            fecqdmax = meter.fecqdmax
            dqmedio = float(meter.dqmedio)
            qdcontratado = float(meter.qdcontratado)
            excesocaudal = float(meter.excesocaudal)
            temperatura_gas = float(meter.temp)
            pressio_atmosferica = float(meter.presatm)
            consum_kwh_facturat = float(meter.consumokwh)
            for numerador in meter.listanumeradores:
                lectura_desde_m3 = float(numerador.lectant)
                lectura_actual_m3 = float(numerador.lecact)
                origen_desde = numerador.tipolec
                origen_actual = numerador.tipolec
                tipo_lect_num = numerador.tipolecnum
                lectura_desde = lectura_desde_m3 * float(meter.factorconver)
                lectura_actual = lectura_actual_m3 * float(meter.factorconver)
                vals = {
                    'pressio_subministrament': pressio_subministrament,
                    'lectura_desde': lectura_desde,
                    'lectura_actual': lectura_actual,
                    'lectura_desde_m3': lectura_desde_m3,
                    'lectura_actual_m3': lectura_actual_m3,
                    'fecha_desde': fecha_desde,
                    'fecha_actual': fecha_actual,
                    'comptador': comptador,
                    'origen_desde': origen_desde,
                    'origen_actual': origen_actual,
                    'periode': periode or "P1",
                    'ajust': ajust,
                    'motiu': motiu,
                    'tipo_lect_num': tipo_lect_num,
                    'factor_k': factor_k,
                    'pcs': pcs,
                    'ometre': numerador.aparatorelevante == 'N',
                    'consum_m3': float(numerador.consumo),
                    'consum': float(numerador.consumo) * float(meter.factorconver),
                    'qdaplicado': float(qdaplicado),
                    'qdmaximo': float(qdmaximo),
                    'fecqdmax': fecqdmax,
                    'dqmedio': float(dqmedio),
                    'qdcontratado': float(qdcontratado),
                    'excesocaudal': float(excesocaudal),
                    'temperatura_gas': float(temperatura_gas),
                    'pressio_atmosferica': float(pressio_atmosferica),
                }

                # Si el consum que calculem amb el factor_k i el pcs no dona el consum calculat amb el factor de conversio
                # pero si fem servir el factor de conversio informat per la distri si que dona, modfiquem el factor_k perque
                # el factor de conversio calculat sigui igual al informat i aixi el consum també quadri.
                # TODO
                # Revisant un cas concret, sembla que realment ens falta aplicar la zeta, per aixo no quadra.
                # Normalment es 1 pero pot no ser-ho. Aixó es una mandanga per no ahver de treballar amb la zeta.
                consum_calculat_sefons_fomrula = round(vals['consum_m3'] * vals['pcs'] * vals['factor_k'], 3)
                consum_calculat_segons_factor = round(vals['consum'], 3)
                if consum_calculat_segons_factor != consum_calculat_sefons_fomrula:
                    consum_calculat = round(vals['consum_m3'] * meter.factorconver, 3)
                    if consum_calculat_segons_factor == consum_calculat:
                        vals['factor_k'] = meter.factorconver / vals['pcs']

                # Unaltre cas concret de ***
                # Hi ha distris que tot i tindre lectures diaries no apliquen el factor de conversio registart en
                # cada dia, sino que paliquen a totes les lectures de tots els dies el factor de conversio de la
                # ultima lectura
                # Per tant: si el consum facturat per la distri no coincideix amb el consum calculat, ero aplicant
                # el faactor de conversio del ultim dia siq ue aplica, recalculem el factor k perque quadri tot.
                if consum_kwh_facturat != consum_calculat_segons_factor:
                    if not factor_ultima_lectura and self.meters[-1].factorconver:
                        factor_ultima_lectura = float(self.meters[-1].factorconver)
                    if factor_ultima_lectura:
                        vals['factor_k'] = consum_kwh_facturat / (vals['consum_m3'] * vals['pcs'])
                        vals['consum'] = consum_kwh_facturat
                res.append(vals)
        return res

    def get_giro(self):
        return max([10**int(l.digmed) for l in self.listanumeradores])


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


class MediaConsumo(object):
    def __init__(self, data):
        self.obj = data

    @property
    def mediaconsperiodofact5A(self):
        tree = 'mediaconsperiodofact5A'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def mediaconsperiodofact(self):
        tree = 'mediaconsperiodofact'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False


# Datos para B7032
class B7032(B7031):
    pass


class B7033(B7032):
    pass


class Factura(Factura):

    @property
    def numpseudofactura(self):
        tree = 'numpseudofactura'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    def get_origin(self):
        res = super(Factura, self).get_origin()
        if self.numpseudofactura:
            return (res or "") + " - " + (self.numpseudofactura or "")
        else:
            return res

    @property
    def numfacturarect(self):
        tree = 'numfacturarect'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def numfactorigen(self):
        if self.numfacturarect:
            return self.numfacturarect
        else:
            return super(Factura, self).numfactorigen

    @property
    def indfacturarect(self):
        tree = 'indfacturarect'
        data = get_rec_attr(self.obj, tree, False)
        if data is not None and data is not False:
            return data.text
        else:
            return False

    @property
    def clasefact(self):
        if self.indfacturarect:
            return self.indfacturarect
        else:
            return super(Factura, self).clasefact


# Let the user say only B70
class B70(B7031):
    pass


class MultiModeloAparato(Medidor):

    def __init__(self, meter_list):
        self.meters = meter_list
        super(MultiModeloAparato, self).__init__(meter_list[0])

    def _get_single_attribute(self, attribute):
        for meter in self.meters:
            attr_val = getattr(meter, attribute, None)
            if attr_val is not None:
                return attr_val

        return None

    def _get_list_attribute(self, attribute):
        res = []

        for meter in self.meters:
            if hasattr(meter, attribute):
                res += getattr(meter, attribute)

        return res

    def get_dates_inici_i_final(self):
        data_inici = ''
        data_final = ''
        for lect in self.meters:
            data_in_compt = datetime.strptime(
                lect.feclecant, '%Y-%m-%d'
            )
            data_fi_compt = datetime.strptime(
                lect.feclecact, '%Y-%m-%d'
            )

            if not data_inici or data_in_compt < data_inici:
                data_inici = data_in_compt
            if not data_final or data_in_compt > data_final:
                data_final = data_fi_compt

        return data_inici, data_final

    @property
    def feclecant(self):
        return self._get_single_attribute('feclecant')

    @property
    def feclecact(self):
        return self._get_single_attribute('feclecact')

    @property
    def modelomedidor(self):
        return self._get_single_attribute('modelomedidor')

    @property
    def numseriemedidor(self):
        return self._get_single_attribute('numseriemedidor')

    @property
    def factorconver(self):
        return self._get_single_attribute('factorconver')

    @property
    def factork(self):
        return self._get_single_attribute('factork')

    @property
    def pcs(self):
        return self._get_single_attribute('pcs')

    @property
    def consumokwh(self):
        return self._get_single_attribute('consumokwh')

    @property
    def codajuste(self):
        return self._get_single_attribute('codajuste')

    @property
    def ajuste(self):
        return self._get_single_attribute('ajuste')

    @property
    def motivolec(self):
        return self._get_single_attribute('motivolec')

    @property
    def tipo_dh(self):
        return self._get_single_attribute('tipo_dh')

    @property
    def listanumeradores(self):
        return self._get_list_attribute('listanumeradores')
    @property
    def presionsuministro(self):
        return self._get_single_attribute('presionsuministro')


def agrupar_lectures_per_data(lectures):
    """Retorna un diccionari de llistes en què les
       claus són les dates inicial i final de les lectures
    """
    lect = {}
    for i in lectures:
        key = (i['fecha_desde'], i['fecha_actual'])
        if key not in lect:
            lect[key] = []
        lect[key].append(i)
    return lect


def obtenir_data_inici_i_final(dic):
    """Retorna la data inicial i final del diccionari retornat
       per la funció agrupar_lectures_per_data()
    """
    inici_conjunt = None
    final_conjunt = None
    for keys in dic.keys():
        if not inici_conjunt or inici_conjunt > keys[0]:
            inici_conjunt = keys[0]
        if not final_conjunt or final_conjunt < keys[1]:
            final_conjunt = keys[1]

    return inici_conjunt, final_conjunt
