unit uMain;

interface

uses
  Winapi.Windows, Winapi.Messages, System.SysUtils, System.Variants, System.Classes, Vcl.Graphics,
  Vcl.Controls, Vcl.Forms, Vcl.Dialogs, Vcl.WinXCtrls, Vcl.StdCtrls,
  Vcl.ExtCtrls;

type
  TToggleSwitch = class(TForm)
    cbxVclStyles: TComboBox;
    chkEnabled: TCheckBox;
    chkReadOnly: TCheckBox;
    chkShowStateCaptions: TCheckBox;
    grpAlignment: TRadioGroup;
    grpColors: TGroupBox;
    lblColor: TLabel;
    lblThumbColor: TLabel;
    lblFrameColor: TLabel;
    cbxColor: TColorBox;
    cbxThumbColor: TColorBox;
    cbxFrameColor: TColorBox;
    grpState: TRadioGroup;
    grpStateCaptions: TGroupBox;
    lblCaptionOff: TLabel;
    lblCaptionOn: TLabel;
    edtCaptionOff: TEdit;
    edtCaptionOn: TEdit;
    lblVclStyle: TLabel;
    TS: TToggleSwitch;
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  ToggleSwitch: TToggleSwitch;

implementation

{$R *.dfm}

end.
