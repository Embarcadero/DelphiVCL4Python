Installation
============

DelphiVCL package distribution is available via `PyPi <https://pypi.org/project/delphivcl/>`__ 
or by downloading the source via GitHub. DelphiVCL is compiled only for Windows platform. 
All Python versions from 3.6 to 3.11 are supported.

Installing DelphiVCL via PIP
****************************

The easiest way to install DelphiVCL is via PIP:

.. code-block:: bash

   pip install delphivcl


Installing DelphiVCL from source
********************************

You can also install manually by downloading or cloning the repository from GitHub:
`github.com/Embarcadero/DelphiVCL4Python <https://github.com/Embarcadero/DelphiVCL4Python/>`__. 
After cloning or downloading, enter the root DelphiVCL4Python folder/directory and open the 
command prompt or Conda prompt with that path. Now install the package using:

.. code-block:: bash

   python setup.py install


Testing the Installation
************************

On your Windows computer, open up the Python REPL either from the Command prompt or the Conda 
prompt. After installing the package using ``pip``, let's enter the Python REPL to understand
a few essential things. Python has a predefined ``dir()`` function that lists available names 
in the local scope. So, before importing anything, let's check the available names using the 
``dir()`` function.

.. code-block:: bash

   >>> dir()
   ['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', 
   '__spec__']

Now let's import the installed ``delphivcl`` module to validate its installation and check for 
the output of the ``dir()`` function:

.. code-block:: bash

   >>> import delphivcl
   >>> dir()
   ['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', 
   '__spec__', 'delphivcl']
