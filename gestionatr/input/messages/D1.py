# -*- coding: utf-8 -*-
from gestionatr.input.messages import C1
from gestionatr.utils import get_rec_attr


class D1(C1):
    """Clase que implementa D1."""

    @property
    def motivo_cambio_atr_desde_distribuidora(self):
        tree = '{0}.MotivoCambioATRDesdeDistribuidora'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data:
            return data.text
        else:
            return False

    @property
    def fecha_prevista_aplicacion_cambio_atr(self):
        tree = '{0}.FechaPrevistaAplicacionCambioATR'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data:
            return data.text
        else:
            return False

    @property
    def periodicidad_facturacion(self):
        tree = '{0}.PeriodicidadFacturacion'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data:
            return data.text
        else:
            return False

    @property
    def info_registro_autocons(self):
        tree = '{0}.InfoRegistroAutocons'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data not in [None, False]:
            return InfoRegistroAutocons(data)
        else:
            return False


class InfoRegistroAutocons(object):

    def __init__(self, data):
        self.info_registro_autocons = data

    @property
    def autoconsumo(self):
        data = ''
        try:
            data = Autoconsumo(self.info_registro_autocons.Autoconsumo)
        except AttributeError:
            pass
        return data

    @property
    def datos_suministro(self):
        data = ''
        try:
            data = DatosSuministro(self.info_registro_autocons.DatosSuministro)
        except AttributeError:
            pass
        return data

    @property
    def datos_inst_gen(self):
        data = []
        try:
            for datos in self.info_registro_autocons.DatosInstGen:
                data.append(DatosInstGen(datos))
        except AttributeError:
            pass
        return data

    @property
    def comentarios(self):
        data = ''
        try:
            data = self.info_registro_autocons.Comentarios.text
        except AttributeError:
            pass
        return data


class Autoconsumo(object):

    def __init__(self, data):
        self.autoconsumo = data

    @property
    def cau(self):
        data = ''
        try:
            data = self.autoconsumo.CAU.text
        except AttributeError:
            pass
        return data

    @property
    def seccion_registro(self):
        data = ''
        try:
            data = self.autoconsumo.SeccionRegistro.text
        except AttributeError:
            pass
        return data

    @property
    def sub_seccion(self):
        data = ''
        try:
            data = self.autoconsumo.SubSeccion.text
        except AttributeError:
            pass
        return data

    @property
    def colectivo(self):
        data = ''
        try:
            data = self.autoconsumo.Colectivo.text
        except AttributeError:
            pass
        return data


class DatosSuministro(object):

    def __init__(self, data):
        self.datos_suministro = data

    @property
    def cups(self):
        data = ''
        try:
            data = self.datos_suministro.CUPS.text
        except AttributeError:
            pass
        return data

    @property
    def tipo_cups(self):
        data = ''
        try:
            data = self.datos_suministro.TipoCUPS.text
        except AttributeError:
            pass
        return data

    @property
    def ref_catastro(self):
        data = ''
        try:
            data = self.datos_suministro.RefCatastro.text
        except AttributeError:
            pass
        return data


class DatosInstGen(object):

    def __init__(self, data):
        self.datos_inst_gen = data

    @property
    def cil(self):
        data = ''
        try:
            data = self.datos_inst_gen.CIL.text
        except AttributeError:
            pass
        return data

    @property
    def tec_generador(self):
        data = ''
        try:
            data = self.datos_inst_gen.TecGenerador.text
        except AttributeError:
            pass
        return data

    @property
    def combustible(self):
        data = ''
        try:
            data = self.datos_inst_gen.Combustible.text
        except AttributeError:
            pass
        return data

    @property
    def pot_instalada_gen(self):
        data = ''
        try:
            data = self.datos_inst_gen.PotInstaladaGen.text
        except AttributeError:
            pass
        return data

    @property
    def tipo_instalacion(self):
        data = ''
        try:
            data = self.datos_inst_gen.TipoInstalacion.text
        except AttributeError:
            pass
        return data

    @property
    def esquema_medida(self):
        data = ''
        try:
            data = self.datos_inst_gen.EsquemaMedida.text
        except AttributeError:
            pass
        return data

    @property
    def ssaa(self):
        data = ''
        try:
            data = self.datos_inst_gen.SSAA.text
        except AttributeError:
            pass
        return data

    @property
    def ref_catastro(self):
        data = ''
        try:
            data = self.datos_inst_gen.RefCatastro.text
        except AttributeError:
            pass
        return data

    @property
    def utm(self):
        data = ''
        try:
            data = UTM(self.datos_inst_gen.UTM)
        except AttributeError:
            pass
        return data

    @property
    def titular_representante_gen(self):
        data = ''
        try:
            data = TitularRepresentanteGen(self.datos_inst_gen.TitularRepresentanteGen)
        except AttributeError:
            pass
        return data


