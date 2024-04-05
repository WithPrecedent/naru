"""Tools that remove things from objects.

Contents:
    General Tools (tools that call other functions based on type passed):
        drop_dunders: removes attributes or data from an item that begin with
            double underscores.
        drop_duplicates: removes duplicates from an item.
        drop_prefix: removes a `str` prefix from an item.
        drop_privates: removes attributes or data from an item that begins with
            at least one underscore.
        drop_substring: removes substring from an item.
        drop_suffix: removes a `str` suffix from an item.
    Specific Tools:
        drop_dunders_from_object: removes items from a class, instance, or
            module if the attribute or variable names begin with double
            underscores.
        drop_dunders_from_dict: removes items from a `dict`-like object if the
            key begins with double underscores.
        drop_dunders_from_list: removes items from a `list`-like object if they
            begin with double underscores.
        drop_duplicates_from_dict: drops duplicates from a `dict`-like object.
        drop_duplicates_from_list: drops duplicates from a `list`-like object.
        drop_duplicates_from_str: drops duplicate letters from a `str`.
        drop_duplicates_tuple: drops duplicates from a `tuple`-like object.
        drop_prefix_from_dict: drops a `str` prefix from a `dict`-like object.
        drop_prefix_from_list: drops a `str` prefix from a `list`-like object.
        drop_prefix_from_set: drops a `str` prefix from a `set`-like object.
        drop_prefix_from_str: drops a `str` prefix from a `str`.
        drop_prefix_tuple: drops a `str` prefix from a `tuple`-like object.
        drop_privates_from_object: removes items from a class, instance, or
            module if the attribute or variable names begin with at least one
            underscores.
        drop_privates_from_dict: removes items from a `dict`-like object if the
            key begins with at least one underscores.
        drop_privates_from_list: removes items from a `list`-like object if they
            begin with at least one underscores.
        drop_substring_from_dict: drops a `str` substring from a `dict`-like
            object.
        drop_substring_from_list: drops a `str` substring from a `list`-like
            object.
        drop_substring_from_set: drops a `str` substring from a `set`-like
            object.
        drop_substring_from_str: drops a `str` substring from a `str`.
        drop_substring_from_tuple: drops a `str` substring from a `tuple`-like
            object.
        drop_suffix_from_dict: drops a `str` suffix from a `dict`-like object.
        drop_suffix_from_list: drops a `str` suffix from a `list`-like object.
        drop_suffix_from_set: drops a `str` suffix from a `set`-like object.
        drop_suffix_from_str: drops a `str` suffix from a `str`.
        drop_suffix_from_tuple: drops a `str` suffix from a `tuple`-like object.

To Do:

"""
from __future__ import annotations

import functools
from collections.abc import Mapping, MutableSequence
from collections.abc import Set as AbstractSet
from typing import Any

from .. import configuration, returns

""" Dispatchers """

@functools.singledispatch
def drop_dunders(item: Any, /) -> Any:
    """Drops items in 'item' beginning with a double underscore.

    Args:
        item (Any): item to modify.

    Returns:
        Any: item with entries dropped beginning with a double underscore.

    Raises:
        TypeError: if 'item' is not a registered type.

    """
    raise TypeError(f'item is not a supported type for {__name__}')

@functools.singledispatch
def drop_duplicates(item: Any, /) -> Any:
    """Deduplicates contents of 'item.

    Args:
        item (Any): item to deduplicate.

    Raises:
        TypeError: if no registered function supports the type of 'item'.

    Returns:
        Any: deduplicated item.

    """
    raise TypeError(f'item is not a supported type for {__name__}')

@functools.singledispatch
def drop_prefix(
    item: Any,
    prefix: str,
    divider: str  = '', *,
    recursive: bool | configuration.MISSING = configuration.MISSING,
    raise_error: bool | configuration.MISSING = configuration.MISSING) -> Any:
    """Adds `prefix` to `item` with `divider` in between.

    Args:
        item: item to be modified.
        prefix: prefix to be dropped from `item`.
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
        Modified item.

    Raises:
        TypeError: if no registered function supports the type of `item`.

    """
    return returns._process_return(
        raise_error = raise_error,
        message = f'item is not a supported type for {__name__}',
        item = item)

@functools.singledispatch
def drop_privates(item: Any, /) -> Any:
    """Drops items in 'item' with names beginning with an underscore.

    Args:
        item (Any): item to modify.

    Returns:
        Any: item with entries dropped beginning with an underscore.

    Raises:
        TypeError: if 'item' is not a registered type.

    """
    raise TypeError(f'item is not a supported type for {__name__}')

