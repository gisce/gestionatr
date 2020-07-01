# -*- coding: utf-8 -*-
import os.path
import random
import string
from datetime import datetime

python_code = open("python_code.txt", "w+")
test_code = open("test_code.txt", "w+")
test_data = open("test_data.xml", "w+")
erp_code = open("erp_code.txt", "w+")
erp_create_from_xml_code = open("erp_create_from_xml_code.txt", "w+")

test_template = """self.assertEqual({0}.{1}, {2})\n"""
test_get_list_template = """{0} = {1}.{2}[0]\n"""
test_get_class_template = """{0} = {1}.{0}\n"""
xml_template = """<{0}>{1}</{0}>\n"""

# TEMPLATES DE CLASSES
main_class_template = """
class {0}({1}):

    steps = []

"""

object_class_template = """
class {0}(object):

    def __init__(self, data):
        self.obj = data

"""

# TEMPLATES DE ATRIBUTS
method_main = "    @property\n" \
         "    def {0}(self):\n" \
         "        tree = '{{0}}.{1}'.format(self._header)\n" \
         "        data = get_rec_attr(self.obj, tree, False)\n" \
         "        if data is not None and data is not False:\n" \
         "            return data.text\n" \
         "        else:\n" \
         "            return False\n\n"

method_generic = "    @property\n" \
         "    def {0}(self):\n" \
         "        tree = '{1}'\n" \
         "        data = get_rec_attr(self.obj, tree, False)\n" \
         "        if data is not None and data is not False:\n" \
         "            return data.text\n" \
         "        else:\n" \
         "            return False\n\n"

# TEMPLATES DE CLASSE
method_class_main = "    @property\n" \
         "    def {0}(self):\n" \
         "        tree = '{{0}}.{1}'.format(self._header)\n" \
         "        data = get_rec_attr(self.obj, tree, False)\n" \
         "        if data is not None and data is not False:\n" \
         "            return {1}(data)\n" \
         "        else:\n" \
         "            return False\n\n"

method_class_generic = "    @property\n" \
         "    def {0}(self):\n" \
         "        tree = '{1}'\n" \
         "        data = get_rec_attr(self.obj, tree, False)\n" \
         "        if data is not None and data is not False:\n" \
         "            return {1}(data)\n" \
         "        else:\n" \
         "            return False\n\n"

# TEMPLATES DE ATRIBUTS LLISTA
method_list_main = "    @property\n" \
              "    def {0}(self):\n" \
              "        data = []\n" \
              "        obj = get_rec_attr(self.obj, self._header, False)\n" \
              "        if (hasattr(obj, '{1}') and\n" \
              "                hasattr(obj.{1}, '{2}')):\n" \
              "            for d in obj.{1}.{2}:\n" \
              "                data.append({2}(d))\n" \
              "        return data\n\n"


method_list_generic = "    @property\n" \
              "    def {0}(self):\n" \
              "        data = []\n" \
              "        obj = self.obj\n\n" \
              "        if (hasattr(obj, '{1}') and\n" \
              "                hasattr(obj.{1}, '{2}')):\n" \
              "            for d in obj.{1}.{2}:\n" \
              "                data.append({2}(d))\n" \
              "        return data\n\n"

# TEMPLATES ERP MODELS
erp_column = """'{0}': fields.{1}({2}{3}),\n"""
erp_line = """    '{0}': xml.{1},\n"""


def generate_input_python_code(process_name, info_file, process_file=False, inherit_proces=False):
    input_f = open(info_file, "r")
    # If no proces_file is given, them proces_file is "proces_name"
    if not process_file:
        process_file = process_name + ".py"

    # 2. Calculem a on hem de cpmprovar repetits
    check_repeated = inherit_proces
    if os.path.isfile(process_file):
        proces_module = __import__(process_file.split(".")[0])
        if proces_module:
            check_repeated = process_name

    # 3. Ara el que farem sera guardar a un diccionari la informacio.
    # Les claus son els noms de les clases i la llista de valors els seus camps.
    python_structure = generate_python_structure(process_name, input_f)

    # 4. Un cop tenim l'estructura de python, l'utiliyzem per "escriure" el codi
    write_python_code(process_name, python_structure, check_repeated, inherit_proces)
    return python_structure


