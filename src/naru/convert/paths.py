"""Tools that convert to `pathlib.Path` types.

Contents:
    pathlibify: converts to or validates a pathlib.Path.
    str_to_path

To Do:

"""
from __future__ import annotations

import functools
import pathlib
from typing import Any

""" General Converter """

@functools.singledispatch
def pathify(item: Any, /) -> pathlib.Path:
    """Converts string `path` to pathlib.Path object.

    Args:
        item (str | pathlib.Path): either a string summary of a path or a
            pathlib.Path object.

    Raises:
        TypeError if `path` is neither a str or pathlib.Path type.

    Returns:
        pathlib.Path object.

    """
    if isinstance(item, pathlib.Path):
        return item
    else:
        raise TypeError(
            f'item cannot be converted because it is an unsupported type: '
            f'{type(item).__name__}')

""" Specific Converters """

@pathify.register
def str_to_path(item: str, /) -> pathlib.Path:
    """[summary]

    Args:
        item (str): [description]

    Returns:
        pathlib.Path: [description]
    """
    return pathlib.Path(item)
