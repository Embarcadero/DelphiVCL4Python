import importlib.machinery, importlib.util
import sys

#from ..delphivcl import *
#from . import new_import
def new_import(ext_file=None):
    if ext_file is None:
        ext_file = r"C:\Users\lucio\anaconda3\envs\DelphiVCL_assessment\lib\site-packages\delphivcl\DelphiVCL.pyd"
    loader = importlib.machinery.ExtensionFileLoader("DelphiVCL", ext_file)
    spec = importlib.util.spec_from_file_location("DelphiVCL", ext_file,
        loader=loader, submodule_search_locations=None)
    #ld = loader.create_module(spec)
    package = importlib.util.module_from_spec(spec)
    assert "delphivcl" in sys.modules, sys.modules.keys()
    return
    return package
    return ld

def test_import():
    ld = new_import(r"C:\Users\lucio\PycharmProjects\DelphiVCL_assessment\DelphiVCL4Python\lib\DelphiVCL_Win64_38\DelphiVCL.pyd")
    assert 0, ld

if __name__ == "__main__":
    test_import()