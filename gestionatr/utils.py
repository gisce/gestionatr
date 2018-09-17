from gestionatr import defs
import os
from collections import namedtuple

_ROOT = os.path.abspath(os.path.dirname(__file__))


def get_data(path):
    filename = isinstance(path, (list, tuple)) and path[0] or path
    return os.path.join(_ROOT, 'data', filename)


def get_rec_attr(obj, attr, default=None):
    try:
        res = reduce(getattr, attr.split('.'), obj)
    except:
        if default is not None:
            res = default
        else:
            raise
    return res


def get_description(code, table_name):
    table = getattr(defs, table_name, None)
    if not table:
        raise ValueError(
            "The table with the name '{}' doesn't exist".format(table_name)
        )
    res = dict(table).get(code, None)
    if not res:
        raise ValueError(
            "The key '{}' in the table '{}' doesn't exist".format(
                code, table_name
            )
        )
    return res


ValidationResult = namedtuple('ValidationResult', ['valid', 'error'])


def validate_xml(data, is_gas=False):
    try:
        from gestionatr.input.messages import Message
        m = Message(data)
        m.parse_xml()
        return ValidationResult(True, None)
    except Exception as e:
        try:
            from gestionatr.input.messages import MessageGas
            m = MessageGas(data)
            m.parse_xml()
            return ValidationResult(True, None)
        except Exception as e2:
            if is_gas:
                return ValidationResult(False, u'Invalid File: {0}'.format(str(e2.value)))
            else:
                return ValidationResult(False, u'Invalid File: {0}'.format(str(e.value)))