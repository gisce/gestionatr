# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from .message import Message
from .Deadlines import ProcessDeadline
from gestionatr.input.messages import except_f1
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
        data = []
        tree = get_rec_attr(self.obj, self._header, False)
        if hasattr(tree, 'DatosSuministro'):
            for datos in tree.DatosSuministro:
                data.append(DatosSuministro(datos))
            return data
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
    def rechazos(self):
        tree = '{0}.Rechazos'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data not in [None, False]:
            return Rechazos(data)
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

    def check_minimum_fields(self):
        checker = MinimumFieldsChecker(self)
        return checker.check()


class Rechazos(object):

    def __init__(self, data):
        self.rechazos = data

    @property
    def fecha_rechazo(self):
        data = ''
        try:
            data = self.rechazos.FechaRechazo.text
        except AttributeError:
            pass
        return data

    @property
    def rechazo(self):
        data = []
        try:
            for rechazo in self.rechazos.Rechazo:
                data.append(Rechazo(rechazo))
        except AttributeError:
            pass
        return data


class Rechazo(object):

    def __init__(self, data):
        self.rechazo = data

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
    def comentarios(self):
        data = ''
        try:
            data = self.rechazo.Comentarios.text
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


class TitularRepresentanteGen(object):

    def __init__(self, data):
        self.titular_representante_gen = data

    @property
    def id_titular(self):
        data = ''
        try:
            data = IdTitular(self.titular_representante_gen.IdTitular)
        except AttributeError:
            pass
        return data

    @property
    def nombre(self):
        data = ''
        try:
            data = Nombre(self.titular_representante_gen.Nombre)
        except AttributeError:
            pass
        return data

    @property
    def telefono(self):
        data = []
        try:
            for telefono in self.titular_representante_gen.Telefono:
                data.append((telefono.PrefijoPais.text, telefono.Numero.text))
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


class IdTitular(object):

    def __init__(self, data):
        self.id_titular = data

    @property
    def tipo_identificador(self):
        data = ''
        try:
            data = self.id_titular.TipoIdentificador.text
        except AttributeError:
            pass
        return data

    @property
    def identificador(self):
        data = ''
        try:
            data = self.id_titular.Identificador.text
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


class Direccion(object):

    def __init__(self, data):
        self.direccion = data

    @property
    def pais(self):
        data = ''
        try:
            data = self.direccion.Pais.text.strip()
        except AttributeError:
            pass
        return data

    @property
    def provincia(self):
        data = ''
        try:
            data = self.direccion.Provincia.text.strip()
        except AttributeError:
            pass
        return data

    @property
    def municipio(self):
        data = ''
        try:
            data = self.direccion.Municipio.text.strip()
        except AttributeError:
            pass
        return data

    @property
    def poblacion(self):
        data = ''
        try:
            data = self.direccion.Poblacion.text.strip()
        except AttributeError:
            pass
        return data

    @property
    def cod_postal(self):
        data = ''
        try:
            data = self.direccion.CodPostal.text.strip()
        except AttributeError:
            pass
        return data

    @property
    def tipo_via(self):
        data = ''
        try:
            data = self.direccion.Via.TipoVia.text.strip()
        except AttributeError:
            try:
                data = self.direccion.TipoVia.text.strip()
            except AttributeError:
                pass
        return data

    @property
    def calle(self):
        data = ''
        try:
            data = self.direccion.Via.Calle.text.strip()
        except AttributeError:
            try:
                data = self.direccion.Calle.text.strip()
            except AttributeError:
                pass
        return data

    @property
    def numero_finca(self):
        data = ''
        try:
            data = self.direccion.Via.NumeroFinca.text.strip()
        except AttributeError:
            try:
                data = self.direccion.NumeroFinca.text.strip()
            except AttributeError:
                pass
        return data

    @property
    def duplicador_finca(self):
        data = ''
        try:
            data = self.direccion.Via.DuplicadorFinca.text.strip()
        except AttributeError:
            try:
                data = self.direccion.DuplicadorFinca.text.strip()
            except AttributeError:
                pass
        return data

    @property
    def escalera(self):
        data = ''
        try:
            data = self.direccion.Via.Escalera.text.strip()
        except AttributeError:
            try:
                data = self.direccion.Escalera.text.strip()
            except AttributeError:
                pass
        return data

    @property
    def piso(self):
        data = ''
        try:
            data = self.direccion.Via.Piso.text.strip()
        except AttributeError:
            try:
                data = self.direccion.Piso.text.strip()
            except AttributeError:
                pass
        return data

    @property
    def puerta(self):
        data = ''
        try:
            data = self.direccion.Via.Puerta.text.strip()
        except AttributeError:
            try:
                data = self.direccion.Puerta.text.strip()
            except AttributeError:
                pass
        return data

    @property
    def tipo_aclarador_finca(self):
        data = ''
        try:
            data = self.direccion.Via.TipoAclaradorFinca.text.strip()
        except AttributeError:
            try:
                data = self.direccion.TipoAclaradorFinca.text.strip()
            except AttributeError:
                pass
        return data

    @property
    def aclarador_finca(self):
        data = ''
        try:
            data = self.direccion.Via.AclaradorFinca.text.strip()
        except AttributeError:
            try:
                data = self.direccion.AclaradorFinca.text.strip()
            except AttributeError:
                pass
        return data

    @property
    def apartado_de_correos(self):
        data = ''
        try:
            data = self.direccion.ApartadoDeCorreos.text.strip()
        except AttributeError:
            pass
        return data


