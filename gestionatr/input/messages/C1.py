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
        if sol not in [None, False]:
            return DatosSolicitud(sol)
        else:
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
        if data not in [None, False]:
            return DatosAceptacion(data)
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

    # Datos paso 02 rechazo y paso 04
    @property
    def rechazos(self):
        obj = getattr(self.obj, 'Rechazos')
        data = []
        if obj not in [None, False]:
            for i in obj.Rechazo:
                data.append(Rechazo(i))
            return data
        return data

    @property
    def fecha_rechazo(self):
        tree = '{0}.FechaRechazo'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data:
            return data.text
        else:
            return False

    # Datos paso 05
    @property
    def datos_activacion(self):
        tree = '{0}.DatosActivacion'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data not in [None, False]:
            return DatosActivacion(data)
        else:
            return False

    @property
    def puntos_medida(self):
        data = []
        obj = get_rec_attr(self.obj, self._header, False)
        if (hasattr(obj, 'PuntosDeMedida') and
                hasattr(obj.PuntosDeMedida, 'PuntoDeMedida')):
            for d in obj.PuntosDeMedida.PuntoDeMedida:
                data.append(PuntoDeMedida(d))
        return data

    # Datos paso 06
    @property
    def datos_notificacion(self):
        tree = '{0}.DatosNotificacion'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data not in [None, False]:
            return DatosNotificacion(data)
        else:
            return False

    # Datos paso 09 i 10
    @property
    def fecha_aceptacion(self):
        tree = '{0}.FechaAceptacion'.format(self._header)
        data = get_rec_attr(self.obj, tree, False)
        if data:
            return data.text
        else:
            return False

    # Datos paso 11
    @property
    def fecha_activacion_prevista(self):
        tree = '{0}.FechaActivacionPrevista'.format(self._header)
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
        data = False
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
        data = False
        try:
            data = self.datos_aceptacion.FechaAceptacion.text
        except AttributeError:
            pass
        return data

    @property
    def fecha_ultima_lectura_firme(self):
        data = False
        try:
            data = self.datos_aceptacion.FechaUltimaLecturaFirme.text
        except AttributeError:
            pass
        return data

    @property
    def potencia_actual(self):
        data = ''
        try:
            data = self.datos_aceptacion.PotenciaActual.text
        except AttributeError:
            pass
        return data

    @property
    def actuacion_campo(self):
        data = ''
        try:
            data = self.datos_aceptacion.ActuacionCampo.text
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
        data = False
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
                data.append((int(d.get('Periodo')), int(d.text)))
        return data

    @property
    def cod_contrato(self):
        data = ''
        try:
            data = self.contrato.IdContrato.CodContrato.text
        except AttributeError:
            pass
        return data

    @property
    def tipo_autoconsumo(self):
        data = ''
        try:
            data = self.contrato.TipoAutoconsumo.text
        except AttributeError:
            pass
        return data

    @property
    def periodicidad_facturacion(self):
        data = ''
        try:
            data = self.contrato.CondicionesContractuales.PeriodicidadFacturacion.text
        except AttributeError:
            pass
        return data

    @property
    def tipo_de_telegestion(self):
        data = ''
        try:
            data = self.contrato.CondicionesContractuales.TipodeTelegestion.text
        except AttributeError:
            pass
        return data

    @property
    def marca_medida_con_perdidas(self):
        data = ''
        try:
            data = self.contrato.CondicionesContractuales.MarcaMedidaConPerdidas.text
        except AttributeError:
            pass
        return data

    @property
    def tension_del_suministro(self):
        data = ''
        try:
            data = self.contrato.CondicionesContractuales.TensionDelSuministro.text
        except AttributeError:
            pass
        return data

    @property
    def vas_trafo(self):
        data = ''
        try:
            data = self.contrato.CondicionesContractuales.VAsTrafo.text
        except AttributeError:
            pass
        return data

    @property
    def porcentaje_perdidas(self):
        data = ''
        try:
            data = self.contrato.CondicionesContractuales.PorcentajePerdidas.text
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


