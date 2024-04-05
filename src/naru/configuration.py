"""Global settings for `modify`.

Contents:
    add_supported_type: adds a supported return type to `modify`.
    set_default_value: sets the global default for `kind` to `value`.
    set_raise_error: sets the global default setting of whether to raise errors.
    set_recursive: sets the global default setting for whether to apply a tool
        recursively to nested items.

To Do:

"""
from __future__ import annotations

import dataclasses
import inspect
import pathlib
from collections.abc import Mapping, MutableSequence, Sequence
from collections.abc import Set as AbstractSet
from typing import Any

_DEFAULT_DICT: Any = {}
_DEFAULT_FLOAT: Any = 0.0
_DEFAULT_LIST: Any = []
_DEFAULT_INT: Any = 0
_DEFAULT_PATH: Any = pathlib.Path.cwd()
_DEFAULT_STR: Any = ''
_DEFAULT_TUPLE: Any = ()
_RAISE_ERROR: bool = True
_RECURSIVE: bool = False
_SUPPORTED_TYPES: dict[type, str] = {
    str: 'str',
    Mapping: 'dict',
    MutableSequence: 'list',
    float: 'float',
    int: 'int',
    pathlib.Path: 'path',
    Sequence: 'tuple',
    AbstractSet: 'set'}


@dataclasses.dataclass
class _MISSING_VALUE:  # noqa: N801
    """Sentinel object for a missing data or parameter.

    This follows the same pattern as the `__MISSING_TYPE` class in the builtin
    dataclasses library.
    https://github.com/python/cpython/blob/3.10/Lib/dataclasses.py#L182-L186

    Because None is sometimes a valid argument or data option, this class
    provides an alternative that does not create the confusion that a default of
    None can sometimes lead to.

    """
    pass  # noqa: PIE790


# MISSING, instance of _MISSING_VALUE, should be used for missing values as an
# alternative to None when None is a valid value for an argument. This provides
# a fuller repr and traceback.
MISSING = _MISSING_VALUE()


def add_supported_type(kind: type, name: str, default: Any) -> None:
    """Adds a supported type.

    This function is only needed if you choose not to raise an error and you are
    using a dispatcher for a new type. In such situations, the `dict` of
    supported types is checked so that the appropriate default return value may
    be identified.

    Args:
        kind: the type to associate with the default value of `default`.
        name: `str` name of the type, which is used for naming the global
            default variable.
        default: default value to return when an error is not raised.

    Raises:
        TypeError: if `kind` is not a class or `name` is not a `str`.

    """
    if isinstance(name, str):
        if inspect.isclass(kind):
            globals()['_SUPPORTED_TYPES'][kind] = name
            default_variable_name = f'_DEFAULT_{name.upper()}'
            globals[default_variable_name] = default
        else:
            raise TypeError('kind must be a class, not an instance')
    else:
        raise TypeError('name argument must be a str')

def set_default_value(kind: str, value: Any) -> None:
    """Sets the global default for `kind` to `value`.

    Args:
        kind: short name of the type for which the default balue should be
            changed.
        value: valuet to assign as the default.

    """
    variable_name = f'_DEFAULT_{kind.upper()}'
    try:
        globals()[variable_name] = value
    except KeyError as error:
        message = f'{kind} is not a recognized type with a stored default value'
        raise ValueError(message) from error

def set_raise_error(raise_error: bool) -> None:
    """Sets the global default setting of whether to raise errors.

    Args:
        raise_error: whether to raise an exception (True) when a function cannot
            complete its task or to return a default value instead (False).

    Raises:
        TypeError: if `raise_error` is not a boolean.

    """
    if isinstance(raise_error, bool):
        globals()['_RAISE_ERROR'] = raise_error
    else:
        raise TypeError('raise_error argument must be a boolean')

def set_recursive(recursive: bool) -> None:
    """Sets the global default setting for whether to apply a tool recursively.

    Args:
        recursive: whether to apply the function to nested items (True).

    Raises:
        TypeError: if `recursive` is not a boolean.

    """
    if isinstance(recursive, bool):
        globals()['_RECURSIVE'] = recursive
    else:
        raise TypeError('recursive argument must be a boolean')
