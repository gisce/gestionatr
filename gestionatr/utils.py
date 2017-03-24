import os

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
