program ToggleSwitchDesignExport;

uses
  Vcl.Forms,
  uMain in 'uMain.pas' {ToggleSwitch};

{$R *.res}

begin
  Application.Initialize;
  Application.MainFormOnTaskbar := True;
  Application.CreateForm(TToggleSwitch, ToggleSwitch);
  Application.Run;
end.
