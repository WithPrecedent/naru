"""Tools that convert to `dict` types.

Contents:
    dictify: converts to or validates a `dict`.
    lists_to_dict: converts two lists of equal length to keys and values in a
        `dict`.
    str_to_dict: attempts to use `ast.literal_eval` to turn a `str` into a
        `dict`.

"""
from __future__ import annotations

import ast
import functools
from collections.abc import Hashable, MutableMapping, Sequence
from typing import Any

""" General Converter """

@functools.singledispatch
def dictify(item: Any, /) -> MutableMapping[Hashable, Any]:
    """Converts `item` to a MutableMapping.

    Args:
        item: item to convert to a MutableMapping.

    Raises:
        TypeError: if `item` is a type that is not registered.

    Returns:
        MutableMapping derived from `item`.

    """
    if isinstance(item, MutableMapping):
        return item
    else:
        raise TypeError(
        f'item cannot be converted because it is an unsupported type: '
        f'{type(item).__name__}')


""" Specific Converters """

@dictify.register(Sequence)
def lists_to_dict(
    item: Sequence[Sequence[Any]]) -> MutableMapping[Hashable, Any]:
    """Converts `item` to a MutableMapping.

    Args:
        item: item to convert to a MutableMapping.

    Returns:
        MutableMapping derived from `item`.

    """
    return dict(zip(item[0], item[1]))


@dictify.register(Sequence)
def str_to_dict(item: str) -> MutableMapping[Hashable, Any]:
    """Converts `item` to a MutableMapping.

    Args:
        item: item to convert to a MutableMapping.

    Raises:
        TypeError: if `item` is converted, but not to a MutableMapping.
        ValueError: if `item` cannot be converted to a `dict`.

    Returns:
        MutableMapping derived from `item`.

    """
    try:
        converted = ast.literal_eval(item)
        if isinstance(converted, MutableMapping):
            return converted
        message = f'{item} could not be converted to a dict'
        raise TypeError(message)
    except ValueError as error:
        message = f'{item} could not be converted to a dict'
        raise ValueError(message) from error
