"""Tools that divide an object into objects.

Contents:
    Dispatchers (tools that call other functions based on type passed):
        cleave: divides an item into two parts at `divider`.
        separate: divides an item into n+1 parts based at `divider`.
    Specific Tools:
        cleave_str:
        separate_str:

To Do:


"""
from __future__ import annotations

import functools
from typing import Any

""" Dispatchers """

@functools.singledispatch
def cleave(
    item: Any,
    divider: Any, *,
    return_last: bool = True,
    raise_error: bool = False) -> tuple[Any, Any]:
    """Divides `item` into 2 parts based on `divider`.

    Args:
        item: item to be divided.
        divider: item to divide `item` upon.
        return_last: whether to split `item` upon the first (False) or last
            appearance of `divider`.
        raise_error: whether to raise an error if `divider` is not in `item` or
            to return a tuple containing `item` twice.

    Returns:
        Parts of `item` on either side of `divider` unless `divider` is not in
            `item`.

    Raises:
        TypeError: if no registered function supports the type of `item`.

    """
    raise TypeError(f'item is not a supported type for {__name__}')

@functools.singledispatch
def separate(
    item: Any,
    divider: Any, *,
    raise_error: bool = False) -> tuple[Any, ...]:
    """Divides `item` into n+1 parts based on `divider`.

    Args:
        item (Any): item to be divided.
        divider (Any): item to divide `item` upon.
        raise_error (bool): whether to raise an error if `divider` is not in
            `item` or to return a tuple containing `item` twice.

    Raises:
        TypeError: if no registered function supports the type of `item`.

    Returns:
        list[Any, ...]: parts of `item` on either side of `divider` unless
            `divider` is not in `item`.

    """
    raise TypeError(f'item is not a supported type for {__name__}')

""" Specific Tools """

@cleave.register
def cleave_str(
    item: Any,
    divider: Any = '_', *,
    return_last: bool = True,
    raise_error: bool = False) -> tuple[Any, Any]:
    """Divides `item` into 2 parts based on `divider`.

    Args:
        item: item to be divided.
        divider: item to divide `item` upon. Defaults to an underscore.
        return_last: whether to split `item` upon the first (False) or last
            appearance of `divider`.
        raise_error: whether to raise an error if `divider` is not in `item` or
            to return a tuple containing `item` twice.

    Returns:
        Parts of `item` on either side of `divider` unless `divider` is not in
            `item`.

    Raises:
        ValueError: if `divider` is not in `item` and `raise_error` is True.

    """
    if divider in item:
        suffix = item.split(divider)[-1] if return_last else item.split(divider)[0]
        prefix = item[:-len(suffix) - 1]
    elif raise_error:
        raise ValueError(f'{divider} is not in {item}')
    else:
        prefix = suffix = item
    return prefix, suffix

@separate.register
def separate_str(
    item: str, /,
    divider: str = '_',
    raise_error: bool = False) -> list[str]:
    """Divides 'item' into n+1 parts based on 'divider'.

    Args:
        item (str): item to be divided.
        divider (str): item to divide 'item' upon.
        raise_error (bool): whether to raise an error if 'divider' is not in
            'item' or to return a tuple containing 'item' twice.

    Raises:
        ValueError: if 'divider' is not in 'item' and 'raise_error' is True.

    Returns:
        list[str]: parts of 'item' on either side of 'divider' unless 'divider'
            is not in 'item'.

    """
    if divider in item:
        return item.split(divider)
    elif raise_error:
        raise ValueError(f'{divider} is not in {item}')
    else:
        return [item]
