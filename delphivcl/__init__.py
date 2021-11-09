import sys, platform, os, sys
import importlib, importlib.util


def find_module():
    pfarch = platform.architecture()

    dir_last_level = f"DelphiVCL_{pfarch[0]}_{sys.version_info.major}{sys.version_info.minor}"
    dirbname_full = os.path.join(os.path.dirname(__file__), dir_last_level)

    for fname in os.listdir(dirbname_full):
        if 'delphivcl' in fname.lower():
            return os.path.basename(fname)
    return None


def new_import(internal_name="delphivcl"):
    dirbname_full = os.path.dirname(os.path.abspath(__file__))
    internal_name = "DelphiVCL"
    assert 0, dirbname_full
    loader = importlib.machinery.ExtensionFileLoader(internal_name, os.path.join(dirbname_full, "DelphiVCL.pyd"))
    spec = importlib.util.spec_from_file_location(internal_name, os.path.join(dirbname_full, "DelphiVCL.pyd"),
        loader=loader, submodule_search_locations=None)
    package = importlib.util.module_from_spec(spec)
    sys.modules["delphivcl"] = package
    spec.loader.exec_module(package)
    return package

package = new_import()
