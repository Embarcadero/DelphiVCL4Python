import os                                                                                              
from delphivcl import *                                                                                
                                                                                                       
class MainForm(Form):                                                                        
    def __init__(self, owner):                                                                         
        self.Label1 = None
        self.Image1 = None
        self.Panel1 = None
        self.Button1 = None
        self.Button2 = None
        self.Memo1 = None
        self.Panel2 = None
        self.SpeedButton1 = None
        self.Edit1 = None
        self.CheckBox1 = None
        self.ComboBox1 = None
        self.ScrollBar1 = None
        self.ActionList1 = None
        self.actSpeedButton = None
        self.MainMenu1 = None
        self.File1 = None
        self.Exit1 = None                                                                                    
        self.LoadProps(os.path.join(os.path.dirname(os.path.abspath(__file__)), "MainForm.pydfm")) 

def main():
    Application.Initialize()
    Application.Title = "Hello Python"
    Main = MainForm(Application)
    Main.Show()
    FreeConsole()
    Application.Run()
    Main.Destroy()

if __name__ == '__main__':
    main()          
