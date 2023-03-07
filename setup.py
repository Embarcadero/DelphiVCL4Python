import setuptools, os, sys, platform, distutils.dir_util
from pathlib import Path

pkgname = "delphivcl"

#Force platform wheel
try:
  from wheel.bdist_wheel import bdist_wheel as _bdist_wheel
  class bdist_wheel(_bdist_wheel):
    def finalize_options(self):
      _bdist_wheel.finalize_options(self)
      self.root_is_pure = ("--universal" in sys.argv)
except ImportError:
  bdist_wheel = None

def get_release_version():
  lcals = locals()
  gbals = globals()
  with open(os.path.join(os.getcwd(), pkgname, "__version__.py"), "rt") as opf:
      opffilecontents = opf.read()
      retvalue = exec(opffilecontents, gbals, lcals)
  versorigstr = lcals["__version__"]
  return versorigstr

pkg_dir = os.path.join(os.curdir, pkgname)
if ("sdist" in sys.argv) or (("bdist_wheel" in sys.argv) and ("--universal" in sys.argv)):
  #sdist deploys all shared libraries
  distutils.dir_util.copy_tree("lib", pkg_dir)
else:
  #Deploy the current platform shared library only
  ossys = platform.system()
  platmac = platform.machine()
  libdir = None
  if ossys == "Windows":
    if (sys.maxsize > 2**32):
      #Win x64
      libdir = "Win64"
    else:
      #Win x86
      libdir = "Win32"

  if libdir:
    distutils.dir_util.copy_tree(os.path.join("lib", libdir), os.path.join(pkg_dir, libdir))
  else:
    raise ValueError("Unsupported platform.")

#Copy the doc files to the package folder into the doc subfolder
if os.path.exists(os.path.join("docs", "xml", "docs.xml")):
  pkg_doc_dir = os.path.join(pkg_dir, "doc")
  if not os.path.exists(pkg_doc_dir):
    os.mkdir(pkg_doc_dir)
  distutils.file_util.copy_file(os.path.join("docs", "xml", "docs.xml"), os.path.join(pkg_doc_dir, "docs.xml"))

#Create the package data.
pkgdata = []
for dir_, _, files in os.walk(pkg_dir):
  for file_name in files:
    rel_dir = os.path.relpath(dir_, pkg_dir)
    rel_file = os.path.join(rel_dir, file_name)
    #Add the shared library.
    if ''.join(Path(rel_file).suffixes) in ['.pyd', '.tds']:
      pkgdata.append(rel_file)
    #Add the doc xml file
    elif (rel_file.endswith('.xml')):
      pkgdata.append(rel_file)

#Read the current version from __version.py__
versnewstr = get_release_version()

with open("README.md", "r") as fh:
  long_description = fh.read()

setuptools.setup(
  name=pkgname,
  version=versnewstr,
  description="Delphi VCL for Python",
  author="Lucas Belo, Jim McKeeth",
  author_email="lucas.belo@live.com",
  long_description=long_description,
  long_description_content_type="text/markdown",
  license="Other/Proprietary License",
  license_files=["LICENSE.md"],
  url="https://github.com/Embarcadero/DelphiVCL4Python",
  python_requires=">=3.6",
  packages=[pkgname],
  package_data={pkgname: pkgdata},
  classifiers=[            
            'Intended Audience :: Developers',
            'Topic :: Software Development',
            'License :: Other/Proprietary License',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
            'Programming Language :: Python :: 3.10',
            'Programming Language :: Python :: 3.11',
            'Programming Language :: Python :: 3 :: Only',
            'Operating System :: Microsoft :: Windows',                        
        ],		
  cmdclass={
    'bdist_wheel': bdist_wheel
  }
)
