"""Tools that convert to Hashable types.

Contents:
    hashify: converts to or validates a hashable object.
    dict_to_hash: converts a `dict` to a `tuple` with keys and values.
    list_to_hash: converts a `list` to a `tuple` of its values.

To Do:

"""

from __future__ import annotations

import functools
from collections.abc import Hashable, MutableMapping, MutableSequence
from typing import Any

from ..configuration import MISSING

""" General Converter """

@functools.singledispatch
def hashify(item: Any, /, default: Any = MISSING) -> Hashable:
    """Converts `item` to a Hashable.

    Args:
        item (Any): item to convert to a Hashable.

    Raises:
        TypeError: if `item` is a type that is not registered.

    Returns:
        Hashable: derived from 'item'.

    """
    if isinstance(item, Hashable):
        return item
    else:
        raise TypeError(
        f'item cannot be converted because it is an unsupported type: '
        f'{type(item).__name__}')

""" Specific Converters """

@hashify.register(MutableMapping)
def dict_to_hash(item: MutableMapping[Hashable, Any]) -> Hashable:
    """Converts `item` to a Hashable tuple with keys and values.

    Args:
        item: item to convert to a Hashable.

    Returns:
        Hashable tuple with keys and values derived from `item`.

    """
    keys, values = tuple(item.keys()), tuple(item.values())
    return tuple(keys, values)


@hashify.register(MutableSequence)
def list_to_hash(item: MutableSequence[Any]) -> Hashable:
    """Converts `item` to a Hashable tuple with keys and values.

    Args:
        item: item to convert to a Hashable.

    Returns:
        Hashable tuple with keys and values derived from `item`.

    """
    return tuple(item)
