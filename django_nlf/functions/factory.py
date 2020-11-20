from functools import wraps
from typing import Callable

from django_nlf.types import FunctionMeta, FunctionRole


class FunctionFactory:

    registry = {}

    @classmethod
    def register(cls, fn_name: str, func: Callable, meta: FunctionMeta):
        if fn_name in cls.registry:
            pass

        cls.registry[fn_name] = (func, meta)

    @classmethod
    def get_function(cls, fn_name: str, model=None) -> Callable:
        if fn_name not in cls.registry:
            raise AttributeError(f"Unknown function '{fn_name}'!")

        func, meta = cls.registry[fn_name]

        if meta.models and model and model not in meta.models:
            raise ValueError(f"Function '{fn_name}' cannot be used for {model.__name__}")

        return func


def nlf_function(fn_name: str = None, **kwargs):
    meta = FunctionMeta(**kwargs)

    def decorator(func):
        name = fn_name or func.__name__
        FunctionFactory.register(name, func, meta)

        @wraps(func)
        def wrapper(func):
            return func

        return wrapper

    return decorator