class DatosActivacion(object):

    def __init__(self, data):
        self.datos_activacion = data

    @property
    def fecha(self):
        data = False
        try:
            data = self.datos_activacion.Fecha.text
        except AttributeError:
            pass
        return data


class PuntoDeMedida(object):

    def __init__(self, data):
        self.pm = data

    @property
    def cod_pm(self):
        data = ''
        try:
            data = self.pm.CodPM.text
        except AttributeError:
            pass
        return data

    @property
    def tipo_movimiento(self):
        data = ''
        try:
            data = self.pm.TipoMovimiento.text
        except AttributeError:
            pass
        return data

    @property
    def tipo_pm(self):
        data = ''
        try:
            data = self.pm.TipoPM.text
        except AttributeError:
            pass
        return data

    @property
    def cod_pm_principal(self):
        data = ''
        try:
            data = self.pm.CodPMPrincipal.text
        except AttributeError:
            pass
        return data

    @property
    def modo_lectura(self):
        data = ''
        try:
            data = self.pm.ModoLectura.text
        except AttributeError:
            pass
        return data

    @property
    def funcion(self):
        data = ''
        try:
            data = self.pm.Funcion.text
        except AttributeError:
            pass
        return data

    @property
    def direccion_enlace(self):
        data = ''
        try:
            data = self.pm.DireccionEnlace.text
        except AttributeError:
            pass
        return data

    @property
    def direccion_punto_medida(self):
        data = ''
        try:
            data = self.pm.DireccionPuntoMedida.text
        except AttributeError:
            pass
        return data

    @property
    def num_linea(self):
        data = ''
        try:
            data = self.pm.NumLinea.text
        except AttributeError:
            pass
        return data

    @property
    def telefono_telemedida(self):
        data = ''
        try:
            data = self.pm.TelefonoTelemedida.text
        except AttributeError:
            pass
        return data

    @property
    def estado_telefono(self):
        data = ''
        try:
            data = self.pm.EstadoTelefono.text
        except AttributeError:
            pass
        return data

    @property
    def clave_acceso(self):
        data = ''
        try:
            data = self.pm.ClaveAcceso.text
        except AttributeError:
            pass
        return data

    @property
    def tension_pm(self):
        data = ''
        try:
            data = self.pm.TensionPM.text
        except AttributeError:
            pass
        return data

    @property
    def fecha_vigor(self):
        data = False
        try:
            data = self.pm.FechaVigor.text
        except AttributeError:
            pass
        return data

    @property
    def fecha_alta(self):
        data = False
        try:
            data = self.pm.FechaAlta.text
        except AttributeError:
            pass
        return data

    @property
    def fecha_baja(self):
        data = False
        try:
            data = self.pm.FechaBaja.text
        except AttributeError:
            pass
        return data

    @property
    def comentarios(self):
        data = ''
        try:
            data = self.pm.Comentarios.text
        except AttributeError:
            pass
        return data

    @property
    def aparatos(self):
        data = []
        obj = get_rec_attr(self.pm, "Aparatos", False)
        if obj is not None and hasattr(obj, 'Aparato'):
            for d in obj.Aparato:
                data.append(Aparato(d))
        return data


