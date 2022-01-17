# -*- encoding: utf-8 -*-
import sys
from gestionatr.input.messages import message
from gestionatr.input.messages.message import except_f1 
from gestionatr import __version__

sys.stdout.write(u'Switching version: {0}\n'.format(__version__))
with open(sys.argv[1], 'r') as xml_file:
    try:
        data = xml_file.read()
        m = message.Message(data)
        m.parse_xml()
        sys.stdout.write(u'Fitxer Correcte\n')
    except Exception as e:
        sys.stdout.write(u'Fitxer Invàlid: {0}\n'.format(e))

