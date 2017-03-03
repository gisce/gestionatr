# -*- coding: utf-8 -*-
from message import Message
from Deadlines import ProcessDeadline, DeadLine, Workdays, Naturaldays
from gestionatr.utils import get_rec_attr


class C1(Message, ProcessDeadline):
    """Clase que implementa C1."""

    steps = [
        DeadLine('01', Workdays(5), '02'),
        DeadLine('02_activation', Workdays(1), '05'),
        DeadLine('02', Naturaldays(60), '05'),
        DeadLine('05_activation', Workdays(1), '05'),
        DeadLine('08', Workdays(5), '09')
    ]

    # Datos paso 01
    @property
    def datos_solicitud(self):
        tree = '{0}.DatosSolicitud'.format(self._header)
        sol = get_rec_attr(self.obj, tree, False)
        if sol:
            return DatosSolicitud(sol)
        else:
            return False

    @property
    def cliente(self):
        tree = '{0}.Cliente'.format(self._header)
        cli = get_rec_attr(self.obj, tree, False)
        if cli:
            return Cliente(cli)
        else:
            return False

    @property
    def comentarios(self):
        tree = '{0}.Comentarios'.format(self._header)
        com = get_rec_attr(self.obj, tree, False)
        if com:
            return com.text
        else:
            return False

    @property
    def registros_documento(self):
        data = []
        obj = get_rec_attr(self.obj, self._header, False)
        if not hasattr(obj, 'RegistrosDocumento'):
            obj = get_rec_attr(self.obj, 'Rechazos', False)
        if (hasattr(obj, 'RegistrosDocumento') and
                hasattr(obj.RegistrosDocumento, 'RegistroDoc')):
            for d in obj.RegistrosDocumento.RegistroDoc:
                data.append(RegistroDoc(d))
        return data

    # Datos paso 02 aceptacion
    @property
    def datos_aceptacion(self):
        tree = '{0}.DatosAceptacion'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data:
            return DatosAceptacion(data)
        else:
            return False

    @property
    def contrato(self):
        tree = '{0}.Contrato'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data:
            return Contrato(data)
        else:
            return False

    # Datos paso 02 rechazo y paso 4
    @property
    def rechazos(self):
        obj = getattr(self.obj, 'Rechazos')
        data = []
        if obj:
            for i in obj.Rechazo:
                data.append(Rechazo(i))
            return data
        return data

    @property
    def fecha_rechazo(self):
        tree = 'Rechazos.FechaRechazo'
        data = get_rec_attr(self.obj, tree, False)
        if data:
            return data.text
        else:
            return False


class DatosSolicitud(object):

    def __init__(self, data):
        self.datos_solicitud = data

    @property
    def ind_activacion(self):
        data = ''
        try:
            data = self.datos_solicitud.IndActivacion.text
        except AttributeError:
            pass
        return data

    @property
    def fecha_prevista_accion(self):
        data = ''
        try:
            data = self.datos_solicitud.FechaPrevistaAccion.text
        except AttributeError:
            pass
        return data

    @property
    def contratacion_incondicional_ps(self):
        data = ''
        try:
            data = self.datos_solicitud.ContratacionIncondicionalPS.text
        except AttributeError:
            pass
        return data


class Cliente(object):

    def __init__(self, data):
        self.cliente = data

    @property
    def tipo_identificador(self):
        data = ''
        try:
            data = self.cliente.IdCliente.TipoIdentificador.text
        except AttributeError:
            pass
        return data

    @property
    def identificador(self):
        data = ''
        try:
            data = self.cliente.IdCliente.Identificador.text
        except AttributeError:
            pass
        return data

    @property
    def tipo_persona(self):
        data = ''
        try:
            data = self.cliente.IdCliente.TipoPersona.text
        except AttributeError:
            try:
                nom = self.cliente.Nombre.NombreDePila.text
                data = 'F'
            except AttributeError:
                try:
                    nom = self.cliente.Nombre.RazonSocial.text
                    data = 'J'
                except AttributeError:
                    pass
        return data

    @property
    def nombre_de_pila(self):
        data = ''
        try:
            data = self.cliente.Nombre.NombreDePila.text
        except AttributeError:
            pass
        return data

    @property
    def primer_apellido(self):
        data = ''
        try:
            data = self.cliente.Nombre.PrimerApellido.text
        except AttributeError:
            pass
        return data

    @property
    def segundo_apellido(self):
        data = ''
        try:
            data = self.cliente.Nombre.SegundoApellido.text
        except AttributeError:
            pass
        return data

    @property
    def razon_social(self):
        data = ''
        try:
            data = self.cliente.Nombre.RazonSocial.text
        except AttributeError:
            pass
        return data

    @property
    def nombre(self):
        """Nombre completo según sea persona física o jurídica"""
        if self.tipo_persona == 'F':
            nom = '{0}, {1}'.format(
                (' '.join([self.primer_apellido, self.segundo_apellido])).strip(),
                self.nombre_de_pila
            )
        else:
            nom = self.razon_social
        return nom

    @property
    def telfono_numero(self):
        data = ''
        try:
            data = self.cliente.Telefono.Numero.text
        except AttributeError:
            pass
        return data

    @property
    def telfono_prefijo_pais(self):
        data = ''
        try:
            data = self.cliente.Telefono.PrefijoPais.text
        except AttributeError:
            pass
        return data

    @property
    def correo_electronico(self):
        data = ''
        try:
            data = self.cliente.CorreoElectronico.text
        except AttributeError:
            pass
        return data


class RegistroDoc(object):

    def __init__(self, data):
        self.doc = data

    @property
    def tipo_doc_aportado(self):
        data = ''
        try:
            data = self.doc.TipoDocAportado.text
        except AttributeError:
            pass
        return data

    @property
    def direccion_url(self):
        data = ''
        try:
            data = self.doc.DireccionUrl.text
        except AttributeError:
            pass
        return data


class DatosAceptacion(object):

    def __init__(self, data):
        self.datos_aceptacion = data

    @property
    def fecha_aceptacion(self):
        data = ''
        try:
            data = self.datos_aceptacion.FechaAceptacion.text
        except AttributeError:
            pass
        return data

    @property
    def fecha_ultima_lectura_firme(self):
        data = ''
        try:
            data = self.datos_aceptacion.FechaUltimaLecturaFirme.text
        except AttributeError:
            pass
        return data


class Contrato(object):

    def __init__(self, data):
        self.contrato = data

    @property
    def tipo_contrato_atr(self):
        data = ''
        try:
            data = self.contrato.TipoContratoATR.text
        except AttributeError:
            pass
        return data

    @property
    def tipo_activacion_prevista(self):
        data = ''
        try:
            data = self.contrato.TipoActivacionPrevista.text
        except AttributeError:
            pass
        return data

    @property
    def fecha_activacion_prevista(self):
        data = ''
        try:
            data = self.contrato.FechaActivacionPrevista.text
        except AttributeError:
            pass
        return data

    @property
    def tarifa_atr(self):
        data = ''
        try:
            data = self.contrato.CondicionesContractuales.TarifaATR.text
        except AttributeError:
            pass
        return data

    @property
    def modo_control_potencia(self):
        data = ''
        try:
            data = self.contrato.CondicionesContractuales.ModoControlPotencia.text
        except AttributeError:
            pass
        return data

    @property
    def potencias_contratadas(self):
        data = []
        obj = self.contrato.CondicionesContractuales
        if (hasattr(obj, 'PotenciasContratadas') and
                hasattr(obj.PotenciasContratadas, 'Potencia')):
            for d in obj.PotenciasContratadas.Potencia:
                data.append(d.text)
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
