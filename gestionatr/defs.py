# -*- coding: utf-8 -*-

# Mapeig de distribuïdores
provincies_arago = ['22', '44', '50']  # Osca, Terol, Saragossa
conv_dict_5 = {
    # ENDESA
    '00311': '0023',  # cia sevillana
    '00313': '0120',  # Aragonesa actividades
    '00315': '0288',  # Balears: Gas y electricidad
    '00316': '0363',  # Unión Eléctrica Canárias SUP
    '02240': '0224',  # Elèctrica de Jafre
    # FENOSA
    '03900': '0022',
}


conv_dict_6 = {'003130': '0029', }  # FECSA Aragó


# Not standarized table. Used in CIE forms
TIPUS_DOCUMENT_INST_CIE = [
    ('nif', 'NIF'),
    ('codigo', 'Código')
]


# For modcon wizard
SEL_CONFIG_MODCON_WIZ_TYPE = [
    ('tarpot', 'Tarifa/potència'),
    ('owner', 'Titular'),
    ('both', u'Ambdós')
]


REPRESENTANT = [('S', 'Substituto'),
                ('M', 'Mandatario')]


PERSONA = [('F', 'Física'),
           ('J', 'Jurídica')]


TARIFES_SEMPRE_MAX = ['003', '011', '012', '013', '014', '015', '016', '017']
TARIFES_6_PERIODES = ['012', '013', '014', '015', '016', '017']


# Data about R101 subtypes and their minimum fields
SUBTYPES_R101 = [
    ({
        'min_fields': ['nif_cliente', 'nombre_cliente',
                       'telefono_contacto', 'cups',
                       'fecha_incidente', 'comentarios',
                       'persona_de_contacto',
                       'tipo_atencion_incorrecta'],
        'code': '001',
        'name': u'ATENCION INCORRECTA',
        'type': '01',
    }),
    ({
        'min_fields': ['nif_cliente', 'nombre_cliente', 'cups',
                       'comentarios'],
        'code': '002',
        'name': u'PRIVACIDAD DE LOS DATOS',
        'type': '01',
    }),
    ({
        'min_fields': ['nif_cliente', 'nombre_cliente',
                       'telefono_contacto', 'cups', 'comentarios',
                       'codigo_incidencia'],
        'code': '003',
        'name': u'INCIDENCIA EN EQUIPOS DE MEDIDA',
        'type': '02',
    }),
    ({
        'min_fields': ['nif_cliente', 'nombre_cliente',
                       'telefono_contacto', 'cups',
                       'fecha_incidente', 'comentarios',
                       'importe_reclamado'],
        'code': '004',
        'name': u'DAÑOS ORIGINADOS POR EQUIPO DE MEDIDA',
        'type': '02',
    }),
    ({
        'min_fields': ['nif_cliente', 'nombre_cliente',
                       'telefono_contacto', 'cups', 'comentarios'],
        'code': '005',
        'name': u'CONTADOR EN FACTURA NO CORRESPONDE CON INSTALADO',
        'type': '02',
    }),
    ({
        'min_fields': ['nif_cliente', 'nombre_cliente', 'cups',
                       'comentarios'],
        'code': '006',
        'name': u'CONTRATOS ATR QUE NO SE FACTURAN',
        'type': '02',
    }),
    ({
        'min_fields': ['nif_cliente', 'nombre_cliente', 'cups',
                       'comentarios', 'num_fact'],
        'code': '007',
        'name': u'CUPS NO PERTENECE A COMERCIALIZADORA O NO VIGENTE'
                u' EN PERIODO DE FACTURA',
        'type': '02',
    }),
    ({
        'min_fields': ['nif_cliente', 'nombre_cliente', 'cups',
                       'comentarios', 'num_fact',
                       'tipo_concepto_facturado'],
        'code': '008',
        'name': u'DISCONFORMIDAD CON CONCEPTOS FACTURADOS',
        'type': '02',
    }),
    ({
        'min_fields': ['nif_cliente', 'nombre_cliente', 'cups',
                       'comentarios', 'num_fact'],
        'code': '009',
        'name': u'DISCONFORMIDAD CON LECTURA FACTURADA',
        'type': '02',
    }),
    ({
        'min_fields': ['nif_cliente', 'nombre_cliente', 'cups',
                       'comentarios', 'num_fact'],
        'code': '010',
        'name': u'DISCONFORMIDAD EN FACTURA ANOMALÍA / FRAUDE',
        'type': '02',
    }),
    ({
        'min_fields': ['nif_cliente', 'nombre_cliente', 'cups',
                       'comentarios', 'num_fact'],
        'code': '011',
        'name': u'RECLAMACIÓN FACTURA PAGO DUPLICADO',
        'type': '02',
    }),
    ({
        'min_fields': ['nif_cliente', 'nombre_cliente', 'cups',
                       'comentarios', 'num_fact'],
        'code': '012',
        'name': u'REFACTURACION NO RECIBIDA',
        'type': '02',
    }),
    ({
        'min_fields': ['nif_cliente', 'cups', 'comentarios',
                       'codigo_de_solicitud'],
        'code': '013',
        'name': u'DISCONFORMIDAD CON CAMBIO DE SUMINISTRADOR',
        'type': '03',
    }),
    ({
        'min_fields': ['nif_cliente', 'nombre_cliente',
                       'telefono_contacto', 'cups',
                       'persona_de_contacto', 'cta_banco'],
        'code': '014',
        'name': u'REQUERIMIENTO DE FIANZA / DEPÓSITO DE GARANTÍA',
        'type': '03',
    }),
    ({
        'min_fields': ['cups', 'codigo_de_solicitud'],
        'code': '015',
        'name': u'RETRASO CORTE DE SUMINISTRO',
        'type': '03',
    }),
    ({
        'min_fields': ['nombre_cliente', 'telefono_contacto', 'comentarios',
                       'sol_nuevos_suministro'],
        'code': '018',
        'name': u'DISCONFORMIDAD CON CRITERIOS ECONÓMICOS / COBROS',
        'type': '04',
    }),
    ({
        'min_fields': ['nombre_cliente', 'telefono_contacto', 'comentarios',
                       'sol_nuevos_suministro'],
        'code': '019',
        'name': u'DISCONFORMIDAD CON CRITERIOS TÉCNICOS / OBRA '
                u'EJECUTADA',
        'type': '04',
    }),
    ({
        'min_fields': ['cups', 'comentarios', 'fecha_desde',
                       'fecha_hasta'],
        'code': '020',
        'name': u'CALIDAD DE ONDA',
        'type': '05',
    }),
    ({
        'min_fields': ['cups', 'comentarios', 'fecha_desde',
                       'fecha_hasta', 'importe_reclamado'],
        'code': '021',
        'name': u'CON PETICIÓN DE INDEMNIZACIÓN',
        'type': '05',
    }),
    ({
        'min_fields': ['cups', 'comentarios', 'fecha_desde',
                       'fecha_hasta'],
        'code': '022',
        'name': u'SIN PETICIÓN DE INDEMNIZACIÓN',
        'type': '05',
    }),
    ({
        'min_fields': ['cups', 'comentarios',
                       'cod_reclam_anterior'],
        'code': '023',
        'name': u'RETRASO EN PAGO INDEMNIZACION',
        'type': '05',
    }),
    ({
        'min_fields': ['comentarios', 'persona_de_contacto',
                       'fecha_desde', 'fecha_hasta',
                       'ubicacion_incidencia'],
        'code': '024',
        'name': u'DAÑOS A TERCEROS POR INSTALACIONES',
        'type': '06',
    }),
    ({
        'min_fields': ['telefono_contacto', 'comentarios',
                       'persona_de_contacto', 'fecha_desde',
                       'fecha_hasta'],
        'code': '025',
        'name': u'IMPACTO AMBIENTAL INSTALACIONES',
        'type': '06',
    }),
    ({
        'min_fields': ['comentarios', 'ubicacion_incidencia'],
        'code': '026',
        'name': u'RECLAMACIONES SOBRE INSTALACIONES',
        'type': '06',
    }),
    ({
        'min_fields': ['cups', 'comentarios'],
        'code': '027',
        'name': u'DISCONFORMIDAD DESCUENTO SERVICIO INDIVIDUAL',
        'type': '07',
    }),
    ({
        'min_fields': ['cups', 'comentarios'],
        'code': '028',
        'name': u'EJECUCIÓN INDEBIDA DE CORTE',
        'type': '07',
    }),
    ({
        'min_fields': ['comentarios', 'cod_reclam_anterior'],
        'code': '029',
        'name': u'RETRASO EN LA ATENCIÓN A RECLAMACIONES',
        'type': '07',
    }),
    ({
        'min_fields': ['comentarios', 'sol_nuevos_suministro'],
        'code': '030',
        'name': u'RETRASO PLAZO DE CONTESTACIÓN NUEVOS SUMINISTROS',
        'type': '07',
    }),
    ({
        'min_fields': ['comentarios', 'sol_nuevos_suministro'],
        'code': '031',
        'name': u'RETRASO PLAZO DE EJECUCIÓN NUEVO SUMINISTRO',
        'type': '07',
    }),
    ({
        'min_fields': ['cups', 'comentarios',
                       'codigo_de_solicitud'],
        'code': '032',
        'name': u'RETRASO REENGANCHE TRAS CORTE',
        'type': '07',
    }),
    ({
        'min_fields': ['nif_cliente', 'nombre_cliente', 'telefono_contacto',
                       'cups', 'importe_reclamado'],
        'code': '033',
        'name': u'POR URGENCIAS',
        'type': '08',
    }),
    ({
        'min_fields': ['cups', 'codigo_de_solicitud',
                       'concepto_contratacion'],
        'code': '034',
        'name': u'DISCONFORMIDAD CON CONCEPTOS DE CONTRATACIÓN '
                u'ATR-PEAJE',
        'type': '03',
    }),
    ({
        'min_fields': ['cups', 'codigo_de_solicitud'],
        'code': '035',
        'name': u'DISCONFORMIDAD RECHAZO SOLICITUD ATR-PEAJE',
        'type': '03',
    }),
    ({
        'min_fields': ['nif_cliente', 'nombre_cliente', 'cups',
                       'comentarios', 'num_fact', 'lectura',
                       'fecha_de_lectura'],
        'code': '036',
        'name': u'PETICIÓN DE REFACTURACIÓN APORTANDO LECTURA',
        'type': '02',
    }),
    ({
        'min_fields': ['cups', 'comentarios'],
        'code': '037',
        'name': u'FICHERO XML INCORRECTO',
        'type': '02',
    }),
    ({
        'min_fields': ['nif_cliente', 'nombre_cliente', 'cups',
                       'comentarios'],
        'code': '038',
        'name': u'PRIVACIDAD DE LOS DATOS',
        'type': '01',
    }),
    ({
        'min_fields': ['cups', 'comentarios', 'fecha_desde',
                       'fecha_hasta'],
        'code': '039',
        'name': u'SOLICITUD DE CERTIFICADO / INFORME DE CALIDAD',
        'type': '05',
    }),
    ({
        'min_fields': ['nif_cliente', 'nombre_cliente', 'cups',
                       'comentarios', 'num_fact'],
        'code': '040',
        'name': u'SOLICITUD DE DUPLICADO DE FACTURA',
        'type': '02',
    }),
    ({
        'min_fields': ['telefono_contacto', 'comentarios',
                       'persona_de_contacto',
                       'ubicacion_incidencia'],
        'code': '041',
        'name': u'SOLICITUD DE ACTUACIÓN SOBRE INSTALACIONES',
        'type': '06',
    }),
    ({
        'min_fields': ['nif_cliente', 'telefono_contacto', 'cups',
                       'comentarios', 'persona_de_contacto'],
        'code': '042',
        'name': u'SOLICITUD DE DESCARGO',
        'type': '06',
    }),
    ({
        'min_fields': ['telefono_contacto', 'cups', 'comentarios',
                       'persona_de_contacto'],
        'code': '043',
        'name': u'PETICIÓN DE PRECINTADO / DESPRECINTADO DE '
                u'EQUIPOS',
        'type': '06',
    }),
    ({
        'min_fields': ['telefono_contacto', 'cups', 'comentarios',
                       'persona_de_contacto'],
        'code': '044',
        'name': u'PETICIONES CON ORIGEN EN CAMPAÑAS DE TELEGESTIÓN',
        'type': '06',
    }),
    ({
        'min_fields': ['cups', 'comentarios'],
        'code': '045',
        'name': u'ACTUALIZACION DIRECCIÓN PUNTO DE SUMINISTRO',
        'type': '03',
    }),
    ({
        'min_fields': ['cups', 'comentarios', 'fecha_desde',
                       'fecha_hasta'],
        'code': '046',
        'name': u'CERTIFICADO DE LECTURA',
        'type': '02',
    }),
    ({
        'min_fields': ['cups', 'comentarios', 'num_fact'],
        'code': '047',
        'name': u'SOLICITUD RECALCULO CCH SIN MODIFICACION '
                u'CIERRE ATR',
        'type': '02',
    }),
    ({
        'min_fields': ['cups', 'comentarios',
                       'codigo_de_solicitud'],
        'code': '048',
        'name': u'PETICIÓN INFORMACIÓN ADICIONAL RECHAZO',
        'type': '03',
    }),
    ({
        'min_fields': ['cups', 'comentarios', 'fecha_desde',
                       'fecha_hasta'],
        'code': '049',
        'name': u'FALTA FICHERO MEDIDA',
        'type': '02',
    }),
    ({
        'min_fields': ['cups', 'comentarios', 'num_factura'],
        'code': '050',
        'name': u'DESACUERDO FACTURACIÓN',
        'type': '09',
    }),
    ({
        'min_fields': ['nif_cliente', 'nombre_cliente', 'telefono_contacto', 'cups', 'comentarios'],
        'code': '051',
        'name': u'CONDUCTA INADECUADA',
        'type': '09',
    }),
    ({
        'min_fields': ['nif_cliente', 'nombre_cliente', 'telefono_contacto', 'cups', 'comentarios'],
        'code': '052',
        'name': u'DISCONFORMIDAD TRABAJOS REALIZADOS',
        'type': '09',
    }),
    ({
        'min_fields': ['telefono_contacto', 'cups', 'comentarios', 'persona_de_contacto'],
        'code': '053',
        'name': u'INCUMPLIMIENTO HORA',
        'type': '09',
    }),
    ({
        'min_fields': ['nombre_cliente', 'telefono_contacto', 'cups', 'fecha_incidente', 'comentarios'],
        'code': '054',
        'name': u'DAÑOS INSPECCIÓN',
        'type': '09',
    }),
    ({
        'min_fields': ['cups', 'comentarios', 'num_fact'],
        'code': '055',
        'name': u'DISCONFORMIDAD SOBRE IMPORTE FACTURADO '
                u'AUTOCONSUMO',
        'type': '02',
    }),
    ({
        'min_fields': ['cups', 'comentarios', 'num_fact'],
        'code': '056',
        'name': u'PETICIÓN DESGLOSE IMPORTE A FACTURAR AUTOCONSUMO',
        'type': '02',
    }),
    ({
        'min_fields': ['nif_cliente', 'nombre_cliente', 'comentarios', 'numero_expediente_fraude'],
        'code': '057',
        'name': u'DISCONFORMIDAD CON EXPEDIENTE DE ANOMALIA Y FRAUDE (sin factura emitida)',
        'type': '02',
    }),
    ({
        'min_fields': ['cups', 'codigo_de_solicitud'],
        'code': '058',
        'name': u'RETRASO EN PLAZO ACEPTACIÓN CAMBIO DE COMERCIALIZADOR',
        'type': '03',
    }),
    ({
        'min_fields': ['cups', 'codigo_de_solicitud'],
        'code': '059',
        'name': u'RETRASO EN PLAZO ACTIVACIÓN CAMBIO DE COMERCIALIZADOR ',
        'type': '03',
    }),
    ({
        'min_fields': ['cups', 'codigo_de_solicitud'],
        'code': '060',
        'name': u'RETRASO EN PLAZO ACEPTACIÓN MODIFICACIÓN CONTRACTUAL',
        'type': '03',
    }),
    ({
        'min_fields': ['cups', 'codigo_de_solicitud'],
        'code': '061',
        'name': u'RETRASO EN PLAZO ACTIVACIÓN MODIFICACIÓN CONTRACTUAL',
        'type': '03',
    }),
    ({
        'min_fields': ['cups', 'codigo_de_solicitud'],
        'code': '062',
        'name': u'RETRASO EN PLAZO ACEPTACIÓN ALTA DE UN NUEVO SUMINISTRO',
        'type': '03',
    }),
    ({
        'min_fields': ['cups', 'codigo_de_solicitud'],
        'code': '063',
        'name': u'RETRASO EN PLAZO ACTIVACIÓN ALTA DE UN NUEVO SUMINISTRO',
        'type': '03',
    }),
    ({
        'min_fields': ['cups', 'codigo_de_solicitud'],
        'code': '064',
        'name': u'RETRASO EN PLAZO ACEPTACIÓN DE UNA BAJA DE UN SUMINISTRO',
        'type': '03',
    }),
    ({
        'min_fields': ['cups', 'codigo_de_solicitud'],
        'code': '065',
        'name': u'RETRASO EN PLAZO ACTIVACIÓN BAJA DE UN SUMINISTRO',
        'type': '03',
    }),
    ({
        'min_fields': ['cups', 'codigo_de_solicitud', 'concepto_contratacion'],
        'code': '066',
        'name': u'INFORMACIÓN/VALIDACIÓN SOBRE DATOS DEL CONTRATO ATR/PEAJE',
        'type': '03',
    }),
    ({
        'min_fields': ['telefono_contacto', 'cups', 'comentarios', 'persona_de_contacto', ],
        'code': '067',
        'name': u'VERIFICACIÓN DE CONTADOR',
        'type': '02',
    }),
    ({
        'min_fields': ['nif_cliente', 'nombre_cliente', 'cups', 'comentarios', 'num_fact'],
        'code': '068',
        'name': u'RECLAMACIÓN POR APLICACIÓN DEL FACTOR DE CONVERSIÓN O EL PCS',
        'type': '02',
    }),
    ({
        'min_fields': ['cups', 'comentarios', 'num_fact'],
        'code': '069',
        'name': u'COPIA F1 EN PDF',
        'type': '02',
    }),
    ({
        'min_fields': ['comentarios', 'cod_reclam_anterior'],
        'code': '070',
        'name': u'RETRASO EN LA ATENCIÓN A RECLAMACIONES NO SUJETAS A ATENCIÓN REGLAMENTARIA',
        'type': '01',
    }),
({
        'min_fields': ['cups', 'codigo_de_solicitud'],
        'code': '071',
        'name': u'RETRASO EN PLAZO ACEPTACIÓN DESISTIMIENTO',
        'type': '03',
    }),
({
        'min_fields': ['cups', 'codigo_de_solicitud'],
        'code': '072',
        'name': u'RETRASO EN PLAZO ACTIVACIÓN DESISTIMIENTO',
        'type': '03',
    }),
({
        'min_fields': ['nif_cliente', 'nombre_cliente', 'telefono_contacto', 'cups', 'comentarios',],
        'code': '073',
        'name': u'PARÁMETROS DE COMUNICACIÓN',
        'type': '02',
    }),
({
        'min_fields': ['cups', 'codigo_de_solicitud', 'cod_reclam_anterior'],
        'code': '074',
        'name': u'RETRASO PLAZO ACEPTACIÓN ANULACIÓN',
        'type': '03',
    }),
    ({
        'min_fields': [],
        'code': '100',
        'name': u'INCIDENCIAS CONTRATACIÓN BONO SOCIAL',
        'type': '03',
    }),
    ({
        'min_fields': [],
        'code': '101',
        'name': u'DATOS BANCARIOS/FORMA DE PAGO ERRÓNEA',
        'type': '02',
    }),
    ({
        'min_fields': [],
        'code': '102',
        'name': u'ERRORES EN COBROS/ ABONOS',
        'type': '02',
    }),
    ({
        'min_fields': [],
        'code': '103',
        'name': u'DISCONFORMIDAD PRECIOS FACTURADOS O REPERCUTIDOS POR LA COMERCIALIZADORA',
        'type': '02',
    }),
    ({
        'min_fields': [],
        'code': '104',
        'name': u'DISCONFORMIDAD FRACCIONAMIENTO O GASTOS ESPECIALES COBRADOS',
        'type': '02',
    }),
    ({
        'min_fields': [],
        'code': '105',
        'name': u'DISCONFORMIDAD CON EL RECOBRO',
        'type': '02',
    }),
    ({
        'min_fields': [],
        'code': '106',
        'name': u'DISCONFORMIDAD CON PENALIZACIÓN POR PRONTA RESOLUCIÓN',
        'type': '03',
    }),
    ({
        'min_fields': [],
        'code': '107',
        'name': u'INSUFICIENTE INFORMACIÓN EN EL MOMENTO DE LA CONTRATACIÓN (Condiciones contractuales, derecho de desistimiento)',
        'type': '03',
    }),
    ({
        'min_fields': [],
        'code': '108',
        'name': u'RECLAMACION  RESPECTO AL DERECHO DE DESISTIMIENTO',
        'type': '03',
    }),
    ({
        'min_fields': [],
        'code': '109',
        'name': u'FACTURACION DE OTROS SERVICIOS TRAS LA CANCELACIÓN DEL SUMINISTRO',
        'type': '02',
    }),
    ({
        'min_fields': [],
        'code': '110',
        'name': u'FALTA DE CLARIDAD EN LAS FACTURAS ',
        'type': '02',
    }),
    ({
        'min_fields': [],
        'code': '111',
        'name': u'FALTA DE CLARIDAD CONDICIONES CONTRACTUALES',
        'type': '03',
    }),
    ({
        'min_fields': [],
        'code': '112',
        'name': u'DIFICULTAD EN LA CONTRATACIÓN DE LA TUR/PVPC CON EL CUR/COR',
        'type': '03',
    }),
    ({
        'min_fields': [],
        'code': '113',
        'name': u'RECLAMACIONES POR PRACTICAS COMERCIALES INCORRECTAS',
        'type': '03',
    }),
    ({
        'min_fields': [],
        'code': '114',
        'name': u'RETRASO EN FACTURACIÓN COMERCIALIZADOR',
        'type': '03',
    }),
]

