# naru

<p align="center">
<img src="https://github.com/WithPrecedent/wonka/blob/main/docs/images/logo.png" alt="logo" style="width:250px;"/>
</p>

| | |
| --- | --- |
| Version | [![PyPI Latest Release](https://img.shields.io/pypi/v/naru.svg?style=for-the-badge&color=steelblue&label=PyPI&logo=PyPI&logoColor=yellow)](https://pypi.org/project/naru/) [![GitHub Latest Release](https://img.shields.io/github/v/tag/WithPrecedent/naru?style=for-the-badge&color=navy&label=GitHub&logo=github)](https://github.com/WithPrecedent/naru/releases)
| Status | [![Build Status](https://img.shields.io/github/actions/workflow/status/WithPrecedent/naru/ci.yml?branch=main&style=for-the-badge&color=cadetblue&label=Tests&logo=pytest)](https://github.com/WithPrecedent/naru/actions/workflows/ci.yml?query=branch%3Amain) [![Development Status](https://img.shields.io/badge/Development-Active-seagreen?style=for-the-badge&logo=git)](https://www.repostatus.org/#active) [![Project Stability](https://img.shields.io/pypi/status/naru?style=for-the-badge&logo=pypi&label=Stability&logoColor=yellow)](https://pypi.org/project/naru/)
| Documentation | [![Hosted By](https://img.shields.io/badge/Hosted_by-Github_Pages-blue?style=for-the-badge&color=navy&logo=github)](https://WithPrecedent.github.io/naru)
| Tools | [![Documentation](https://img.shields.io/badge/MkDocs-magenta?style=for-the-badge&color=deepskyblue&logo=markdown&labelColor=gray)](https://squidfunk.github.io/mkdocs-material/) [![Linter](https://img.shields.io/endpoint?style=for-the-badge&url=https://raw.githubusercontent.com/charliermarsh/Ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/Ruff) [![Dependency Manager](https://img.shields.io/badge/PDM-mediumpurple?style=for-the-badge&logo=affinity&labelColor=gray)](https://PDM.fming.dev) [![Pre-commit](https://img.shields.io/badge/pre--commit-darkolivegreen?style=for-the-badge&logo=pre-commit&logoColor=white&labelColor=gray)](https://github.com/TezRomacH/python-package-template/blob/master/.pre-commit-config.yaml) [![CI](https://img.shields.io/badge/GitHub_Actions-navy?style=for-the-badge&logo=githubactions&labelColor=gray&logoColor=white)](https://github.com/features/actions) [![Editor Settings](https://img.shields.io/badge/Editor_Config-paleturquoise?style=for-the-badge&logo=editorconfig&labelColor=gray)](https://editorconfig.org/) [![Repository Template](https://img.shields.io/badge/snickerdoodle-bisque?style=for-the-badge&logo=cookiecutter&labelColor=gray)](https://www.github.com/WithPrecedent/naru) [![Dependency Maintainer](https://img.shields.io/badge/dependabot-navy?style=for-the-badge&logo=dependabot&logoColor=white&labelColor=gray)](https://github.com/dependabot)
| Compatibility | [![Compatible Python Versions](https://img.shields.io/pypi/pyversions/naru?style=for-the-badge&color=steelblue&label=Python&logo=python&logoColor=yellow)](https://pypi.python.org/pypi/naru/) [![Linux](https://img.shields.io/badge/Linux-lightseagreen?style=for-the-badge&logo=linux&labelColor=gray&logoColor=white)](https://www.linux.org/) [![MacOS](https://img.shields.io/badge/MacOS-snow?style=for-the-badge&logo=apple&labelColor=gray)](https://www.apple.com/macos/) [![Windows](https://img.shields.io/badge/windows-blue?style=for-the-badge&logo=Windows&labelColor=gray&color=orangered)](https://www.microsoft.com/en-us/windows?r=1)
| Stats | [![PyPI Download Rate (per month)](https://img.shields.io/pypi/dm/naru?style=for-the-badge&color=steelblue&label=Downloads%20💾&logo=pypi&logoColor=yellow)](https://pypi.org/project/naru) [![GitHub Stars](https://img.shields.io/github/stars/WithPrecedent/naru?style=for-the-badge&color=navy&label=Stars%20⭐&logo=github)](https://github.com/WithPrecedent/naru/stargazers) [![GitHub Contributors](https://img.shields.io/github/contributors/WithPrecedent/naru?style=for-the-badge&color=navy&label=Contributors%20🙋&logo=github)](https://github.com/WithPrecedent/naru/graphs/contributors) [![GitHub Issues](https://img.shields.io/github/issues/WithPrecedent/naru?style=for-the-badge&color=navy&label=Issues%20📘&logo=github)](https://github.com/WithPrecedent/naru/graphs/contributors) [![GitHub Forks](https://img.shields.io/github/forks/WithPrecedent/naru?style=for-the-badge&color=navy&label=Forks%20🍴&logo=github)](https://github.com/WithPrecedent/naru/forks)
| | |

-----

## What is naru?

*naru (Japanese) なる: to become; to change; to attain*

`naru` gives you tools to modify and transfrom Python data using a universal,
intuitive syntax.

## Why use naru?

Rather than remembering every command and its parameters for modifying and
transforming Python objects, you can simply import `naru` and use the same
syntax and parameters for any supported modification or transforming command.

## Getting started

### Installation

To install `naru`, use `pip`:

```sh
pip install naru
```

### Usage


In this readme and the package documentation:

* "converter": function that changes an item's type.
* "modifier": function that changes an item, but not its type
(although, in a couple cases, a `modifier` will produce more than 1 of the original type).
* "transformer": either a "converter" or "modifier".

### Dispatchers vs Specific Tools

`naru` supports Python's `singledispatch` system. That means you can call the
generic function for transformation and it will call the
appropriate function based on the type of the first positional argument
passed.[^1]

Alternatively, every function called by `naru`'s dispatchers is also callable
directly using a straightforward syntax. For example,
to add a string prefix to every item in a `list` (or `list`-like object), you could call:

```python
add_prefix(your_list, prefix, divider) # divider is optional
```

or:

```python
add_prefix_to_list(your_list, prefix, divider) # divider is optional
```

The dispatchers are just a convenience for shorter calls and require you to
remember less verbiage. However, the specific functions are also included for
effectuate greater
reliability and clarity in your code.

### Dispatchers

| name | effect | supported types | recursive option |
| --- | --- | --- | --- |
| `add_prefix` | Adds `prefix` to `item` with optional `divider` | `dict`, `list`, `set`, `str`, `tuple` | ✅ |
| `add_suffix` | Adds `suffix` to `item` with optional `divider` | `dict`, `list`, `set`, `str`, `tuple` | ✅ |
| `capitalify` | Changes text to capital case | `dict`, `list`, `set`, `str`, `tuple` | ✅ |
| `cleave` | Divides 1 object into 2 objects | `dict`, `list`, `str`, `tuple` | |
| `drop_dunders` | Drops items that begin with 2 underscores | `dict`, `list`, `object`, `str`, `tuple` | |
| `drop_duplicates` | Drops duplicate items | `list`, `str`, `tuple` | |
| `drop_dunders` | Drops items that begin with at least 1 underscore | `dict`, `list`, `object`, `str`, `tuple` | |
| `drop_prefix` | Drops `suffix` from `item` with optional `divider` | `dict`, `list`, `set`, `str`, `tuple` | ✅ |
| `drop_substring` |  Drops `substring` from `item` | `dict`, `list`, `set`, `str`, `tuple` | ✅ |
| `drop_suffix` | Adds `suffix` from `item` with optional `divider` | `dict`, `list`, `set`, `str`, `tuple` | ✅ |
| `separate` | Divides 1 object into *n* objects | `dict`, `list`, `str`, `tuple` | |
| `snakify` | Changes text to snake case | `dict`, `list`, `set`, `str`, `tuple` | ✅ |

### Specific Modifiers

| | `dict` | `list` | `object` | `set` | `str` | `tuple` |
| --- | --- | --- | --- | --- | --- | --- |
| `add_prefix_to_` | ✅ | ✅ | | ✅ | ✅ | ✅ |
| `add_slots_` | | | ✅ | | | |
| `add_suffix_to_` | ✅ | ✅ | | ✅ | ✅ | ✅ |
| `capitalify_` | ✅ | ✅ | | ✅ | ✅ | ✅ |
| `cleave_` | ✅ | ✅ | | | ✅ | ✅ |
| `drop_dunders_from_` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `drop_duplicates_from_` | | ✅ | | | ✅ | ✅ |
| `drop_prefix_from_` | ✅ | ✅ | | ✅ | ✅ | ✅ |
| `drop_privates_from_` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `drop_substring_from_` | ✅ | ✅ | | ✅ | ✅ | ✅ |
| `drop_suffix_from_` | ✅ | ✅ | | ✅ | ✅ | ✅ |
| `separate_` | ✅ | ✅ | | | ✅ | ✅ |
| `snakify_` | ✅ | ✅ | | ✅ | ✅ | ✅ |

## Contributing

Contributors are always welcome. Feel free to grab an [issue](https://www.github.com/WithPrecedent/naru/issues) to work on or make a suggested improvement. If you wish to contribute, please read the [Contribution Guide](https://www.github.com/WithPrecedent/naru/contributing.md) and [Code of Conduct](https://www.github.com/WithPrecedent/naru/code_of_conduct.md).

## Similar Projects

* **`itertools`**:
* **`more-itertools`**:

## Acknowledgments


## License

Use of this repository is authorized under the [Apache Software License 2.0](https://www.github.com/WithPrecedent/naru/blog/main/LICENSE).

[^1]: Python's `singlddispatch` only supports dispatching based on the first
    positional argument. Because `naru` was designed to be lightweight, it uses
    this limited system rather than relying on a more sophisticated dispatching package.