def generate_python_structure(process_name, input_f):
    print "Generem l'estructura python amb les classes i atributs necessaris."
    nonumber_lines = 0
    parent_added_check = True
    python_structure = {
        process_name: []
    }
    parents = [process_name]
    last_number = -1
    for line in input_f.readlines():
        try:
            aux = line.split(">")[0]
            aux2 = line.split("<")[-1]
            number, field = aux.split("<")
        except Exception, e:
            print "    Skip line {0}".format(line.strip())
            continue
        number = int(number.strip()) if number.strip() else False
        field = field.strip()[:]

        # Hem de ignorar les linies fins que haguem passat el header
        if not number:
            nonumber_lines += 1
        if nonumber_lines < 2:
            continue

        # Si no te numero vol dir que sera una nova classe.
        # L'afegim a la llista de pares (sera el pare de les noves) i afegim
        # una nova entrada al diccionari
        if not number:
            if last_number == -1:
                continue
            parents.append(field)
            parent_added_check = True
            if not python_structure.get(field):
                python_structure[field] = []
            continue

        # Gestionem un camp "normal"
        else:
            # Si l'ultim numero no es l'anterior al actual, vol dir que hem
            # "acavat" amb una classe i eliminem el pare de la llista.
            if last_number != number-1 and not parent_added_check:
                parents.pop(-1)
            parent_added_check = False
            # Afegim el camp al diccionari utilitzant el pare que toqui
            field_data = get_field_data(field, aux2)
            python_structure[parents[-1]].append(field_data)
            last_number = number
    print "    S'han trobat {0} classes python: {1}".format(len(python_structure.keys()), python_structure.keys())
    return python_structure


def get_field_data(field, line):
    data = line.strip().split("\t")
    data = [d for d in data if d.strip() not in ["", "\t"]]

    norm_class_attr = field.lower()[0]
    for c in field.lower()[1:]:
        if c.isupper():
            norm_class_attr += "_{0}".format(c.lower())
        else:
            norm_class_attr += c
    ok_data = [norm_class_attr]
    desc = data[1]
    # Treiem elements fins que trobem el que indica si es obligatori o no.
    # Sabem que despres be el que ens diu quin tipus es.
    i = 0
    for i in range(len(data)):
        if data[i] in ("S", "N"):
            break
    data = data[i+1:]
    if len(data) > 2:
        raise Exception("Something gone wrong with {0}".format(field))

    data_taula = "SENSE_TAULA"
    if len(data) > 1:
        tdata = data[1].strip()[5:].replace("Á", "A").replace("É", "E").replace("Í", "I").replace("Ó", "O").replace("Ú", "U")
        if not tdata:
            pass
        if tdata[0] == " ":
            tdata = tdata[1:]
        data_taula = "TAULA_"
        for c in tdata:
            if c.isupper():
                data_taula += c
            elif c == ' ' and data_taula[-1] != "_":
                data_taula += "_"
            else:
                break
        if data_taula[-1] == "_":
            data_taula = data_taula[:-1]
    if field.endswith("list"):
        ok_data += ["L", "SENSE_TAULA"]
    elif len(data) == 0:
        ok_data += ["C", "SENSE_TAULA"]
    else:
        ok_data += [data[0], data_taula]
    return ok_data + [desc]


def write_python_code(process_name, python_structure, check_repeated=False, inherit_proces=False):
    print "Emplenem el fitxer ''python_code.txt''."
    if check_repeated:
        check_repeated = __import__(check_repeated)

    # Tenim nuna estructura en que cada clau es una clase i el seu valor es una
    # llista amb els seus atributs
    for python_class, class_attrs in python_structure.iteritems():

        # 1. Comprovem si hi ha algun camp no repetit, sino no escrivim res
        no_rep = class_attrs[:]
        if check_repeated:
            rep_class = getattr(check_repeated, python_class, False)
            if not rep_class and python_class == process_name and inherit_proces:
                rep_class = getattr(check_repeated, inherit_proces, False)
            no_rep = [a[0] for a in class_attrs if not hasattr(rep_class, a[0])]
            if not len(no_rep):
                print "    La classe {0} ja te tots els atributs.".format(python_class)
                continue
        else:
            no_rep = [a[0] for a in class_attrs]

        # 2. Escrivim la classe. Depenguent si es la principal
        # o no te estructures diferents
        in_main_class = python_class == process_name
        if in_main_class:
            python_code.write(main_class_template.format(python_class, inherit_proces or "object"))
        else:
            python_code.write(object_class_template.format(python_class, inherit_proces or "object"))

        # 3. Per cada camp, si no està repetit l'escrivim
        for class_attr in no_rep:
            print class_attr
            # "Normalitzem" el nom. Els atributs tenen nom normalitzat
            norm_class_attr = class_attr.lower()[0]
            for c in class_attr.lower()[1:]:
                if c.isupper():
                    norm_class_attr += "_{0}".format(c.lower())
                else:
                    norm_class_attr += c

            # 3.1 Comprovem si es un "atribut llista"
            if class_attr.endswith("list"):
                class_name = class_attr[:-4]
                if in_main_class:
                    python_code.write(method_list_main.format(norm_class_attr, class_attr, class_name))
                else:
                    python_code.write(method_list_generic.format(norm_class_attr, class_attr, class_name))

            # 3.2 Comprovem si es un "atribut classe"
            elif class_attr in python_structure.keys():
                if in_main_class:
                    python_code.write(method_class_main.format(norm_class_attr, class_attr))
                else:
                    python_code.write(method_class_generic.format(norm_class_attr, class_attr))
            # 3.3 Es un "atribut text"
            else:
                if in_main_class:
                    python_code.write(method_main.format(norm_class_attr, class_attr))
                else:
                    python_code.write(method_generic.format(norm_class_attr, class_attr))
        print "    S'han afegit {0} atributs a la classe {1}: {2}".format(len(no_rep), python_class, no_rep)


