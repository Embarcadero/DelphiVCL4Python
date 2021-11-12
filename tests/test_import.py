import importlib.machinery, importlib.util
import sys

def test_import():
    #from ..delphivcl import *
    # from . import new_import
    from delphivcl import new_import
    ld = new_import(r"C:\Users\lucio\PycharmProjects\DelphiVCL_assessment\DelphiVCL4Python\lib\DelphiVCL_Win64_38\DelphiVCL.pyd")
    assert 0, ld

if __name__ == "__main__":
    test_import()