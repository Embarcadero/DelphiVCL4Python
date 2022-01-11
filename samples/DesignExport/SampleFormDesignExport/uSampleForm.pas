unit uSampleForm;

interface

uses
  Winapi.Windows, Winapi.Messages, System.SysUtils, System.Variants, System.Classes, Vcl.Graphics,
  Vcl.Controls, Vcl.Forms, Vcl.Dialogs, Vcl.StdCtrls, Vcl.Buttons, Vcl.ExtCtrls,
  System.Actions, Vcl.ActnList, Vcl.Menus, Vcl.Imaging.pngimage;

type
  Tsampleform = class(TForm)
    Panel1: TPanel;
    Button1: TButton;
    Button2: TButton;
    Memo1: TMemo;
    Panel2: TPanel;
    SpeedButton1: TSpeedButton;
    Label1: TLabel;
    Edit1: TEdit;
    CheckBox1: TCheckBox;
    ComboBox1: TComboBox;
    ActionList1: TActionList;
    actSpeedButton: TAction;
    MainMenu1: TMainMenu;
    File1: TMenuItem;
    Exit1: TMenuItem;
    ScrollBar1: TScrollBar;
    Image1: TImage;
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  sampleform: Tsampleform;

implementation

{$R *.dfm}

end.