SUBTYPES_R1_ATC = [(x['code'], x['name']) for x in SUBTYPES_R101]


# TABLES
TABLA_3 = [
    ('01', 'Envío información sobre autoconsumo desde CCAA a Distribuidor'),
    ('02', 'Envío información sobre autoconsumo desde Distribuidor a CCAA'),
]

TABLA_6 = [
    ('NI', 'NIF'),
    ('NV', 'N.I.V.A'),
    ('OT', 'Otro'),
    ('PS', 'Pasaporte'),
    ('NE', 'NIE')
]
TIPUS_DOCUMENT = TABLA_6

TABLA_7 = [
    ('S', u"(S) La solicitud de modificación contractual es únicamente de tipo "
          u"administrativa"),
    ('N', u"(N) La solicitud de modificación contractual es únicamente de "
          u"modificaciones técnicas"),
    ('A', u"(A) La solicitud de modificación contractual implica cambios "
          u"técnicos y administrativos")
]

TABLA_8_OLD = [('S', 'Según ciclo de lectura'),
               ('N', 'Al cabo de 15 días (plazo legal)')]

TABLA_8 = [('A', u"La activación se debe producir cuanto antes"),
           ('L', u"La activación se debe producir con próxima lectura del "
                 u"ciclo"),
           ('F', u"La activación se producirá según la fecha fija solicitada")]

TABLA_9 = [('01', 'Anual'),
           ('02', 'Eventual medido'),
           ('03', 'Temporada'),
           ('05', 'Suministro Régimen especial'),
           ('07', 'Suministro de Obras'),
           ('08', 'Suministro de Socorro'),
           ('09', 'Eventual a tanto alzado'),
           ('10', 'Pruebas'),
           ('11', 'Duplicado'),
           ('12', 'De reserva')]

TABLA_10 = [('01', u"Cese Actividad"),
            ('02', u"Fin de contrato de energía"),
            ('03', u"Corte de suministro"),
            ('04', u"Baja por impago")]

TABLA_11 = [('S', u"(S) Si el domicilio fiscal coincide "
                  u"con el de suministro"),
            ('F', u"(F) Si el domicilio fiscal no coincide "
                  u"con el de suministro")]

TABLA_12 = [
    ('AC', 'Acceso'),
    ('AD', 'Aldea'),
    ('AF', 'Afueras'),
    ('AG', 'Agrupación'),
    ('AL', 'Alameda'),
    ('AR', 'Arrabal'),
    ('AU', 'Autopista / Autovía'),
    ('AV', 'Avenida'),
    ('BC', 'Barranco'),
    ('BD', 'Barriada'),
    ('BL', 'Bloque'),
    ('BO', 'Barrio'),
    ('CA', 'Colonia'),
    ('CF', 'Callejón'),
    ('CH', 'Chalet'),
    ('CI', 'Carril'),
    ('CJ', 'Calleja'),
    ('CL', 'Calle'),
    ('CM', 'Complejo'),
    ('CN', 'Camino'),
    ('CO', 'Cooperativa'),
    ('CR', 'Carretera'),
    ('CS', 'Casa'),
    ('CT', 'Cuesta'),
    ('DI', 'Diseminado extrarradio'),
    ('ED', 'Edificio'),
    ('EN', 'Entrada'),
    ('FC', 'Finca'),
    ('FI', 'Ficticio'),
    ('GL', 'Glorieta'),
    ('GR', 'Grupo'),
    ('LG', 'Lugar'),
    ('MA', 'Masía'),
    ('MU', 'Muelle'),
    ('MZ', 'Manzana'),
    ('NU', 'Núcleo'),
    ('OV', 'Otros'),
    ('PA', 'Parque'),
    ('PB', 'Poblado'),
    ('PD', 'Partida'),
    ('PE', 'Paseo'),
    ('PI', 'Políg.industrial'),
    ('PJ', 'Paraje'),
    ('PL', 'Pantalan'),
    ('PO', 'Polígono'),
    ('PQ', 'Parque'),
    ('PR', 'Prolongación'),
    ('PS', 'Pasaje'),
    ('PT', 'Plazoleta'),
    ('PY', 'Playa'),
    ('PZ', 'Plaza'),
    ('RA', 'Rambla'),
    ('RD', 'Ronda'),
    ('RS', 'Residencial'),
    ('SD', 'Senda'),
    ('TR', 'Travesía'),
    ('UR', 'Urbanización'),
    ('VI', 'Vial'),
    ('ZN', 'Zona'),
]
TIPO_VIA = TABLA_12

# TABLA_13 ESCALERA Optional , thus not implemented

# TABLA_14 PISO Optional , thus not implemented

# TABLA_15 PUERTA Optional , thus not implemented

# TABLA_16 ACLARADOR DE FINCA Optional , thus not implemented

TABLA_17 = [
    ('001', '2.0A'),
    ('003', '3.0A'),
    ('004', '2.0DHA'),
    ('005', '2.1A'),
    ('006', '2.1DHA'),
    ('007', '2.0DHS'),
    ('008', '2.1DHS'),
    ('011', '3.1A'),
    ('012', '6.1A'),
    ('013', '6.2'),
    ('014', '6.3'),
    ('015', '6.4'),
    ('016', '6.5'),
    ('017', '6.1B'),
]

TABLA_20 = [
    ('C', 'Cliente'),
    ('D', 'Distribuidor'),
]

TABLA_22 = [
    ('L00', 'El que corresponda Reglamentariamente'),
    ('L01', 'Tipo 1'),
    ('L02', 'Tipo 2'),
    ('L03', 'Tipo 3'),
    ('L04', 'Tipo 4 - 6 períodos'),
    ('L05', 'Tipo 4 - horario'),
    ('L06', 'Tipo 5 - un período'),
    ('L07', 'Tipo 5- dos períodos'),
    ('L08', 'Tipo 5 - seis períodos'),
    ('L09', 'Tipo 5 - horario'),
    ('L10', 'Tipo 4 - transitorio'),
    ('R00', 'Sin discriminación horaria'),
    ('R01', 'Sin contador discriminador'),
    ('R02', 'Dos períodos'),
    ('R03', 'Tres períodos, sin discriminación de sábados y festivos'),
    ('R04', 'Tres períodos, con discriminación de sábados y festivos'),
    ('R05', 'Cinco períodos'),
    ('R06', 'Seis períodos'),
    ('R07', 'Siete períodos'),
]
TIPO_EM_APARATO = TABLA_22

