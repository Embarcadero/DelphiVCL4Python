import sys, platform, os, sys
import importlib, importlib.util

def findmodule():
  for fname in os.listdir(dirbname_full):
    print("fname", os.curdir, fname)
    if 'delphivcl' in fname.lower():
      return os.path.basename(fname)
  return None 
          
def new_import():
    dirbname_full = os.path.dirname(os.path.abspath(__file__))
    print("diba", dirbname_full)
    loader = importlib.machinery.ExtensionFileLoader("DelphiVCL", os.path.join(dirbname_full, "DelphiVCL.pyd"))
    #lm = loader.load_module()

    #print("ld")
    #print("lm", lm)
    spec = importlib.util.spec_from_file_location("DelphiVCL", os.path.join(dirbname_full, "DelphiVCL.pyd"),
        loader=loader, submodule_search_locations=None)
    ld = loader.create_module(spec)
    #package = importlib.util.module_from_spec(spec)
    sys.modules["delphivcl"] = package
    spec.loader.exec_module(package)
    return package

package = new_import()
