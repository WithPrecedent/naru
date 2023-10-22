"""Tools that convert to `str` types.

Contents:
    stringify: converts to or validates a str.
    int_to_str
    float_to_str
    list_to_str
    none_to_str
    path_to_str
    datetime_to_str

To Do:

"""
from __future__ import annotations

import functools
from collections.abc import Iterable, Sequence
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    import datetime
    import pathlib


""" General Converter """

@functools.singledispatch
def stringify(item: Any, /, default: Any | None = None) -> Any:
    """Converts `item` to a str from a Sequence.

    Args:
        item (Any): item to convert to a str from a list if it is a list.
        default (Any): value to return if `item` is equivalent to a null
            value when passed. Defaults to None.

    Raises:
        TypeError: if `item` is not a str or list-like object.

    Returns:
        Any: str, if item was a list, None or the default value if a null value
            was passed, or the item as it was passed if there previous two
            conditions don't appply.

    """
    if item is None:
        if default is None:
            return ''
        elif default in ['None', 'none']:
            return None
        else:
            return default
    elif isinstance(item, str):
        return item
    elif isinstance(item, Sequence):
        return ', '.join(item)
    else:
        raise TypeError('item must be str or a sequence')

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