class Aparato(object):

    def __init__(self, data):
        self.aparato = data

    @property
    def tipo_aparato(self):
        data = ''
        try:
            data = self.aparato.ModeloAparato.TipoAparato.text
        except AttributeError:
            pass
        return data

    @property
    def marca_aparato(self):
        data = ''
        try:
            data = self.aparato.ModeloAparato.MarcaAparato.text
        except AttributeError:
            pass
        return data

    @property
    def modelo_marca(self):
        data = ''
        try:
            data = self.aparato.ModeloAparato.ModeloMarca.text
        except AttributeError:
            pass
        return data

    @property
    def tipo_movimiento(self):
        data = ''
        try:
            data = self.aparato.TipoMovimiento.text
        except AttributeError:
            pass
        return data

    @property
    def tipo_equipo_medida(self):
        data = ''
        try:
            data = self.aparato.TipoEquipoMedida.text
        except AttributeError:
            pass
        return data

    @property
    def tipo_propiedad_aparato(self):
        data = ''
        try:
            data = self.aparato.TipoPropiedadAparato.text
        except AttributeError:
            pass
        return data

    @property
    def propietario(self):
        data = ''
        try:
            data = self.aparato.Propietario.text
        except AttributeError:
            pass
        return data

    @property
    def tipo_dhedm(self):
        data = ''
        try:
            data = self.aparato.TipoDHEdM.text
        except AttributeError:
            pass
        return data

    @property
    def modo_medida_potencia(self):
        data = ''
        try:
            data = self.aparato.ModoMedidaPotencia.text
        except AttributeError:
            pass
        return data

    @property
    def lectura_directa(self):
        data = ''
        try:
            data = self.aparato.LecturaDirecta.text
        except AttributeError:
            pass
        return data

    @property
    def cod_precinto(self):
        data = ''
        try:
            data = self.aparato.CodPrecinto.text
        except AttributeError:
            pass
        return data

    @property
    def periodo_fabricacion(self):
        data = ''
        try:
            data = self.aparato.DatosAparato.PeriodoFabricacion.text
        except AttributeError:
            pass
        return data

    @property
    def numero_serie(self):
        data = ''
        try:
            data = self.aparato.DatosAparato.NumeroSerie.text
        except AttributeError:
            pass
        return data

    @property
    def funcion_aparato(self):
        data = ''
        try:
            data = self.aparato.DatosAparato.FuncionAparato.text
        except AttributeError:
            pass
        return data

    @property
    def num_integradores(self):
        data = ''
        try:
            data = self.aparato.DatosAparato.NumIntegradores.text
        except AttributeError:
            pass
        return data

    @property
    def constante_energia(self):
        data = ''
        try:
            data = self.aparato.DatosAparato.ConstanteEnergia.text
        except AttributeError:
            pass
        return data

    @property
    def constante_maximetro(self):
        data = ''
        try:
            data = self.aparato.DatosAparato.ConstanteMaximetro.text
        except AttributeError:
            pass
        return data

    @property
    def ruedas_enteras(self):
        data = ''
        try:
            data = self.aparato.DatosAparato.RuedasEnteras.text
        except AttributeError:
            pass
        return data

    @property
    def ruedas_decimales(self):
        data = ''
        try:
            data = self.aparato.DatosAparato.RuedasDecimales.text
        except AttributeError:
            pass
        return data

    @property
    def medidas(self):
        data = []
        obj = get_rec_attr(self.aparato, "Medidas", False)
        if obj is not None and hasattr(obj, 'Medida'):
            for d in obj.Medida:
                data.append(Medida(d))
        return data


class Medida(object):

    def __init__(self, data):
        self.medida = data

    @property
    def tipo_dhedm(self):
        data = ''
        try:
            data = self.medida.TipoDHEdM.text
        except AttributeError:
            pass
        return data

    @property
    def periodo(self):
        data = ''
        try:
            data = self.medida.Periodo.text
        except AttributeError:
            pass
        return data

    @property
    def magnitud_medida(self):
        data = ''
        try:
            data = self.medida.MagnitudMedida.text
        except AttributeError:
            pass
        return data

    @property
    def procedencia(self):
        data = ''
        try:
            data = self.medida.Procedencia.text
        except AttributeError:
            pass
        return data

    @property
    def ultima_lectura_firme(self):
        data = ''
        try:
            data = self.medida.UltimaLecturaFirme.text
        except AttributeError:
            pass
        return data

    @property
    def fecha_lectura_firme(self):
        data = False
        try:
            data = self.medida.FechaLecturaFirme.text
        except AttributeError:
            pass
        return data

    @property
    def anomalia(self):
        data = ''
        try:
            data = self.medida.Anomalia.text
        except AttributeError:
            pass
        return data

    @property
    def comentarios(self):
        data = ''
        try:
            data = self.medida.Comentarios.text
        except AttributeError:
            pass
        return data


class DatosNotificacion(object):

    def __init__(self, data):
        self.datos_notificacion = data

    @property
    def fecha_activacion(self):
        data = False
        try:
            data = self.datos_notificacion.FechaActivacion.text
        except AttributeError:
            pass
        return data
