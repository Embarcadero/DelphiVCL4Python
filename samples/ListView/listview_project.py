# ---------------------------------------------------------------------------------
# Name:       listview_project.py
# Purpose:    DelphiVCL for Python sample
#
# Author:     lmbelo, Priyatham
#
# Created:    08/28/2023
# Copyright:  2020-2023 Embarcadero Technologies, Inc.
# License:    https://github.com/Embarcadero/DelphiVCL4Python/blob/main/LICENSE.md
# ---------------------------------------------------------------------------------

from delphivcl import *
from listview_unit import ListViewForm

def main():
    Application.Initialize()
    Application.Title = 'List View Sample'
    MainForm = ListViewForm(Application)
    MainForm.Show()
    FreeConsole()
    Application.Run()

if __name__ == '__main__':
    main()
