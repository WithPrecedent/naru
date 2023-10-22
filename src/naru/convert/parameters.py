"""Tools that convert to arg or kwarg formats.

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

from ..modify import modify

if TYPE_CHECKING:
    import datetime


""" General Converters """

def instancify(item: type[Any] | object, **kwargs: Any) -> Any:
    """Returns `item` as an instance with `kwargs` as parameters/attributes.

    If `item` is already an instance, kwargs are added as attributes to the
    existing `item`. This will overwrite any existing attributes of the same
    name.

    Args:
        item (Type[Any] | object)): class to make an instance out of by
            passing kwargs or an instance to add kwargs to as attributes.

    Raises:
        TypeError: if `item` is neither a class nor instance.

    Returns:
        object: a class instance with `kwargs` as attributes or passed as
            parameters (if `item` is a class).

    """
    if inspect.isclass(item):
        return item(**kwargs)
    elif isinstance(item, object):
        for key, value in kwargs.items():
            setattr(item, key, value)
        return item
    else:
        raise TypeError('item must be a class or class instance')

def kwargify(item: type[Any], /, args: tuple[Any]) -> dict[Hashable, Any]:
    """Converts args to kwargs.

    Args:
    item (Type): the item with annotations used to construct kwargs.
        args (tuple): arguments without keywords passed to `item`.

    Raises:
        ValueError: if there are more args than annotations in `item`.

    Returns:
        dict[Hashable, Any]: kwargs based on `args` and `item`.

    """
    annotations = list(item.__annotations__.keys())
    if len(args) > len(annotations):
        raise ValueError('There are too many args for item')
    else:
        return dict(zip(annotations, args))

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

def typify(item: str) -> Sequence[Any] | int | float | bool | str:
    """Converts stings to appropriate, supported datatypes.

    The method converts strings to list (if ', ' is present), int, float,
    or bool datatypes based upon the content of the string. If no
    alternative datatype is found, the item is returned in its original
    form.

    Args:
        item (str): string to be converted to appropriate datatype.

    Returns:
        Sequence[Any] | int | float | bool | str: converted item.

    """
    if not isinstance(item, str):
        return item
    else:
        try:
            return int(item)
        except ValueError:
            try:
                return float(item)
            except ValueError:
                if item.lower() in ['true', 'yes']:
                    return True
                elif item.lower() in ['false', 'no']:
                    return False
                elif ', ' in item:
                    item = item.split(', ')
                    return [typify(i) for i in item]
                else:
                    return item