TABLA_23 = [
    ('S', 'Suministro'),
    ('F', 'Fiscal'),
    ('O', 'Otra'),
]

TABLA_24 = [
    ('BP', 'Bloque pruebas'),
    ('CA', 'Contador activa'),
    ('CC', 'Contador combinado'),
    ('CG', 'Contador registrador'),
    ('CO', 'Contactor'),
    ('CR', 'Contador reactiva'),
    ('TG', 'Contador de telegestión'),
    ('CT', 'Contador tarifador'),
    ('IH', 'Interruptor horario'),
    ('IP', 'I.C.P.'),
    ('MO', 'Modem'),
    ('P', 'Contador rpm'),
    ('RG', 'Registrador'),
    ('RT', 'Relé selector tensión'),
    ('TA', 'Tarifador'),
    ('TC', 'Transformador combinado'),
    ('TI', 'Transformador intensidad'),
    ('TP', 'Transformador potencia'),
    ('TT', 'Transformador de tensión')
]
TIPO_APARATO = TABLA_24


TABLA_25 = [
    ('001', 'AB'),
    ('002', 'ABB'),
    ('003', 'ITRON'),
    ('004', 'AEG'),
    ('005', 'AEMSA'),
    ('006', 'AGORRIA'),
    ('007', 'AGS'),
    ('008', 'AGUT'),
    ('009', 'ALSTHOM'),
    ('010', 'ARON'),
    ('011', 'ARTECHE'),
    ('012', 'ASEA'),
    ('013', 'BAER'),
    ('014', 'BALTEAV'),
    ('015', 'BARBERG'),
    ('016', 'BERGMAN'),
    ('017', 'BK'),
    ('018', 'BRINER'),
    ('019', 'BROW BOVERI'),
    ('020', 'CDC/SCH'),
    ('021', 'CELSA'),
    ('022', 'CEPED'),
    ('023', 'CHAMON'),
    ('024', 'CHASSERAL'),
    ('025', 'CIAMA'),
    ('026', 'CIRCUTOR'),
    ('027', 'COMPACT MODEM GSM'),
    ('028', 'CONTIMETER'),
    ('029', 'DAG'),
    ('031', 'DIFERENCIAL'),
    ('032', 'DIMACO'),
    ('033', 'DINUY'),
    ('034', 'DOPAS'),
    ('035', 'DYTEMAT (CRADY)'),
    ('036', 'EGA'),
    ('037', 'EGUREN'),
    ('038', 'ELIOP'),
    ('134', 'ENEL'),
    ('039', 'ERICSON'),
    ('040', 'FECHA'),
    ('041', 'FIERRO'),
    ('042', 'FLASH'),
    ('043', 'FTM'),
    ('044', 'FTR'),
    ('045', 'G.E.E.'),
    ('046', 'GALEICO'),
    ('047', 'GALIL'),
    ('048', 'GANZ'),
    ('049', 'GAVE'),
    ('050', 'GEAL'),
    ('051', 'GENERAL ELEC.'),
    ('052', 'GRASSILIN'),
    ('053', 'GUIJARRO HNOS.'),
    ('054', 'HAGER'),
    ('055', 'HARDWARE'),
    ('056', 'HB'),
    ('057', 'HELIOWATT'),
    ('058', 'INDRA'),
    ('059', 'INDRA/TARCON'),
    ('060', 'ISKRA-METREGA (METRELEC)'),
    ('061', 'ISODEL'),
    ('062', 'ISOLUX WAT S.A.'),
    ('063', 'ISSARIA'),
    ('064', 'KAINOS'),
    ('065', 'KAINOTRAF'),
    ('066', 'KLOCKNER MOELLER'),
    ('067', 'KORTING-KANDEN'),
    ('068', 'LABORAT. ELEC.'),
    ('069', 'LANDIS'),
    ('070', 'LANDIS-ESPAÑA'),
    ('071', 'LANDIS/SIEM.METERING'),
    ('072', 'LARRAÑAGA'),
    ('073', 'LATECNO'),
    ('074', 'LAURK'),
    ('075', 'LEGRAND'),
    ('076', 'LEISA'),
    ('077', 'LEMAG'),
    ('078', 'M.M.E.'),
    ('079', 'MEDEX'),
    ('080', 'MERC LIBERALIZ CAPT'),
    ('081', 'MERLIN GERIN'),
    ('082', 'METREGA/ISKRA'),
    ('083', 'METRON'),
    ('084', 'MONTROUGE'),
    ('085', 'NORMA'),
    ('086', 'O.P.U.'),
    ('087', 'OCESA'),
    ('088', 'OCREICON'),
    ('089', 'OERLIKON'),
    ('090', 'ORBIS'),
    ('091', 'P.F.N.'),
    ('092', 'PELEPTRIC'),
    ('093', 'POPPER'),
    ('094', 'QL Y TOC'),
    ('095', 'RIESA (ROMANILLOS)'),
    ('096', 'ROMANILLOS'),
    ('097', 'ROMO'),
    ('098', 'S.C.G.'),
    ('099', 'SABADEL'),
    ('100', 'SACI'),
    ('101', 'SAGEM'),
    ('102', 'SAUTER'),
    ('103', 'SAVIR'),
    ('104', 'SCHLUMBERGER'),
    ('105', 'SIEMENS'),
    ('106', 'SIEMENS METERING'),
    ('107', 'SIFAN'),
    ('108', 'SIMON'),
    ('109', 'SISTELTROM'),
    ('110', 'SISTELTRON/ELECTROMATIC'),
    ('111', 'SKUPP'),
    ('112', 'SODECO'),
    ('113', 'SPRECHER'),
    ('114', 'STOTZ KONTAKT (ABB)'),
    ('115', 'STRONG'),
    ('116', 'SUMASA'),
    ('117', 'TARCON'),
    ('118', 'TAUBE'),
    ('119', 'TELEC'),
    ('120', 'TELEMECANICA'),
    ('121', 'TEMPER'),
    ('122', 'TERASAKI'),
    ('123', 'UNELCO'),
    ('124', 'UNELEC'),
    ('125', 'VAYRIS'),
    ('126', 'WANDLER   BG'),
    ('127', 'WAVECOM'),
    ('128', 'WESTINGHOUSE'),
    ('129', 'WIKERS'),
    ('130', 'XACOM'),
    ('131', 'ZENIT'),
    ('132', 'ZIV'),
    ('133', 'ZURC'),
    ('198', 'VARIOS'),
    ('199', 'DESCONOCIDA'),
]
MARCA_APARATO = TABLA_25

TABLA_26 = [('S', 'Si'), ('N', 'No')]
SINO = TABLA_26

TABLA_27 = [
    ('01', 'No existe Punto de Suministro asociado al CUPS'),
    ('02', 'Inexistencia de Contrato de ATR previo en vigor'),
    ('03', 'NIF-CIF No coincide con el del Contrato en vigor'),
    ('07', 'Tipo de Contrato sin informar o erróneo'),
    ('08', 'Fecha de finalización del Contrato sin informar o no válida'),
    ('09', 'Existencia de sentencia judicial relativa a deuda del cliente'),
    ('11', 'Comercializadora incorrecta'),
    ('12', 'Contrato cortado por impago'),
    ('14', 'Potencia Solicitada mayor que la Potencia Máxima Autorizada en baja tensión'),
    ('15', 'Secuencia de Potencias incorrectas, Pi>Pi+1'),
    ('17', 'Tarifa no válida para la Tensión de Suministro'),
    ('18', 'Equipo nuevo propiedad del Cliente no cumple los criterios de Contratación ATR'),
    ('20', 'Instalación no disponible o ampliación suministro en trámite (Expediente Abierto + Código de Expediente + Motivo de Expediente)'),
    ('21', 'Existencia de Contrato Previo en vigor'),
    ('22', 'Potencia Solicitada mayor que la Potencia Máxima Reconocida de Extensión'),
    ('23', 'CNAE No Informado o no válido'),
    ('26', 'Acceso imposibilitado más de dos veces por causas ajenas a la Distribuidora'),
    ('27', 'Caja ICP no válida o inexistente'),
    ('28', 'Rechazo por Anormalidad'),
    ('29', 'Falta Equipo Cliente'),
    ('31', 'Impedimento del Titular'),
    ('32', 'Suministro Esencial'),
    ('34', 'Cliente no cortable por orden judicial o administrativa'),
    ('35', 'Cliente ya cortado'),
    ('36', 'NIF-CIF Erróneo'),
    ('37', 'Existencia de Solicitud previa en curso A3'),
    ('38', 'Existencia de Solicitud previa en curso C1'),
    ('39', 'Existencia de Solicitud previa en curso C2'),
    ('40', 'Existencia de Solicitud previa en curso M1'),
    ('42', 'No es posible anulación. OT ya en campo o acciones no anulables en una reclamación'),
    ('43', 'No es posible anulación. Solicitud ya activada'),
    ('44', 'Error en las horas de utilización (Eventuales)'),
    ('46', 'Fecha de la operación solicitada con carácter retroactivo'),
    ('47', 'Potencias No Normalizadas en Suministro Trifásico'),
    ('48', 'Potencias No Normalizadas en Suministro Monofásico'),
    ('49', 'Necesario cambio de Tensión Monofásica a Trifásica'),
    ('50', 'Transformadores de medida fuera de rango'),
    ('52', 'Tarifa no válida para Potencias Solicitadas'),
    ('53', 'Necesidad de abrir Expediente de Acometida'),
    ('54', 'No Existe Boletín Eventual'),
    ('55', 'Nuevo Cliente coincide con el Actual'),
    ('56', 'Falta de Datos en Campo 84 en Modificaciones'),
    ('57', 'Falta documentación técnica de baja tensión'),
    ('58', 'Falta teléfono de contacto'),
    ('59', 'Armario / Módulo no válido o inexistente'),
    ('60', 'Instalación incompleta o con elementos no válidos'),
    ('61', 'CGP no válida o inexistente'),
    ('62', 'Actuación Solicitada por Comercializador no acorde con requerimientos Cliente'),
    ('63', 'Potencia Solicitada no puede ser inferior a Potencia de B.I.E. (Suministros en Modo 2 no interrumpibles)'),
    ('64', 'Desconexión no posible técnicamente en Corte'),
    ('65', 'Más de una modificación de potencia en un punto de suministro en menos de 12 meses para el mismo titular del punto de suministro'),
    ('66', 'Suministro telegestionado.'),
    ('67', 'Suministro con maxímetro.'),
    ('68', 'No permitido a comercializadora de ML'),
    ('69', 'El distribuidor no está de acuerdo'),
    ('70', 'Comercializador inhabilitado'),
    ('71', 'Existen varios cont. para el mismo suministro'),
    ('72', 'Contrato en baja'),
    ('73', 'Sum. Con potencia > 15 kW.'),
    ('74', 'Suministro con más  de un contador'),
    ('75', 'Discrepancia entre información de lecturas y número de integradores'),
    ('76', 'Más dígitos que número de ruedas'),
    ('77', 'Lectura menor a ultima real'),
    ('78', 'Consumo excesivo'),
    ('79', 'Periodo de lectura inferior'),
    ('80', 'Suministro con maxímetro y/o reactiva'),
    ('83', 'Pobreza Energética'),
    ('84', 'Reclamación Duplicada'),
    ('85', 'Falta campo obligatorio "xxxx"'),
    ('86', 'Código de Expediente de Acometida Erróneo'),
    ('87', 'Factura inexistente'),
    ('88', 'Factura no telegestionada'),
    ('90', 'Autoconsumo 1 o 2B: Titular del consumo no coincide con el de la instalación'),
    ('91', 'Autoconsumo: Falta solicitud del contrato asociado'),
    ('92', 'Autoconsumo: No coincide la categoría del autoconsumo de la solicitud con el registrado en Distribuidora.'),
    ('93', 'Autoconsumo:  Tipo de autoconsumo no válido.'),
    ('94', 'Autoconsumo: Imposible tramitar solicitud sobre ese suministro'),
    ('95', 'Autoconsumo: Modalidad solicitada no coincide contrato técnico.'),
    ('96', 'Autoconsumo: Potencia contratada mayor a 100kW'),
    ('97', 'Autoconsumo: Potencia contratada menor a la instalada en generación'),
    ('98', 'Autoconsumo: periodo mínimo de permanencia en modalidad de autoconsumo no respetado'),
    ('A1', 'Incidencia no subsanada'),
    ('A2', 'Contrato cortado por el distribuidor'),
    ('A3', 'Instalación peligrosa'),
    ('A4', 'Rechazo a solicitud de la comercializadora'),
    ('A5', 'Potencia superior/inferior al tipo de contrato'),
    ('A6', 'Potencia solicitada difiere de la autorizada'),
    ('A7', 'Fecha de autorización vencida'),
    ('A8', 'Precisa autorización ministerial'),
    ('A9', 'Potencia Solicitada mayor que la Potencia Máxima Autorizada en alta tensión'),
    ('B1', 'Falta documentación técnica de alta tensión'),
    ('B2', 'Rechazo por Fraude contrastado'),
    ('B3', 'Punto de suministro no localizado'),
    ('B4', 'Comercializador fuera de su ámbito geográfico'),
    ('B5', 'Existencia de Solicitud previa en curso B1 (motivo 01)'),
    ('B6', 'Existencia de Solicitud previa en curso B1 (motivo 02)'),
    ('B7', 'Existencia de Solicitud previa en curso B1 (motivo 03)'),
    ('B8', 'Existencia de Solicitud previa en curso B1 (motivo 04)'),
    ('B9', 'Existencia de solicitud de baja por impago en curso no anulable B1 (motivo, 01, 02 (si la COR ha rechazado el traspaso y ya se han iniciado trabajos para dar de baja) 04 o motivo 03 en el proceso de baja del contrato de acceso).'),
    ('C1', 'Concurrencia con cambio de comercializador/Traspaso a la COR. Se prioriza la activación del cambio sobre la baja'),
    ('C2', 'Imposible reenganchar por causas técnicas'),
    ('C3', 'Comercializador en proceso de inhabilitación'),
    ('C4', 'Desconexión no posible técnicamente en Corte por peligrosidad'),
    ('C5', 'No es posible solicitar un cambio/modificación/alta a fecha fija para una fecha > 30 días naturales'),
    ('C6', 'Oposición expresa del titular en campo. Se adjunta documentación.'),
    ('C7', 'Impedimento del Titular. Iniciar si procede, el proceso de fraude'),
    ('C8', 'Rechazo de la suspensión del suministro por concurrencia con baja por impago'),
    ('C9', 'El tipo de activación solicitada no es coherente con el tipo de solicitud'),
    ('D1', 'Suministro acogido a bono social'),
    ('D2', 'No es posible anulación ya que no existe solicitud previa'),
    ('D3', 'No cumple con la potencia normalizada para el PS ni el múltiplo de potencia establecido'),
    ('D4', 'El tipo de tensión solicitada es la que ya tiene el PS.'),
    ('D5', 'Falta documentación según lo establecido en la Ley 12/2017 de las Islas Baleares.'),
    ('D6', 'Identificador del titular del proceso subyacente no coincide con el titular que pretende desistir'),
    ('D7', 'Desistimiento sobre un proceso de contratación en curso'),
    ('D8', 'Desistimiento no posible técnicamente en campo'),
    ('D9', 'Desistimiento no posible por movimiento de contratación posterior'),
    ('E1', 'Código de solicitud de referencia no existe en la distribuidora'),
    ('E2', 'El desistimiento no aplica al proceso subyacente'),
    ('E3', 'Desistimiento solicitado por Persona Jurídica'),
    ('E4', 'Impago Previo'),
    ('E5', 'CUPS sujeto a LOPD'),
    ('E6', 'Modificación del tipo de autoconsumo no permitida. No ha trascurrido un año desde la última modificación.'),
    ('E7', 'Falta acuerdo de reparto/Acuerdo de reparto incorrecto/Faltan coeficientes de reparto en acuerdo'),
    ('E8', 'No recibida información técnica de la CCAA (para BT y <=100kW).'),
    ('E9', 'En el periodo establecido, no se han recibido el resto de solicitudes de modificación del colectivo'),
    ('F1', 'Disconformidad del consumidor a la información sobre autoconsumo'),
    ('F2', 'No existe un alta en autoconsumo previo'),
    ('F3', 'Tipo de autoconsumo no coherente con el esquema de medida'),
    ('F4', 'Tipo de autoconsumo no coherente con el tipo de instalación'),
    ('F5', 'Instalación de >100kW en BT o Instalación en AT'),
    ('G1', 'Sólo se podrá modificar: -el tipo de identificador y el identificador o, -nombre y apellidos (razón social).'),
    ('G2', 'Revisión interior incorrecta, debe aportar documentación técnica posterior a la revisión'),
    ('G3', 'Código solicitud ATR/reclamación anterior inexistente'),
    ('99', 'Otros'),
]

