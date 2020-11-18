from functools import wraps
from typing import Callable


class FunctionFactory:

    registry = {}

    @classmethod
    def register(cls, fn_name: str, func: Callable, models=()):
        if fn_name in cls.registry:
            pass

        cls.registry[fn_name] = (func, models)

    @classmethod
    def get_function(cls, fn_name: str, model=None) -> Callable:
        if fn_name not in cls.registry:
            raise AttributeError(f"Unknown function '{fn_name}'!")

        fn, allowed_models = cls.registry[fn_name]

        if allowed_models and model and model not in allowed_models:
            raise ValueError(f"Function '{fn_name}' cannot be used for {model.__name__}")

        return fn


def nlf_function(fn_name, models=()):
    def decorator(func):
        FunctionFactory.register(fn_name, func, models)

        @wraps(func)
        def wrapper(func):
            return func

        return wrapper

    return decorator