def generate_input_test_files_main(process_name, process_data):
    print "Emplenem el fitxer ''test_code.txt'' i ''test_data.xml per el model {0}''".format(process_name)
    generate_input_test_files(process_name, process_data)


def generate_input_test_files(process_name, process_data):
    # Iterem en cada atribut de la classe principal
    test_data.write("<{0}>\n".format(process_name))
    for fdata in process_data[process_name]:
        fname = fdata[0]
        tipus = fdata[1]
        taula = fdata[2]
        res = False
        if tipus[0] == "X":
            if taula == "SENSE_TAULA":
                res = process_text_field(fname, tipus)
            else:
                res = process_selection_field(fname, tipus, taula)
        elif tipus[0] in ["9", "S"]:
            if "V" in tipus:
                res = process_float_field(fname, tipus)
            else:
                res = process_integer_field(fname, tipus)
        elif tipus == "HH:MM:SS":
            res = process_time_field("%H:%M:%S")
        elif tipus == "AAAA-MM-DD":
            res = process_time_field("%Y-%m-%d")
        elif tipus == "AAAA-MM-DD HH:MM:SS":
            res = process_time_field("%Y-%m-%d %H:%M")
        elif tipus[0] == "L":
            res = process_list_field(process_name, fname, process_data)
        elif tipus[0] == "C":
            res = process_class_field(process_name, fname, process_data)
        else:
            raise Exception("    Tipus desconegut per l'atribut {0}: {1}".format(fname, tipus))
        if res:
            test_data.write(xml_template.format(fname, res))
            # if isinstance(res, basestring):
            #     res = 'u"'+res+'"'
            res = 'u"' + str(res) + '"'
            test_code.write(test_template.format(process_name, fname, res))
    test_data.write("</{0}>\n".format(process_name))


def process_text_field(fname, tipus, max_len=30):
    flen = int(tipus.split(")")[0][2:])
    if flen == 1:
        return "1"
    elif flen == 2:
        return "2_"
    else:
        rm = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(flen-1-len(str(flen)))])
        return "{0}_{1}".format(flen, rm[:min(max_len, flen)])


def process_integer_field(fname, tipus):
    enters = tipus.split("(")[1].split(")")[0]
    max_val = ""
    for n in range(int(enters)):
        max_val += "9"
    max_val = int(max_val)
    min_val = -1*max_val if "S" in tipus else 0
    return int(random.uniform(min_val, max_val))


def process_float_field(fname, tipus):
    enters = tipus.split("(")[1].split(")")[0]
    decimals = int(tipus.split("(")[2].split(")")[0])
    max_val = ""
    for n in range(int(enters)):
        max_val += "9"
    max_val = float(max_val)
    min_val = -1*max_val if "S" in tipus else 0
    return round(random.uniform(min_val, max_val), decimals)


def process_time_field(format):
    return datetime.now().strftime(format)


def process_list_field(base_atr, list_atr, process_data):
    class_name = list_atr[:-4]
    test_code.write(test_get_list_template.format(class_name, base_atr, list_atr))
    test_data.write("<{0}>\n".format(list_atr))
    process_class_field(base_atr, class_name, process_data, no_test=True)
    test_data.write("</{0}>\n".format(list_atr))


def process_class_field(base_atr, class_name, process_data, no_test=False):
    if class_name not in process_data.keys():
        raise Exception("Classe no trobada {0}".format(class_name))
    print "    Emplenem per la classe {0}".format(class_name)
    if not no_test:
        test_code.write(test_get_class_template.format(class_name, base_atr))
    generate_input_test_files(class_name, process_data)
    return False


def process_selection_field(fname, tipus, taula_name):
    flen = int(tipus.split(")")[0][2:])
    import gestionatr.defs_gas as dgas
    import gestionatr.defs as dele
    taula = False
    if hasattr(dgas, taula_name):
        taula = getattr(dgas, taula_name)
    elif hasattr(dele, taula_name):
        taula = getattr(dgas, taula_name)
    if not taula:
        print "    Taula no trobada: {0}".format(taula_name)
        res = ""
        for i in range(flen):
            res += "0"
        res = res[:-1] + "1"
    else:
        if flen > 8:
            res = taula[0][1]
        else:
            res = taula[0][0]
    return res.strip()


