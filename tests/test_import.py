from delphivcl import _utils as delphivcl_utils
def test_find_module():
    module_path = delphivcl_utils.find_module()

def test_import():
    module_path = delphivcl_utils.find_module()
    ld = delphivcl_utils.new_import("DelphiVCL", module_path)
    frm = ld.Form

if __name__ == "__main__":
    test_import()