import importlib.machinery, importlib.util
def new_import(ext_file):
    loader = importlib.machinery.ExtensionFileLoader("DelphiVCL", ext_file)
    spec = importlib.util.spec_from_file_location("DelphiVCL", ext_file,
        loader=loader, submodule_search_locations=None)
    #print("spec", spec, spec.loader, modulefullpath, __file__)
