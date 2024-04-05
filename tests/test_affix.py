"""Main file for unit tests of `affix` module.

Tests were generated with the assistance of Sourcery.ai.

"""

from __future__ import annotations


import pytest
from modify.alter import affix
from modify import configuration

# Assuming the singledispatch has been registered for specific types, e.g., str, list, etc.
# For the purpose of these tests, let's assume registrations for str and list have been made.

@pytest.mark.parametrize("item, prefix, divider, recursive, raise_error, expected", [
    # Happy path tests
    pytest.param("world", "hello", "-", False, False, "hello-world", id="str_simple"),
    pytest.param(["world"], "hello", "-", False, False, ["hello-world"], id="list_simple"),
    pytest.param("world", "hello", "", False, False, "helloworld", id="str_no_divider"),
    pytest.param(["world", "universe"], "hello", "-", True, False, ["hello-world", "hello-universe"], id="list_recursive"),

    # Edge cases
    pytest.param("", "hello", "-", False, False, "hello-", id="str_empty_item"),
    pytest.param("world", "", "-", False, False, "-world", id="str_empty_prefix"),
    pytest.param("world", "hello", "", False, False, "helloworld", id="str_empty_divider"),
    pytest.param([], "hello", "-", False, False, [], id="list_empty"),

    # Error cases
    pytest.param(123, "hello", "-", False, True, TypeError, id="unsupported_type_raise"),
    pytest.param(123, "hello", "-", False, False, "default", id="unsupported_type_no_raise"),
])
def test_add_prefix(item, prefix, divider, recursive, raise_error, expected):
    # Arrange
    configuration._RECURSIVE = recursive
    configuration._RAISE_ERROR = raise_error

    # Act
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            result = affix.add_prefix(item, prefix, divider, recursive=recursive, raise_error=raise_error)
    else:
        result = affix.add_prefix(item, prefix, divider, recursive=recursive, raise_error=raise_error)

    # Assert
    if not isinstance(expected, type):
        assert result == expected


# if __name__ == '__main__':
#     test_add_prefix()
