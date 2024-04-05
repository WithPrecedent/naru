"""Tools that add things to objects.

Contents:
    General Tools (tools that call other functions based on type passed):
        add_prefix: adds a `str` prefix to an item.
        add_suffix: adds a `str` suffix to an item.
    Specific Tools:
        add_prefix_to_dict: adds a `str` prefix to keys in a `dict`-like object.
        add_prefix_to_list: adds a `str` prefix to a `list`-like object.
        add_prefix_to_set: adds a `str` prefix to a `set`-like object.
        add_prefix_to_str: adds a `str` prefix to a `str`.
        add_prefix_tuple: adds a `str` prefix to a `tuple`-like object.
        add_prefix_to_values: adds a `str` prefix to values in a `dict`-like
            object.
        add_slots: adds `__slots__` to a Python `dataclass`.
        add_suffix_to_dict: adds a `str` suffix to keys in a `dict`-like object.
        add_suffix_to_list: adds a `str` suffix to a `list`-like object.
        add_suffix_to_set: adds a `str` suffix to a `set`-like object.
        add_suffix_to_str: adds a `str` suffix to a `str`.
        add_suffix_tuple: adds a `str` suffix to a `tuple`-like object.
        add_suffix_to_values: adds a `str` suffix to values in a `dict`-like
            object.

To Do:


"""
from __future__ import annotations

import dataclasses
import functools
from collections.abc import Mapping, MutableSequence
from collections.abc import Set as AbstractSet
from typing import Any

from .. import configuration, returns

""" Dispatchers """

@functools.singledispatch
def add_prefix(
    item: Any,
    prefix: str,
    divider: str  = '', *,
    recursive: bool | configuration.MISSING = configuration.MISSING,
    raise_error: bool | configuration.MISSING = configuration.MISSING) -> Any:
    """Adds `prefix` to `item` with `divider` in between.

    Args:
        item: item to be modified.
        prefix: prefix to be added to `item`.
        divider: `str` to add between `item` and `prefix`. Defaults to '', which
            means no divider will be added. `divider` is included as a
            convenience for loops, but if you are just making isolated calls,
            you can just add the divider to `prefix`.
        recursive: if `item` is nested, whether to apply the function to all
            nested objects as well (True) or merely the top level object
            (False). Defaults to `configuration.MISSING`, which means the glo
            raised (since there is no matching default value). Defaults tbal
            setting for `_RECURSIVE` will be used.
        raise_error: whether to raise an error (True) or to return a default
            value based on the type of `item` (False), when possible. If the
            dispatcher cannot find an appropriate type, an error is alwayso
            `configuration.MISSING`, which means the global setting for
            `_RAISE_ERROR` will be used.

    Returns:
        Modified item.

    Raises:
        TypeError: if no registered function supports the type of `item`.

    """
    return returns._process_return(
        raise_error = raise_error,
        message = f'item is not a supported type for {__name__}',
        item = item)

@functools.singledispatch
def add_suffix(
    item: Any,
    suffix: str,
    divider: str  = '', *,
    recursive: bool | configuration.MISSING = configuration.MISSING,
    raise_error: bool | configuration.MISSING = configuration.MISSING) -> Any:
    """Adds `prefix` to `item` with `divider` in between.

    Args:
        item: item to be modified.
        suffix: suffix to be added to `item`.
        divider: `str` to add between `item` and `suffix`. Defaults to '', which
            means no divider will be added. `divider` is included as a
            convenience for loops, but if you are just making isolated calls,
            you can just add the divider to `suffix`.
        recursive: if `item` is nested, whether to apply the function to all
            nested objects as well (True) or merely the top level object
            (False). Defaults to `configuration.MISSING`, which means the global
            setting for `_RECURSIVE` will be used.
        raise_error: whether to raise an error (True) or to return a default
            value based on the type of `item` (False), when possible. If the
            dispatcher cannot find an appropriate type, an error is always
            raised (since there is no matching default value). Defaults to
            `configuration.MISSING`, which means the global setting for
            `_RAISE_ERROR` will be used.

    Returns:
        Modified item.

    Raises:
        TypeError: if no registered function supports the type of 'item'.

    """
    return returns._process_return(
        raise_error = raise_error,
        message = f'item is not a supported type for {__name__}',
        item = item)

""" Specific Tools """

