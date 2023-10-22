"""Functions that convert types.

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

import inspect
from typing import Any

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
