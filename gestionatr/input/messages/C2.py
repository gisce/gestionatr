# -*- coding: utf-8 -*-
from C1 import C1, DatosSolicitud, Contrato, Cliente
from Deadlines import DeadLine, Workdays, Naturaldays
from gestionatr.utils import get_rec_attr


class C2(C1):
    """Clase que implementa C2."""

    steps = [
        DeadLine('01', Workdays(5)),
        DeadLine('02', Workdays(1)),
        DeadLine('03', Naturaldays(30)),
        DeadLine('05', Workdays(1)),
        DeadLine('06', Workdays(1)),
        DeadLine('08', Workdays(5))
    ]

    # Datos paso 01
    @property
    def datos_solicitud(self):
        tree = '{0}.DatosSolicitud'.format(self._header)
        sol = get_rec_attr(self.obj, tree, False)
        if sol not in [None, False]:
            return DatosSolicitud(sol)
        return False

    @property
    def cliente(self):
        tree = '{0}.Cliente'.format(self._header)
        cli = get_rec_attr(self.obj, tree, False)
        if cli not in [None, False]:
            return Cliente(cli)
        else:
            return False

    @property
    def contrato(self):
        tree = '{0}.Contrato'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data not in [None, False]:
            return Contrato(data)
        else:
            return False

    @property
    def medida(self):
        tree = '{0}.Medida'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data not in [None, False]:
            return Medida(data)
        else:
            return False

    @property
    def doc_tecnica(self):
        tree = '{0}.DocTecnica'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data not in [None, False]:
            return DocTecnica(data)
        else:
            return False

    # Datos Paso 03
    @property
    def fecha_prevista_accion(self):
        tree = '{0}.FechaPrevistaAccion'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data:
            return data.text
        else:
            return False

    @property
    def fecha_incidencia(self):
        tree = '{0}.FechaIncidencia'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data:
            return data.text
        else:
            return False

    @property
    def incidencias(self):
        tree = '{0}.Incidencia'.format(self._header)
        obj = get_rec_attr(self.obj, tree, False)
        data = []
        if obj not in [None, False]:
            for i in obj:
                data.append(Incidencia(i))
            return data
        return data

    # Datos paso 13
    @property
    def contestacion_incidencia(self):
        tree = '{0}.ContestacionIncidencia'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data:
            return data.text
        else:
            return False

    @property
    def contacto(self):
        tree = '{0}.Contacto'.format(self._header)
        con = get_rec_attr(self.obj, tree, False)
        if con not in [None, False]:
            return Contacto(con)
        else:
            return False

class DatosSolicitud(DatosSolicitud):

    @property
    def tipo_modificacion(self):
        data = ''
        try:
            data = self.datos_solicitud.TipoModificacion.text
        except AttributeError:
            pass
        return data

    @property
    def tipo_solicitud_administrativa(self):
        data = ''
        try:
            data = self.datos_solicitud.TipoSolicitudAdministrativa.text
        except AttributeError:
            pass
        return data

    @property
    def cnae(self):
        data = ''
        try:
            data = self.datos_solicitud.CNAE.text
        except AttributeError:
            pass
        return data

    @property
    def solicitud_tension(self):
        data = ''
        try:
            data = self.datos_solicitud.SolicitudTension.text
        except AttributeError:
            pass
        return data

    @property
    def tension_solicitada(self):
        data = ''
        try:
            data = self.datos_solicitud.TensionSolicitada.text
        except AttributeError:
            pass
        return data


class Contrato(Contrato):

    @property
    def fecha_finalizacion(self):
        data = False
        try:
            data = self.contrato.FechaFinalizacion.text
        except AttributeError:
            pass
        return data

    @property
    def contacto(self):
        data = ''
        try:
            data = Contacto(self.contrato.Contacto)
        except AttributeError:
            pass
        return data

    @property
    def periodicidad_facturacion(self):
        data = ''
        try:
            data = self.contrato.PeriodicidadFacturacion.text
        except AttributeError:
            try:
                data = self.contrato.CondicionesContractuales.PeriodicidadFacturacion.text
            except:
                pass
        return data

    @property
    def consumo_anual_estimado(self):
        data = ''
        try:
            data = self.contrato.ConsumoAnualEstimado.text
        except AttributeError:
            pass
        return data


class Contacto(object):

    def __init__(self, data):
        self.contacto = data

    @property
    def persona_de_contacto(self):
        data = ''
        try:
            data = self.contacto.PersonaDeContacto.text
        except AttributeError:
            pass
        return data

    @property
    def telefonos(self):
        data = []
        try:
            for tel in self.contacto.Telefono:
                data.append((tel.PrefijoPais.text, tel.Numero.text))
        except AttributeError:
            pass
        return data

    @property
    def correo_electronico(self):
        data = ''
        try:
            data = self.contacto.CorreoElectronico.text
        except AttributeError:
            pass
        return data


class Cliente(Cliente):

    @property
    def indicador_tipo_direccion(self):
        data = ''
        try:
            data = self.cliente.IndicadorTipoDireccion.text
        except AttributeError:
            pass
        return data

    @property
    def direccion(self):
        data = ''
        try:
            data = Direccion(self.cliente.Direccion)
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


class Medida(object):

    def __init__(self, data):
        self.medida = data

    @property
    def propiedad_equipo(self):
        data = ''
        try:
            data = self.medida.PropiedadEquipo.text
        except AttributeError:
            pass
        return data

    @property
    def tipo_equipo_medida(self):
        data = ''
        try:
            data = self.medida.TipoEquipoMedida.text
        except AttributeError:
            pass
        return data

    @property
    def modelos_aparato(self):
        data = []
        obj = self.medida
        if (hasattr(obj, 'ModelosAparato') and
                hasattr(obj.ModelosAparato, 'ModeloAparato')):
            for d in obj.ModelosAparato.ModeloAparato:
                data.append(ModeloAparato(d))
        return data


