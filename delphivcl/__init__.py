import sys, platform, os, sys, io
import importlib, importlib.util

def init_module_defs():
    pyversionstrshort = f"{sys.version_info.major}.{sys.version_info.minor}"
    with io.open("moduledefs.json", "w+") as moduledefs:
        moduledefs.write(r'{"python_ver":  "@ver"}'.replace('@ver', pyversionstrshort))
   
def new_import():  
    dirbname_full = os.path.dirname(os.path.abspath(__file__))    
    loader = importlib.machinery.ExtensionFileLoader("DelphiVCL", os.path.join(dirbname_full, "DelphiVCL.pyd"))
    spec = importlib.util.spec_from_file_location("DelphiVCL", os.path.join(dirbname_full, "DelphiVCL.pyd"),
        loader=loader, submodule_search_locations=None)
    ld = loader.create_module(spec)
    package = importlib.util.module_from_spec(spec)
    sys.modules["delphivcl"] = package
    spec.loader.exec_module(package)
    return package

init_module_defs()
package = new_import()
