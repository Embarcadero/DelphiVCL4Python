import importlib, os, sys, platform

def new_import(internal_name="delphivcl", module_full_path=None):
    internal_name = "DelphiVCL"
    if module_full_path is None:
        dirbname_full = os.path.dirname(os.path.abspath(__file__))
        module_full_path = os.path.join(dirbname_full, "DelphiVCL.pyd")
    loader = importlib.machinery.ExtensionFileLoader(internal_name, module_full_path)
    spec = importlib.util.spec_from_file_location(internal_name, module_full_path,
        loader=loader, submodule_search_locations=None)
    package = importlib.util.module_from_spec(spec)
    sys.modules["delphivcl"] = package
    spec.loader.exec_module(package)
    return package

def find_module():
    platmac = platform.machine()
    if platmac.endswith('64'):
      # Win x64
      platmacshort = "Win64"
    else:
      # Win x86
      platmacshort = "Win32"

    dir_last_level = f"DelphiVCL_{platmacshort}_{sys.version_info.major}{sys.version_info.minor}"
    my_folder = os.path.dirname(os.path.abspath(os.path.join(os.getcwd(), __file__)))
    dirbname_full = os.path.normpath(os.path.join(my_folder, "..", "lib", dir_last_level))

    for fname in os.listdir(dirbname_full):
        if 'delphivcl' in fname.lower():
            return os.path.join(dirbname_full, fname)
    return None