class ModeloAparato(object):
    def __init__(self, data):
        self.modelo_aparato = data

    @property
    def tipo_aparato(self):
        data = ''
        try:
            data = self.modelo_aparato.TipoAparato.text
        except AttributeError:
            pass
        return data

    @property
    def marca_aparato(self):
        data = ''
        try:
            data = self.modelo_aparato.MarcaAparato.text
        except AttributeError:
            pass
        return data

    @property
    def modelo_marca(self):
        data = ''
        try:
            data = self.modelo_aparato.ModeloMarca.text
        except AttributeError:
            pass
        return data


class DocTecnica(object):

    def __init__(self, data):
        self.doc_tecnica = data

    @property
    def datos_cie(self):
        data = ''
        try:
            data = DatosCie(self.doc_tecnica.DatosCie)
        except AttributeError:
            pass
        return data

    @property
    def datos_apm(self):
        data = ''
        try:
            data = DatosAPM(self.doc_tecnica.DatosAPM)
        except AttributeError:
            pass
        return data


class DatosCie(object):

    def __init__(self, data):
        self.datos_cie = data

    @property
    def cie_papel(self):
        data = ''
        try:
            data = CIEPapel(self.datos_cie.CIEPapel)
        except AttributeError:
            pass
        return data

    @property
    def cie_electronico(self):
        data = ''
        try:
            data = CIEElectronico(self.datos_cie.CIEElectronico)
        except AttributeError:
            pass
        return data

    @property
    def validez_cie(self):
        data = ''
        try:
            data = self.datos_cie.ValidezCIE.text
        except AttributeError:
            pass
        return data


class CIEPapel(object):

    def __init__(self, data):
        self.cie_papel = data

    @property
    def codigo_cie(self):
        data = ''
        try:
            data = self.cie_papel.CodigoCie.text
        except AttributeError:
            pass
        return data

    @property
    def potencia_inst_bt(self):
        data = ''
        try:
            data = self.cie_papel.PotenciaInstBT.text
        except AttributeError:
            pass
        return data

    @property
    def potencia_no_interrumpible(self):
        data = ''
        try:
            data = self.cie_papel.PotenciaNoInterrumpible.text
        except AttributeError:
            pass
        return data

    @property
    def fecha_emision_cie(self):
        data = False
        try:
            data = self.cie_papel.FechaEmisionCie.text
        except AttributeError:
            pass
        return data

    @property
    def fecha_caducidad_cie(self):
        data = False
        try:
            data = self.cie_papel.FechaCaducidadCie.text
        except AttributeError:
            pass
        return data

    @property
    def nif_instalador(self):
        data = ''
        try:
            data = self.cie_papel.NifInstalador.text
        except AttributeError:
            pass
        return data

    @property
    def codigo_instalador(self):
        data = ''
        try:
            data = self.cie_papel.CodigoInstalador.text
        except AttributeError:
            pass
        return data

    @property
    def tension_suministro_cie(self):
        data = ''
        try:
            data = self.cie_papel.TensionSuministroCIE.text
        except AttributeError:
            pass
        return data

    @property
    def tipo_suministro(self):
        data = ''
        try:
            data = self.cie_papel.TipoSuministro.text
        except AttributeError:
            pass
        return data


class CIEElectronico(object):

    def __init__(self, data):
        self.cie_electronico = data

    @property
    def codigo_cie(self):
        data = ''
        try:
            data = self.cie_electronico.CodigoCie.text
        except AttributeError:
            pass
        return data

    @property
    def sello_electronico(self):
        data = ''
        try:
            data = self.cie_electronico.SelloElectronico.text
        except AttributeError:
            pass
        return data


class DatosAPM(object):

    def __init__(self, data):
        self.datos_apm = data

    @property
    def codigo_apm(self):
        data = ''
        try:
            data = self.datos_apm.CodigoApm.text
        except AttributeError:
            pass
        return data

    @property
    def potencia_inst_at(self):
        data = ''
        try:
            data = self.datos_apm.PotenciaInstAT.text
        except AttributeError:
            pass
        return data

    @property
    def fecha_emision_apm(self):
        data = False
        try:
            data = self.datos_apm.FechaEmisionApm.text
        except AttributeError:
            pass
        return data

    @property
    def fecha_caducidad_apm(self):
        data = False
        try:
            data = self.datos_apm.FechaCaducidadApm.text
        except AttributeError:
            pass
        return data

    @property
    def tension_suministro_apm(self):
        data = ''
        try:
            data = self.datos_apm.TensionSuministroAPM.text
        except AttributeError:
            pass
        return data

    @property
    def nif_instalador(self):
        data = ''
        try:
            data = self.datos_apm.NifInstalador.text
        except AttributeError:
            pass
        return data

    @property
    def codigo_instalador(self):
        data = ''
        try:
            data = self.datos_apm.CodigoInstalador.text
        except AttributeError:
            pass
        return data


class Incidencia(object):

    def __init__(self, data):
        self.incidencia = data

    @property
    def secuencial(self):
        data = ''
        try:
            data = self.incidencia.Secuencial.text
        except AttributeError:
            pass
        return data

    @property
    def codigo_motivo(self):
        data = ''
        try:
            data = self.incidencia.CodigoMotivo.text
        except AttributeError:
            pass
        return data

    @property
    def comentarios(self):
        data = ''
        try:
            data = self.incidencia.Comentarios.text
        except AttributeError:
            pass
        return data
