[![Python package](https://github.com/santokalayil/function_params_to_argparse/actions/workflows/python-package.yml/badge.svg)](https://github.com/santokalayil/function_params_to_argparse/actions/workflows/python-package.yml)

# function_params_to_argparse
Accessing python functions params from commandline 

Installation:
---
```
pip install git+https://github.com/santokalayil/function_params_to_argparse.git
```

Usage:
---

In your module (eg: main.py), add the function as param to the commandline wrapper function.
```python
from function_params_to_argparse import commandline_wrapper


def add_numbers(n1:int, n2:int, boolean_value:bool, some_string: str):
    return n1+n2, boolean_value, some_string


if __name__ == "__main__":
    out = commandline_wrapper(add_numbers)
    print(out)
```
Now you can arg-parse your function params from commandline like follwing:
```
python3 main.py --n1 2 --n2 3 --boolean_value True --some_string "This is string"
```
Currenly string, int, float and boolean are only supported for argparsing. In all other scenarios, the params will be ignored.


To Do:
---
- web API arg parsing from given function names

Contributions:
---
Contributions are welcome.
