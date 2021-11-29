import setuptools, os, sys, platform, shutil

#Force platform wheel
try:
  from wheel.bdist_wheel import bdist_wheel as _bdist_wheel
  class bdist_wheel(_bdist_wheel):
    def finalize_options(self):
      _bdist_wheel.finalize_options(self)
      self.root_is_pure = False
except ImportError:
  bdist_wheel = None
  
#Find sys/machine file
def buildfilepath():
  ossys = platform.system()
  platmac = platform.machine()
  platmacshort = ""
  sfilename = ""
  #print("OS:", ossys, "Machine", platmac)
  if ossys == "Windows":
    sfilename = "DelphiVCL.pyd"
    if platmac.endswith('64'):
      #Win x64	
      platmacshort = "Win64"
    else:
      #Win x86
      platmacshort = "Win32"
    
  if not platmacshort:
    raise ValueError("Undetermined platform.")
    
  return f"DelphiVCL_{platmacshort}{os.sep}{sfilename}"

#Copy target file from lib to pkg folder
def copylibfiletopkg(slibfile, spkgfile): 
  spkgdirname = os.path.dirname(spkgfile)
  if not os.path.exists(spkgdirname):
    os.makedirs(spkgdirname)
  shutil.copy(slibfile, spkgfile)

#Validate lib paths
def validatelibpaths(slibdir, slibfile):
  #print(f"Check for lib dir: {slibdir}")    
  if not os.path.exists(f"{slibdir}"):
    raise ValueError(f"Invalid lib path: {slibdir}")
    
  #print(f"Check for lib path: {slibfile}")
  if not os.path.exists(slibfile):
    raise ValueError(f"File not found: {slibfile}")
  
#Validate pkg paths
def validatepkgpaths(spkgfile):
  #print(f"Check for pkg path: {spkgfile}")
  if not os.path.exists(spkgfile):
    raise ValueError(f"File not found {spkgfile}")
    
#Clear pkg files (trash)
def clearpkgtrashfiles():
  sdir = os.path.join(os.curdir, "delphivcl")
  files = os.listdir(sdir)
  filtered_files = [file for file in files if file.endswith(".so") or file.endswith(".pyd")]
  for file in filtered_files:
    fpath = os.path.join(sdir, file)
    #print("Removing trash file:", fpath)
    os.remove(fpath)
    
def finddistfile():
  sdir = os.path.join(os.curdir, "delphivcl")  
  for fname in os.listdir(sdir):
    if 'DelphiVCL' in fname:
      return os.path.basename(fname)
  return None  
    
def copylibfile():
  spath = buildfilepath()
  sfilename = os.path.basename(spath)

  slibdir = os.path.join(os.curdir, "lib")
  slibfile = os.path.join(slibdir, spath)
  
  spkgdir = os.path.join(os.curdir, "delphivcl")
  spkgfile = os.path.join(spkgdir, sfilename)
 
  clearpkgtrashfiles()	  
  validatelibpaths(slibdir, slibfile)
  copylibfiletopkg(slibfile, spkgfile)
  validatepkgpaths(spkgfile)     
  
  return sfilename   
  
def get_release_version():
    """Creates a new version incrementing by 1 the number of build specified in the
    DelphiVCL-0-01/__version__.py file."""
    lcals = locals()
    gbals = globals()
    with open(os.path.join(os.getcwd(), "delphivcl", "__version__.py"), "rt") as opf:
        opffilecontents = opf.read()
        retvalue = exec(opffilecontents, gbals, lcals)
    versorigstr = lcals["__version__"]
    return versorigstr

extra_args = {}
#We don't want to share the compiled files via sdist (we don't have them)
if not ("sdist" in sys.argv):  
  slibdir = os.path.join(os.curdir, "lib")
  #Binary distribution
  if ("bdist_wheel" in sys.argv) and os.path.exists(slibdir):
    bdata = copylibfile()
    extra_args = {'package_data': {"delphivcl": [bdata]}}
  else:
    #Final user installation
    bdata = finddistfile()
    if bdata:
      extra_args = {'package_data': {"delphivcl": [bdata]}}      
    
versnewstr = get_release_version()   

with open("README.md", "r") as fh:
  long_description = fh.read()    

setuptools.setup(
  name="delphivcl",
  version=versnewstr,
  description="Delphi VCL for Python",
  author="Lucas Belo, Jim McKeeth",
  author_email="lucas.belo@live.com",
  long_description=long_description,
  long_description_content_type="text/markdown",
  license="Other/Proprietary License",
  license_files=["LICENSE.md"],
  url = "https://github.com/Embarcadero/DelphiVCL4Python",
  packages=["delphivcl"],    
  classifiers=[
            'Development Status :: 1 - Planning',
            'Intended Audience :: Developers',
            'Topic :: Software Development',
            'License :: Other/Proprietary License',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
            'Programming Language :: Python :: 3 :: Only',
            'Operating System :: Microsoft :: Windows',                        
        ],		
  cmdclass={'bdist_wheel': bdist_wheel},
  **extra_args
)