@add_prefix.register(str)
def add_prefix_to_str(
    item: Any,
    prefix: str,
    divider: str  = '', *,
    recursive: bool | configuration.MISSING = configuration.MISSING,
    raise_error: bool | configuration.MISSING = configuration.MISSING) -> Any:
    """Adds `prefix` to `item` with `divider` in between.

    Args:
        item: item to be modified.
        prefix: prefix to be added to `item`.
        divider: `str` to add between `item` and `prefix`. Defaults to '', which
            means no divider will be added. `divider` is included as a
            convenience for loops, but if you are just making isolated calls,
            you can just add the divider to `prefix`.
        recursive: ignored for `str` types because they cannot be nested.
        raise_error: whether to raise an error (True) or to return a default
            value based on the type of `item` (False), when possible. If the
            dispatcher cannot find an appropriate type, an error is always
            raised (since there is no matching default value). Defaults to
            `configuration.MISSING`, which means the global setting for
            `_RAISE_ERROR` will be used.

    Returns:
        Modified `str`.

    """
    try:
        return divider.join([prefix, item])
    except TypeError:
        return returns._process_return(
            raise_error = raise_error,
            message = f'item is not a supported type for {__name__}',
            kind = 'str')

@add_prefix.register(Mapping)
def add_prefix_to_dict(
    item: Any,
    prefix: str,
    divider: str  = '', *,
    recursive: bool | configuration.MISSING = configuration.MISSING,
    raise_error: bool | configuration.MISSING = configuration.MISSING) -> Any:
    """Adds `prefix` to `item` with `divider` in between.

    Args:
        item: item to be modified.
        prefix: prefix to be added to `item`.
        divider: `str` to add between `item` and `prefix`. Defaults to '', which
            means no divider will be added. `divider` is included as a
            convenience for loops, but if you are just making isolated calls,
            you can just add the divider to `prefix`.
        recursive: if `item` is nested, whether to apply the function to all
            nested objects as well (True) or merely the top level object
            (False). Defaults to `configuration.MISSING`, which means the global
            setting for `_RECURSIVE` will be used.
        raise_error: whether to raise an error (True) or to return a default
            value based on the type of `item` (False), when possible. If the
            dispatcher cannot find an appropriate type, an error is always
            raised (since there is no matching default value). Defaults to
            `configuration.MISSING`, which means the global setting for
            `_RAISE_ERROR` will be used.

    Returns:
        Modified `dict`.

    """
    try:
        base = type(item)
        kwargs = {'prefix': prefix, 'divider': divider, 'recursive': recursive}
        tool = add_prefix if recursive else add_prefix_to_str
        return base({tool(k, **kwargs): v for k, v in item.items()})
    except TypeError:
        return returns._process_return(
            raise_error = raise_error,
            message = f'item is not a supported type for {__name__}',
            kind = 'dict')

@add_prefix.register(MutableSequence)
def add_prefix_to_list(
    item: Any,
    prefix: str,
    divider: str  = '', *,
    recursive: bool | configuration.MISSING = configuration.MISSING,
    raise_error: bool | configuration.MISSING = configuration.MISSING) -> Any:
    """Adds `prefix` to `item` with `divider` in between.

    Args:
        item: item to be modified.
        prefix: prefix to be added to `item`.
        divider: `str` to add between `item` and `prefix`. Defaults to '', which
            means no divider will be added. `divider` is included as a
            convenience for loops, but if you are just making isolated calls,
            you can just add the divider to `prefix`.
        recursive: if `item` is nested, whether to apply the function to all
            nested objects as well (True) or merely the top level object
            (False). Defaults to `configuration.MISSING`, which means the global
            setting for `_RECURSIVE` will be used.
        raise_error: whether to raise an error (True) or to return a default
            value based on the type of `item` (False), when possible. If the
            dispatcher cannot find an appropriate type, an error is always
            raised (since there is no matching default value). Defaults to
            `configuration.MISSING`, which means the global setting for
            `_RAISE_ERROR` will be used.

    Returns:
        Modified `list`.

    """
    try:
        base = type(item)
        kwargs = {'prefix': prefix, 'divider': divider, 'recursive': recursive}
        tool = add_prefix if recursive else add_prefix_to_str
        return base([tool(i, **kwargs) for i in item])
    except TypeError:
        return returns._process_return(
            raise_error = raise_error,
            message = f'item is not a supported type for {__name__}',
            kind = 'list')

