"""Tools that convert to numerical types.

Contents:
    integerify: converts to or validates an int.
    numify: converts to or validates a numerical type.
    str_to_int
    float_to_int
    int_to_float
    str_to_float

To Do:

"""
from __future__ import annotations

import ast
import collections
import functools
import inspect
import itertools
import pathlib
from collections.abc import (
    Hashable,
    Iterable,
    MutableMapping,
    MutableSequence,
    Sequence,
)
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    import datetime


""" General Converters """

@functools.singledispatch
def integerify(item: Any, /) -> int:
    """Converts `item` to an int.

    Args:
        item (Any): item to convert.

    Raises:
        TypeError: if `item` is a type that cannot be converted.

    Returns:
        int: derived from `item`.

    """
    if isinstance(item, int):
        return item
    else:
        raise TypeError(
            f'item cannot be converted because it is an '
            f'unsupported type: {type(item).__name__}')


@functools.singledispatch
def numify(item: Any, raise_error: bool = False) -> int | float | Any:
    """Converts `item` to a numeric type.

    If `item` cannot be converted to a numeric type and `raise_error` is False,
        `item` is returned as is.

    Args:
        item (str): item to be converted.
        raise_error (bool): whether to raise a TypeError when conversion to a
            numeric type fails (True) or to simply return `item` (False).
            Defaults to False.

    Raises:
        TypeError: if `item` cannot be converted to a numeric type and
            `raise_error` is True.

    Returns:
        int | float | Any: converted to numeric type, if possible.

    """
    try:
        return int(item)
    except ValueError:
        try:
            return float(item)
        except ValueError:
            if raise_error:
                raise TypeError(
                    f'{item} not able to be converted to a numeric type')
            else:
                return item

""" Specific Converters """

@integerify.register
def float_to_int(item: float, /) -> int:
    """Converts `item` to an int.

    Args:
        item (float): item to convert.

    Returns:
        int: derived from `item`.

    """
    return int(item)

@integerify.register
def str_to_int(item: str, /) -> int:
    """Converts `item` to an int.

    Args:
        item (str): item to convert.

    Returns:
        int: derived from `item`.

    """
    return int(item)

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

def int_to_float(item: int, /) -> float:
    """[summary]

    Args:
        item (int): [description]

    Returns:
        float: [description]
    """
    """Converts an int to a float."""
    return float(item)

def str_to_float(item: str, /) -> float:
    """[summary]

    Args:
        item (str): [description]

    Returns:
        float: [description]
    """
    """Converts a str to a float."""
    return float(item)
