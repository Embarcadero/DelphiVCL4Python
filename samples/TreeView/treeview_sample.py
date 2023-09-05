# ---------------------------------------------------------------------------------
# Name:       treeview_sample.py
# Purpose:    DelphiVCL for Python sample
#
# Author:     lmbelo, Priyatham
#
# Created:    28/08/2023
# Copyright:  2020-2023 Embarcadero Technologies, Inc.
# License:    https://github.com/Embarcadero/DelphiVCL4Python/blob/main/LICENSE.md
# ---------------------------------------------------------------------------------

from delphivcl import *

class TreeViewSample(Form):


    def __init__(self, owner):
        self.tree_view = TreeView(self)
        self.panel = Panel(self)
        self.memo = Memo(self)

        self.tg_checkboxes = CheckBox(self.panel)
        self.check_styles_groupbox = GroupBox(self.panel)
        self.check_styles_cs_partial = CheckBox(self.check_styles_groupbox)
        self.check_styles_cs_dimmed = CheckBox(self.check_styles_groupbox)
        self.check_styles_cs_excluded = CheckBox(self.check_styles_groupbox)
        self.tg_multi_select = CheckBox(self.panel)
        self.tg_show_buttons = CheckBox(self.panel)
        self.multi_select_groupbox = GroupBox(self.panel)
        self.multi_select_ms_control_select = CheckBox(self.multi_select_groupbox)
        self.multi_select_ms_shift_select = CheckBox(self.multi_select_groupbox)
        self.multi_select_ms_visible_only = CheckBox(self.multi_select_groupbox)
        self.multi_select_ms_sibling_only = CheckBox(self.multi_select_groupbox)
        self.tg_show_lines = CheckBox(self.panel)
        self.tg_tv_visibility = CheckBox(self.panel)

        self.config()

        root_node = self.tree_view.Items.Add(None, "TreeView")
        root_node_child1 = self.tree_view.Items.AddChild(root_node, "Lucas")
        root_node_child2 = self.tree_view.Items.AddChild(root_node, "Priyatham")
        root_node.Expand(True)

    
    def log_event(self, log):
        self.memo.lines.Add("Event: "+log)


    def config(self):
        self.SetProps(
            Width = 850,
            Height = 700
        )

        self.tree_view.SetProps(
            Parent = self,
            Width = 605,
            Height = 520,
            Align = "alClient",
            # CheckBoxes = True,
            #events
            OnAddition = self.do_addition,
            OnAdvancedCustomDraw = self.do_advanced_custom_draw,
            OnAdvancedCustomDrawItem = self.do_advanced_custom_draw_item,
            OnCancelEdit = self.do_cancel_edit,
            OnChange = self.do_change,
            OnChanging = self.do_changing,
            OnCheckStateChanged = self.do_check_state_changed,
            OnCheckStateChanging = self.do_check_state_changing,
            OnClick = self.do_click,
            OnCollapsed = self.do_collapsed,
            OnCollapsing = self.do_collapsing,
            OnCompare = self.do_compare,
            OnContextPopup = self.do_context_popup,
            OnCreateNodeClass = self.do_create_node_class,
            OnCustomDraw = self.do_custom_draw,
            OnCustomDrawItem = self.do_custom_draw_item,
            OnEdited = self.do_edited,
            OnEditing = self.do_editing,
            OnExpanding = self.do_expanding,
            OnExpanded = self.do_expanded,
            OnHint = self.do_hint
        )

        self.panel.SetProps(
            Parent = self,
            Width = 240,
            Height = 520,
            Align = "alRight"
        )

        self.memo.SetProps(
            Parent = self,
            Width = 850,
            Height = 140,
            Align = "alBottom"
        )
        
        self.tg_checkboxes.SetProps(
            Parent = self.panel,
            Caption = "Toggle checkboxes",
            Left = 14,
            Top = 48,
            Width = 230,
            OnClick = self.do_tg_checkboxes_click
        )
        
        self.check_styles_groupbox.SetProps(
            Parent = self.panel,
            Caption = "CheckStyles",
            Left = 6,
            Top = 98,
            Height = 90,
            Width = 180
        )

        self.check_styles_cs_partial.SetProps(
            Parent = self.check_styles_groupbox,
            Caption = "csPartial",
            Align = "alTop",
            AlignWithMargins = True,
            OnClick = self.do_check_styles_change
        )

        self.check_styles_cs_dimmed.SetProps(
            Parent = self.check_styles_groupbox,
            Caption = "csDimmed",
            Align = "alTop",
            AlignWithMargins = True,
            OnClick = self.do_check_styles_change
        )

        self.check_styles_cs_excluded.SetProps(
            Parent = self.check_styles_groupbox,
            Caption = "csExclusion",
            Align = "alTop",
            AlignWithMargins = True,
            OnClick = self.do_check_styles_change
        )

        self.tg_multi_select.SetProps(
            Parent = self.panel,
            Caption = "Toggle MultiSelect",
            Top = 208,
            Left = 14,
            Width = 160,
            OnClick = self.do_tg_multi_select_click
        )

        self.tg_show_buttons.SetProps(
            Parent = self.panel,
            Caption = "Toggle Show Buttons",
            Left = 14,
            Top = 240,
            Width = 170,
            OnClick = self.do_tg_show_buttons_click
        )

        self.multi_select_groupbox.SetProps(
            Parent = self.panel,
            Caption = "MultiSelectStyle",
            Left = 6,
            Top = 288,
            Width = 180,
            Height = 124
        )

        self.multi_select_ms_control_select.SetProps(
            Parent = self.multi_select_groupbox,
            Caption = "msControlSelect",
            Align = "alTop",
            AlignWithMargins = True,
            OnClick = self.do_multi_select_style_change
        )

        self.multi_select_ms_shift_select.SetProps(
            Parent = self.multi_select_groupbox,
            Caption = "msShiftSelect",
            Align = "alTop",
            AlignWithMargins = True,
            OnClick = self.do_multi_select_style_change
        )

        self.multi_select_ms_visible_only.SetProps(
            Parent = self.multi_select_groupbox,
            Caption = "msVisibleOnly",
            Align = "alTop",
            AlignWithMargins = True,
            OnClick = self.do_multi_select_style_change
        )

        self.multi_select_ms_sibling_only.SetProps(
            Parent = self.multi_select_groupbox,
            Caption = "msSiblingOnly",
            Align = "alTop",
            AlignWithMargins = True,
            OnClick = self.do_multi_select_style_change
        )

        self.tg_show_lines.SetProps(
            Parent = self.panel,
            Caption = "Toggle Show Lines",
            Left = 6,
            Top = 425,
            Width = 195,
            OnClick = self.do_tg_show_lines_click
        )

        self.tg_tv_visibility.SetProps(
            Parent = self.panel,
            Caption = "Toggle TreeView Visibility",
            Left = 6,
            Top = 456,
            Width = 195,
            OnClick = self.do_tg_tv_visibility_click
        )


    def do_tg_checkboxes_click(self, Sender):
        if not self.tree_view.CheckBoxes:
            self.tree_view.CheckBoxes = True
        else:
            self.tree_view.CheckBoxes = False


    def do_check_styles_change(self, Sender):
        check_styles = self.tree_view.CheckStyles
        if Sender.Caption in self.tree_view.CheckStyles:
            check_styles.remove(Sender.Caption)
        else:
            check_styles.append(Sender.Caption)
        self.tree_view.CheckStyles = check_styles


    def do_tg_multi_select_click(self, Sender):
        if not self.tree_view.MultiSelect:
            self.tree_view.MultiSelect = True
        else:
            self.tree_view.MultiSelect = False


    def do_tg_show_buttons_click(self, Sender):
        if not self.tree_view.ShowButtons:
            self.tree_view.ShowButtons = True
        else:
            self.tree_view.ShowButtons = False


    def do_multi_select_style_change(self, Sender):
        multiselect_style = self.tree_view.MultiSelectStyle
        if Sender.Caption in self.tree_view.MultiSelectStyle:
            multiselect_style.remove(Sender.Caption)
        else:
            multiselect_style.append(Sender.Caption)
        self.tree_view.MultiSelectStyle = multiselect_style


    def do_tg_show_lines_click(self, Sender):
        if not self.tree_view.ShowLines:
            self.tree_view.ShowLines = True
        else:
            self.tree_view.ShowLines = False


    def do_tg_tv_visibility_click(self, Sender):
        if not self.tree_view.Visible:
            self.tree_view.Visible = True
        else:
            self.tree_view.Visible = False


    def do_addition(self, Sender, Node):
        self.log_event("OnAdittion(Sender, Node))")


    def do_advanced_custom_draw(self, Sender, ARect, Stage, DefaultDraw):
        self.log_event("OnAdvancedCustomDraw(Sender, ARect, Stage, var DefaultDraw)")


    def do_advanced_custom_draw_item(self, Sender, Node, State, Stage, PaintImages, DefaultDraw):
        self.log_event("OnAdvancedCustomDrawItem(Sender, Node, State, Stage, var PaintImages, var DefaultDraw)")


    def do_cancel_edit(self, Sender, Node):
        self.log_event("OnCancelEdit(Sender, Node))")


    def do_change(self, Sender, Node):
        self.log_event("OnChange(Sender, Node))")


    def do_changing(self, Sender, Node, AllowChange):
        self.log_event("OnChanging(Sender, Node, var AllowChange))")


    def do_check_state_changed(self, Sender, Node, CheckState):
        self.log_event("OnCheckStateChanged(Sender, Node, CheckState))")


    def do_check_state_changing(self, Sender, Node, NewCheckState, OldCheckState, AllowChange):
        self.log_event("OnCheckStateChanging(Sender, Node, NewCheckState, OldCheckState, var AllowChange))")


    def do_click(self, Sender):
        self.log_event("OnClick(Sender)")


    def do_collapsed(self, Sender, Node):
        self.log_event("OnCollapsed(Sender, Node)")


    def do_collapsing(self, Sender, Node, AllowCollapse):
        self.log_event("OnCollapsing(Sender, Node, var AllowCollapse)")


    def do_compare(self, Sender, Node1, Node2, Data, Compare):
        self.log_event("OnCompare(Sender, Node1, Node2, Data, Compare)")


    def do_context_popup(self, Sender, MousePos, Handled):
        self.log_event("OnContextPopup(Sender, MousePos, var Handled)")


    def do_create_node_class(self, Sender, NodeClass):
        self.log_event("OnCreateNodeClass(Sender, var NodeClass)")


    def do_custom_draw(self, Sender, ARect, DefaultDraw):
        self.log_event("OnCustomDraw(Sender, ARect, var DefaultDraw)")


    def do_custom_draw_item(self, Sender, Node, State, DefaultDraw):
        self.log_event("OnCustomDrawItem(Sender, Node, State, var DefaultDraw)")


    def do_edited(self, Sender, Node, S):
        self.log_event("OnEdited(Sender, Node, var S)")


    def do_editing(self, Sender, Node, AllowEdit):
        self.log_event("OnEditing(Sender, Node, var AllowEdit)")


    def do_expanding(self, Sender, Node, AllowExpansion):
        self.log_event("OnExpanding(Sender, Node, var AllowExpansion)")


    def do_expanded(self, Sender, Node):
        self.log_event("OnExpanded(Sender, Node)")


    def do_hint(self, Sender, Node, Hint):
        self.log_event("OnHint(Sender, Node, var Hint)")


def main():
    Application.Initialize()
    Application.Title = "TreeView Sample"
    MainForm = TreeViewSample(Application)
    MainForm.Show()
    FreeConsole()
    Application.Run()
    MainForm.Destroy()


if __name__ == "__main__":
    main()