TABLA_28 = [
    ('01', 'Cliente ausente'),
    ('08', 'Cita concertada'),
    ('09', 'Deficiencia subsanable en la instalación'),
    ('10', 'Deficiencia subsanable en EdM'),
    ('11', 'Trabajos pendientes de finalizar'),
    ('12', 'Teléfono de contacto erróneo'),
    ('13', 'El consumidor en campo no quiere la baja por cese de actividad'),
    ('14', 'Pendiente resto solicitudes asociadas al autoconsumo colectivo')
]

TABLA_30 = [
    ('01', u"Punto de medida tipo 1"),
    ('02', u"Punto de medida tipo 2"),
    ('03', u"Punto de medida tipo 3"),
    ('04', u"Punto de medida tipo 4"),
    ('05', u"Punto de medida tipo 5"),
]
TIPUS_PM = TABLA_30


TABLA_31 = [
    ('CX', 'Conexión y precintado'),
    ('MO', 'Montaje'),
    ('RE', 'Reparametrización'),
    ('DX', 'Desconexión'),
]
TIPO_MOVIMIENTO_APARATO = TABLA_31

TABLA_32 = [
    ('1', 'Distribuidor'),
    ('2', 'Cliente'),
    ('3', 'Comercializador'),
    ('4', 'Otros'),
]
TIPO_PROPIEDAD_APARATO = TABLA_32

TABLA_33 = [
    ('C', 'Control'),
    ('M', 'Medición'),
]
FUNCION_APARATO = TABLA_33

TABLA_35 = [
    ('1', 'Sin discriminación horaria'),
    ('2', 'Dos períodos'),
    ('3', 'Tres períodos, sin discriminación de sábados y festivos'),
    ('4', 'Tres períodos, con discriminación de sábados y festivos'),
    ('6', 'Seis períodos'),
    ('8', 'DH Supervalle'),
]
TIPO_DH_APARATO = TABLA_35

TABLA_36 = [('S', 'Lectura no acumulativa'),
            ('N', 'Lectura acumulativa')]

TABLA_37 = [('A', 'Alta'),
            ('B', 'Baja'),
            ('M', 'Modificación')]
TIPUS_MOVIMENT = TABLA_37

TABLA_38 = [('1', 'Lectura local manual'),
            ('2', 'Lectura local optoacoplador'),
            ('3', 'Lectura local puerto serie'),
            ('4', 'Telemedida operativa'),
            ('5', 'Telemedida no operativa')]
MODE_PM = TABLA_38

TABLA_39 = [('1', 'Alta'),
            ('2', 'Baja'),
            ('3', "Tramitación de Alta"),
            ('4', 'Tramitación de Baixa'),
            ('5', 'Tramitación de Modificación')]
ESTAT_PM = TABLA_39

TABLA_40 = [('C', 'Comprobante'),
            ('P', 'Principal'),
            ('R', 'Redundante')]
FUNCIO_PM = TABLA_40

TABLA_41 = [
    ('1', 'Correcto'),
    ('2', 'No probado'),
    ('3', 'Línea telef. fuera servicio'),
    ('4', 'Módem no enlaza'),
    ('5', 'Registrador desprogramado'),
    ('6', 'Falla la dire de enlace'),
    ('7', 'Falla el pto y clave medida'),
    ('8', 'El registrado mide ceros'),
    ('9', 'Otras'),
]
ESTAT_TEL_PM = TABLA_41

TABLA_42 = [
    ('10', 'Totalizador'),
    ('20', 'Totalizador'),
    ('21', 'Punta'),
    ('22', 'Llano+Valle'),
    ('30', 'Totalizador'),
    ('31', 'Punta'),
    ('32', 'Llano'),
    ('33', 'Valle'),
    ('40', 'Totalizador'),
    ('41', 'Punta'),
    ('42', 'Llano'),
    ('43', 'Valle'),
    ('60', 'Totalizador'),
    ('61', 'Período 1'),
    ('62', 'Período 2'),
    ('63', 'Período 3'),
    ('64', 'Período 4'),
    ('65', 'Período 5'),
    ('66', 'Período 6'),
    ('80', 'Totalizador'),
    ('81', 'Punta+Llano'),
    ('82', 'Valle'),
    ('83', 'SuperValle'),
]
PERIODO = TABLA_42


TABLA_43 = [
    ('AE', 'Energía activa entrante'),
    ('AS', 'Energía activa saliente'),
    ('EP', 'Excesos de potencia'),
    ('PM', 'Potencia máxima'),
    ('R1', 'Energía reactiva en cuadrante 1'),
    ('R2', 'Energía reactiva en cuadrante 2'),
    ('R3', 'Energía reactiva en cuadrante 3'),
    ('R4', 'Energía reactiva en cuadrante 4'),
]
MAGNITUD = TABLA_43

TABLA_44 = [
    ('10', u'Telemedida'),
    ('20', u'TPL'),
    ('30', u'Visual'),
    ('31', u'Visual corregida'),
    ('40', u'Estimada'),
    ('50', u'Autolectura'),
    ('60', u'Telegestión'),
    ('99', u'Sin lectura'),
]
PROCEDENCIA = TABLA_44

TABLA_45 = [
    ('01', 'Punto de medida inaccesible'),
    ('02', 'Punta de medida ilocalizable'),
    ('03', 'Presunto fraude'),
    ('04', 'Registrador apagado'),
    ('05', 'Registrador no comunica'),
    ('99', 'Otras anomalías'),
]
ANOMALIA_MESURA = TABLA_45

TABLA_50 = [
    ('1', 'Una sola potencia contratada sin maxímetro'),
    ('2', 'Una sola potencia contratada con maxímetro'),
    ('4', 'Modo 4 con tres maxímetros'),
    ('8', 'Tarifa de 6 máximas'),
]
TIPO_DH_MAX = TABLA_50

TABLA_51 = [('1', 'ICP'), ('2', 'Maxímetro')]
CONTROL_POTENCIA = TABLA_51


TABLA_53 = [
    ('T', 'Cambio de titular por traspaso'),
    ('S', 'Cambio de titular por subrogación'),
    ('A',
     'Cambio datos administrativos (excepto cambio de titular y corrección de datos identificativos del cliente)'),
    ('C', 'Corrección datos que identifican al cliente'),
    ('P', 'La solicitud implica cambio en la periodicidad de la facturación'),
    ('R', 'Modificación acuerdo de reparto de un autoconsumo colectivo')
]

TABLA_55 = [
    ('L0', 'En ciclo de lectura'),
    ('C0', 'Tras actuaciones en campo'),
    ('F0', 'En fecha fija sin actuaciones en campo'),
    ('B1', 'Concurrencia con solicitud baja motivo 01'),
    ('B2', 'Concurrencia con solicitud baja motivo 02'),
    ('B3', 'Concurrencia con solicitud baja motivo 03'),
    ('B4', 'Concurrencia con solicitud baja motivo 04'),
    ('A0', 'Cuanto antes sin actuaciones en campo'),
    ('P0', 'Por incumplimiento del plazo mínimo de preaviso'),
    ('C1', 'Con la activación de la última de las solicitudes de modificación asociadas al colectivo '
           'que reciba el distribuidor '),
    ('T1', 'Concurrencia con Traspaso a la COR')
]
TIPUS_ACTIVACIO = TABLA_55

TABLA_61 = [
    ('01', u'CIE consumo'),
    ('02', u'Acta de Puesta en Marcha'),
    ('03', u'Acta de Inspección'),
    ('04', u'Reclamación'),
    ('05', u'Respuesta a reclamación'),
    ('06', u'Facturas'),
    ('07', u'Otra documentación del cliente'),
    ('08', u'Otros'),
    ('09', u'Acuerdo reparto'),
    ('10', u'CIE generación')
]

TABLA_62 = [
    ('AL', u'Almacén'),
    ('AP', u'Alumbrado publico'),
    ('AS', u'Ascensores'),
    ('AT', u'Antena Telefonía Móvil'),
    ('BA', u'Batería de acumuladores'),
    ('CM', u'Centro de Maniobra y Control'),
    ('EA', u'Escalera-Ascensor'),
    ('ES', u'Escalera'),
    ('FT', u'Fabrica y Talleres sin Riesgo Especifico'),
    ('FV', u'Inst. Fotovoltaica'),
    ('GA', u'Garaje'),
    ('GB', u'Grupo Bombeo, Riego por Goteo'),
    ('HP', u'Loc.Húmedos con Riesgo Corrosión o Polv.'),
    ('IN', u'Nave industrial'),
    ('IT', u'Instalación Temporal en Emplazam.Abierto'),
    ('KC', u'Kioskos / cabinas tfno'),
    ('LB', u'Locales a Baja Temperatura'),
    ('LC', u'Local comercial'),
    ('OF', u'Oficina'),
    ('PC', u'Publica concurrencia'),
    ('RA', u'Refugio o Albergue Agrícola'),
    ('RT', u'Repetidor de Televisión'),
    ('SA', u'Servicios Auxiliares'),
    ('SC', u'Sumtro complementario'),
    ('SE', u'Sumtro eventual'),
    ('SG', u'Servicio general vivienda'),
    ('SM', u'Semáforo'),
    ('SO', u'Sumtro obras'),
    ('TL', u'Telecomunicaciones'),
    ('TR', u'Trastero'),
    ('UF', u'Uso finca'),
    ('UV', u'Usos Varios'),
    ('VI', u'Vivienda'),
]

TABLA_63 = [
    ('A001', u'Programación/parametrización errónea'),
    ('A002', u'Equipo de Medida con conexión errónea'),
    ('A003', u'Equipo de Medida inadecuado a instalación'),
    ('A004', u'Contador averiado'),
    ('A005', u'Transformadores averiados'),
    ('A006', u'Módem averiado/Fallo comunicación'),
    ('A007', u'Error medición fuera de margen'),
    ('A008', u'Programación/parametrización errónea por avería'),
    ('A009', u'Contador no se lee'),
    ('A010', u'Constante contador no corresponde a constante facturación'),
    ('A011', u'Lectura errónea'),
    ('A012', u'Suministro no se factura'),
    ('A013', u'Corriente directa autorizada'),
    ('A014', u'Tarifa/Discriminación horaria mal informada o aplicada'),
    ('F001', u'Corriente directa con contrato'),
    ('F002', u'Corriente directa con contrato (doble acometida)'),
    ('F003', u'Corriente directa sin contrato (sin contador)'),
    ('F004', u'Corriente directa sin contrato (con contador)'),
    ('F005', u'Inversión entrada-salida'),
    ('F006', u'Puente entrada-salida en la misma fase (shunt)'),
    ('F007', u'Puente de tensión aislado/desconectado'),
    ('F008', u'Equipo de medida manipulado'),
    ('F009', u'Conexión de equipo de medida manipulada'),
    ('F010', u'Cambio de placa características de transformadores I/T'),
    ('F011', u'Equipo de medida sustituido sin autorización'),
    ('F012', u'Programación/parametrización alterada'),
    ('F013', u'ICP puenteado o no ajustado a potencia contratada'),
    ('F014', u'Cesión de energía'),
]

TABLA_64 = [
    ('01', u'1X220'),
    ('02', u'1X230'),
    ('03', u'3X380'),
    ('04', u'3X380/220'),
    ('05', u'3X400'),
    ('06', u'3X400/230'),
    ('07', u'1X127'),
    ('08', u'1X133'),
    ('09', u'2X220'),
    ('10', u'2X230'),
    ('11', u'3X220'),
    ('12', u'3X220/127'),
    ('13', u'3X230'),
    ('14', u'3X230/133'),
    ('15', u'5.000'),
    ('16', u'6.000'),
    ('17', u'7.200'),
    ('18', u'8.000'),
    ('19', u'10.000'),
    ('20', u'11.000'),
    ('21', u'12.000'),
    ('22', u'13.000'),
    ('23', u'13.200'),
    ('24', u'15.000'),
    ('25', u'16.500'),
    ('26', u'17.000'),
    ('27', u'20.000'),
    ('28', u'22.000'),
    ('29', u'25.000'),
    ('30', u'26.500'),
    ('31', u'30.000'),
    ('32', u'36.000'),
    ('33', u'44.000'),
    ('34', u'45.000'),
    ('35', u'66.000'),
    ('36', u'110.000'),
    ('37', u'132.000'),
    ('38', u'220.000'),
    ('39', u'400.000'),
    ('40', u'1200'),
    ('41', u'2000'),
    ('42', u'5500'),
    ('43', u'55000'),
    ('44', u'130000'),
    ('45', u'100'),
    ('46', u'150'),
    ('47', u'3x100'),
    ('48', u'3x150/260'),
    ('49', u'3x260'),
    ('99', u'Otra tensión obsoleta'),
]

