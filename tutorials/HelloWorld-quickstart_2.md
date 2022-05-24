We discussed the most basic ideas about the `delphivcl` library in the first simplest quickstart. We created an empty GUI application without displaying anything on the Form/GUI window. Also, we didn't use any object-oriented approach to create the GUI application. So, let's expand on those ideas and develop an object-oriented version of that and display a text message.

First, let's look at the code to achieve our idea. You might be able to guess what the below code does as you understood the basics from the first guide.

```python
from delphivcl import *

class GUIApp(Form):

    def __init__(self, owner):
        self.SetProps(Caption = "Welcome")

        self.lblHello = Label(self)
        self.lblHello.SetProps(
            Parent=self,
            Caption="Hello DelphiVCL for Python")

def main():
    Application.Initialize()
    Application.Title = "Hello Delphi VCL"
    app = GUIApp(Application)
    app.Show()
    FreeConsole()
    Application.Run()
    app.Destroy()

main()
```

As you save the above code in a Python file and run it, you'll get the following GUI window with a text message as follows:

![HelloWorld-quickstart](https://user-images.githubusercontent.com/17174106/154672767-b8369bca-b3bf-4359-9a32-43ce53ce0abc.png)


In the following line of the code;

```python
    app = FirstGUIApp(Application)
```

Instead of instantiating the `Form` directly, we instantiated a class - `GUIApp` that inherited the `Form` class. Let's investigate the code in the `GUIApp` class:

```python
class GUIApp(Form):

    def __init__(self, owner):
        self.SetProps(Caption = "Welcome")

        self.lblHello = Label(self)
        self.lblHello.SetProps(
            Parent=self,
            Caption="Hello DelphiVCL for Python")
```

As we instantiated the `GUIApp` using `app = GUIApp(Application)`, the `owner` argument gets assigned with the `Application` object. After that, `Form` uses the `owner` in its initialization and creates an empty Form/GUI window. This `owner` variable can be of any other name as it's just a placeholder of the `Application` object. In the first line of the `GUIApp` initialization, we've set the `Caption` property of the `Form`.

Then we instantiated the `Label` component/class with the instance/object of the `Form` as its parameter using the `self.lblHello = Label(self)` code snippet. We use `Label` to display any single-line text messages. Every component other than `Form` will have a parent and is set using the `Parent` property. The parent holds the child component in it.

In our code, we're setting `Label`'s parent as `Form` using the `Parent=self`. So, now the `Form` object - `app` holds the `Label` object - `lblHello`. Next, the text of the `Label` is set using its `Caption` property. So, the Form/GUI window gets populated by a text message - **Hello DelphiVCL for Python**.

We used all the default positions and sizes of the `Form` and `Label` and didn't handle any events in this guide. However, we shall implement them and introduce some new components in the following advanced quick start guide.
