from .conf import nlf_settings


def coerce_bool(value):
    if isinstance(value, str):
        return value[0].lower() not in nlf_settings.FALSE_VALUES
    return value


def coerce_datetime(value):
    return value