TABLA_65 = [
    ('ES', u'Estatal'),
    ('AU', u'Autonómico'),
    ('PR', u'Provincial'),
    ('LO', u'Local'),
]

TABLA_73 = [
    ('0010101', 'Se piden disculpas'),
    ('0010201', 'Desacuerdo con la reclamación'),
    ('0010202', 'Improcedente. Se adjunta explicación en comentarios'),
    ('0020101', 'Se modifica estado Cliente Robinson/ Cliente'),
    ('0020102', 'Se indemniza al cliente'),
    ('0020201', 'No consta solicitud previa'),
    ('0020202', 'Ajeno a la distribuidora'),
    ('0020203', 'Improcedente. Se adjunta explicación en comentarios'),
    ('0030101', 'Equipo incorrecto. Incluye equipo desaparecido.'),
    ('0030102', 'Instalación incorrecta. Incluye relación de transformación'),
    ('0030103', 'Lectura errónea'),
    ('0030104', 'Contador parado'),
    ('0030105', 'Error programación EDM'),
    ('0030106', 'ICP inadecuado para la potencia contratada'),
    ('0030107', 'Se normalizar telemedida. Se aportan parámetros'),
    ('0030201', 'Equipo correcto'),
    ('0030202', 'Instalación correcta'),
    ('0030203', 'Histórico de consumos / lecturas coherente.'),
    ('0030204', 'Detectada anomalía en visita'),
    ('0030205', 'Expediente por anomalía en curso'),
    ('0030206', 'Elemento externo responsabilidad de cliente'),
    ('0030207', 'Improcedente. Se adjunta explicación en comentarios'),
    ('0030208', 'Telemedida no obligatoria/ No solicitado modem'),
    ('0030209', 'Telemedida no operativa/ Comunicaciones propiedad del usuario'),
    ('0030301', 'No se localiza al cliente'),
    ('0030302', 'No corresponde a distribuidora.'),
    ('0030303', 'Cliente no aporta información adicional.'),
    ('0030304', 'Acceso denegado'),
    ('0030305', 'Visita anulada por cliente'),
    ('0040101', 'Favorable'),
    ('0040201', 'Desfavorable con explicación de motivos en texto resultado'),
    ('0040202', 'Sin incidencia'),
    ('0040203', 'Incidencia que no justifica daños'),
    ('0040204', 'Trabajos programados que no justifican daños'),
    ('0040205', 'Avería instalación particular cliente'),
    ('0040206', 'Originada por terceros'),
    ('0040207', 'Tiempo de interrupción no justifica pérdida de perecederos'),
    ('0040208', 'Se reitera la respuesta anterior'),
    ('0040209', 'Detectada anomalía en visita'),
    ('0040210', 'Expediente por anomalía en curso'),
    ('0040301', 'Imposible por documentación pendiente por parte del cliente'),
    ('0040302', 'Imposible llegar a un acuerdo'),
    ('0040303', 'Acceso Impedido'),
    ('0040304', 'Cliente ausente'),
    ('0050101', 'Asignamos correctamente y refacturamos'),
    ('0050102', 'informamos correctamente el nº contador (no hay que refacturar)'),
    ('0050103', 'Inversión de contadores'),
    ('0050104', 'Corte realizado por distribuidora'),
    ('0050201', 'El contador es correcto'),
    ('0050202', 'Expediente por anomalía en curso'),
    ('0050203', 'Improcedente. Se adjunta explicación en comentarios'),
    ('0050301', 'No se localiza al cliente'),
    ('0050302', 'Acceso denegado'),
    ('0050303', 'Visita anulada por cliente'),
    ('0060101', 'Error del Sistema'),
    ('0060102', 'Incidencia: datos Concentrador Secundario /Telemedida'),
    ('0060103', 'Modificaciones contractuales pendientes (fuera de plazo)'),
    ('0060104', 'Contador interior'),
    ('0060105', 'Pendiente trabajo domicilio cliente (Facturado. Tarea de cliente realizada)'),
    ('0060201', 'No tomada medida real'),
    ('0060202', 'Modificaciones contractuales pendientes (dentro de plazo)'),
    ('0060203', 'Período legal de facturación'),
    ('0060204', 'Contrato Facturado'),
    ('0060205', 'Pendiente trabajo domicilio cliente (sigue pendiente tarea del cliente)'),
    ('0060206', 'Contrato en baja'),
    ('0060207', 'Contrato con otra comercializadora'),
    ('0060209', 'CUPS no vigente en periodo de factura'),
    ('0060210', 'Expediente por anomalía/fraude en curso'),
    ('0060211', 'Improcedente. Se adjunta explicación en comentarios'),
    ('0070101', 'Se anula factura'),
    ('0070201', 'Facturación correcta. (incluir explicación en campo comentarios)'),
    ('0070202', 'Improcedente. Se adjunta explicación en comentarios'),
    ('0080101', 'Se refactura el concepto reclamado'),
    ('0080102', 'Se refacturan otros conceptos / varios conceptos'),
    ('0080201', 'Conceptos reclamados correctamente facturados (incluir explicación en campo comentarios)'),
    ('0080202', 'ICP no instalado'),
    ('0080203', 'Improcedente. Se adjunta explicación en comentarios'),
    ('0090101', 'Equipo de Medida con acceso y consumo acumulado más de un año se refactura  a un año'),
    ('0090102', 'Se anula estimación'),
    ('0090103', 'Error Lectura Montaje/Desmontaje'),
    ('0090104', 'Error lectura lector'),
    ('0090105', 'Perfil estimado curva de carga en gráfico factura'),
    ('0090106', 'Error en Telemedida / Telegestión'),
    ('0090107', 'No conforme aplicación reactiva'),
    ('0090108', 'Error cargo/abono realizado'),
    ('0090109', 'Se refactura lectura reclamada'),
    ('0090201', 'Equipo de Medida sin acceso más de un año, facturación correcta'),
    ('0090202', 'Consumo correcto  (lectura correcta)'),
    ('0090203', 'Estimación correcta'),
    ('0090204', 'Lectura aportada errónea'),
    ('0090205', 'Consumo acumulado'),
    ('0090206', 'Contador interior'),
    ('0090207', 'Lectura real correcta'),
    ('0090208', 'Perfil estimado curva de carga en gráfico factura'),
    ('0090209', 'Aplicación reactiva correcta'),
    ('0090210', 'Cargo/Abono realizado correcto'),
    ('0090211', 'Improcedente. Se adjunta explicación en comentarios'),
    ('0090301', 'Visita fallida'),
    ('0100101', 'Se refactura'),
    ('0100102', 'Se anula la factura'),
    ('0100201', 'Factura correcta según normativa'),
    ('0100202', 'Expediente en curso'),
    ('0100203', 'Improcedente. Se adjunta explicación en comentarios'),
    ('0110101', 'Se abona el duplicado'),
    ('0110102', 'Se refactura'),
    ('0110103', 'Se anula la factura'),
    ('0110201', 'Factura correcta'),
    ('0110202', 'Improcedente. Se adjunta explicación en comentarios'),
    ('0120101', 'Se refactura'),
    ('0120201', 'Factura ya estaba rectificada'),
    ('0120202', 'No procede la refacturación'),
    ('0120203', 'Improcedente. Se adjunta explicación en comentarios'),
    ('0130101', 'Corregido cambio de suministrador realizado'),
    ('0130201', 'Cambio de suministrador realizado correctamente'),
    ('0130202', 'Improcedente. Se adjunta explicación en comentarios'),
    ('0130203', 'No existe solicitud'),
    ('0140101', 'Se devuelve fianza'),
    ('0140102', 'Se corrige devolución errónea y se reenvía fianza'),
    ('0140201', 'La devolución se efectuó correctamente'),
    ('0140202', 'No procede devolver'),
    ('0140203', 'Improcedente. Se adjunta explicación en comentarios'),
    ('0150101', 'Corte ejecutado'),
    ('0150201', 'Corte ejecutado en plazo'),
    ('0150202', 'Corte ejecutado con retraso imputable a cliente'),
    ('0150203', 'Improcedente. Se adjunta explicación en comentarios'),
    ('0150204', 'No existe solicitud'),
    ('0150301', 'Imputable a cliente'),
    ('0150302', 'Requerimiento de la administración judicial / legal (incluye esencialidad)'),
    ('0180101', 'Se corrigen criterios económicos en presupuesto'),
    ('0180102', 'Se corrige factura emitida (datos de facturación, importe)'),
    ('0180201', 'Factura correcta'),
    ('0180202', 'Criterios económicos correctos'),
    ('0180203', 'Improcedente. Se adjunta explicación en comentarios'),
    ('0190101', 'Se modifican criterios técnicos'),
    ('0190102', 'Se reparan desperfectos/se indemnizan daños'),
    ('0190103', 'Licencia de obra/permisos particulares de obra no solicitados'),
    ('0190104', 'Ejecución incorrecta de obras'),
    ('0190105', 'Asesoramiento técnico erróneo en contestación'),
    ('0190201', 'Criterios técnicos/ejecución obra correctos'),
    ('0190202', 'Petición de suministro no finalizada'),
    ('0190203', 'Plazo correcto'),
    ('0190204', 'Pendiente de documentación del cliente'),
    ('0190205', 'Improcedente. Se adjunta explicación en comentarios'),
    ('0190301', 'Impedido acceso a la instalación por cliente'),
    ('0200101', 'Se corrige calidad de onda (tensión, frecuencia, armónicos e interrupciones)'),
    ('0200201', 'Incidencia con origen ajeno a la red de distribución (tercero y/o propio cliente))'),
    ('0200202', 'Calidad de onda correcta  (tensión, frecuencia,  e interrupciones por actuación protecciones)'),
    ('0200203', 'Nos reiteramos respuesta anterior'),
    ('0200204', 'Expediente por anomalía/fraude en curso'),
    ('0200205', 'Improcedente. Se adjunta explicación en comentarios'),
    ('0210101', 'Favorable'),
    ('0210201', 'Desfavorable con explicación de motivos en texto resultado'),
    ('0210202', 'Sin incidencia'),
    ('0210203', 'Incidencia que no justifica daños'),
    ('0210204', 'Trabajos programados que no justifican daños'),
    ('0210205', 'Avería instalación particular cliente'),
    ('0210206', 'Originada por terceros'),
    ('0210207', 'Tiempo de interrupción no justifica pérdida de perecederos'),
    ('0210208', 'Se actúa de acuerdo a la normativa de calidad individual y zonal vigente'),
    ('0210209', 'Se reitera la respuesta anterior'),
    ('0210210', 'Expediente anomalía/fraude en curso'),
    ('0210211', 'Improcedente. Se adjunta explicación en comentarios'),
    ('0210301', 'Imposible por documentación pendiente por parte del cliente'),
    ('0210302', 'Imposible llegar a un acuerdo'),
    ('0210303', 'Imposible por falta de acceso al cliente'),
    ('0220101', 'Se corrige situación'),
    ('0220201', 'Desfavorable con explicación de motivos en texto resultado'),
    ('0220202', 'Sin incidencia'),
    ('0220203', 'Trabajos programados'),
    ('0220204', 'Avería instalación particular cliente'),
    ('0220205', 'Originada por terceros'),
    ('0220206', 'Se reitera la respuesta anterior'),
    ('0220207', 'No legitimada. Relación extracontractual.'),
    ('0220208', 'Expediente por anomalía/fraude en curso'),
    ('0220209', 'Improcedente. Se adjunta explicación en comentarios'),
    ('0220301', 'Imposible por falta de acceso al cliente'),
    ('0230101', 'Favorable'),
    ('0230201', 'Desfavorable con explicación de motivos en texto resultado'),
    ('0230202', 'No legitimada. Relación extracontractual.'),
    ('0230301', 'Imposible localizar al cliente'),
    ('0240101', 'Favorable. Se corrige o resarcen daños.'),
    ('0240201', 'Desfavorable con explicación de motivos en texto resultado'),
    ('0240202', 'No legitimada. Relación extracontractual.'),
    ('0240203', 'Improcedente. Se adjunta explicación en comentarios'),
    ('0250101', 'Se corrige la situación'),
    ('0250201', 'Instalación correcta'),
    ('0250202', 'No legitimada. Relación extracontractual'),
    ('0250203', 'Instalación ajena a la distribuidora'),
    ('0250204', 'Improcedente. Se adjunta explicación en comentarios'),
    ('0250301', 'Imposible gestionar por faltar datos'),
    ('0260101', 'Corregimos situación'),
    ('0260201', 'Instalación correcta'),
    ('0260202', 'No legitimada. Relación extracontractual'),
    ('0260203', 'Instalación ajena a la distribuidora'),
    ('0260204', 'Expediente por anomalía/fraude en curso'),
    ('0260205', 'Improcedente. Se adjunta explicación en comentarios'),
    ('0270101', 'Se corrige importe y se traslada al comercializador'),
    ('0270102', 'Retraso en facturación CIS/CICE. Se genera factura'),
    ('0270201', 'Cálculo y pago  ICDS correcto'),
    ('0270202', 'Cálculo correcto. No procede el abono'),
    ('0270203', 'Improcedente. Se adjunta explicación en comentarios'),
    ('0280101', 'Se reestablece el suministro'),
    ('0280102', 'Se reestablece el suministro con indemnización'),
    ('0280201', 'Corte correcto por solicitud del comercializador'),
    ('0280202', 'Corte correcto por cualquier motivo reconocido en la normativa vigente'),
    ('0280203', 'No existe corte realizado'),
    ('0280204', 'Improcedente. Se adjunta explicación en comentarios'),
    ('0290101', 'Se indemniza incumplimiento de calidad de atención en próxima factura'),
    ('0290102', 'Se indemniza'),
    ('0290103', 'Pendiente indemnización. No se ha podido conseguir datos necesarios a través de un paso 04. '
                'Contacte con distribuidor'),
    ('0290201', 'Reclamación atendida en plazo'),
    ('0290202', 'Retraso imputable al cliente/ comercializadora'),
    ('0290203', 'Improcedente. Se adjunta explicación en comentarios'),
    ('0300101', 'Se indemniza incumplimiento de calidad de atención en próxima factura'),
    ('0300102', 'Se indemniza incumplimiento de calidad de atención'),
    ('0300103', 'Pendiente indemnización. No se ha podido conseguir datos necesarios a través de un paso 04. '
                'Contacte con distribuidor'),
    ('0300201', 'Solicitud de información NNSS atendida en plazo'),
    ('0300202', 'Improcedente. Se adjunta explicación en comentarios'),
    ('0310101', 'Se indemniza incumplimiento de calidad de atención en próxima factura'),
    ('0310201', 'Ejecución de NNSS atendido en plazo'),
    ('0310102', 'Se indemniza incumplimiento de calidad de atención'),
    ('0310103', 'Pendiente indemnización. No se ha podido conseguir datos necesarios a través de un paso 04. '
                'Contacte con distribuidor'),
    ('0310202', 'Improcedente. Se adjunta explicación en comentarios'),
    ('0320101', 'Se indemniza incumplimiento de calidad de atención en próxima factura'),
    ('0320102', 'Se indemniza incumplimiento de calidad de atención'),
    ('0320103', 'Pendiente indemnización. No se ha podido conseguir datos necesarios a través de un paso 04. '
                'Contacte con distribuidor'),
    ('0320201', 'Reconexión atendida en plazo'),
    ('0320202', 'Incumplimiento por causa imputable al cliente'),
    ('0320203', 'Plazo superado por motivos ajenos a la distribuidora (indicar motivo)'),
    ('0320204', 'Imposible ejecutar reenganche por causa ajena'),
    ('0320205', 'Expediente por anomalía/fraude en curso'),
    ('0320206', 'Improcedente. Se adjunta explicación en comentarios'),
    ('0340101', 'Corregido parámetro'),
    ('0340102', 'Corregido parámetro potencia'),
    ('0340103', 'Corregido parámetro tensión'),
    ('0340104', 'Corregido parámetro tarifa'),
    ('0340105', 'Corregido parámetro caudal'),
    ('0340106', 'Corregido parámetro fecha activación'),
    ('0340107', 'Corregido parámetro dirección'),
    ('0340108', 'Corregido parámetro titular'),
    ('0340201', 'Contratación realizada según solicitud'),
    ('0340202', 'Improcedente. Se adjunta explicación en comentarios'),
    ('0340203', 'No existe solicitud'),
    ('0350101', 'Problema resuelto, reenviar solicitud'),
    ('0350201', 'Solicitud correctamente rechazada'),
    ('0350202', 'Imposible contactar con cliente'),
    ('0350203', 'Deficiencias en la instalación'),
    ('0350204', 'Falta documentación (CIE)'),
    ('0350205', 'Error de formato'),
    ('0350206', 'Datos ATR incoherentes'),
    ('0350207', 'Error en el cliente/NIF'),
    ('0350208', 'Improcedente. Se adjunta explicación en comentarios'),
    ('0350209', 'No existe solicitud'),
    ('0360101', 'Se refactura con lectura aportada'),
    ('0360201', 'Lectura con integradores incorrectos'),
    ('0360202', 'Lectura anterior a la última real'),
    ('0360203', 'El suministro se liquida con curva de carga'),
    ('0360204', 'Periodo ajeno a esa comercializadora'),
    ('0360205', 'Estimación superior a un año'),
    ('0360206', 'Lectura aportada adelantada'),
    ('0360207', 'Lectura aportada errónea'),
    ('0360208', 'Improcedente. Se adjunta explicación en comentarios'),
    ('0370101', 'Se republica fichero'),
    ('0370201', 'Fichero correcto'),
    ('0370202', 'Improcedente. Se adjunta explicación en comentarios'),
    ('0380101', 'Alta / baja cliente Robinson'),
    ('0380201', 'Cliente no consta en la base de datos'),
    ('0380202', 'Improcedente. Se adjunta explicación en comentarios'),
    ('0390101', 'Se envía certificado / informe'),
    ('0390201', 'No existe obligación legal de enviar certificado / informe'),
    ('0390202', 'Sin incidencia'),
    ('0390203', 'Trabajos programados'),
    ('0390204', 'Avería instalación particular cliente'),
    ('0390205', 'Originada por terceros'),
    ('0390206', 'Improcedente. Se adjunta explicación en comentarios'),
    ('0390301', 'No gestionable por falta de datos'),
    ('0400101', 'Se envía duplicado solicitado'),
    ('0400201', 'No es posible enviar duplicado. (motivos en texto resultado)'),
    ('0400202', 'Periodo ajeno a esa comercializadora'),
    ('0400203', 'Improcedente. Se adjunta explicación en comentarios'),
    ('0410101', 'Se corrige la situación'),
    ('0410201', 'Instalación correcta'),
    ('0410202', 'No legitimada. Relación extracontractual'),
    ('0410203', 'Instalación ajena a la distribuidora'),
    ('0410204', 'Expediente por anomalía/ fraude en curso'),
    ('0410205', 'Improcedente. Se adjunta explicación en comentarios'),
    ('0410301', 'No gestionable por falta de datos'),
    ('0410302', 'Imposible por falta de acceso al cliente'),
    ('0420101', 'Solicitud descargo aceptada'),
    ('0420201', 'Solicitud descargo rechazada'),
    ('0420202', 'Instalación ajena a la distribuidora'),
    ('0420203', 'Expediente por anomalía/ fraude en curso'),
    ('0420204', 'Improcedente. Se adjunta explicación en comentarios'),
    ('0430101', 'Se procede al precintado / desprecintado'),
    ('0430201', 'No se procede al precintado / desprecintado'),
    ('0430202', 'Instalación incorrecta'),
    ('0430203', 'Expediente por anomalía/ fraude en curso'),
    ('0430204', 'Improcedente. Se adjunta explicación en comentarios'),
    ('0430301', 'Acceso impedido'),
    ('0430302', 'Cliente ausente'),
    ('0440101', 'Procede, explicación en campo resultado'),
    ('0440201', 'No procede, explicación en campo resultado'),
    ('0450101', 'Dirección actualizada'),
    ('0450201', 'Improcedente. Se adjunta explicación en comentarios'),
    ('0460101', 'Procede'),
    ('0460201', 'Improcedente. Se adjunta explicación en comentarios'),
    ('0470101', 'Se genera curva'),
    ('0470201', 'No existe mejor curva disponible(no se genera curva)'),
    ('0470202', 'Improcedente. Se adjunta explicación en comentarios'),
    ('0480101', 'Aclaración enviada'),
    ('0480201', 'No existe rechazo'),
    ('0480202', 'Improcedente. Se adjunta explicación en comentarios'),
    ('0480203', 'No existe solicitud'),
    ('0490101', 'Enviado fichero'),
    ('0490201', 'No existe fichero'),
    ('0490202', 'Improcedente. Se adjunta explicación en comentarios'),
    ('0550101', 'Se corrige facturación autoconsumo'),
    ('0550201', 'No existe autoconsumo asociado al CUPS'),
    ('0550202', 'Factura autoconsumo correcta. Se adjunta desglose'),
    ('0550203', 'Improcedente. Se adjunta explicación en comentarios'),
    ('0560101', 'Se envía desglose de importes facturados autoconsumo'),
    ('0560201', 'No existe autoconsumo asociado al CUPS'),
    ('0560202', 'Improcedente. Se adjunta explicación en comentarios'),
    ('0570101', 'Expediente anulado'),
    ('0570102', 'Expediente rectificado'),
    ('0570103', 'El cliente aporta documentación que justifica suministro sin actividad'),
    ('0570104', 'Error en periodo de recuperación'),
    ('0570105', 'Retraso en contratación con nuevo titular distinto del titular del expediente.'),
    ('0570201', 'Expediente correcto según normativa'),
    ('0570202', 'La distribuidora aporta prueba que justifican el expediente abierto'),
    ('0570203', 'No regularizado por impedimento del cliente'),
    ('0570204', 'El cliente no aporta documentación que justifica suministro sin actividad'),
    ('0570205', 'Improcedente. Se adjunta explicación en comentarios'),
    ('0580101', 'Se gestiona la publicación del paso'),
    ('0580102', 'Movimiento realizado fuera de plazo'),
    ('0580201', 'No existe solicitud'),
    ('0580202', 'Movimiento realizado en plazo'),
    ('0580203', 'Improcedente. Se adjunta explicación en comentarios'),
    ('0590101', 'Se gestiona la publicación del paso'),
    ('0590102', 'Movimiento realizado fuera de plazo'),
    ('0590201', 'No existe solicitud'),
    ('0590202', 'Movimiento realizado en plazo'),
    ('0590203', 'Movimiento fuera de plazo imputable al cliente'),
    ('0590204', 'Improcedente. Se adjunta explicación en comentarios'),
    ('0600101', 'Se gestiona la publicación del paso'),
    ('0600102', 'Movimiento realizado fuera de plazo'),
    ('0600201', 'No existe solicitud'),
    ('0600202', 'Movimiento realizado en plazo'),
    ('0600203', 'Improcedente. Se adjunta explicación en comentarios'),
    ('0610101', 'Se gestiona la publicación del paso'),
    ('0610102', 'Movimiento realizado fuera de plazo'),
    ('0610201', 'No existe solicitud'),
    ('0610202', 'Movimiento realizado en plazo'),
    ('0610203', 'Movimiento fuera de plazo imputable al cliente'),
    ('0610204', 'Improcedente. Se adjunta explicación en comentarios'),
    ('0620101', 'Se gestiona la publicación del paso'),
    ('0620102', 'Movimiento realizado fuera de plazo'),
    ('0620201', 'No existe solicitud'),
    ('0620202', 'Movimiento realizado en plazo'),
    ('0620203', 'Improcedente. Se adjunta explicación en comentarios'),
    ('0630101', 'Se gestiona la publicación del paso'),
    ('0630102', 'Movimiento realizado fuera de plazo'),
    ('0630103', 'Se indemniza incumplimiento de calidad de atención en próxima factura'),
    ('0630104', 'Se indemniza incumplimiento de calidad de atención'),
    ('0630105', 'Pendiente indemnización. No se ha podido conseguir datos necesarios a través de un paso 04. '
                'Contacte con distribuidor'),
    ('0630201', 'No existe solicitud'),
    ('0630202', 'Movimiento realizado en plazo'),
    ('0630203', 'Movimiento fuera de plazo imputable al cliente'),
    ('0630204', 'Improcedente. Se adjunta explicación en comentarios'),
    ('0640101', 'Se gestiona la publicación del paso'),
    ('0640102', 'Movimiento realizado fuera de plazo'),
    ('0640201', 'No existe solicitud'),
    ('0640202', 'Movimiento realizado en plazo'),
    ('0640203', 'Improcedente. Se adjunta explicación en comentarios'),
    ('0650101', 'Se gestiona la publicación del paso'),
    ('0650102', 'Movimiento realizado fuera de plazo'),
    ('0650201', 'No existe solicitud'),
    ('0650202', 'Movimiento realizado en plazo'),
    ('0650203', 'Movimiento fuera de plazo imputable al cliente'),
    ('0650204', 'Improcedente. Se adjunta explicación en comentarios'),
    ('0660101', 'Corregido parámetro'),
    ('0660102', 'Corregido parámetro potencia'),
    ('0660103', 'Corregido parámetro tensión'),
    ('0660104', 'Corregido parámetro tarifa'),
    ('0660105', 'Corregido parámetro caudal'),
    ('0660106', 'Corregido parámetro fecha activación'),
    ('0660107', 'Corregido parámetro dirección'),
    ('0660108', 'Corregido parámetro titular'),
    ('0660201', 'Contratación realizada según solicitud'),
    ('0660202', 'Improcedente. Se adjunta explicación en comentarios'),
    ('0670101', 'Equipo incorrecto. Incluye equipo desaparecido.'),
    ('0670102', 'Instalación incorrecta. Incluye relación de transformación'),
    ('0670103', 'Lectura errónea'),
    ('0670104', 'Contador parado'),
    ('0670105', 'Error programación EDM'),
    ('0670106', 'ICP inadecuado para la potencia contratada'),
    ('0670201', 'Equipo correcto'),
    ('0670202', 'Instalación correcta'),
    ('0670203', 'Histórico de consumos / lecturas coherente.'),
    ('0670204', 'Detectada anomalía en visita'),
    ('0670205', 'Expediente por anomalía en curso'),
    ('0670206', 'Elemento externo responsabilidad de cliente'),
    ('0670207', 'Improcedente. Se adjunta explicación en comentarios'),
    ('0670301', 'No se localiza al cliente'),
    ('0670302', 'No corresponde a distribuidora. No realiza verificaciones'),
    ('0670303', 'Cliente no aporta información adicional.'),
    ('0670304', 'Acceso denegado'),
    ('0670305', 'Visita anulada por cliente'),
    ('0690101', 'Procedente. Se envía copia del F1 en PDF.'),
    ('0690201', 'Improcedente. Se adjunta explicación en comentarios.'),
    ('0700101', 'Procedente. Se agiliza trámite de reclamación.'),
    ('0700201', 'Retraso imputable al cliente/comercializador'),
    ('0700202', 'Improcedente. Se adjunta explicación en comentarios.'),
    ('0710101', 'Se gestiona la publicación del paso'),
    ('0710102', 'Movimiento realizado fuera de plazo'),
    ('0710201', 'No existe solicitud'),
    ('0710202', 'Movimiento realizado en plazo'),
    ('0710203', 'Improcedente. Se adjunta explicación en comentarios'),
    ('0720101', 'Se gestiona la publicación del paso'),
    ('0720102', 'Procedente. Se agiliza trámite de desistimiento'),
    ('0720201', 'No existe solicitud'),
    ('0720202', 'Movimiento retrasado imputable al cliente. Se adjunta explicación en comentarios'),
    ('0720203', 'Improcedente. Se adjunta explicación en comentarios'),
    ('0730101', 'Se aportan parámetros'),
    ('0730201', 'Telemedida no obligatoria/ No solicitado modem'),
    ('0730202', 'Telemedida no operativa/ Comunicaciones propiedad del usuario'),
    ('0730203', 'Improcedente. Se adjunta explicación en comentarios'),
    ('0730301', 'Acceso denegado'),
    ('0730302', 'Visita anulada por el cliente'),
    ('0730303', 'Cliente no aporta información adicional'),
    ('0730304', 'No se localiza al cliente'),
    ('0740101', 'Se gestiona la publicación del paso'),
    ('0740102', 'Movimiento realizado fuera de plazo'),
    ('0740201', 'No existe solicitud'),
    ('0740202', 'Movimiento realizado en plazo'),
    ('0740203', 'Movimiento fuera de plazo imputable al cliente'),
    ('0740204', 'Improcedente. Se adjunta explicación en comentarios'),
]

