import importlib, os, sys, platform

def new_import(internal_name="delphivcl"):
    dirbname_full = os.path.dirname(os.path.abspath(__file__))
    internal_name = "DelphiVCL"
    module_full_path = os.path.join(dirbname_full, "DelphiVCL.pyd")
    print("mfp", module_full_path)
    loader = importlib.machinery.ExtensionFileLoader(internal_name, module_full_path)
    spec = importlib.util.spec_from_file_location(internal_name, module_full_path,
        loader=loader, submodule_search_locations=None)
    package = importlib.util.module_from_spec(spec)
    sys.modules["delphivcl"] = package
    spec.loader.exec_module(package)
    return package

def find_module():
    pfarch = platform.architecture()

    dir_last_level = f"DelphiVCL_{pfarch[0]}_{sys.version_info.major}{sys.version_info.minor}"
    dirbname_full = os.path.join(os.path.dirname(__file__), dir_last_level)

    for fname in os.listdir(dirbname_full):
        if 'delphivcl' in fname.lower():
            return os.path.basename(fname)
    return None
