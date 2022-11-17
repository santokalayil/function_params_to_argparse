# import function_params_to_argparse_santokalayil
import os, subprocess
import pathlib




def test_commandline_api():
    CURRENT_DIR = pathlib.Path(__file__).resolve().parent
    wrapper_path = CURRENT_DIR / 'wrapper.py'

    cmd = f'''python3 {wrapper_path} --name Santo --age 34 --is_married False'''


    result = subprocess.check_output(args=cmd.split()).decode(encoding='utf-8')
    # print(result.split())

    assert result.split() == '''Santo 34 False'''.split()


# def test_web_api():
#     raise NotImplementedError("WEB API is not implemented")


    


if __name__ == "__main__":
    test_commandline_api()