@add_prefix.register(AbstractSet)
def add_prefix_to_set(
    item: Any,
    prefix: str,
    divider: str  = '', *,
    recursive: bool | configuration.MISSING = configuration.MISSING,
    raise_error: bool | configuration.MISSING = configuration.MISSING) -> Any:
    """Adds `prefix` to `item` with `divider` in between.

    Args:
        item: item to be modified.
        prefix: prefix to be added to `item`.
        divider: `str` to add between `item` and `prefix`. Defaults to '', which
            means no divider will be added. `divider` is included as a
            convenience for loops, but if you are just making isolated calls,
            you can just add the divider to `prefix`.
        recursive: if `item` is nested, whether to apply the function to all
            nested objects as well (True) or merely the top level object
            (False). Defaults to `configuration.MISSING`, which means the global
            setting for `_RECURSIVE` will be used.
        raise_error: whether to raise an error (True) or to return a default
            value based on the type of `item` (False), when possible. If the
            dispatcher cannot find an appropriate type, an error is always
            raised (since there is no matching default value). Defaults to
            `configuration.MISSING`, which means the global setting for
            `_RAISE_ERROR` will be used.

    Returns:
        Modified `set`.

    """
    try:
        base = type(item)
        kwargs = {'prefix': prefix, 'divider': divider, 'recursive': recursive}
        tool = add_prefix if recursive else add_prefix_to_str
        return base({tool(i, **kwargs) for i in item})
    except TypeError:
        return returns._process_return(
            raise_error = raise_error,
            message = f'item is not a supported type for {__name__}',
            kind = 'set')

@add_prefix.register(tuple)
def add_prefix_to_tuple(
    item: Any,
    prefix: str,
    divider: str  = '', *,
    recursive: bool | configuration.MISSING = configuration.MISSING,
    raise_error: bool | configuration.MISSING = configuration.MISSING) -> Any:
    """Adds `prefix` to `item` with `divider` in between.

    Args:
        item: item to be modified.
        prefix: prefix to be added to `item`.
        divider: `str` to add between `item` and `prefix`. Defaults to '', which
            means no divider will be added. `divider` is included as a
            convenience for loops, but if you are just making isolated calls,
            you can just add the divider to `prefix`.
        recursive: if `item` is nested, whether to apply the function to all
            nested objects as well (True) or merely the top level object
            (False). Defaults to `configuration.MISSING`, which means the global
            setting for `_RECURSIVE` will be used.
        raise_error: whether to raise an error (True) or to return a default
            value based on the type of `item` (False), when possible. If the
            dispatcher cannot find an appropriate type, an error is always
            raised (since there is no matching default value). Defaults to
            `configuration.MISSING`, which means the global setting for
            `_RAISE_ERROR` will be used.

    Returns:
        Modified `tuple`.

    """
    try:
        kwargs = {'prefix': prefix, 'divider': divider, 'recursive': recursive}
        return tuple(add_prefix_to_list(item, **kwargs))
    except TypeError:
        return returns._process_return(
            raise_error = raise_error,
            message = f'item is not a supported type for {__name__}',
            kind = 'tuple')

def add_prefix_to_values(
    item: Any,
    prefix: str,
    divider: str  = '', *,
    recursive: bool | configuration.MISSING = configuration.MISSING,
    raise_error: bool | configuration.MISSING = configuration.MISSING) -> Any:
    """Adds `prefix` to values in `item` with `divider` in between.

    Args:
        item: item to be modified.
        prefix: prefix to be added to `item`.
        divider: `str` to add between `item` and `prefix`. Defaults to '', which
            means no divider will be added. `divider` is included as a
            convenience for loops, but if you are just making isolated calls,
            you can just add the divider to `prefix`.
        recursive: if `item` is nested, whether to apply the function to all
            nested objects as well (True) or merely the top level object
            (False). Defaults to `configuration.MISSING`, which means the global
            setting for `_RECURSIVE` will be used.
        raise_error: whether to raise an error (True) or to return a default
            value based on the type of `item` (False), when possible. If the
            dispatcher cannot find an appropriate type, an error is always
            raised (since there is no matching default value). Defaults to
            `configuration.MISSING`, which means the global setting for
            `_RAISE_ERROR` will be used.

    Returns:
        Modified `dict`.

    """
    try:
        base = type(item)
        kwargs = {'prefix': prefix, 'divider': divider, 'recursive': recursive}
        tool = add_prefix if recursive else add_prefix_to_str
        return base({k: tool(v, **kwargs) for k, v in item.items()})
    except TypeError:
        return returns._process_return(
            raise_error = raise_error,
            message = f'item is not a supported type for {__name__}',
            kind = 'dict')

