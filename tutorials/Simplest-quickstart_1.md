After installing `delphivcl` library using `pip`, let's enter the Python REPL to understand a few essential things. Python has a pre-defined `dir()` function that lists available names in the local scope. So, before importing anything, let's check the available names using the `dir()` function;

```python
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']
```

Now let's import the installed `delphivcl` module to validate its installation and check for the output of the `dir()` function:

```python
>>> import delphivcl
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'delphivcl']
```

In the above output list, we have `delphivcl` as part of the available names in the local scope. In this case, if we need to use any classes or functions avialable in the `delphivcl` module, we should use a dot (`.`) operator after it. Now let's import everything using `*` from the `delphivcl` library and check for the available classes, functions, objects, constants, etc.

```python
>>> from delphivcl import *
>>> dir()
>>> dir()[0:45]
['Abort', 'Action', 'ActionList', 'ActivityIndicator', 'Application', 'BasicAction', 'Bevel', 'BitBtn', 'Bitmap',
'BoundLabel', 'Button', 'Canvas', 'CheckBox', 'Collection', 'ColorBox', 'ComboBox', 'Component', 'ContainedAction',
'ContainedActionList', 'Control', 'ControlBar', 'CreateComponent', 'CustomAction', 'CustomActionList',
'CustomActivityIndicator', 'CustomControl', 'CustomDrawGrid', 'CustomEdit', 'CustomForm', 'CustomGrid',
'CustomMemo', 'CustomStyleServices', 'CustomTabControl', 'CustomToggleSwitch', 'DateTimePicker',
'DelphiDefaultContainer', 'DelphiDefaultIterator', 'DelphiMethod', 'DrawGrid', 'Edit', 'FileOpenDialog', 'Form',
'FreeConsole', 'Graphic', 'GroupBox']
```

To avoid an enormous list of names, we checked for the first 46 elements only using `dir()[0:45]`. Let's check for a few available classes, functions, and objects.

```python
>>> CreateComponent
<built-in function CreateComponent>
>>> Button
<class 'Button'>
>>> Form
<class 'Form'>
>>> Application
<Delphi object of type TApplication at 2033DFE9C30>
```
 
We need to create an instance/object for other classes like `Button` and `Form`. But, `Application` is an instance/object by itself and is ready to be used with dot(`.`) operator. There are so many classes and functions but only one object called `Application` is readily available as part of our import. The `Application` object/instance is the source of all GUI applications that we create.

Let's now create a simple GUI application. The code for it is;

```python
from delphivcl import *

Application.Initialize()
Application.Title = "Hello Delphi VCL"
app = Form(Application)
app.SetProps(Caption = "Welcome")
app.Show()
FreeConsole()
Application.Run()
app.Destroy()
```

Using the above code, we just create an empty GUI app. Please save the above code and run it to see the following output:

![Simplest-quickstart](https://user-images.githubusercontent.com/17174106/154675584-761a3076-8b0d-45a9-a2e6-2e439c724ca1.png)


Let's explore and understand the functionality of the code;

```python
from delphivcl import *

Application.Initialize()
Application.Title = "Hello Delphi VCL"
```
At first, we import everything from `delphivcl`. Then, we initialized the application and set a title for it. Later, we create the GUI Application window using the following code;

```python
app = Form(Application)
app.SetProps(Caption = "Welcome")
```

We can to refer all the classes as part of the import as **components**. The `Form` is a special component and is different from all other components that create the GUI window and contain all other components. We instantiated the `Form` with `Application` as a parameter in the above code and assigned it to the `app` object. All the components, including `Form`, has a method `setProps()` to set their properties. Here we've set the name that appears on the title bar of the Form/GUI window using the `Caption` property.

Let's look at the following few lines of the code;

```python
app.Show()
FreeConsole()
Application.Run()
app.Destroy()
```

As we created the application and set its properties, we shall show it on the screen using the `app.show()` code snippet. GUI applications run in interaction with the command window (console). To make the GUI perform better without lags, we use `FreeConsole()` to give primary control to the GUI interface. `Application.Run()` starts the GUI interaction loop between the GUI and the user of the GUI application. When we close the GUI application, `app.Destroy()` takes care of not crashing it.
