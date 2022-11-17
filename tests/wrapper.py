import sys
import pathlib


def dummy_function(name:str, age:int, is_married:bool=False):
    print(name, age, is_married)

if __name__ == "__main__":
    CURRENT_DIR = pathlib.Path(__file__).resolve().parent
    PROJECT_ROOT_DIR = CURRENT_DIR.parent  # .parent if not using pytest
    MODULE_SRC_DIR = PROJECT_ROOT_DIR / 'src'
    
    # adding Folder_2 to the system path
    sys.path.insert(0, str(MODULE_SRC_DIR))
    from function_params_to_argparse import commandline_wrapper

    commandline_wrapper(dummy_function)