def add_slots(
    item: type[dataclasses.dataclass],
    raise_error: bool | configuration.MISSING = configuration.MISSING) -> (
        type[dataclasses.dataclass]):
    """Adds slots to dataclass with default values.

    This function is needed for those that want to use slots with Python
    dataclasses. There is no native support. So, slots have to be added after
    the fact (which cannot be done with ordinary Python classes).

    Derived from code here:
    https://gitquirks.com/ericvsmith/dataclasses/blob/master/dataclass_tools.py

    Args:
        item: dataclass to add slots to.
        raise_error: whether to raise an error (True) or to return `item'
            unmodified (False). Defaults to `configuration.MISSING`, which means 
            the global setting for `_RAISE_ERROR` will be used.

    Returns:
        dataclass with `__slots__` added.

    Raises:
        TypeError: if `__slots__` is already in `item` and the raise error
            settings is True.

    """
    if '__slots__' in item.__dict__:
        if raise_error is configuration.MISSING:
            raise_error = configuration._RAISE_ERROR
        if raise_error:
            raise TypeError(f'{item.__name__} already contains __slots__')
        else:
            return item
    else:
        item_dict = dict(item.__dict__)
        field_names = tuple(f.name for f in dataclasses.fields(item))
        item_dict['__slots__'] = field_names
        for field_name in field_names:
            item_dict.pop(field_name, None)
        item_dict.pop('__dict__', None)
        qualname = getattr(item, '__qualname__', None)
        item = type(item)(item.__name__, item.__bases__, item_dict)
        if qualname is not None:
            item.__qualname__ = qualname
    return item

@add_suffix.register(str)
def add_suffix_to_str(
    item: Any,
    suffix: str,
    divider: str  = '', *,
    recursive: bool | configuration.MISSING = configuration.MISSING,
    raise_error: bool | configuration.MISSING = configuration.MISSING) -> Any:
    """Adds `prefix` to `item` with `divider` in between.

    Args:
        item: item to be modified.
        suffix: suffix to be added to `item`.
        divider: `str` to add between `item` and `suffix`. Defaults to '', which
            means no divider will be added. `divider` is included as a
            convenience for loops, but if you are just making isolated calls,
            you can just add the divider to `suffix`.
        recursive: ignored for `str` types because they cannot be nested.
        raise_error: whether to raise an error (True) or to return a default
            value based on the type of `item` (False), when possible. If the
            dispatcher cannot find an appropriate type, an error is always
            raised (since there is no matching default value). Defaults to
            `configuration.MISSING`, which means the global setting for
            `_RAISE_ERROR` will be used.

    Returns:
        Modified item.

    """
    try:
        return divider.join([item, suffix])
    except TypeError:
        return returns._process_return(
            raise_error = raise_error,
            message = f'item is not a supported type for {__name__}',
            kind = 'str')

@add_suffix.register(Mapping)
def add_suffix_to_dict(
    item: Any,
    suffix: str,
    divider: str  = '', *,
    recursive: bool | configuration.MISSING = configuration.MISSING,
    raise_error: bool | configuration.MISSING = configuration.MISSING) -> Any:
    """Adds `prefix` to `item` with `divider` in between.

    Args:
        item: item to be modified.
        suffix: suffix to be added to `item`.
        divider: `str` to add between `item` and `suffix`. Defaults to '', which
            means no divider will be added. `divider` is included as a
            convenience for loops, but if you are just making isolated calls,
            you can just add the divider to `suffix`.
        recursive: if `item` is nested, whether to apply the function to all
            nested objects as well (True) or merely the top level object
            (False). Defaults to `configuration.MISSING`, which means the global
            setting for `_RECURSIVE` will be used.
        raise_error: whether to raise an error (True) or to return a default
            value based on the type of `item` (False), when possible. If the
            dispatcher cannot find an appropriate type, an error is always
            raised (since there is no matching default value). Defaults to
            `configuration.MISSING`, which means the global setting for
            `_RAISE_ERROR` will be used.

    Returns:
        Modified `dict`.

    """
    try:
        base = type(item)
        kwargs = {'suffix': suffix, 'divider': divider, 'recursive': recursive}
        tool = add_suffix if recursive else add_suffix_to_str
        return base({tool(k, **kwargs): v for k, v in item.items()})
    except TypeError:
        return returns._process_return(
            raise_error = raise_error,
            message = f'item is not a supported type for {__name__}',
            kind = 'dict')

