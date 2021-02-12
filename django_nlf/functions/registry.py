import inspect
from functools import wraps
from typing import Callable, Dict, Tuple

from django_nlf.types import FunctionMeta, FunctionRole


class FunctionRegistry:
    """A Registry that holds supported functions.
    :attr Dict[str, Tuple[Callable, FunctionMeta]] registry: Dictionary of registered functions
                                                             and meta data.
    """

    registry: Dict[str, Tuple[Callable, FunctionMeta]] = {}

    @classmethod
    def register(cls, fn_name: str, func: Callable, meta: FunctionMeta):
        """Registers functions with their metadata for use in the filter language.

        :param str fn_name: The name used in the language to reference the function.
        :param Callable func: The function to register.
        :param FunctionMeta meta: The metadata for the function.
        :return: None
        """
        if fn_name in cls.registry:
            pass

        cls.registry[fn_name] = (func, meta)

    @classmethod
    def get_function(
        cls,
        fn_name: str,
        role: FunctionRole = FunctionRole.VALUE,
        model: "django.db.models.Model" = None,
    ) -> Callable:
        """Returns the function by name. Checks for `role` and `model` restrictions.

        :param str fn_name: The name of the function to look up.
        :param FunctionRole role: The role in which the function is used.
                                  Defaults to FunctionRole.VALUE.
        :param type model: The current model that is operated on. Defaults to None.
        :return: The callable function
        :rtype: Callable
        :raises AttributeError: When no function is found by the given name.
        :raises ValueError: When the function is used in an invalid `role` or
                            for a not supported `model`.
        """
        if fn_name not in cls.registry:
            raise AttributeError(f"Unknown function '{fn_name}'!")

        func, meta = cls.registry[fn_name]

        if meta.models and model and model not in meta.models:
            raise ValueError(f"Function '{fn_name}' cannot be used for {model.__name__}")

        if role != meta.role:
            raise ValueError(f"Function '{fn_name}' must be used as a(n) {meta.role.name.title()}")

        return func

    @classmethod
    def get_functions_for(cls, model: "django.db.models.Model") -> Dict[FunctionRole, str]:
        """Returns available functions for a given model.

        :param "django.db.models.Model" model: The current model that is operated on..
        :return: A dictionary of function names where the key is the function role.
        :rtype: list
        """
        return [
            meta for _, meta in cls.registry.values() if not meta.models or model in meta.models
        ]


def nlf_function(fn_name: str = None, **kwargs) -> Callable:
    """Decorator to register custom functions for the filter language.

    :param str fn_name: The name under which the function should be available.
                        Defaults to `__name__` of the function.
    :param type **kwargs: Keyword arguments to
                          :class:`FunctionMeta <django_nlf.types.FunctionMeta>`.
    :return: A decorator function that registers the decorated function.
    :rtype: Callable
    """

    def decorator(func: Callable) -> Callable:
        name = fn_name or func.__name__
        signature = inspect.signature(func)
        meta = FunctionMeta(
            **kwargs,
            name=name,
            params=[p for p in signature.parameters],
            rtype=str(signature.return_annotation),
        )

        FunctionRegistry.register(name, func, meta)

        @wraps(func)
        def wrapper(func: Callable) -> Callable:
            return func

        return wrapper

    return decorator
