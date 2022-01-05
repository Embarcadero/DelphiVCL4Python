import setuptools, os, sys, json, platform, shutil, distutils.dir_util
from pathlib import Path
from setuptools.command.install import install
from setuptools.command.develop import develop

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

class BaseInstallCommand(object):
  #Install arguments (not supported by wheels) for local installation
  #Used by --install-option
  #  --install-option="--python-home=my_python_home"
  user_options = [
    ('python-home=', None, 'The Python home path'),
    ('python-bin=', None, 'Python program name directory'),
    ('python-lib=', None, 'Python shared library directory'),
  ]

  def initialize_options(self):
    super().initialize_options()
    self.python_home = ''
    self.python_bin = ''
    self.python_lib = ''
    self.python_ver = f"{sys.version_info.major}.{sys.version_info.minor}"

  def finalize_options(self):
    super().finalize_options()

  def run(self):
    moduledefs = {
      "python_home": self.python_home,
      "python_bin": self.python_bin,
      "python_lib": self.python_lib,
      "python_ver": self.python_ver,
    }
    moduledefs_path = os.path.join(os.path.join(os.curdir, pkgname), 'moduledefs.json')
    with open(moduledefs_path, 'w+') as openfile:
       openfile.write(json.dumps(moduledefs))

    super().run()

class InstallCommand(BaseInstallCommand, install):
  user_options = getattr(install, 'user_options', []) + BaseInstallCommand.user_options

class DevelopCommand(BaseInstallCommand, develop):
  user_options = getattr(develop, 'user_options', []) + BaseInstallCommand.user_options

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

#Create the package data.
pkgdata = []
for dir_, _, files in os.walk(pkg_dir):
  for file_name in files:
    rel_dir = os.path.relpath(dir_, pkg_dir)
    rel_file = os.path.join(rel_dir, file_name)
    if ''.join(Path(rel_file).suffixes) in ['.pyd']:
      pkgdata.append(rel_file)
print(pkgdata)
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
  python_requires=">=3.3<=3.10",
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
            'Programming Language :: Python :: 3 :: Only',
            'Operating System :: Microsoft :: Windows',                        
        ],		
  cmdclass={
    'bdist_wheel': bdist_wheel,
    'install': InstallCommand,
    'develop': DevelopCommand,
  }
)