@add_suffix.register(MutableSequence)
def add_suffix_to_list(
    item: Any,
    suffix: str,
    divider: str  = '', *,
    recursive: bool | configuration.MISSING = configuration.MISSING,
    raise_error: bool | configuration.MISSING = configuration.MISSING) -> Any:
    """Adds `prefix` to `item` with `divider` in between.

    Args:
        item: item to be modified.
        suffix: suffix to be added to `item`.
        divider: `str` to add between `item` and `suffix`. Defaults to '', which
            means no divider will be added. `divider` is included as a
            convenience for loops, but if you are just making isolated calls,
            you can just add the divider to `suffix`.
        recursive: if `item` is nested, whether to apply the function to all
            nested objects as well (True) or merely the top level object
            (False). Defaults to `configuration.MISSING`, which means the global
            setting for `_RECURSIVE` will be used.
        raise_error: whether to raise an error (True) or to return a default
            value based on the type of `item` (False), when possible. If the
            dispatcher cannot find an appropriate type, an error is always
            raised (since there is no matching default value). Defaults to
            `configuration.MISSING`, which means the global setting for
            `_RAISE_ERROR` will be used.

    Returns:
        Modified `list`.

    """
    try:
        base = type(item)
        kwargs = {'suffix': suffix, 'divider': divider, 'recursive': recursive}
        tool = add_suffix if recursive else add_suffix_to_str
        return base([tool(i, **kwargs) for i in item])
    except TypeError:
        return returns._process_return(
            raise_error = raise_error,
            message = f'item is not a supported type for {__name__}',
            kind = 'list')

@add_suffix.register(AbstractSet)
def add_suffix_to_set(
    item: Any,
    suffix: str,
    divider: str  = '', *,
    recursive: bool | configuration.MISSING = configuration.MISSING,
    raise_error: bool | configuration.MISSING = configuration.MISSING) -> Any:
    """Adds `prefix` to `item` with `divider` in between.

    Args:
        item: item to be modified.
        suffix: suffix to be added to `item`.
        divider: `str` to add between `item` and `suffix`. Defaults to '', which
            means no divider will be added. `divider` is included as a
            convenience for loops, but if you are just making isolated calls,
            you can just add the divider to `suffix`.
        recursive: if `item` is nested, whether to apply the function to all
            nested objects as well (True) or merely the top level object
            (False). Defaults to `configuration.MISSING`, which means the global
            setting for `_RECURSIVE` will be used.
        raise_error: whether to raise an error (True) or to return a default
            value based on the type of `item` (False), when possible. If the
            dispatcher cannot find an appropriate type, an error is always
            raised (since there is no matching default value). Defaults to
            `configuration.MISSING`, which means the global setting for
            `_RAISE_ERROR` will be used.

    Returns:
        Modified `set`.

    """
    try:
        base = type(item)
        kwargs = {'suffix': suffix, 'divider': divider, 'recursive': recursive}
        tool = add_suffix if recursive else add_suffix_to_str
        return base({tool(i, **kwargs) for i in item})
    except TypeError:
        return returns._process_return(
            raise_error = raise_error,
            message = f'item is not a supported type for {__name__}',
            kind = 'set')

@add_suffix.register(tuple)
def add_suffix_to_tuple(
    item: Any,
    suffix: str,
    divider: str  = '', *,
    recursive: bool | configuration.MISSING = configuration.MISSING,
    raise_error: bool | configuration.MISSING = configuration.MISSING) -> Any:
    """Adds `prefix` to `item` with `divider` in between.

    Args:
        item: item to be modified.
        suffix: suffix to be added to `item`.
        divider: `str` to add between `item` and `suffix`. Defaults to '', which
            means no divider will be added. `divider` is included as a
            convenience for loops, but if you are just making isolated calls,
            you can just add the divider to `suffix`.
        recursive: if `item` is nested, whether to apply the function to all
            nested objects as well (True) or merely the top level object
            (False). Defaults to `configuration.MISSING`, which means the global
            setting for `_RECURSIVE` will be used.
        raise_error: whether to raise an error (True) or to return a default
            value based on the type of `item` (False), when possible. If the
            dispatcher cannot find an appropriate type, an error is always
            raised (since there is no matching default value). Defaults to
            `configuration.MISSING`, which means the global setting for
            `_RAISE_ERROR` will be used.

    Returns:
        Modified `tuple`.

    """
    try:
        kwargs = {'suffix': suffix, 'divider': divider, 'recursive': recursive}
        return tuple(add_suffix_to_list(item, **kwargs))
    except TypeError:
        return returns._process_return(
            raise_error = raise_error,
            message = f'item is not a supported type for {__name__}',
            kind = 'tuple')
