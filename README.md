# Python TDD starter template

Basic folder structure with working test, starter requirements and gitignore.

![CodeQL](https://github.com/lifekaizen/template-python/actions/workflows/codeql-analysis.yml/badge.svg)
![pytest](https://github.com/lifekaizen/template-python/actions/workflows/pytest.yml/badge.svg)

# Usage

Sum numbers:
`python src/main.py sum 2 3 -- -1`

## Dev usage

Spell check:

```sh
cspell "*.md"
```

# Test

Run tests:
`python -m pytest tests`

the

Check types:
`pytype ./src`

# Install

## Update badges

Update URLs to match project.

## Setup virtual environment

```sh
python -m venv venv
source venv/bin/activate
python -m pip install -e .
```

# Architecture choices

## Typing

- MS's Pyright is built into VS Code. So easy to use with IDE, but library not part of repo.

- Google's pytype may do better inference but must be run manually.
-
- mypy / pydantic not scoped for inference

## Style

- use Black as straight out of the box as possible
  - can override with comments in rare cases
- and Prettier for non-Python (i.e. .md)
- Pylint has a setup file from Google to match their style guide
- Use Google Style for general code style

# Setup

- started with simple requirements file
- appears to be good practice to create a module (i.e. for imports)
- and .cfg is more modern, .toml easy to read
- but the pyscaffold is too much for most projects
- so somewhere between basic requirements and a module; moving this repo towards module by default

# Reference

- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
- [pytest docs](https://docs.pytest.org/en/6.2.x/example/index.html)
- [TDD with Python, 2E](https://learning.oreilly.com/library/view/test-driven-development-with/9781491958698/part01.html#part1)
- [Click docs](https://click.palletsprojects.com/en/8.0.x/#documentation)

## Style Guide Notes

```py
module_name = None
package_name = None
_private_module = None

ClassName = None
_PrivateClass = None
ExceptionName = None


def method_name(function_parameter):  # functions, methods
    pass


def _private_method(_private_method_parameter):
    pass


GLOBAL_CONSTANT_NAME = None
CLASS_CONSTANT_NAME = None
_PRIVATE_GLOBAL_CONSTANT = None

global_var_name = None
instance_var_name = None
local_var_name = None
_private_variable = None

i = 0  # counter
e = False  # try/except statements
f = Path()  # file handle in 'with' statements
```
