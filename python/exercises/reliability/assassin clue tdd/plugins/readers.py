import pandas as pd
import json as jsonlib

_READERS = {}

def register(func):
    _READERS[func.__name__] = func
    return func

def read(format, *args, **kwargs):
    if format in _READERS:
        return _READERS[format](*args, **kwargs)
    else:
        raise TypeError(f"{format} files are not supported")

@register
def csv(file_path):
    return pd.read_csv(file_path)

@register
def json(file_path):
    json_dict = jsonlib.loads(file_path.read_text())
    return pd.DataFrame(json_dict)
