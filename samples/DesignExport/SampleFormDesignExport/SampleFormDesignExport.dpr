program SampleFormDesignExport;

uses
  Vcl.Forms,
  uSampleForm in 'uSampleForm.pas' {sampleform};

{$R *.res}

begin
  Application.Initialize;
  Application.MainFormOnTaskbar := True;
  Application.CreateForm(Tsampleform, sampleform);
  Application.Run;
end.
