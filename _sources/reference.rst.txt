Reference Manual
================

This reference manual details classes, functions, and variables included in
DelphiVCL, describing what they are and what they do. For learning how to use
DelphiVCL, see :doc:`quickstart`.  For a list of changes since the last release, see
the :doc:`changelog`.

.. warning:: The pages linked to here are currently a work in progress.

Inheritance Graphs
------------------


delphivcl.Object
****************

.. inheritance-diagram::
   delphivcl.Object
   delphivcl.Persistent
   delphivcl.Stream
   delphivcl.CustomStyleServices
   delphivcl.Monitor
   delphivcl.StyleManager
   :parts: 1
   :top-classes: delphivcl.Object

delphivcl.Persistent
********************

.. inheritance-diagram::
   delphivcl.Persistent
   delphivcl.Component
   delphivcl.Picture
   delphivcl.Strings
   delphivcl.Collection
   delphivcl.Canvas
   delphivcl.Bitmap
   delphivcl.Icon
   delphivcl.Metafile

delphivcl.Component
*******************

.. inheritance-diagram::
   delphivcl.Component
   delphivcl.Timer
   delphivcl.SaveDialog
   delphivcl.MenuItem
   delphivcl.PopupMenu
   delphivcl.MainMenu
   delphivcl.FileOpenDialog
   delphivcl.ActionList
   delphivcl.Label
   delphivcl.MediaPlayer
   delphivcl.ActivityIndicator
   delphivcl.ToggleSwitch
   delphivcl.BoundLabel
   delphivcl.WinControl
   delphivcl.BindingsList
   delphivcl.BasicBindComponent
   delphivcl.Action
   delphivcl.CustomAction
   delphivcl.PrototypeBindSource
   :parts: 1
   :top-classes: delphivcl.Component

delphivcl.BasicBindComponent
****************************

.. inheritance-diagram::
   delphivcl.BasicBindComponent
   delphivcl.LinkPropertyToField
   delphivcl.LinkControlToField
   delphivcl.LinkListControlToField
   :parts: 1
   :top-classes: delphivcl.BasicBindComponent

delphivcl.WinControl
********************

.. inheritance-diagram::
   delphivcl.TrackBar
   delphivcl.ToolBar
   delphivcl.TabSheet
   delphivcl.StaticText
   delphivcl.SpinButton
   delphivcl.ScrollBar
   delphivcl.RadioButton
   delphivcl.RadioGroup
   delphivcl.Panel
   delphivcl.PageControl
   delphivcl.Page
   delphivcl.Notebook
   delphivcl.ListBox
   delphivcl.LabeledEdit
   delphivcl.Header
   delphivcl.GroupBox
   delphivcl.DateTimePicker
   delphivcl.TabControl
   delphivcl.StatusBar
   delphivcl.Form
   delphivcl.SpinEdit
   delphivcl.Edit
   delphivcl.NumberBox
   delphivcl.Memo
   delphivcl.StringGrid
   delphivcl.ControlBar
   delphivcl.ComboBox
   delphivcl.ColorBox
   delphivcl.CheckBox
   delphivcl.BitBtn
   delphivcl.Button
   :parts: 1
   :top-classes: delphivcl.WinControl

delphivcl.Stream
****************

.. inheritance-diagram::
   delphivcl.StringStream
   delphivcl.ResourceStream
   delphivcl.BufferedFileStream
   :parts: 1
   :top-classes: delphivcl.Stream

.. delphivcl
.. *********

