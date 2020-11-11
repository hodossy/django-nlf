import warnings


def deprecate(msg, level_modifier=0):
    warnings.warn(msg, DeprecationWarning, stacklevel=3 + level_modifier)
