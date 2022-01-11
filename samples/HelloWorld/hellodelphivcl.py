from delphivcl import *


class MainForm(Form):

    def __init__(self, owner):
        self.Caption = "A VCL Form..."
        self.SetBounds(10, 10, 500, 400)
        self.Position = "poScreenCenter"

        self.lblHello = Label(self)
        self.lblHello.SetProps(Parent=self, 
            Caption="Hello DelphiVCL for Python")
        self.lblHello.SetBounds(10, 10, 300, 24)

        self.OnClose = self.__on_form_close


    def __on_form_close(self, sender, action):
        action.Value = caFree


def main():
    Application.Initialize()
    Application.Title = "Hello Python"
    Main = MainForm(Application)
    Main.Show()
    FreeConsole()
    Application.Run()
    Main.Destroy()


main()