class UTM(object):

    def __init__(self, data):
        self.utm = data

    @property
    def x(self):
        data = ''
        try:
            data = self.utm.X.text
        except AttributeError:
            pass
        return data

    @property
    def y(self):
        data = ''
        try:
            data = self.utm.Y.text
        except AttributeError:
            pass
        return data

    @property
    def huso(self):
        data = ''
        try:
            data = self.utm.Huso.text
        except AttributeError:
            pass
        return data

    @property
    def banda(self):
        data = ''
        try:
            data = self.utm.Banda.text
        except AttributeError:
            pass
        return data


class TitularRepresentanteGen(object):

    def __init__(self, data):
        self.titular_representante_gen = data

    @property
    def nombre(self):
        data = ''
        try:
            data = Nombre(self.titular_representante_gen.Nombre)
        except AttributeError:
            pass
        return data

    @property
    def nif(self):
        data = ''
        try:
            data = self.titular_representante_gen.NIF.text
        except AttributeError:
            pass
        return data

    @property
    def telefono(self):
        data = []
        try:
            for telefono in self.titular_representante_gen.Telefono:
                data.append(Telefono(telefono))
        except AttributeError:
            pass
        return data

    @property
    def correo_electronico(self):
        data = ''
        try:
            data = self.titular_representante_gen.CorreoElectronico.text
        except AttributeError:
            pass
        return data

    @property
    def direccion(self):
        data = ''
        try:
            data = Direccion(self.titular_representante_gen.Direccion)
        except AttributeError:
            pass
        return data


class Nombre(object):

    def __init__(self, data):
        self.nombre = data

    @property
    def nombre_de_pila(self):
        data = ''
        try:
            data = self.nombre.NombreDePila.text
        except AttributeError:
            pass
        return data

    @property
    def primer_apellido(self):
        data = ''
        try:
            data = self.nombre.PrimerApellido.text
        except AttributeError:
            pass
        return data

    @property
    def segundo_apellido(self):
        data = ''
        try:
            data = self.nombre.SegundoApellido.text
        except AttributeError:
            pass
        return data

    @property
    def razon_social(self):
        data = ''
        try:
            data = self.nombre.RazonSocial.text
        except AttributeError:
            pass
        return data


class Telefono(object):

    def __init__(self, data):
        self.telefono = data

    @property
    def prefijo_pais(self):
        data = ''
        try:
            data = self.telefono.PrefijoPais.text
        except AttributeError:
            pass
        return data

    @property
    def numero(self):
        data = ''
        try:
            data = self.telefono.Numero.text
        except AttributeError:
            pass
        return data


class Direccion(object):

    def __init__(self, data):
        self.direccion = data

    @property
    def pais(self):
        data = ''
        try:
            data = self.direccion.Pais.text
        except AttributeError:
            pass
        return data

    @property
    def provincia(self):
        data = ''
        try:
            data = self.direccion.Provincia.text
        except AttributeError:
            pass
        return data

    @property
    def municipio(self):
        data = ''
        try:
            data = self.direccion.Municipio.text
        except AttributeError:
            pass
        return data

    @property
    def poblacion(self):
        data = ''
        try:
            data = self.direccion.Poblacion.text
        except AttributeError:
            pass
        return data

    @property
    def cod_postal(self):
        data = ''
        try:
            data = self.direccion.CodPostal.text
        except AttributeError:
            pass
        return data

    @property
    def via(self):
        data = ''
        try:
            data = Via(self.direccion.Via)
        except AttributeError:
            pass
        return data

    @property
    def apartado_de_correos(self):
        data = ''
        try:
            data = self.direccion.ApartadoDeCorreos.text
        except AttributeError:
            pass
        return data


class Via(object):

    def __init__(self, data):
        self.via = data

    @property
    def tipo_via(self):
        data = ''
        try:
            data = self.via.TipoVia.text
        except AttributeError:
            pass
        return data

    @property
    def calle(self):
        data = ''
        try:
            data = self.via.Calle.text
        except AttributeError:
            pass
        return data

    @property
    def numero_finca(self):
        data = ''
        try:
            data = self.via.NumeroFinca.text
        except AttributeError:
            pass
        return data

    @property
    def duplicador_finca(self):
        data = ''
        try:
            data = self.via.DuplicadorFinca.text
        except AttributeError:
            pass
        return data

    @property
    def escalera(self):
        data = ''
        try:
            data = self.via.Escalera.text
        except AttributeError:
            pass
        return data

    @property
    def piso(self):
        data = ''
        try:
            data = self.via.Piso.text
        except AttributeError:
            pass
        return data

    @property
    def puerta(self):
        data = ''
        try:
            data = self.via.Puerta.text
        except AttributeError:
            pass
        return data

    @property
    def tipo_aclarador_finca(self):
        data = ''
        try:
            data = self.via.TipoAclaradorFinca.text
        except AttributeError:
            pass
        return data

    @property
    def aclarador_finca(self):
        data = ''
        try:
            data = self.via.AclaradorFinca.text
        except AttributeError:
            pass
        return data
