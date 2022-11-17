# function_params_to_argparse
Accessing python functions params from commandline 

Installation:
---
```
pip install git+https://github.com/santokalayil/function_params_to_argparse.git
```

Usage:
---
```python
from function_params_to_argparse import commandline_wrapper


def add_numbers(n1:int, n2:int):
    return n1+n2

out = commandline_wrapper(add_numbers)

print(out)
```
Currently the module supports only commandline arg parsing.
Later web API arg parsing also will be done