@functools.singledispatch
def drop_substring(item: Any, /, substring: str) -> Any:
    """Drops 'substring' from 'item' with a possible 'divider' in between.

    Args:
        item (Any): item to be modified.
        substring (str): substring to be added to 'item'.

    Raises:
        TypeError: if no registered function supports the type of 'item'.

    Returns:
        Any: modified item.

    """
    raise TypeError(f'item is not a supported type for {__name__}')

""" Specific Tools """

@drop_duplicates.register(MutableSequence)
def drop_duplicates_list(item: MutableSequence[Any], /) -> MutableSequence[Any]:
    """Deduplicates contents of 'item.

    Args:
        item (MutableSequence[Any]): item to deduplicate.

    Returns:
        MutableSequence[Any]: deduplicated item.

    """
    base = type(item)
    contents = list(dict.fromkeys(item))
    return base(contents)

@drop_duplicates.register(tuple)
def drop_duplicates_tuple(item: tuple[Any, ...], /) -> tuple[Any, ...]:
    """Deduplicates contents of 'item.

    Args:
        item (tuple[Any, ...]): item to deduplicate.

    Returns:
        tuple[Any, ...]: deduplicated item.

    """
    return tuple(drop_duplicates_list(item))

@drop_dunders.register(Mapping)
def drop_dunders_dict(item: Mapping[str, Any], /) -> Mapping[str, Any]:
    """Drops items in 'item' beginning with a double underscore.

    Args:
        item (Mapping[str, Any]): dict-like object with str keys that might have
            double underscores at the beginning of the key names.

    Returns:
        Mapping[str, Any]: dict-luke object with entries dropped if the key name
            begin with a double underscore.

    """
    base = type(item)
    return base({k: v for k, v in item.items() if not k.startswith('__')})

@drop_dunders.register(MutableSequence)
def drop_dunders_list(
    item: MutableSequence[str | object], /) -> MutableSequence[str | object]:
    """Drops items in 'item' beginning with a double underscore.

    Args:
        item (MutableSequence[str | object]): list-like object with str items or
            names that might have double underscores at their beginnings.

    Returns:
        MutableSequence[str | object]: list-like object with items dropped if
            they or their names begin with a double underscore.

    Raises:
        TypeError: if 'item' does not contain str types or objects with either
            'name' or '__name__' attributes.

    """
    base = type(item)
    if len(item) > 0 and all(isinstance(i, str) for i in item):
        return base([i for i in item if not i.startswith('__')])
    elif len(item) > 0 and all(hasattr(i, 'name') for i in item):
        return base([i for i in item if not i.name.startswith('__')])
    elif len(item) > 0 and all(hasattr(i, '__name__') for i in item):
        return base([i for i in item if not i.__name__.startswith('__')])
    elif len == 0:
        return item
    else:
        raise TypeError(
            'items in item must be str types or have name or __name__ '
            'attributes')

@drop_prefix.register
def drop_prefix_from_str(item: str, /, prefix: str, divider: str = '') -> str:
    """Drops 'prefix' from 'item' with 'divider' in between.

    Args:
        item (str): item to be modified.
        prefix (str): prefix to be added to 'item'.
        divider (str): str to add between 'item' and 'prefix'. Defaults to '',
            which means no divider will be added.

    Returns:
        str: modified str.

    """
    prefix = ''.join([prefix, divider])
    if item.startswith(prefix):
        return item[len(prefix):]
    else:
        return item

@drop_prefix.register(Mapping)
def drop_prefix_from_dict(
    item: Mapping[str, Any], /,
    prefix: str,
    divider: str = '') -> Mapping[str, Any]:
    """Drops 'prefix' from keys in 'item' with 'divider' in between.

    Args:
        item (Mapping[str, Any]): item to be modified.
        prefix (str): prefix to be added to 'item'.
        divider (str): str to add between 'item' and 'prefix'. Defaults to '',
            which means no divider will be added.

    Returns:
        Mapping[str, Any]: modified mapping.

    """
    contents = {
        drop_prefix(item = k, prefix = prefix, divider = divider): v
        for k, v in item.items()}
    return contents if isinstance(item, dict) else item.__class__(contents)

