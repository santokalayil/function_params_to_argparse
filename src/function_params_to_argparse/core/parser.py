import inspect, argparse
from ..config import TYPE_OF_PARAMETERIZATION


def wrapper(function: callable):
    params = inspect.signature(function).parameters

    parser = argparse.ArgumentParser()
    bool_param_list = []
    for param in params:
        param_type = params[param].annotation if params[param].annotation is not inspect._empty else None
        if param_type is None:
            parser.add_argument(f"--{param}", help=f"Function parameter '{param}' (type={param_type})")
        elif param_type in [str, int, float]:
            parser.add_argument(f"--{param}", help=f"Function parameter '{param}' of type", type=param_type)
        elif param_type is bool:
            parser.add_argument(f"--{param}", help=f"Function parameter '{param}' of type")
            bool_param_list.append(param)
        else:
            print(f"The param '{param}' is not of a type which can be accessible via {TYPE_OF_PARAMETERIZATION} args.")
            pass

    params = parser.parse_args().__dict__

    updated_params = dict()
    for key in params.keys():
        if key not in bool_param_list:
            updated_params[key] = params[key]
        else:
            updated_params[key] = True if params[key].upper() == "TRUE" else False if params[key].upper() == "FALSE" else None
            if updated_params[key] is None: 
                raise Exception(f"The value for param '{key}' should either be True or False. Currently given value is '{params[key]}'")



    return function(**updated_params)