import os                                                                                              
from delphivcl import *                                                                                
                                                                                                       
class ToggleSwitch(Form):                                                                        
    def __init__(self, owner):                                                                         
        self.lblVclStyle = None
        self.cbxVclStyles = None
        self.chkEnabled = None
        self.chkReadOnly = None
        self.chkShowStateCaptions = None
        self.grpAlignment = None
        self.grpColors = None
        self.lblColor = None
        self.lblThumbColor = None
        self.lblFrameColor = None
        self.cbxColor = None
        self.cbxThumbColor = None
        self.cbxFrameColor = None
        self.grpState = None
        self.grpStateCaptions = None
        self.lblCaptionOff = None
        self.lblCaptionOn = None
        self.edtCaptionOff = None
        self.edtCaptionOn = None
        self.TS = None                                                                                    
        self.LoadProps(os.path.join(os.path.dirname(os.path.abspath(__file__)), "ToggleSwitch.pydfm"))  

def main():
    Application.Initialize()
    Application.Title = "Toggle Switch Design Export"
    Main = ToggleSwitch(Application)
    Main.Show()
    FreeConsole()
    Application.Run()
    Main.Destroy()

if __name__ == '__main__':
    main()           
