"""Tools that convert to `list` or `tuple` types.

Contents:
    dictify: converts to or validates a dict.
    hashify: converts to or validates a hashable object.
    instancify: converts to or validates an instance. If it is already an
        instance, any passed kwargs are added as attributes to the instance.
    integerify: converts to or validates an int.
    iterify: converts to or validates an iterable.
    kwargify: uses annotations to turn positional arguments into keyword
        arguments.
    listify: converts to or validates a list.
    namify: returns hashable name for passed item.
    numify: converts to or validates a numerical type.
    pathlibify: converts to or validates a pathlib.Path.
    stringify: converts to or validates a str.
    tuplify: converts to or validates a tuple.
    typify: converts a str type to other common types, if possible.
    windowify: Returns a sliding window of `length` over `item`.
    to_dict:
    to_index
    str_to_index
    to_int
    str_to_int
    float_to_int
    to_list
    str_to_list
    to_float
    int_to_float
    str_to_float
    to_path
    str_to_path
    to_str
    int_to_str
    float_to_str
    list_to_str
    none_to_str
    path_to_str
    datetime_to_str

To Do:
    Add more flexible tools.

"""
from __future__ import annotations

import ast
import functools
import pathlib
from collections.abc import Iterable, MutableSequence
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    import datetime


""" General Converters """

@functools.singledispatch
def iterify(item: Any, /) -> Iterable:
    """Returns `item` as an iterable, but does not iterate str types.

    Args:
        item (Any): item to turn into an iterable

    Returns:
        Iterable: of `item`. A str type will be stored as a single item in an
            Iterable wrapper.

    """
    if item is None:
        return iter(())
    elif isinstance(item, (str, bytes)):
        return iter([item])
    else:
        try:
            return iter(item)
        except TypeError:
            return iter((item,))

@functools.singledispatch
def listify(item: Any, /, default: Any | None = None) -> Any:
    """Returns passed item as a list (if not already a list).

    Args:
        item (Any): item to be transformed into a list to allow proper
            iteration.
        default (Optional[Any]): the default value to return if `item` is None.
            Unfortunately, to indicate you want None to be the default value,
            you need to put `None` in quotes. If not passed, `default` is set to
            [].

    Returns:
        Any: a passed list, `item` converted to a list, or the `default`
            argument.

    """
    if item is None:
        if default is None:
            return []
        elif default in ['None', 'none']:
            return None
        else:
            return default
    elif isinstance(item, MutableSequence) and not isinstance(item, str):
        return item
    else:
        return [item]

@functools.singledispatch
def tuplify(item: Any, /, default: Any | None = None) -> Any:
    """Returns passed item as a tuple (if not already a tuple).

    Args:
        item (Any): item to be transformed into a tuple.
        default (Any): the default value to return if `item` is None.
            Unfortunately, to indicate you want None to be the default value,
            you need to put `None` in quotes. If not passed, `default`
            is set to ().

    Returns:
        tuple[Any]: a passed tuple, `item` converted to a tuple, or
            `default`.

    """
    if item is None:
        if default is None:
            return ()
        elif default in ['None', 'none']:
            return None
        else:
            return default
    elif isinstance(item, tuple):
        return item
    elif isinstance(item, Iterable):
        return tuple(item)
    else:
        return (item,)

""" Specific Converters """

def to_list(item: Any, /) -> list[Any]:
    """Converts `item` to a list.

    Args:
        item (Any): item to convert to a list.

    Raises:
        TypeError: if `item` is a type that is not registered.

    Returns:
        list[Any]: derived from `item`.

    """
    if isinstance(item, list[Any]):
        return item
    else:
        raise TypeError(
            f'item cannot be converted because it is an unsupported type: '
            f'{type(item).__name__}')

# @to_list.register
def str_to_list(item: str, /) -> list[Any]:
    """[summary]

    Args:
        item (str): [description]

    Returns:
        list[Any]: [description]
    """
    """Converts a str to a list."""
    return ast.literal_eval(item)