class MinimumFieldsChecker(object):

    def __init__(self, a1):
        self.a1 = a1

    def check(self):
        errors = []

        for field in self.get_minimum_fields(pas=self.a1.pas):
            valid = getattr(self, 'check_{0}'.format(field), None)
            if not valid():
                errors.append(field)
        return errors

    def get_minimum_fields(self, pas='01'):
        if pas == '01':
            return [
                'moviment', 'cau', 'seccio_registre', 'collectiu', 'cups', 'tec_generador',
                'pot_installada_gen', 'tipus_installacio', 'ssaa', 'nom_titular', 'tipus_identificador',
                'identificador', 'telefon', 'pais', 'provincia', 'municipi', 'codi_postal', 'via_or_apartat_correus'
            ]
        elif pas == '02':
            return ['cau']
        else:
            return False

    def check_moviment(self):
        return get_rec_attr(self.a1, "movimiento", False)

    def check_cau(self):
        return get_rec_attr(self.a1, "autoconsumo.cau", False)

    def check_seccio_registre(self):
        return get_rec_attr(self.a1, "autoconsumo.seccion_registro", False)

    def check_collectiu(self):
        return get_rec_attr(self.a1, "autoconsumo.colectivo", False)

    def check_cups(self):
        valid = True
        for datos in self.a1.datos_suministro:
            valid = valid and get_rec_attr(datos, "cups", False)
        return valid

    def check_tec_generador(self):
        valid = True
        for datos in self.a1.datos_inst_gen:
            valid = valid and get_rec_attr(datos, "tec_generador", False)
        return valid

    def check_pot_installada_gen(self):
        valid = True
        for datos in self.a1.datos_inst_gen:
            valid = valid and get_rec_attr(datos, "pot_instalada_gen", False)
        return valid

    def check_tipus_installacio(self):
        valid = True
        for datos in self.a1.datos_inst_gen:
            valid = valid and get_rec_attr(datos, "tipo_instalacion", False)
        return valid

    def check_ssaa(self):
        valid = True
        for datos in self.a1.datos_inst_gen:
            valid = valid and get_rec_attr(datos, "ssaa", False)
        return valid

    def check_nom_titular(self):
        valid = True
        if self.a1.autoconsumo.seccion_registro == '2':
            for datos in self.a1.datos_inst_gen:
                nom = datos.titular_representante_gen.nombre
                check = get_rec_attr(nom, "nombre_de_pila", False) and \
                        get_rec_attr(nom, "primer_apellido", False) or \
                        get_rec_attr(nom, "razon_social", False)
                valid = valid and check
        return valid

    def check_tipus_identificador(self):
        valid = True
        if self.a1.autoconsumo.seccion_registro == '2':
            for datos in self.a1.datos_inst_gen:
                valid = valid and get_rec_attr(datos.titular_representante_gen.id_titular, "tipo_identificador", False)
        return valid

    def check_identificador(self):
        valid = True
        if self.a1.autoconsumo.seccion_registro == '2':
            for datos in self.a1.datos_inst_gen:
                valid = valid and get_rec_attr(datos.titular_representante_gen.id_titular, "identificador", False)
        return valid

    def check_telefon(self):
        valid = True
        if self.a1.autoconsumo.seccion_registro == '2':
            for datos in self.a1.datos_inst_gen:
                telefon = get_rec_attr(datos.titular_representante_gen, "telefono", False)
                if not telefon:
                    return False
                valid = valid and len(telefon) > 0
        return valid

    def check_pais(self):
        valid = True
        if self.a1.autoconsumo.seccion_registro == '2':
            for datos in self.a1.datos_inst_gen:
                direccio = datos.titular_representante_gen.direccion
                valid = valid and get_rec_attr(direccio, "pais", False)
        return valid

    def check_provincia(self):
        valid = True
        if self.a1.autoconsumo.seccion_registro == '2':
            for datos in self.a1.datos_inst_gen:
                direccio = datos.titular_representante_gen.direccion
                valid = valid and get_rec_attr(direccio, "provincia", False)
        return valid

    def check_municipi(self):
        valid = True
        if self.a1.autoconsumo.seccion_registro == '2':
            for datos in self.a1.datos_inst_gen:
                direccio = datos.titular_representante_gen.direccion
                valid = valid and get_rec_attr(direccio, "municipio", False)
        return valid

    def check_codi_postal(self):
        valid = True
        if self.a1.autoconsumo.seccion_registro == '2':
            for datos in self.a1.datos_inst_gen:
                direccio = datos.titular_representante_gen.direccion
                valid = valid and get_rec_attr(direccio, "cod_postal", False)
        return valid

    def check_via_or_apartat_correus(self):
        valid = True
        if self.a1.autoconsumo.seccion_registro == '2':
            for datos in self.a1.datos_inst_gen:
                direccio = datos.titular_representante_gen.direccion
                has_apartado_correos = get_rec_attr(direccio, "apartado_de_correos", False)
                has_via = get_rec_attr(direccio, "tipo_via", False) and \
                          get_rec_attr(direccio, "calle", False) and \
                          get_rec_attr(direccio, "numero_finca", False)
                valid = valid and (has_apartado_correos or has_via)
        return valid
