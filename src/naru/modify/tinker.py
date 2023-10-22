"""Tools that reorganize objects but do not change the object's type.

Contents:
    Dispatchers (tools that call other functions based on type passed):
        capitalify: converts data from a snake case `str` to capital case.
        snakify: converts data from a capital case `str` to snake case.
    Specific Tools:
        capitalify_dict: converts keys in a `dict`-like object to capital case.
        capitalify_list: converts items in a `list`-like object to capital case.
        capitalify_set: converts items in a `set`-like object to capital case.
        capitalify_str: converts a `str` to capital case.
        capitalify_tuple: converts items in a `tuple`-like object to capital
            case.
        snakify_dict: converts keys in a `dict`-like object to snake case.
        snakify_list: converts items in a `list`-like object to snake case.
        snakify_set: converts items in a `set`-like object to snake case.
        snakify_str: converts a `str` to snake case.
        snakify_tuple: converts items in a `tuple`-like object to snake case.
        windowify: Returns a sliding window of a sequence of `length` over
            `item`.

To Do:


"""
from __future__ import annotations

import collections
import itertools
import re
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from collections.abc import Sequence


def capitalify(item: str) -> str:
    """Converts a snake case str to capital case.

    Args:
        item (str): str to convert.

    Returns:
        str: 'item' converted to capital case.

    """
    return item.replace('_', ' ').title().replace(' ', '')

def snakify(item: str) -> str:
    """Converts a capitalized str to snake case.

    Args:
        item (str): str to convert.

    Returns:
        str: 'item' converted to snake case.

    """
    item = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', item)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', item).lower()

def windowify(
    item: Sequence[Any],
    length: int,
    fill_value: Any | None = None,
    step: int | None = 1) -> Sequence[Any]:
    """Returns a sliding window of `length` over `item`.

    This code is adapted from more_itertools.windowed to remove a dependency.

    Args:
        item (Sequence[Any]): sequence from which to return windows.
        length (int): length of window.
        fill_value (Optional[Any]): value to use for items in a window that do
            not exist when length > len(item). Defaults to None.
        step (Optional[Any]): number of items to advance between each window.
            Defaults to 1.

    Raises:
        ValueError: if `length` is less than 0 or step is less than 1.

    Returns:
        Sequence[Any]: windowed sequence derived from arguments.

    """
    if length < 0:
        raise ValueError('length must be >= 0')
    if length == 0:
        yield ()
        return
    if step < 1:
        raise ValueError('step must be >= 1')
    window = collections.deque(maxlen = length)
    i = length
    for _ in map(window.append, item):
        i -= 1
        if not i:
            i = step
            yield tuple(window)
    size = len(window)
    if size < length:
        yield tuple(itertools.chain(
            window, itertools.repeat(fill_value, length - size)))
    elif 0 < i < min(step, length):
        window += (fill_value,) * i
        yield tuple(window)
