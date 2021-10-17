DelphiVCL4Python - VCL.ActivityIndicator Sample[]()
# DelphiVCL4Python - VCL.ActivityIndicator Sample 


This is a sample that shows the use of the [TActivityIndicator](http://docwiki.embarcadero.com/Libraries/en/Vcl.WinXCtrls.TActivityIndicator) control directly from a Python script.
## Contents



* [1 Location](#Location)
* [2 Description](#Description)
* [3 How to Use the Sample](#How_to_Use_the_Sample)
* [4 Implementation](#Implementation)

* [4.1 ActivityIndicatorForm](#TActivityIndicatorForm)

* [5 Uses](#Uses)
* [6 See Also](#See_Also)


## Location 

You can find the **ActivityIndicator** sample project at:

* **GitHub Repository for DelphiVCL4Python:** [https://github.com/Embarcadero/DelphiVCL4Python/tree/main/samples/ActivityIndicator](https://github.com/Embarcadero/DelphiVCL4Python/tree/main/samples/ActivityIndicator)

## Description 

This application demonstrates the [ActivityIndicator](http://docwiki.embarcadero.com/Libraries/en/Vcl.WinXCtrls.TActivityIndicator) control and shows how to modify its various properties directly from a Python script. The application uses the following controls:

* `ai`: The activity indicator.
* `grp_indicator_size`: Sets the [size](http://docwiki.embarcadero.com/Libraries/en/Vcl.WinXCtrls.TActivityIndicator.IndicatorSize) of the activity indicator.
* `grp_indicator_color`: Sets the [color](http://docwiki.embarcadero.com/Libraries/en/Vcl.WinXCtrls.TActivityIndicator.IndicatorColor) of the activity indicator.
* `grp_indicator_type`: Sets the [type](http://docwiki.embarcadero.com/Libraries/en/Vcl.WinXCtrls.TActivityIndicator.IndicatorType) of the activity indicator.
* `trk_frame_delay`: Sets the [frame delay](http://docwiki.embarcadero.com/Libraries/en/Vcl.WinXCtrls.TActivityIndicator.FrameDelay) of the activity indicator.
* `chk_animate`: Toggles the [Animate](http://docwiki.embarcadero.com/Libraries/en/Vcl.WinXCtrls.TActivityIndicator.Animate) property of the activity indicator.
* `cbx_form_color`: Sets the [Color](http://docwiki.embarcadero.com/Libraries/en/Vcl.Forms.TForm.Color) of the form if the current style is `Windows`.
* `cbx_vcl_styles`: A combo box that allows you to change the style of the application. You can choose between any style that is active in the [Application Appearance - Custom Styles](http://docwiki.embarcadero.com/RADStudio/en/Application_Appearance) options for this project.

## How to Use the Sample 


1. We strongly recommend using PyScripter IDE: 

* SourceForge: https://sourceforge.net/projects/pyscripter/
* GitHub: https://github.com/pyscripter/pyscripter

2. Navigate to the location given above and open:

*  PyScripter IDE: **activityindicator.py**.

3. Under **Tools->Tools** choose **Install Packages with pip**.

4. In the dialog box **Package Name** type **delphivcl**.

5.  Press **Ctrl + F9** or choose **Run > Run**.

6.  Change the different options on the form and test the functionality of the activity indicator. Modify color, size, animation speed and the type of the activity indicator.

## Implementation 


### ActivityIndicatorForm 

On initialization **__init__**, the `__create_comps` creates all the visual components and attatch them to the `ActivityIndicatorForm` form. The `__config_comps` set all visual components properties. The application defines the following event handlers: 

* `__grp_indicator_type_click`: Changes the [type](http://docwiki.embarcadero.com/Libraries/en/Vcl.WinXCtrls.TActivityIndicator.IndicatorType) of the activity indicator.
* `__grp_indicator_size_click`: Changes the [size](http://docwiki.embarcadero.com/Libraries/en/Vcl.WinXCtrls.TActivityIndicator.IndicatorSize) of the activity indicator.
* `__grp_indicator_color_click`: Changes the [color](http://docwiki.embarcadero.com/Libraries/en/Vcl.WinXCtrls.TActivityIndicator.IndicatorColor) of the activity indicator.
* `__cbx_form_color_change`: Changes the [size](http://docwiki.embarcadero.com/Libraries/en/Vcl.WinXCtrls.TActivityIndicator.IndicatorSize) of the activity indicator.
* `__trk_frame_delay_change`: Changes the [frame delay](http://docwiki.embarcadero.com/Libraries/en/Vcl.WinXCtrls.TActivityIndicator.FrameDelay) of the activity indicator.
* `__cbx_vcl_styles_change`: Sets the style for the application.
* `__chk_animate_click`: Enables or disables the animation of the activity indicator.

## Uses 


* [Vcl.WinXCtrls](http://docwiki.embarcadero.com/Libraries/en/Vcl.WinXCtrls)
* [Vcl.Themes](http://docwiki.embarcadero.com/Libraries/en/Vcl.Themes)
* [Vcl.ExtCtrls](http://docwiki.embarcadero.com/Libraries/en/Vcl.ExtCtrls)
* [Vcl.StdCtrls](http://docwiki.embarcadero.com/Libraries/en/Vcl.StdCtrls)
* [Vcl.ComCtrls](http://docwiki.embarcadero.com/Libraries/en/Vcl.ComCtrls)
* [Vcl.Dialogs](http://docwiki.embarcadero.com/Libraries/en/Vcl.Dialogs)

## See Also 


* [Vcl.WinXCtrls.TActivityIndicator](http://docwiki.embarcadero.com/Libraries/en/Vcl.WinXCtrls.TActivityIndicator)
* [VCL Styles Overview](http://docwiki.embarcadero.com/RADStudio/en/VCL_Styles_Overview)

* [Including Bi-directional Functionality in Applications](http://docwiki.embarcadero.com/RADStudio/en/Including_Bi-directional_Functionality_in_Applications)
* [Vcl.Controls.TControl.BiDiMode](http://docwiki.embarcadero.com/Libraries/en/Vcl.Controls.TControl.BiDiMode)

* [Application Appearance](http://docwiki.embarcadero.com/RADStudio/en/Application_Appearance)




