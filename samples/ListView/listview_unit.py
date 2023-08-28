# ---------------------------------------------------------------------------------
# Name:       listview_unit.py
# Purpose:    DelphiVCL for Python sample
#
# Author:     lmbelo, Priyatham
#
# Created:    08/28/2023
# Copyright:  2020-2023 Embarcadero Technologies, Inc.
# License:    https://github.com/Embarcadero/DelphiVCL4Python/blob/main/LICENSE.md
# ---------------------------------------------------------------------------------

import os
import io
from PIL import Image as PILImg
from delphivcl import *

class ListViewForm(Form):


    def __init__(self, owner):
        self.il_images=ImageList(self)
        self.il_small_images=ImageList(self)
        self.list_view=ListView(self)
        self.memo_evts=Memo(self)
        self.pnl_actions=Panel(self)
        self.pnl_add=Panel(self)
        self.btn_remove_all=Button(self)
        self.btn_remove_selected=Button(self)
        self.pnl_remove=Panel(self)
        self.btn_add_many=Button(self)
        self.btn_add_single=Button(self)
        self.rg_view_style=RadioGroup(self)
        self.gb_options=GroupBox(self)
        self.pnl_sort_type=Panel(self)        
        self.lb_sort_type=Label(self)
        self.cb_sort_type=ComboBox(self)        
        self.cb_checkboxes=CheckBox(self)
        self.cb_column_click=CheckBox(self)
        self.cb_show_work_areas=CheckBox(self)
        self.cb_multi_select=CheckBox(self)
        self.cb_row_select=CheckBox(self)      
        
        # Basic settings
        self.config()
        # Fill default data
        self.fill_data()  
        # Fill up image list
        self.fill_images()

   
    def config(self):
        self.SetProps(
            Parent=self,
            Caption='Form1',
            Left = 0,
            Top = 0,
            Height=700,
            Width=1100,            
            Color=clBtnFace,
            TextHeight=15,
            Position="poDesktopCenter",
            TabOrder=0,
        )

        self.Font.SetProps(
            Charset=1,#DEFAULT_CHARSET
            Color=clWindowText,
            Height=-12,
            Name='Segoe UI',
            Style=[],
        )
        
        self.il_images.SetProps(
            ColorDepth="cd32Bit",
            DrawingStyle="dsTransparent",
            Height=32,
            Width=32,
        )

        self.il_small_images.SetProps(
            ColorDepth="cd32Bit",
            DrawingStyle="dsTransparent",
            Height=16,
            Width=16,
        )

        self.list_view.SetProps(
            Parent=self,
            Width=743,
            Height=416,
            Align="alClient",
            TabOrder=0,
            LargeImages=self.il_images,
            SmallImages=self.il_small_images,
            # Events
            OnAdvancedCustomDraw=self.list_view_advanced_custom_draw,
            OnAdvancedCustomDrawItem=self.list_view_advanced_custom_draw_item,
            OnAdvancedCustomDrawSubItem=self.list_view_advanced_custom_draw_sub_item,
            OnChange=self.list_view_change,
            OnChanging=self.list_view_changing,
            OnClick=self.list_view_click,
            OnColumnClick=self.list_view_column_click,
            OnColumnRightClick=self.list_view_column_right_click,
            OnCompare=self.list_view_compare,
            OnContextPopup=self.list_view_context_popup,
            OnCustomDraw=self.list_view_custom_draw,
            OnCustomDrawItem=self.list_view_custom_draw_item,
            OnCustomDrawSubItem=self.list_view_custom_draw_sub_item,
            OnCreateItemClass=self.list_view_create_item_class,
            OnData=self.list_view_data,
            OnDataFind=self.list_view_data_find,
            OnDataHint=self.list_view_data_hint,
            OnDataStateChange=self.list_view_data_state_change,
            OnDrawItem=self.list_view_draw_item,
            OnEdited=self.list_view_edited,
            OnEditing=self.list_view_editing,
            OnEnter=self.list_view_enter,
            OnGetSubItemImage=self.list_view_get_sub_item_image,
            OnInfoTip=self.list_view_info_tip,
            OnInsert=self.list_view_insert,
            OnKeyDown=self.list_view_key_down,
            OnSelectItem=self.list_view_select_item,
            OnItemChecked=self.list_view_item_checked,
        )

        self.memo_evts.SetProps(
            Parent=self,
            Width=1083,
            Height=152,
            Align="alBottom",
            TabOrder=1,    
        )

        self.pnl_actions.SetProps(
            Parent=self,
            Width=340,
            Height=416,
            Align="alRight",
            BevelOuter="bvNone",
            TabOrder=2,  
        )

        self.pnl_add.SetProps(
            Parent=self.pnl_actions,
            AlignWithMargins=True,
            Left = 3,
            Top = 3,
            Width = 334,
            Height = 41,
            Align="alTop",
            BevelOuter="bvNone",
            TabOrder=0,
        )

        self.btn_add_single.SetProps(
            Parent=self.pnl_add,
            AlignWithMargins=True,
            Left = 3,
            Top = 3,
            Width=160,
            Height=35,
            Align="alLeft",
            Caption='Add Item',
            ImageIndex=0,            
            Images=self.il_images,
            TabOrder=1,
            OnClick=self.do_add_single_click,
        )

        self.btn_add_single.ImageMargins.SetProps(
            Left=20,
        )

        self.btn_add_many.SetProps(
            Parent=self.pnl_add,
            AlignWithMargins=True,
            Left = 169,
            Top = 3,
            Width=160,
            Height=35,
            Align="alLeft",
            Caption='Add Many Items',
            ImageIndex=0,
            Images=self.il_images,
            TabOrder=0,
            OnClick=self.do_add_many_click,
        )

        self.btn_add_many.ImageMargins.SetProps(
            Left=20,
        )

        self.pnl_remove.SetProps(
            Parent=self.pnl_actions,
            AlignWithMargins=True,
            Left = 3,
            Top = 50,
            Width=334,
            Height=41,
            Align="alTop",
            BevelOuter="bvNone",
            TabOrder=0,
        )

        self.btn_remove_selected.SetProps(
            Parent=self.pnl_remove,
            AlignWithMargins=True,
            Left = 3,
            Top = 3,
            Width=160,
            Height=35,
            Align="alLeft",
            Caption='Remove Selected',
            ImageIndex=1,            
            Images=self.il_images,
            TabOrder=1,
            OnClick=self.do_remove_selected,
        )

        self.btn_remove_selected.ImageMargins.SetProps(
            Left=20,
        )

        self.btn_remove_all.SetProps(
            Parent=self.pnl_remove,
            AlignWithMargins=True,
            Left = 169,
            Top = 3,
            Width=160,
            Height=35,
            Align="alLeft",
            Caption='Remove All',
            ImageIndex=1,            
            Images=self.il_images,
            TabOrder=0,
            OnClick=self.do_remove_all,
        )

        self.btn_remove_all.ImageMargins.SetProps(
            Left=20,
        )

        self.rg_view_style.SetProps(
            Parent=self.pnl_actions,
            AlignWithMargins=True,
            Left = 3,
            Top = 97,
            Width=334,
            Height=105,
            Align="alTop",
            Caption='View Stytle',
            Columns=2,            
            TabOrder=2,
            OnClick=self.do_rg_view_style_click
        )

        self.gb_options.SetProps(
            Parent=self.pnl_actions,
            AlignWithMargins=True,
            Left = 3,
            Top = 208,
            Width=334,
            Height=240,
            Align="alTop",
            Caption='Options',
            TabOrder=3,
        )

        self.pnl_sort_type.SetProps(
            Parent=self.gb_options,
            Left=2,
            Top=17,
            Width=330,
            Height=50,
            Align="alTop",
            BevelOuter="bvNone",
            TabOrder=5,
        )

        self.lb_sort_type.SetProps(
            Parent=self.pnl_sort_type,
            AlignWithMargins=True,
            Left=3,
            Top=3,
            Width=324,
            Height=15,
            Align="alTop",
            Caption='Sort Type',            
        )

        self.cb_sort_type.SetProps(
            Parent=self.pnl_sort_type,
            AlignWithMargins=True,            
            Left=3,
            Top=24,
            Width=324,
            Height=23,
            Align="alTop",            
            TabOrder=0,        
            OnChange=self.do_sort_type_change    
        )     

        self.cb_checkboxes.SetProps(
            Parent=self.gb_options,
            AlignWithMargins=True,
            Left=5,
            Top=70,
            Width=324,
            Height=17,
            Align="alTop",
            Caption='Checkboxes',
            TabOrder=0,
            OnClick=self.do_cb_checkboxes,
        )

        self.cb_column_click.SetProps(
            Parent=self.gb_options,
            AlignWithMargins=True,
            Left=5,
            Top=93,
            Width=324,
            Height=17,
            Align="alTop",
            Caption='Column Click',
            TabOrder=1,
            OnClick=self.do_cb_column_click,
        )

        self.cb_show_work_areas.SetProps(
            Parent=self.gb_options,
            AlignWithMargins=True,
            Left=5,
            Top=162,
            Width=324,
            Height=17,
            Align="alTop",
            Caption='Show Work Areas',
            TabOrder=2,
            OnClick=self.do_cb_show_work_areas,
        )

        self.cb_multi_select.SetProps(
            Parent=self.gb_options,
            AlignWithMargins=True,
            Left=5,
            Top=116,
            Width=324,
            Height=17,
            Align="alTop",
            Caption='Multiselect',
            TabOrder=3,
            OnClick=self.do_cb_multi_select,
        )

        self.cb_row_select.SetProps(
            Parent=self.gb_options,
            AlignWithMargins=True,
            Left=5,
            Top=139,
            Width=324,
            Height=17,
            Align="alTop",
            Caption='Row Select',
            TabOrder=4,
            OnClick=self.do_cb_row_select,
        )


    def fill_data(self):
        # ListView Columns
        # Column 1
        col = self.list_view.Columns.Add()
        col.Caption = "First Column"
        col.Width = 100
        # Column 2
        col = self.list_view.Columns.Add()
        col.Caption = "Second Column"
        col.Width = 150
        # Column 3
        col = self.list_view.Columns.Add()
        col.Caption = "Third Column"
        col.Width = 150

        # ListView View Styles
        self.rg_view_style.Items.Add("vsIcon")
        self.rg_view_style.Items.Add("vsList")
        self.rg_view_style.Items.Add("vsReport")
        self.rg_view_style.Items.Add("vsSmallIcon")
        self.rg_view_style.ItemIndex = 0

        # ListView Sort Type
        self.cb_sort_type.Items.Add("stBoth")
        self.cb_sort_type.Items.Add("stData")
        self.cb_sort_type.Items.Add("stNone")
        self.cb_sort_type.Items.Add("stText")
        self.cb_sort_type.ItemIndex = 2


    def png_to_bmp(self, file_path):
        img = PILImg.open(file_path, mode='r')        
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format='BMP')
        byte_arr = img_byte_arr.getvalue()

        return BytesStream(byte_arr)


    def add_image(self, file_path, image_list):
        img_stream = self.png_to_bmp(file_path)
        try:
            bm = Bitmap(image_list.Height, image_list.Width)
            try:
                bm.LoadFromStream(img_stream)
                # Add the image to the image container
                image_list.AddMasked(bm, clNone)
            finally:                        
                bm.Free()
        finally:
            img_stream.Free()


    def fill_images(self):
        base_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images")
        # 32x32 images
        self.add_image(os.path.join(base_path, "add-32.png"), self.il_images)
        self.add_image(os.path.join(base_path, "remove-32.png"), self.il_images)
        self.add_image(os.path.join(base_path, "item-32.png"), self.il_images)
        # 16x16 images
        self.add_image(os.path.join(base_path, "add-16.png"), self.il_small_images)
        self.add_image(os.path.join(base_path, "remove-16.png"), self.il_small_images)
        self.add_image(os.path.join(base_path, "item-16.png"), self.il_small_images)

    
    def add_item(self):
        item = self.list_view.Items.Add()
        item.Caption = 'Item ' + str(self.list_view.Items.Count)
        item.SubItems.Add(item.Caption + ' Subitem 1')
        item.SubItems.Add(item.Caption + ' Subitem 2')
        item.ImageIndex=2


    def do_add_single_click(self, sender):
        self.add_item()


    def do_add_many_click(self, sender):
        for i in range(10):
            self.add_item()


    def do_remove_selected(self, sender):
        self.list_view.DeleteSelected()


    def do_remove_all(self, sender):
        self.list_view.Items.Clear()

    
    def do_rg_view_style_click(self, sender):
        match self.rg_view_style.ItemIndex:
            case 0:
                self.list_view.ViewStyle = "vsIcon"
            case 1:
                self.list_view.ViewStyle = "vsList"
            case 2:
                self.list_view.ViewStyle = "vsReport"
            case 3:
                self.list_view.ViewStyle = "vsSmallIcon"

    
    def do_sort_type_change(self, sender):
        self.list_view.SortType = self.cb_sort_type.Text


    def do_cb_checkboxes(self, sender):
        self.list_view.CheckBoxes = self.cb_checkboxes.Checked


    def do_cb_column_click(self, sender):
        self.list_view.ColumnClick = self.cb_column_click.Checked


    def do_cb_show_work_areas(self, sender):
        self.list_view.ShowWorkAreas = self.cb_show_work_areas.Checked


    def do_cb_multi_select(self, sender):
        self.list_view.Multiselect = self.cb_multi_select.Checked


    def do_cb_row_select(self, sender):
        self.list_view.RowSelect = self.cb_row_select.Checked


    def log_evt(self, log):
        self.memo_evts.Lines.Add(log)


    def list_view_advanced_custom_draw(self, Sender, ARect, Stage, DefaultDraw):
        self.log_evt("list_view_advanced_custom_draw(self, Sender, ARect, Stage, var DefaultDraw)")


    def list_view_advanced_custom_draw_item(self, Sender, Item, State, Stage, DefaultDraw):
        self.log_evt("list_view_advanced_custom_draw_item(self, Sender, Item, State, Stage, var DefaultDraw)")


    def list_view_advanced_custom_draw_sub_item(self, Sender, Item, SubItem, State, Stage, DefaultDraw):
        self.log_evt("list_view_advanced_custom_draw_sub_item(self, Sender, Item, SubItem, State, Stage, var DefaultDraw)")


    def list_view_change(self, Sender, Item, Change):
        self.log_evt("list_view_change(self, Sender, Item, Change)")


    def list_view_changing(self, Sender, Item, Change, AllowChange):
        self.log_evt("list_view_changing(self, Sender, Item, Change, var AllowChange)")     


    def list_view_click(self, Sender):
        self.log_evt("list_view_click(self, Sender)")


    def list_view_column_click(self, Sender, Column):
        self.log_evt("list_view_column_click(self, Sender, Column)")


    def list_view_column_right_click(self, Sender, Column, Point):
        self.log_evt("list_view_column_right_click(self, Sender, Column, Point)")


    def list_view_compare(self, Sender, Item1, Item2, Data, Compare):
        self.log_evt("list_view_compare(self, Sender, Item1, Item2, Data, Compare)")


    def list_view_context_popup(self, Sender, MousePos, Handled):
        self.log_evt("list_view_context_popup(self, Sender, MousePos, var Handled)")


    def list_view_custom_draw(self, Sender, ARect, DefaultDraw):
        self.log_evt("list_view_custom_draw(self, Sender, ARect, var DefaultDraw)")


    def list_view_custom_draw_item(self, Sender, Item, State, DefaultDraw):
        self.log_evt("list_view_custom_draw_item(self, Sender, Item, State, var DefaultDraw)")


    def list_view_custom_draw_sub_item(self, Sender, Item, SubItem, State, DefaultDraw):
        self.log_evt("list_view_custom_draw_sub_item(self, Sender, Item, SubItem, State, var DefaultDraw)")


    def list_view_create_item_class(self, Sender, ItemClass):
        self.log_evt("list_view_create_item_class(self, Sender, var ItemClass)")


    def list_view_data(self, Sender, Item):
        self.log_evt("list_view_data(self, Sender, Item)")


    def list_view_data_find(self, Sender, Find, FindString, FindPosition, FindData, StartIndex, Direction, Wrap, Index):
        self.log_evt("list_view_data_find(self, Sender, Find, FindString, FindPosition, FindData, StartIndex, Direction, Wrap, Index)")


    def list_view_data_hint(self, Sender, StartIndex, EndIndex):
        self.log_evt("list_view_data_hint(self, Sender, StartIndex, EndIndex)")


    def list_view_data_state_change(self, Sender, StartIndex, EndIndex, OldState, NewState):
        self.log_evt("list_view_data_state_change(self, Sender, StartIndex, EndIndex, OldState, NewState)")


    def list_view_draw_item(self, Sender, Item, Rect, State):
        self.log_evt("list_view_draw_item(self, Sender, Item, Rect, State)")


    def list_view_edited(self, Sender, Item, S):
        self.log_evt("list_view_edited(self, Sender, Item, var S)")


    def list_view_editing(self, Sender, Item, AllowEdit):
        self.log_evt("list_view_editing(self, Sender, Item, var AllowEdit)")


    def list_view_enter(self, Sender):
        self.log_evt("list_view_enter(self, Sender)")


    def list_view_get_sub_item_image(self, Sender, Item, SubItem, ImageIndex):
        self.log_evt("list_view_get_sub_item_image(self, Sender, Item, SubItem, var ImageIndex)")


    def list_view_info_tip(self, Sender, Item, InfoTip):
        self.log_evt("list_view_info_tip(self, Sender, Item, var InfoTip)")


    def list_view_insert(self, Sender, Item):
        self.log_evt("list_view_insert(self, Sender, Item)")


    def list_view_key_down(self, Sender, Key, Shift):
        self.log_evt("list_view_key_down(self, Sender, Key, Shift)")


    def list_view_select_item(self, Sender, Item, Selected):
        self.log_evt("list_view_select_item(self, Sender, Item, Selected)")


    def list_view_item_checked(self, Sender, Item):
        self.log_evt("list_view_item_checked(self, Sender, Item)")