# @camina.dynamic.dispatcher
def to_float(item: Any, /) -> float:
    """Converts `item` to a float.

    Args:
        item (Any): item to convert to a float.

    Raises:
        TypeError: if `item` is a type that is not registered.

    Returns:
        float: derived from `item`.

    """
    if isinstance(item, float):
        return item
    else:
        raise TypeError(
            f'item cannot be converted because it is an unsupported type: '
            f'{type(item).__name__}')

# @to_float.register
def int_to_float(item: int, /) -> float:
    """[summary]

    Args:
        item (int): [description]

    Returns:
        float: [description]
    """
    """Converts an int to a float."""
    return float(item)

# @to_float.register
def str_to_float(item: str, /) -> float:
    """[summary]

    Args:
        item (str): [description]

    Returns:
        float: [description]
    """
    """Converts a str to a float."""
    return float(item)

# @camina.dynamic.dispatcher
def to_path(item: Any, /) -> pathlib.Path:
    """Converts `item` to a pathlib.Path.

    Args:
        item (Any): item to convert to a pathlib.Path.

    Raises:
        TypeError: if `item` is a type that is not registered.

    Returns:
        pathlib.Path: derived from `item`.

    """
    if isinstance(item, pathlib.Path):
        return item
    else:
        raise TypeError(
            f'item cannot be converted because it is an unsupported type: '
            f'{type(item).__name__}')

@to_path.register
def str_to_path(item: str, /) -> pathlib.Path:
    """[summary]

    Args:
        item (str): [description]

    Returns:
        pathlib.Path: [description]
    """
    """Converts a str to a pathlib.Path."""
    return pathlib.pathlib.Path(item)

# @camina.dynamic.dispatcher
def to_str(item: Any, /) -> str:
    """Converts `item` to a str.

    Args:
        item (Any): item to convert to a str.

    Raises:
        TypeError: if `item` is a type that is not registered.

    Returns:
        str: derived from `item`.

    """
    if isinstance(item, str):
        return item
    else:
        raise TypeError(
            f'item cannot be converted because it is an unsupported type: '
            f'{type(item).__name__}')

# @to_str.register
def int_to_str(item: int, /) -> str:
    """[summary]

    Args:
        item (int): [description]

    Returns:
        str: [description]
    """
    """Converts an int to a str."""
    return str(item)

# @to_str.register
def float_to_str(item: float, /) -> str:
    """[summary]

    Args:
        item (float): [description]

    Returns:
        str: [description]
    """
    """Converts an float to a str."""
    return str(item)

# @to_str.register
def list_to_str(item: list[Any], /) -> str:
    """[summary]

    Args:
        item (list[Any]): [description]

    Returns:
        str: [description]
    """
    """Converts a list to a str."""
    return ', '.join(item)

# @to_str.register
def none_to_str(item: None, /) -> str:
    """[summary]

    Args:
        item (None): [description]

    Returns:
        str: [description]
    """
    """Converts None to a str."""
    return 'None'

# @to_str.register
def path_to_str(item: pathlib.Path, /) -> str:
    """Converts a pathlib.Path to a str.

    Args:
        item (pathlib.Path): [description]

    Returns:
        str: [description]

    """
    return str(item)

# @to_str.register
def datetime_to_string(
    item: datetime.datetime, /,
    time_format: str | None = '%Y-%m-%d_%H-%M') -> str:
    """Return datetime `item` as a str based on `time_format`.

    Args:
        item (datetime.datetime): datetime object to convert to a str.
        time_format (Optional[str]): format to create a str from datetime. The
            passed argument should follow the rules of datetime.strftime.
            Defaults to '%Y-%m-%d_%H-%M'.

    Returns:
        str: converted datetime `item`.

    """
    return item.strftime(time_format)