.. .. inheritance-diagram::
..    delphivcl.Action
..    delphivcl.ActionList
..    delphivcl.ActivityIndicator
..    delphivcl.BaseBindScopeComponent
..    delphivcl.BaseLinkingBindSource
..    delphivcl.BaseObjectBindSource
..    delphivcl.BasicAction
..    delphivcl.BasicBindComponent
..    delphivcl.Bevel
..    delphivcl.BindComponentDelegate
..    delphivcl.BindingsList
..    delphivcl.BitBtn
..    delphivcl.Bitmap
..    delphivcl.BoundLabel
..    delphivcl.BufferedFileStream
..    delphivcl.Button
..    delphivcl.BytesStream
..    delphivcl.Canvas
..    delphivcl.CheckBox
..    delphivcl.Collection
..    delphivcl.ColorBox
..    delphivcl.ComboBox
..    delphivcl.Component
..    delphivcl.ContainedAction
..    delphivcl.ContainedActionList
..    delphivcl.ContainedBindComponent
..    delphivcl.Control
..    delphivcl.ControlBar
..    delphivcl.CustomAction
..    delphivcl.CustomActionList
..    delphivcl.CustomActivityIndicator
..    delphivcl.CustomBindingsList
..    delphivcl.CustomControl
..    delphivcl.CustomDrawGrid
..    delphivcl.CustomEdit
..    delphivcl.CustomForm
..    delphivcl.CustomGrid
..    delphivcl.CustomLinkControlToField
..    delphivcl.CustomLinkListControlToField
..    delphivcl.CustomLinkPropertyToField
..    delphivcl.CustomMemo
..    delphivcl.CustomMemoryStream
..    delphivcl.CustomNumberBox
..    delphivcl.CustomPrototypeBindSource
..    delphivcl.CustomStatusBar
..    delphivcl.CustomStyleServices
..    delphivcl.CustomTabControl
..    delphivcl.CustomToggleSwitch
..    delphivcl.DateTimePicker
..    delphivcl.DelphiDefaultContainer
..    delphivcl.DelphiDefaultIterator
..    delphivcl.DelphiMethod
..    delphivcl.DrawGrid
..    delphivcl.Edit
..    delphivcl.FileOpenDialog
..    delphivcl.FileStream
..    delphivcl.Form
..    delphivcl.Graphic
..    delphivcl.GroupBox
..    delphivcl.HandleStream
..    delphivcl.Header
..    delphivcl.Icon
..    delphivcl.Image
..    delphivcl.Label
..    delphivcl.LabeledEdit
..    delphivcl.LinkControlDelegate
..    delphivcl.LinkControlToField
..    delphivcl.LinkControlToFieldDelegate
..    delphivcl.LinkListControlToField
..    delphivcl.LinkPropertyToField
..    delphivcl.LinkPropertyToFieldDelegate
..    delphivcl.ListBox
..    delphivcl.MainMenu
..    delphivcl.MediaPlayer
..    delphivcl.Memo
..    delphivcl.MemoryStream
..    delphivcl.Menu
..    delphivcl.MenuItem
..    delphivcl.Metafile
..    delphivcl.Monitor
..    delphivcl.Notebook
..    delphivcl.NumberBox
..    delphivcl.Object
..    delphivcl.OpenDialog
..    delphivcl.Page
..    delphivcl.PageControl
..    delphivcl.PaintBox
..    delphivcl.Panel
..    delphivcl.PascalInterface
..    delphivcl.PascalRecord
..    delphivcl.Persistent
..    delphivcl.Picture
..    delphivcl.Point
..    delphivcl.PopupMenu
..    delphivcl.PrototypeBindSource
..    delphivcl.RadioButton
..    delphivcl.RadioGroup
..    delphivcl.Rect
..    delphivcl.ResourceStream
..    delphivcl.SaveDialog
..    delphivcl.ScrollBar
..    delphivcl.Shape
..    delphivcl.Size
..    delphivcl.SpeedButton
..    delphivcl.SpinButton
..    delphivcl.SpinEdit
..    delphivcl.Splitter
..    delphivcl.StaticText
..    delphivcl.StatusBar
..    delphivcl.Stream
..    delphivcl.StringGrid
..    delphivcl.StringStream
..    delphivcl.Strings
..    delphivcl.StyleInfo
..    delphivcl.StyleManager
..    delphivcl.TabControl
..    delphivcl.TabSheet
..    delphivcl.Timer
..    delphivcl.ToggleSwitch
..    delphivcl.ToolBar
..    delphivcl.ToolButton
..    delphivcl.TrackBar
..    delphivcl.VarParameter
..    delphivcl.WinControl
..    :parts: 1
..    :top-classes: delphivcl.Object


Module Index
************

.. toctree::
   :maxdepth: 2

   reference_index/delphivcl_classes


