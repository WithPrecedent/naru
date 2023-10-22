"""Tools for error processing and returning values.

Contents:

To Do:

"""
from __future__ import annotations

import inspect
from typing import Any

from . import configuration


def _infer_type(item: Any) -> str:
    """Infers type of `item` among supported types.

    This function is only needed when using a dispatcher and the raise error is
    False.

    Args:
        item: _description_

    Returns:
        _description_

    """
    kind = None
    if not inspect.isclass(item):
        item = type(item)
    for key, value in configuration._SUPPORTED_TYPES.items():
        if issubclass(item, key):
            kind = value
            break
    return kind

def _process_return(
    raise_error: bool | configuration.MISSING,
    message: str,
    kind: str | None = None,
    item: type | None = None ) -> Any:
    """Raises error with `message` or returns appropriate default value.

    Args:
        raise_error: whether to raise and error (True) or return a default value
            based on the argument of `kind`. If the argument is
            `configuration.MISSING`, then the global setting for raising errors
            will be used.
        message: error message to use if an error is raised.
        kind: str name of the type to be returned. Defaults to None.
        item: item passed to tool. Defaults to None. `item` is only used if 
            `kind` is None.

    Raises:
        TypeError: if 1) `raise_error` is True or 2) `raise_error` is
            `configuration.MISSING` and the global setting for raising errors is
            True.
        ValueError: if both `kind` and `item` are None.

    """
    if raise_error is configuration.MISSING:
        raise_error = configuration._RAISE_ERROR
    if raise_error:
        return TypeError(message)
    if not kind:
        if not item:
            value_message = 'either the kind or item argument must not be None'
            raise ValueError(value_message)
        kind = _infer_type(item)
        if kind is None:
            raise TypeError(message)
    return getattr(configuration, f'_DEFAULT_{kind.upper()}')

# def _process_return(item: Any, default: Any, kind: str) -> Any:
#     """Returns default or raises exception for a conversion function.

#     Args:
#         item: item for which conversion failed.
#         default: default value to use.
#         kind: name of the type that `item` was to be converted to.

#     Returns:
#         Default value from `default` or, if `default` is MISSING, the
#             appropriate default value for `kind`.

#     """
#     if default is configuration.MISSING:
#         if configuration._RAISE_ERROR:
#             message = (
#                 f'item cannot be converted to {kind} because it is an '
#                 f'unsupported type: {type(item).__name__}')
#             raise TypeError(message)
#         else:
#             default_variable = f'_DEFAULT_{kind.upper()}'
#             try:
#                 return getattr(configuration, default_variable)
#             except AttributeError as error:
#                 message = (
#                     f'{kind} is not a recognized type with a stored '
#                     f'default value')
#                 raise ValueError(message) from error
#     else:
#         return default
