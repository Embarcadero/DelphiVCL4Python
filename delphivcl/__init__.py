import sys
import os
import platform
import importlib
import importlib.machinery
import importlib.util


def find_extension_module():
    py_ver = f"{sys.version_info.major}.{sys.version_info.minor}"
    plat_sys = platform.system()
    lib_dir = None

    if not (py_ver in ["3.6", "3.7", "3.8", "3.9", "3.10", "3.11"]):
        raise ValueError(f"DelphiVCL doesn't support Python{py_ver}.")

    if plat_sys == "Windows":
        if (sys.maxsize > 2**32):
            # Win x64
            lib_dir = "Win64"
        else:
            # Win x86
            lib_dir = "Win32"

    if not lib_dir:
        raise ValueError("Unsupported platform.")

    lib_dir = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), lib_dir)
    if not os.path.exists(lib_dir):
        raise ValueError(
            "DelphiVCL module not found. \
            Try to reinstall the delphivcl package or check for support compatibility.")

    for file_name in os.listdir(lib_dir):
        if 'DelphiVCL' in file_name:
            return os.path.join(lib_dir, os.path.basename(file_name))

    raise ValueError(
        "DelphiVCL module not found. Try to reinstall the delphivcl package.")


def new_import():
    lib_path = find_extension_module()
    loader = importlib.machinery.ExtensionFileLoader("DelphiVCL", lib_path)
    spec = importlib.util.spec_from_file_location("DelphiVCL",
                                                  lib_path,
                                                  loader=loader,
                                                  submodule_search_locations=None)
    loader.create_module(spec)
    package = importlib.util.module_from_spec(spec)
    sys.modules["delphivcl"] = package
    spec.loader.exec_module(package)
    return package


# Import the extension module
package = new_import()
