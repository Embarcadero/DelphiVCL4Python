DelphiVCL4Python - VCL.DesignExport Samples[]()
# DelphiVCL4Python - VCL.DesignExport Samples 


This is a sample set that shows the use of the [Export to Python](https://github.com/Embarcadero/DelphiVCL4Python/tree/main/samples/DesignExport) directly from a Delphi form.
## Contents

* [1 Location](#Location)
* [2 Description](#Description)
* [3 How to Use Samples](#How_to_Use_Samples)

## Location 

You can find the **DesignExport** samples at:

* **GitHub Repository for DelphiVCL4Python:** [https://github.com/Embarcadero/DelphiVCL4Python/tree/main/samples/DesignExport](https://github.com/Embarcadero/DelphiVCL4Python/tree/main/samples/DesignExport)

## Description 

This application demonstrates the [Export to Python](https://github.com/Embarcadero/DelphiVCL4Python/tree/main/samples/DesignExport) routine and shows how to export a Delphi Design form to Python:

## How to Use the Sample 

1. Open the Experts folder and install the **dclDelphiVCLExperts** component: 

* Experts: https://github.com/Embarcadero/DelphiVCL4Python/tree/main/experts

2. Once installed, now you're able to export any TForm descendant.

3. Under **DesignExport/** choose a sample and open the given project.

4. Using the Form View, left window **Structure->||FORM_NAME||** or on the Form Design.

5. Press **right click** and choose **Export to Delphi**.

6. A save dialog is displayed. Save it with the same name of the form (by default) - a .py and .pydfm file will be created.

7. Don't forget to include the app initialization onto your module:

```

    def main():
        Application.Initialize()        
        Application.Title = "DelphiDesignExport"
        MainForm = MainForm(Application)
        MainForm.Show()
        FreeConsole()
        Application.Run()
        MainForm.Destroy()

    if __name__ == '__main__':
        main()
        
```        
        
--------------------        
