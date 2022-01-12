unit uMainForm;

interface

uses
  Winapi.Windows, Winapi.Messages, System.SysUtils, System.Variants, System.Classes, Vcl.Graphics,
  Vcl.Controls, Vcl.Forms, Vcl.Dialogs, Vcl.StdCtrls, Vcl.Buttons, Vcl.ExtCtrls,
  System.Actions, Vcl.ActnList, Vcl.Menus, Vcl.Imaging.pngimage, Vcl.Grids,
  Vcl.ComCtrls;

type
  TMainForm = class(TForm)
    Panel1: TPanel;
    Button1: TButton;
    Button2: TButton;
    Memo1: TMemo;
    Panel2: TPanel;
    Label1: TLabel;
    ActionList1: TActionList;
    actSpeedButton: TAction;
    MainMenu1: TMainMenu;
    File1: TMenuItem;
    Exit1: TMenuItem;
    Image1: TImage;
    Label2: TLabel;
    SpeedButton1: TSpeedButton;
    CheckBox1: TCheckBox;
    ComboBox1: TComboBox;
    Edit1: TEdit;
    ScrollBar1: TScrollBar;
    Panel3: TPanel;
    StringGrid1: TStringGrid;
    Shape1: TShape;
    Shape2: TShape;
    Shape3: TShape;
    ColorBox1: TColorBox;
    TabControl1: TTabControl;
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  MainForm: TMainForm;

implementation

{$R *.dfm}

end.