@drop_prefix.register(MutableSequence)
def drop_prefix_from_list(
    item: MutableSequence[str], /,
    prefix: str,
    divider: str = '') -> MutableSequence[str]:
    """Drops 'prefix' from items in 'item' with 'divider' in between.

    Args:
        item (MutableSequence[str]): item to be modified.
        prefix (str): prefix to be added to 'item'.
        divider (str): str to add between 'item' and 'prefix'. Defaults to '',
            which means no divider will be added.

    Returns:
        MutableSequence[str]: modified sequence.

    """
    contents = [
        drop_prefix(item = i, prefix = prefix, divider = divider) for i in item]
    return contents if isinstance(item, list) else item.__class__(contents)

@drop_prefix.register(AbstractSet)
def drop_prefix_from_set(
    item: AbstractSet[str], /,
    prefix: str,
    divider: str = '') -> AbstractSet[str]:
    """Drops 'prefix' from items in 'item' with 'divider' in between.

    Args:
        item (Set[str]): item to be modified.
        prefix (str): prefix to be added to 'item'.
        divider (str): str to add between 'item' and 'prefix'. Defaults to '',
            which means no divider will be added.

    Returns:
        Set[str]: modified set.

    """
    contents = {
        drop_prefix(item = i, prefix = prefix, divider = divider) for i in item}
    return contents if isinstance(item, set) else item.__class__(contents)

@drop_prefix.register(tuple)
def drop_prefix_from_tuple(
    item: tuple[str, ...], /,
    prefix: str,
    divider: str = '') -> tuple[str, ...]:
    """Drops 'prefix' from items in 'item' with 'divider' in between.

    Args:
        item (tuple[str, ...]): item to be modified.
        prefix (str): prefix to be added to 'item'.
        divider (str): str to add between 'item' and 'prefix'. Defaults to '',
            which means no divider will be added.

    Returns:
        tuple[str, ...]: modified tuple.

    """
    return tuple(
        drop_prefix(item=i, prefix=prefix, divider=divider) for i in item)

@drop_privates.register(Mapping)
def drop_privates_dict(item: Mapping[str, Any], /) -> Mapping[str, Any]:
    """Drops items in 'item' with key names beginning with an underscore.

    Args:
        item (Mapping[str, Any]): dict-like object with str keys that might have
            underscores at the beginning of the key names.

    Returns:
        Mapping[str, Any]: dict-luke object with entries dropped if the key name
            begin with an underscore.

    """
    base = type(item)
    return base({k: v for k, v in item.items() if not k.startswith('_')})

@drop_privates.register(MutableSequence)
def drop_privates_list(
    item: MutableSequence[str | object], /) -> MutableSequence[str | object]:
    """Drops items in 'item' with names beginning with an underscore.

    Args:
        item (MutableSequence[str | object]): list-like object with str items or
            names that might have underscores at their beginnings.

    Returns:
        MutableSequence[str | object]: list-like object with items dropped if
            they or their names begin with an underscore.

    Raises:
        TypeError: if 'item' does not contain str types or objects with either
            'name' or '__name__' attributes.

    """
    base = type(item)
    if len(item) > 0 and all(isinstance(i, str) for i in item):
        return base([i for i in item if not i.startswith('_')])
    elif len(item) > 0 and all(hasattr(i, 'name') for i in item):
        return base([i for i in item if not i.name.startswith('_')])
    elif len(item) > 0 and all(hasattr(i, '__name__') for i in item):
        return base([i for i in item if not i.__name__.startswith('_')])
    elif len == 0:
        return item
    else:
        raise TypeError(
            'items in item must be str types or have name or __name__ '
            'attributes')

@drop_substring.register
def drop_substring_from_str(item: str, /, substring: str) -> str:
    """Drops 'substring' from 'item'.

    Args:
        item (str): item to be modified.
        substring (str): substring to be added to 'item'.

    Returns:
        str: modified str.

    """
    return item.replace(substring, '') if substring in item else item

@drop_substring.register(Mapping)
def drop_substring_from_dict(
    item: Mapping[str, Any], /,
    substring: str) -> Mapping[str, Any]:
    """Drops 'substring' from keys in 'item'.

    Args:
        item (Mapping[str, Any]): item to be modified.
        substring (str): substring to be added to 'item'.

    Returns:
        Mapping[str, Any]: modified mapping.

    """
    contents = {
        drop_substring(item = k, substring = substring): v
        for k, v in item.items()}
    return contents if isinstance(item, dict) else item.__class__(contents)