def generate_erp_models_main(process_name, process_data):
    print "Emplenem el fitxer ''erp_code.txt''".format(process_name)
    generate_erp_models(process_name, process_data)


def generate_erp_models(process_name, process_data):
    # Iterem en cada atribut de la classe principal
    erp_create_from_xml_code.write("{0}_vals: {{\n".format(process_name))
    for fdata in process_data[process_name]:
        fname = fdata[0]
        tipus = fdata[1]
        taula = fdata[2]
        nom = "'{}'".format(fdata[3])
        res = False
        if tipus[0] == "X":
            if taula == "SENSE_TAULA":
                res = process_erp_text_field(fname, tipus, nom)
            else:
                res = process_erp_selection_field(fname, tipus, taula, nom)
        elif tipus[0] in ["9", "S"]:
            if "V" in tipus:
                res = process_erp_float_field(fname, tipus, nom)
            else:
                res = process_erp_integer_field(fname, tipus, nom)
        elif tipus == "HH:MM:SS":
            res = process_erp_time_field(fname,"%H:%M:%S", nom)
        elif tipus == "AAAA-MM-DD":
            res = process_erp_time_field(fname,"%Y-%m-%d", nom)
        elif tipus == "AAAA-MM-DD HH:MM:SS":
            res = process_erp_time_field(fname,"%Y-%m-%d %H:%M", nom)
        elif tipus[0] == "L":
            res = process_erp_list_field(fname, nom, process_data)
        elif tipus[0] == "C":
            res = process_erp_class_field(fname, nom, process_data)
        else:
            raise Exception("    Tipus desconegut per l'atribut {0}: {1}".format(fname, tipus))
        if res:
            erp_code.write(erp_column.format(*res))
            erp_create_from_xml_code.write(erp_line.format(res[0], res[0]))
    erp_create_from_xml_code.write("}\n")


def process_erp_text_field(fname, tipus, nom, max_len=30):
    flen = int(tipus.split(")")[0][2:])
    tipus = "text" if flen >= 100 else "char"
    return [fname, tipus, nom, ", size={0}".format(flen)]


def process_erp_integer_field(fname, tipus, nom):
    enters = int(tipus.split("(")[1].split(")")[0])
    return [fname, "integer", nom, ", size={0}".format(enters)]


def process_erp_float_field(fname, tipus, nom):
    enters = int(tipus.split("(")[1].split(")")[0])
    decimals = int(tipus.split("(")[2].split(")")[0])
    return [fname, "float", nom, ", digits=({0}, {1})".format(enters+decimals, decimals)]


def process_erp_time_field(fname, format, nom):
    tipus = "date" if format == "AAAA-MM-DD" else "datetime"
    return [fname, tipus, nom, ""]


def process_erp_list_field(fname, nom, process_data):
    erp_create_from_xml_code.write("    '{0}': \n".format(fname))
    res = [fname[:-4]+"_ids", "one2many", "'giscegas.atr.{}'".format(fname[:-4]), ", 'pas_id', {}".format(nom)]
    erp_code.write(erp_column.format(*res))
    return process_erp_class_field(fname[:-4], nom.split(" ")[-1], process_data, write_class_id=False)


def process_erp_class_field(fname, nom, process_data, write_class_id=True):
    if write_class_id:
        res = [fname+"_id", "many2one", "'giscegas.atr.{}'".format(fname), ", 'pas_id', {}".format(nom)]
        erp_code.write(erp_column.format(*res))
        erp_create_from_xml_code.write("    '{0}': \n".format(fname))
    print "    Emplenem per la classe {0}".format(fname)
    erp_code.write("## Data from {0}\n".format(fname))
    generate_erp_models(fname, process_data)
    erp_code.write("## End of {0}\n".format(fname))


def process_erp_selection_field(fname, tipus, taula_name, nom):
    flen = int(tipus.split(")")[0][2:])
    if flen > 8:
        return process_erp_text_field(fname, tipus, nom)

    import gestionatr.defs_gas as dgas
    import gestionatr.defs as dele
    taula = False
    if hasattr(dgas, taula_name):
        taula = getattr(dgas, taula_name)
    elif hasattr(dele, taula_name):
        taula = getattr(dgas, taula_name)
    if not taula:
        print "    Taula no trobada: {0}".format(taula_name)

    return [fname, "selection", taula_name, ", "+nom]

data = generate_input_python_code("A1_03", "info", inherit_proces="A1_44")
generate_input_test_files_main("A1_03", data)
generate_erp_models_main("A1_03", data)