TABLA_74 = [('01', u'Concertacion de visita'),
            ('02', u'Ejecución visita')]

TABLA_75 = [('001', u'Ausente'),
            ('002', u'Imposible de localizar'),
            ('003', u'Deshabitado'),
            ('004', u'Anomalía instalación'),
            ('005', u'No realizada por causas imputables al cliente'),
            ('006', u'No realizada por causas imputables al distribuidor'),
            ('007', u'Concertación de Visita'),
            ('008', u'Concertación anterior anulada. Pendiente concertar'),
            ('009', u'Concertación fallida'),
            ('010', u'No concertado'),
            ('011', u'Programado en > 6 días')
            ]

TABLA_76 = [('01', u'Nuevo teléfono de contacto'),
            ('02', u'Nueva persona de contacto'),
            ('03', u'Nuevo email de contacto'),
            ('04', u'IBAN')
            ]

TABLA_77 = [
    ('01', u'Potencia'),
        ('02', u'Reactiva'),
        ('03', u'Penalización ICP'),
        ('04', u'Alquiler de equipo de medida'),
        ('05', u'Impuestos'),
        ('06', u'Excesos de potencia'),
        ('08', u'Depósito de garantía'),
        ('09', u'Verificación de equipos de medida'),
        ('10', u'Derechos de corte y reconexión'),
        ('11', u'Abono por calidad de suministro'),
        ('12', u'Abono por calidad individual'),
        ('13', u'Coste de reposición'),
        ('14', u'Refacturaciones regulatorias'),
        ('16', u'Derechos de acceso'),
        ('17', u'Derechos de extensión'),
        ('18', u'Derechos de enganche'),
        ('19', u'Derechos de actuación en equipo de medida'),
        ('20', u'Derechos de supervisión'),
        ('21', u'Tarifa'),
        ('22', u'Impuesto Eléctrico'),
        ('23', u'Desglose Suplemento Territorial')
]