@drop_substring.register(MutableSequence)
def drop_substring_from_list(
    item: MutableSequence[str], /,
    substring: str) -> MutableSequence[str]:
    """Drops 'substring' from items in 'item'.

    Args:
        item (MutableSequence[str]): item to be modified.
        substring (str): substring to be added to 'item'.

    Returns:
        MutableSequence[str]: modified sequence.

    """
    contents = [drop_substring(item = i, substring = substring) for i in item]
    return contents if isinstance(item, list) else item.__class__(contents)

@drop_substring.register(AbstractSet)
def drop_substring_from_set(item: AbstractSet[str], /, substring: str) -> AbstractSet[str]:
    """Drops 'substring' from items in 'item'.

    Args:
        item (Set[str]): item to be modified.
        substring (str): substring to be added to 'item'.

    Returns:
        Set[str]: modified set.

    """
    contents = {drop_substring(item = i, substring = substring) for i in item}
    return contents if isinstance(item, set) else item.__class__(contents)

@drop_substring.register(tuple)
def drop_substring_from_tuple(
    item: tuple[str, ...], /,
    substring: str) -> tuple[str, ...]:
    """Drops 'substring' from items in 'item'.

    Args:
        item (tuple[str, ...]): item to be modified.
        substring (str): substring to be added to 'item'.

    Returns:
        tuple[str, ...]: modified tuple.

    """
    return tuple(drop_substring(item = i, substring = substring) for i in item)

@functools.singledispatch
def drop_suffix(item: Any, /, suffix: str, divider: str = '') -> Any:
    """Drops 'suffix' from 'item' with 'divider' in between.

    Args:
        item (Any): item to be modified.
        suffix (str): suffix to be added to 'item'.

    Raises:
        TypeError: if no registered function supports the type of 'item'.

    Returns:
        Any: modified item.

    """
    raise TypeError(f'item is not a supported type for {__name__}')

@drop_suffix.register
def drop_suffix_from_str(item: str, /, suffix: str, divider: str = '') -> str:
    """Drops 'suffix' from 'item' with 'divider' in between.

    Args:
        item (str): item to be modified.
        suffix (str): suffix to be added to 'item'.

    Returns:
        str: modified str.

    """
    suffix = ''.join([suffix, divider])
    return item.removesuffix(suffix) if item.endswith(suffix) else item

@drop_suffix.register(Mapping)
def drop_suffix_from_dict(
    item: Mapping[str, Any], /,
    suffix: str,
    divider: str = '') -> Mapping[str, Any]:
    """Drops 'suffix' from keys in 'item' with 'divider' in between.

    Args:
        item (Mapping[str, Any]): item to be modified.
        suffix (str): suffix to be added to 'item'.

    Returns:
        Mapping[str, Any]: modified mapping.

    """
    contents = {
        drop_suffix(item = k, suffix = suffix, divider = divider): v
        for k, v in item.items()}
    return contents if isinstance(item, dict) else item.__class__(contents)

@drop_suffix.register(MutableSequence)
def drop_suffix_from_list(
    item: MutableSequence[str], /,
    suffix: str,
    divider: str = '') -> MutableSequence[str]:
    """Drops 'suffix' from items in 'item' with 'divider' in between.

    Args:
        item (MutableSequence[str]): item to be modified.
        suffix (str): suffix to be added to 'item'.

    Returns:
        MutableSequence[str]: modified sequence.

    """
    contents = [
        drop_suffix(item = i, suffix = suffix, divider = divider) for i in item]
    return contents if isinstance(item, list) else item.__class__(contents)

@drop_suffix.register(AbstractSet)
def drop_suffix_from_set(
    item: AbstractSet[str], /,
    suffix: str,
    divider: str = '') -> AbstractSet[str]:
    """Drops 'suffix' from items in 'item' with 'divider' in between.

    Args:
        item (Set[str]): item to be modified.
        suffix (str): suffix to be added to 'item'.

    Returns:
        Set[str]: modified set.

    """
    contents = {
        drop_suffix(item = i, suffix = suffix, divider = divider) for i in item}
    return contents if isinstance(item, set) else item.__class__(contents)

@drop_suffix.register(tuple)
def drop_suffix_from_tuple(
    item: tuple[str, ...], /,
    suffix: str,
    divider: str = '') -> tuple[str, ...]:
    """Drops 'suffix' from items in 'item' with 'divider' in between.

    Args:
        item (tuple[str, ...]): item to be modified.
        suffix (str): suffix to be added to 'item'.

    Returns:
        tuple[str, ...]: modified tuple.

    """
    return tuple(
        drop_suffix(item=i, suffix=suffix, divider=divider) for i in item)
