# DelphiVCL for Python <a href="https://github.com/Embarcadero/DelphiVCL4Python/"><img align="right" alt="DelphiVCL4Python" src="https://github.com/Embarcadero/DelphiVCL4Python/raw/main/images/DelphiVCL4Python(256px).png"></a>
Delphi's VCL library as a Python module for building native Windows GUI Applications

### Installation: ###

    pip install delphivcl   

### Supports: ###

* Win32 & Win64 x86 architectures
* Python cp3.6, cp3.7, cp3.8, cp3.9 and cp3.10

### Conda support: ###

* Win x86 and x64 from Python cp3.6 to cp3.10

### Quickstart Guide: ###

Let us create a **TODO Task Application** to understand some components of GUI Applications.

Let's take a look at the code to achieve that:

``` python
from delphivcl import *

class TodoApp(Form):

    def __init__(self, Owner):
        self.Caption = "A TODO GUI Application"
        self.SetBounds(100, 100, 700, 500)

        self.task_lbl = Label(self)
        self.task_lbl.SetProps(Parent=self, Caption="Enter your TODO task")
        self.task_lbl.SetBounds(10, 10, 300, 25)

        self.task_text_box = Edit(self)
        self.task_text_box.SetProps(Parent=self)
        self.task_text_box.SetBounds(10, 30, 250, 30)

        self.add_task_btn = Button(self)
        self.add_task_btn.Parent = self
        self.add_task_btn.SetBounds(150, 75,100,30)
        self.add_task_btn.Caption = "Add Task"
        self.add_task_btn.OnClick = self.__add_task_on_click

        self.del_task_btn = Button(self)
        self.del_task_btn.Parent = self
        self.del_task_btn.SetBounds(150,120,100,30)
        self.del_task_btn.Caption = "Delete Task"
        self.del_task_btn.OnClick = self.__del_task_on_click

        self.list_of_tasks = ListBox(self)
        self.list_of_tasks.Parent = self
        self.list_of_tasks.SetBounds(300,50,300,350)

        self.OnClose = self.__on_form_close

    def __on_form_close(self, Sender, Action):
        Action.Value = caFree

    def __add_task_on_click(self, Sender):
        self.list_of_tasks.Items.Add(self.task_text_box.Text)
        self.task_text_box.Text = ""

    def __del_task_on_click(self, Sender):
        self.list_of_tasks.Items.Delete(0)

def main():
    Application.Initialize()
    Application.Title = "TODO App"
    Main = TodoApp(Application)
    Main.Show()
    FreeConsole()
    Application.Run()
    Main.Destroy()

main()
```
As you save and run the above code, you should get the following GUI as a result:

![delphiVCL](images/Quickstart_TODO_GUI_1.png)




For other platforms, check out [DelphiFMX4Python](https://github.com/Embarcadero/DelphiFMX4Python).

Powered by the Best [Windows IDE](https://www.embarcadero.com/products/delphi) Embarcadero Delphi and the [Python4Delphi library](https://github.com/pyscripter/python4delphi).