TABLA_79 = [
    ('01', u'Potencia Contratada'),
    ('02', u'Titular'),
    ('03', u'Tarifa de acceso'),
    ('04', u'Propiedad del equipo de medida'),
    ('05', u'Fecha de activación'),
    ('06', u'Tipo de contrato'),
    ('07', u'Modo control-potencia'),
    ('08', u'Periodicidad facturación'),
    ('09', u'Dirección Punto de Suministro')
]


TABLA_80 = [('01', u'Procedente / Favorable'),
            ('02', u'Improcedente / Desfavorable'),
            ('03', u'No gestionable'),
            ('04', u'Anulada'),
            ('05', u'Duplicada')
            ]

TABLA_81 = [('01', u'ATENCIÓN PERSONAL'),
            ('02', u'FACTURACIÓN Y MEDIDA'),
            ('03', u'CONTRATACIÓN'),
            ('04', u'GESTIÓN DE ACOMETIDAS'),
            ('05', u'CALIDAD DE SUMINISTRO'),
            ('06', u'SITUACIÓN DE INSTALACIONES'),
            ('07', u'ATENCION REGLAMENTARIA'),
            ]

TABLA_82 = [(x['code'], x['name']) for x in SUBTYPES_R101]

TABLA_83 = [('01', u'Titular de PS/ Usuario efectivo'),
            ('02', u'Representante Legal'),
            ('03', u'Aseguradora'),
            ('04', u'Administraciones/ Organísmo público'),
            ('06', u'Comercializador'),
            ('07', u'Juzgados'),
            ('08', u'Afectado no titular del PS'),
            ('09', u'Asociación de Consumidores')
            ]

TABLA_84 = [('01', u'Solicitud de Información adicional'),
            ('02', u'Comunicación de estado intermedia'),
            ('03', u'Comunicación de retipificación de la reclamación'),
            ('04', u'Solicitud de información necesaria para retipificar')
            ]

TABLA_85 = [('01', u'Factura reparación'),
            ('02', u'Nuevos Datos de Contacto'),
            ('03', u'Documento oficial'),
            ('04', u'Contacto y documentos'),
            ('05', u'IBAN'),
            ('06', u'Información mínima incoherente'),
            ]

TABLA_86 = [
    ('01',
     u'Comprobación',
     u'Cliente indica / solicita le comprueben el contador. En caso de equipo '
     u'correcto, implicará asumir los costes asociados a los derechos de '
     u'actuación (si el equipo es de alquiler y en cualquier caso si el '
     u'equipo es propiedad del cliente).'
     ),
    ('02',
     u'Verificación con patrón',
     u'Cliente indica / solicita le verifiquen el contador. El cliente debe '
     u'estar informado de los costes asociados. En caso de equipo correcto, '
     u'implicará asumir los costes asociados a la verificación (si el equipo '
     u'es de alquiler y en cualquier caso si el equipo es propiedad del '
     u'cliente).'
     ),
    ('03', u'Contador robado/ Sin contador', ''),
    ('04', u'Contador averiado: parado, pantalla apagada/falla, sigue contando '
           u'sin nada conectado en domicilio, quemado, error conexionado, '
           u'suministro sin tensión.',
           u'Parado, pantalla apagada / falla, sigue contando sin nada '
           u'conectado en domicilio, quemado, error conexionado, suministro '
           u'sin tensión. En caso de equipo correcto, implicará asumir los '
           u'costes asociados a los derechos de actuación (si el equipo es de '
           u'alquiler y en cualquier caso si el equipo es propiedad del '
           u'cliente).'
     ),
    ('05', u'Incidencias ICP', ''),
    ('06', u'Contador desprogramado: DH o reloj desprogramado (sólo marca en '
           u'punta o en valle o las muestra cambiadas, dígitos contador no se '
           u'corresponde con factura.',
           u'DH o reloj desprogramado (sólo marca en punta o en valle o las '
           u'muestra cambiadas, dígitos contador no se corresponde con '
           u'factura. En caso de equipo correcto, implicará asumir los costes '
           u'asociados a los derechos de actuación (si el equipo es de '
           u'alquiler y en cualquier caso si el equipo es propiedad del '
           u'cliente).'
     ),
    ('07', u'Incidencia en el equipo de telemedida')
]

TABLA_87 = [
    ('01',
     u'Por personal de canales de atención',
     u'Trato inapropiado del personal de atención telefónica, oficinas '
     u'presenciales o cualquier otro canal.'
     ),
    ('02',
     u'Por operarios de equipos de medida',
     u'Trato inapropiado por personal durante la ejecución de trabajos en '
     u'equipo de medida (corte, conexión, precintado, comprobación, etc..)'
     ),
    ('03',
     u'Por operarios de nuevos suministros',
     u'Trato inapropiado por personal durante trabajos de estudios de conexión '
     u'y ejecución de obras de acometidas'
     ),
    ('04',
     u'Por operarios de inspección',
     u'Trato inapropiado por personal de inspección derivados de expedientes '
     u'de anomalía y fraude.'
     ),
    ('05',
     u'Por operaciones',
     u'Trato inapropiado por personal de operación y mantenimiento de red y '
     u'descargos.'
     ),
    ('06',
     u'Por operarios de lecturas',
     u'Trato inapropiado del personal de lectura durante la  toma de lectura '
     u'en campo'
     ),
]

TABLA_101 = [
    ('01', u'De ciclo'),
    ('02', u'Modificación de Contrato'),
    ('03', u'Baja de Contrato'),
    ('04', u'Derechos de Contratación'),
    ('05', u'Depósito de Garantía'),
    ('06', u'Inspección - Anomalía'),
    ('07', u'Atenciones (verificaciones, .)'),
    ('08', u'Indemnización'),
    ('09', u'Intereses de demora'),
    ('10', u'Servicios'),
    ('11', u'Inspección - Fraude')
]

TABLA_102 = [
    ('A', u'Anuladora'),
    ('N', u'Normal'),
    ('R', u'Rectificadora'),
    ('C', u'Complementaria'),
    ('G', u'Regularizadora'),
]

REQUIRE_REFERENCE_TYPES = [
    'A', 'R'
]

TABLA_103 = [
    ('01', u'Indemnización'),
    ('02', u'Derechos de extensión'),
    ('03', u'Derechos de acceso'),
    ('04', u'Derechos de enganche'),
    ('05', u'Derechos de verificación'),
    ('06', u'Depósito de garantía'),
    ('07', u'Gastos de anulación de contratos'),
    ('08', u'Actuaciones en la medida'),
    ('09', u'Reparametrización de la medida'),
    ('11', u'Intereses de demora'),
    ('12', u'Verificación de Equipos de Medida'),
    ('13', u'Derechos de Reconexión'),
    ('15', u'Gastos de acometida'),
    ('16', u'Abonos'),
    ('17', u'Abono por calidad de suministro'),
    ('18', u'Abono por calidad individual'),
    ('19', u'Coste de reposición'),
    ('20', u'Supervisión instalaciones cedidas'),
    ('33', u'Coste de reconexión a petición de comercializador'),
    ('40', u'Recargo fraccionado por refacturación (Orden IET/843/2012) del cuarto trimestre de 2011'),
    ('41', u'Recargo fraccionado por refacturación (Orden IET/843/2012) del primer trimestre de 2012'),
    ('42', u'Recargo fraccionado por refacturación (Orden IET/843/2012) de abril de 2012'),
    ('43', u'Cargo Fijo Autoconsumo'),
    ('44', u'Cargo Variable Autoconsumo'),
    ('45', u'Exención Cargo Fijo Autoconsumo'),
    ('46', u'Exención Cargo Variable Autoconsumo'),
    ('47', u'Derechos de acometida de generación'),
    ('48', u'Suplemento territorial por tributos económicos del año 2013 según la Orden ETU/35/2017'),
    ('49', u'Suplemento territorial por tributos económicos del año 2013 según la Orden TEC/271/2019'),
    ('51', u'Autoconsumo del periodo 1'),
    ('52', u'Autoconsumo del periodo 2'),
    ('53', u'Autoconsumo del periodo 3'),
    ('54', u'Autoconsumo del periodo 4'),
    ('55', u'Autoconsumo del periodo 5'),
    ('56', u'Autoconsumo del periodo 6'),
    ('61', u'Generación neta por el coeficiente del periodo 1'),
    ('62', u'Generación neta por el coeficiente del periodo 2'),
    ('63', u'Generación neta por el coeficiente del periodo 3'),
    ('64', u'Generación neta por el coeficiente del periodo 4'),
    ('65', u'Generación neta por el coeficiente del periodo 5'),
    ('66', u'Generación neta por el coeficiente del periodo 6'),
    ('71', u'Excedente del periodo 1'),
    ('72', u'Excedente del periodo 2'),
    ('73', u'Excedente del periodo 3'),
    ('74', u'Excedente del periodo 4'),
    ('75', u'Excedente del periodo 5'),
    ('76', u'Excedente del periodo 6'),
    ('81', u'Tipo de autoconsumo'),
    ('82', u'Coeficiente de reparto'),
]

CONCEPTOS_CON_FECHA_OPERACION = [
    '01',
    '02',
    '03',
    '04',
    '05',
    '06',
    '07',
    '08',
    '09',
    '12',
    '13',
    '15',
    '19',
    '20',
    '33',
]

TABLA_104 = [('02', u'Euro')]

TABLA_106 = [('01', u'Verificación equipo de medida'),
             ('02', u'Avería en contador'),
             ('03', u'Avería en Trafo de Tensión'),
             ('04', u'Avería en Trafo de intensidad'),
             ('05', u'Desbordamiento del Registrador'),
             ('06', u'Problemas en la sincronización del registrador'),
             ('07', u'Pérdida de alimentación del registrador'),
             ('08', u'Actuación en el equipo'),
             ('09', u'Servicio Directo (sin EM)'),
             ('99', u'Otros')
             ]

TABLA_107 = [
    ('001', u'2.0.A'),
    ('002', u'2.0.N.A'),
    ('003', u'3.0A'),
    ('004', u'2.0DHA'),
    ('005', u'2.1.A'),
    ('006', u'2.1.DHA'),
    ('007', u'2.0 DHS'),
    ('008', u'2.1 DHS'),
    ('011', u'3.1A'),
    ('012', u'6.1A'),
    ('013', u'6.2'),
    ('014', u'6.3'),
    ('015', u'6.4'),
    ('016', u'6.5'),
    ('017', u'6.1B'),
]

TABLA_108 = [('01', u'Mensual'),
             ('02', u'Bimestral')]

TABLA_109 = [('01', u'Telegestión Operativa con CCH'),
             ('02', u'Telegestión No Operativa'),
             ('03', u'Telegestión Operativa sin CCH'),
             ('04', u'Alta en autoconsumo'),
             ('05', u'Modificación de tipo de autoconsumo'),
             ('06', u'Modificación coeficiente de reparto'),
             ('07', u'Modificación potencia generación'),
             ('08', u'Baja en autoconsumo'), ]

TABLA_110 = [('01', u'Acompaña curva de carga'),
             ('02', u'Perfilado'),
             ('03', u'No aplica'), ]

TABLA_111 = [('01', u'Telegestión Operativa con Curva de Carga Horaria'),
             ('02', u'Telegestión Operativa sin Curva de Carga Horaria'),
             ('03', u'Sin Telegestión'), ]

# Converts 109 Table vlues to 111 Table equivalence
CONV_T109_T111 = {'01': '01',  # TG with CCH
                  '02': '03',  # No TG
                  '03': '02'}  # TG without CCH

# Es un tipo de Autoconsumo 2, cuyas instalaciones  de producción conectadas en
# la red interior del consumidor están incluidas en el ámbito de aplicación del
# RD 1699/2011 , la suma de las potencias instaladas de producción no es
# superior a 100kW, el consumidor y los titulares de las instalaciones de
# producción son la misma persona física o jurídica, disponen de la
# configuración de medida establecida en el artículo 13.2.b) del RD 900/2015 y
# han formalizado un solo contrato de acceso conjunto para los SSAA y para el
# consumo asociado

