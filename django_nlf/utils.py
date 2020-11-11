import warnings


def deprecate(msg, level_modifier=0):
    warnings.warn(msg, DeprecationWarning, stacklevel=3 + level_modifier)


def coerce_bool(value):
    return value.lower()[0] == "t"


def coerce_datetime(value):
    return value
