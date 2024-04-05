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

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from collections.abc import Hashable


""" General Converters """

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