TABLA_113 = [
    ('00', u'Sin Autoconsumo'),
    ('01', u'Autoconsumo Tipo 1'),
    ('2A', u'Autoconsumo tipo 2 (según el Art. 13. 2. a) RD 900/2015)'),
    ('2B', u'Autoconsumo tipo 2 (según el Art. 13. 2. b) RD 900/2015)'),
    ('2G', u'Servicios auxiliares de generación ligada a un autoconsumo tipo 2'),
    ('31', u'Sin Excedentes Individual – Consumo'),
    ('32', u'Sin Excedentes Colectivo – Consumo'),
    ('33', u'Sin Excedentes Colectivo con acuerdo de compensación – Consumo'),
    ('41', u'Con excedentes y compensación Individual - Consumo '),
    ('42', u'Con excedentes y compensación Colectivo– Consumo'),
    ('43', u'Con excedentes y compensación Colectivo a través de red– Consumo'),
    ('51', u'Con excedentes sin compensación Individual sin cto de SSAA en Red Interior– Consumo'),
    ('52', u'Con excedentes sin compensación Colectivo sin cto de SSAA en Red Interior– Consumo'),
    ('53', u'Con excedentes sin compensación Individual con cto SSAA en Red Interior– Consumo'),
    ('54', u'Con excedentes sin compensación individual con cto SSAA en Red Interior– SSAA'),
    ('55', u'Con excedentes sin compensación Colectivo/en Red Interior– Consumo'),
    ('56', u'Con excedentes sin compensación Colectivo/en Red Interior - SSAA'),
    ('61', u'Con excedentes sin compensación Individual con cto SSAA a través de red – Consumo'),
    ('62', u'Con excedentes sin compensación individual con cto SSAA a través de red – SSAA'),
    ('63', u'Con excedentes sin compensación Colectivo a través de red – Consumo'),
    ('64', u'Con excedentes sin compensación Colectivo a través de red - SSAA'),
    ('71', u'Con excedentes sin compensación Individual con cto SSAA a través de red y red interior – Consumo'),
    ('72', u'Con excedentes sin compensación individual con cto SSAA a través de red y red interior – SSAA'),
    ('73', u'Con excedentes sin compensación Colectivo con cto de SSAA  a través de red y red interior – Consumo'),
    ('74', u'Con excedentes sin compensación Colectivo con cto de SSAA a través de red y red interior - SSAA'),
]

TENEN_AUTOCONSUM = [x[0] for x in TABLA_113 if x[0] not in ['00', '01', '2A', '2B', '2G']]

TABLA_114 = [
    ('1', u'IVA / IPSI/ IGIC'),
    ('2', u'IVA / IPSI/ IGIC Reducido'),
    ('3', u'IVA / IPSI/ IGIC EXENTO'),
]

TABLA_115 = PERSONA

TABLA_116 = [
    ('0', u'No Bono Social – Retirada del BS'),
    ('1', u'Bono Social'),
]

REQUIRE_PERSON_TYPE = ['NV', 'OT']

TABLA_117 = [
    ('M', u'Monofásica'),
    ('T', u'Trifásica')
]

TABLA_118 = [
    ('01', u'Vuelta a la situación anterior – En servicio'),
    ('02', u'Vuelta a la situación anterior – Sin servicio (cortado)'),
    ('03', u'Traspaso a la COR'),
    ('04', u'Baja del contrato por rechazo de la COR'),
    ('05', u'Baja por cese de actividad'),
    ('06', u'Activación de Cambio de Comercializador'),
]


TABLA_119 = [
    ('01', u'Solicitud de baja por fin de contrato de energía (B1 motivo 02)'),
    ('02', u'Solicitud de desistimiento a un cambio de comercializador de un nuevo titular'),
    ('03', u'Decisión fundada de la Dirección General de Política Energética y Minas, cautelar o '
           u'definitivamente, se traspasan los puntos de suministro al COR'),
]

TABLA_120 = [
    ('01', u'Baja del contrato de acceso de duración inferior a un año según fecha solicitada por la '
           u'empresa comercializadora'),
    ('02', u'Baja del contrato de acceso por suministro cortado/proceso de corte e inhabilitación del '
           u'comercializador en vigor.'),
    ('02', u'Baja del contrato de acceso por orden judicial o mandato de organismo oficial'),
    ('03', u'Baja del contrato de acceso por rechazo del COR al traspaso'),
    ('04', u'Baja del contrato de acceso a iniciativa de la distribuidora por seguridad de la red.'),
    ('05', u'Baja del contrato de acceso por haber pasado dos meses desde que se suspendió un punto de '
           u'suministro tras el desistimiento de un cambio de comercializador activado sobre un punto de '
           u'suministro suspendido por impago'),
]

TABLA_121 = [
    ('01', u'Nuevo teléfono de contacto.'),
    ('02', u'Deficiencia/Trabajos subsanada. Contactar con cliente'),
]

TABLA_122 = [
    ('01', u'Desistimiento en plazo máx. de 14 días naturales'),
    ('02', u'Desistimiento por incumplimiento de comercializador en contratación'),
]

TABLA_123 = [
    ('01', u'El PS no ha pasado la inspección de la instalación de enlace (instalación desde la Caja General '
           u'de Protección, CGP,  al contador)'),
    ('02', u'Instalación eléctrica peligrosa'),
    ('03', u'Necesidad de abrir expediente de acometida: Derechos caducados'),
    ('04', u'Expediente abierto de nuevos suministros'),
    ('05', u'Expediente abierto de inspección'),
    ('06', u'Falta licencia de ocupación, cédula de habitabilidad u otra documentación relevante que impide la '
           u'contratación del NNSS'),
    ('07', u'Orden o Resolución de la Administración Pública competente, Resolución o Mandato Judicial que impide '
           u'la contratación en el PS'),
]

TABLA_124 = [
    ('A300', u'Solicitud de nuevo suministro'),
    ('C100', u'Solicitud de cambio de comercializador sin modificación en el contrato de acceso'),
    ('C200', u'Solicitud de cambio de comercializador con modificación en el contrato de acceso'),
    ('B101', u'Baja por cese de actividad'),
    ('B102', u'Baja por fin de contrato de suministro'),
    ('B103', u'Corte o suspensión del suministro por impago'),
    ('B104', u'Baja por Impago')
]

TABLA_125 = [
    ('01', u'Aumento potencia'),
    ('02', u'Cambio tensión'),
    ('03', u'Cambio tarifa'),
    ('04', u'Nuevo suministro'),
    ('05', u'Colectivo nueva construcción'),
    ('06', u'Colectivo electrificación rural'),
    ('07', u'Informativo Plan urbanístico'),
    ('08', u'Informativo Plan industrial'),
    ('09', u'Informativo Productor de Régimen Especial'),
    ('10', u'Colectivo reconstrucción vivienda'),
    ('11', u'TCT No relacionado a NNSS'),
    ('12', u'TCT Relacionado a NNSS'),
    ('13', u'Colectivo renovación de Instalaciones de enlace varios suministros'),
    ('14', u'Renovación de instalaciones de enlace')
]

TABLA_126 = [
    ('a11', u'[A11] - Cogeneraciones que utilicen como combustible el gas natural, siempre que éste suponga al menos '
            u'el 95 por ciento de la energía primaria utilizada, o al menos el 65 por ciento de la energía primaria '
            u'utilizada cuando el resto provenga de biomasa o biogás de los grupos b.6, b.7 y b.8; siendo los '
            u'porcentajes de la energía primaria utilizada citados medidos por el poder calorífico inferior.'),
    ('a12', u'[A12] - Cogeneraciones que utilicen como combustible principal derivados de petróleo o carbón, siempre '
            u'que suponga al menos el 95 por ciento de la energía primaria utilizada, medida por el poder '
            u'calorífico inferior'),
    ('a13', u'[A13] - Resto de cogeneraciones que utilicen gas natural o derivados de petróleo o carbón, y no cumplan '
            u'con los límites de consumo establecidos para los subgrupos a.1.1 ó a.1.2.'),
    ('a20', u'[A20] - Instalaciones que incluyan una central que utilice energías residuales procedentes de cualquier '
            u'instalación, máquina o proceso industrial cuya finalidad no sea la producción de energía eléctrica.'),
    ('b11', u'[B11] - Instalaciones que únicamente utilicen la radiación solar como energía primaria mediante la '
            u'tecnología fotovoltaica.'),
    ('b12', u'[B12] - Instalaciones que únicamente utilicen procesos térmicos para la transformación de la energía '
            u'solar, como energía primaria, en electricidad.'),
    ('b21', u'[B21] - Instalaciones eólicas ubicadas en tierra.'),
    ('b22', u'[B22] - Instalaciones eólicas ubicadas en espacios marinos, que incluyen tanto las aguas interiores como '
            u'el mar territorial.'),
    ('b30', u'[B30] - Instalaciones que únicamente utilicen como energía primaria la geotérmica, hidrotérmica, '
            u'aerotérmica, la de las olas, la de las mareas, la de las rocas calientes y secas, la oceanotérmica y la '
            u'energía de las corrientes marinas.'),
    ('b41', u'[B41] - Centrales hidroeléctricas cuyas instalaciones hidráulicas (presa o azud, toma, canal y otras) '
            u'hayan sido construidas exclusivamente para uso hidroeléctrico. '
            u'Potencia instalada NO Superior a 10 MW'),
    ('b42', u'[B42] - Centrales hidroeléctricas que hayan sido construidas en infraestructuras existentes (presas, '
            u'canales o conducciones) o dedicadas a otros usos distintos al hidroeléctrico. '
            u'Potencia instalada NO Superior a 10 MW'),
    ('b51', u'[B51] - Centrales hidroeléctricas cuyas instalaciones hidráulicas (presa o azud, toma, canal y otras) '
            u'hayan sido construidas exclusivamente para uso hidroeléctrico. '
            u'Potencia instalada Superior a 10 MW'),
    ('b52', u'[B52] - Centrales hidroeléctricas que hayan sido construidas en infraestructuras existentes (presa, '
            u'canales o conducciones) o dedicadas a otros usos distintos al hidroeléctrico. '
            u'Potencia instalada a Superior a 10 MW'),
    ('b60', u'[B60] - Centrales de generación eléctrica o de cogeneración que utilicen como combustible principal '
            u'biomasa procedente de cultivos energéticos, de actividades agrícolas, ganaderas o de jardinerías, de '
            u'aprovechamientos forestales y otras operaciones silvícolas en las masas forestales y espacios verdes, '
            u'en los términos que figuran en el anexo I. Se entenderá como combustible principal aquel combustible '
            u'que suponga, como mínimo, el 90 por ciento de la energía primaria utilizada, medida por el poder '
            u'calorífico inferior.'),
    ('b71', u'[B71] - Instalaciones que empleen como combustible principal el biogás de vertederos controlados. Estas '
            u'instalaciones podrán abastecerse con hasta un 50 por ciento de energía primaria procedente de biogás '
            u'generado en digestores.'),
    ('b72', u'[B72] - Instalaciones que empleen como combustible principal biolíquidos o el biogás generado en '
            u'digestores procedente de cultivos energéticos o de restos agrícolas, de deyecciones ganaderas, de '
            u'residuos biodegradables de instalaciones industriales, de residuos domiciliarios o similares, de lodos '
            u'de depuración de aguas residuales u otros para los cuales sea de aplicación el proceso de digestión '
            u'anaerobia, tanto individualmente como en co-digestión. Estas instalaciones podrán abastecerse con '
            u'hasta un 50 por ciento de energía primaria procedente de biogás de vertederos controlados.'),
    ('b80', u'[B80] - Centrales de generación eléctrica o de cogeneración que utilicen como combustible principal '
            u'biomasa procedente de instalaciones industriales del sector agrícola o forestal en los términos que '
            u'figuran en el anexo I. Se entenderá como combustible principal aquel combustible que suponga, como '
            u'mínimo, el 90 por ciento de la energía primaria utilizada, medida por el poder calorífico inferior.'),
    ('c10', u'[C10] - Centrales que utilicen como combustible principal residuos domésticos y similares.'),
    ('c20', u'[C20] - Centrales que utilicen como combustible principal otros residuos no contemplados en el grupo '
            u'c.1, combustibles de los grupos b.6, b.7 y b.8 cuando no cumplan con los límites de consumo establecidos '
            u'para los citados grupos, licores negros y las centrales que a la entrada en vigor de este real decreto '
            u'estuvieran inscritas en la categoría c) grupo c.3 prevista en el artículo 2.1 del Real Decreto '
            u'661/2007, de 25 de mayo, por el que se regula la actividad de producción de energía eléctrica en '
            u'régimen especial.'),
    ('c30', u'[C30] - Centrales que a la entrada en vigor de este real decreto estuvieran acogidas a la categoría c) '
            u'grupo c.4 prevista en el artículo 2.1 del Real Decreto 661/2007, de 25 de mayo, utilizando como '
            u'combustible productos de explotaciones mineras de calidades no comerciales para la generación eléctrica '
            u'por su elevado contenido en azufre o cenizas, representando los residuos más del 25 por ciento de la '
            u'energía primaria utilizada.'),
]

TABLA_127 = [('1', u'Sin excedentes'),
             ('2', u'Con excedentes'), ]

TABLA_128 = [('a0', u'Con excedentes y mecanismo de compensación simplificado'),
             ('b1', u'Con excedentes sin mecanismo de compensación y un único contrato de suministro'),
             ('b2', u'Con excedentes sin mecanismo de compensación y varios contratos de suministro'), ]

TABLA_129 = [('01', u'Red interior'),
             ('02', u'Red interior da varios consumidores (instalación de enlace)'),
             ('03', u'Próxima a través de red'), ]

TABLA_130 = [('A', u'EdM Bidireccional en PF'),
             ('B', u'EdM Bidireccional en PF y EdM gen. Neta'),
             ('C', u'EdM Consumo Total y EdM bidireccional gen. Neta'),
             ('D', u'EdM Consumo Total y EdM gen bruta y EdM SSAA'),
             ('E', u'Configuración singular'), ]

TABLA_131 = [('01', u'Consumo'),
             ('02', u'Servicios Auxiliares'), ]

TABLA_132 = [('BT', u'Baja tensión, si tensión <= 1kV'),
             ('AT', u'Alta tensión, si tensión >1kV'), ]