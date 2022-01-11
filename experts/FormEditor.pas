unit FormEditor;

interface

uses
  ToolsApi, DesignIntf, DesignEditors, System.Classes, System.SysUtils,
  System.TypInfo, System.Generics.Collections, Vcl.Dialogs;

type
  TFormComponentEditor = class(TComponentEditor)
  private
    FExportCompList: TList<string>;
    procedure ListComps(const ACompName: string);
    function GenerateClassFile(const ADesigner: IDesigner): string;
    function BuildSaveDialog(const ADefaultName: string): TSaveDialog;
    procedure SavePyFile(const ADesigner: IDesigner; const AFileName: string);
    procedure SavePyDfmFile(const ADesigner: IDesigner; const AFileName: string);
  public
    constructor Create(AComponent: TComponent; ADesigner: IDesigner); override;
    destructor Destroy(); override;

    procedure ExecuteVerb(Index: Integer); override;
    function GetVerbCount(): integer; override;
    function GetVerb(Index: integer): string; override;
  end;

  EFormInheritanceNotSupported = class(Exception)
  end;

procedure Register();

implementation

uses
  System.IOUtils, Vcl.Forms;

procedure Register();
begin
  RegisterComponentEditor(TForm, TFormComponentEditor);
end;

function GetFormEditorFromModule(Module: IOTAModule): IOTAFormEditor;
var
  i: Integer;
  Editor: IOTAEditor;
begin
  Result := nil;
  if Module = nil then
     Exit;
  for i := 0 to Module.GetModuleFileCount - 1 do
  begin
    Editor := Module.GetModuleFileEditor(i);
    if Supports(Editor, IOTAFormEditor, Result) then
      Break;
  end;
end;

{ TFormComponentEditor }

constructor TFormComponentEditor.Create(AComponent: TComponent;
  ADesigner: IDesigner);
begin
  inherited;
  FExportCompList := TList<string>.Create();
end;

destructor TFormComponentEditor.Destroy;
begin
  FExportCompList.Free();
  inherited;
end;

function TFormComponentEditor.GetVerb(Index: integer): string;
begin
  Result := 'Export to Python';
end;

function TFormComponentEditor.GetVerbCount: integer;
begin
  Result := 1;
end;

procedure TFormComponentEditor.ExecuteVerb(Index: Integer);
begin
  if Index = 0 then begin
    var LModule := (BorlandIDEServices as IOTAModuleServices).CurrentModule;
    if Assigned(LModule) then begin
      var LEditor := GetFormEditorFromModule(LModule);
      if Assigned(LEditor) then begin
        var LDes := (LEditor as INTAFormEditor).FormDesigner;
        if Assigned(LDes) then begin
          if (LDes.CurrentParent.ClassParent <> TForm) then
            raise EFormInheritanceNotSupported.Create('TForm direct inheritance only');

          FExportCompList.Clear();
          var LDlg := BuildSaveDialog(LDes.CurrentParent.Name);
          try
            if LDlg.Execute then begin
              SavePyFile(LDes, LDlg.FileName);
              SavePyDfmFile(LDes, ChangeFileExt(LDlg.FileName, '.pydfm'));
            end;
          finally
            LDlg.Free();
          end;
        end;
      end;
    end;
  end;
end;

function TFormComponentEditor.BuildSaveDialog(const ADefaultName: string): TSaveDialog;
begin
  Result := TSaveDialog.Create(nil);
  try
    Result.Filter := 'D4P|*.py';
    Result.DefaultExt := '.py';
    Result.FileName := ADefaultName;
  except
    on E: Exception do  begin
      FreeAndNil(Result);
    end;
  end;
end;

procedure TFormComponentEditor.ListComps(const ACompName: string);
begin
  FExportCompList.Add(ACompName);
end;

function TFormComponentEditor.GenerateClassFile(
  const ADesigner: IDesigner): string;
const
  PY_TEMPLATE =
    'import os                                                                                              ' + sLineBreak
  + 'from delphivcl import *                                                                                ' + sLineBreak
  + '                                                                                                       ' + sLineBreak
  + 'class @CLASSNAME(@CLASSPARENT):                                                                        ' + sLineBreak
  + '    def __init__(self, owner):                                                                         ' + sLineBreak
  + '        @PROPERTIES                                                                                    ' + sLineBreak
  + '        self.LoadProps(os.path.join(os.path.dirname(os.path.abspath(__file__)), "@CLASSNAME.pydfm"))   ' + sLineBreak;
begin
  var LProps := String.Empty;
  for var LCompName in FExportCompList do begin
    if not LProps.IsEmpty() then
      LProps := LProps + sLineBreak + '        ';
    LProps := LProps + 'self.' + LCompName + ' = None';
  end;

  Result := PY_TEMPLATE
    .Replace('@CLASSNAME', System.Copy(ADesigner.CurrentParent.ClassName, 2, Length(ADesigner.CurrentParent.ClassName)), [rfReplaceAll])
    .Replace('@CLASSPARENT', System.Copy(ADesigner.CurrentParent.ClassParent.ClassName, 2, Length(ADesigner.CurrentParent.ClassParent.ClassName)))
    .Replace('@PROPERTIES', LProps);
end;

procedure TFormComponentEditor.SavePyFile(const ADesigner: IDesigner; const AFileName: string);
begin
  ADesigner.GetComponentNames(GetTypeData(TypeInfo(TComponent)), ListComps);
  TFile.WriteAllText(AFileName, GenerateClassFile(ADesigner));
end;

procedure TFormComponentEditor.SavePyDfmFile(const ADesigner: IDesigner;
  const AFileName: string);
begin
  var LStream := TFileStream.Create(AFileName, fmOpenWrite or fmCreate);
  try
    LStream.WriteComponent(ADesigner.CurrentParent);
  finally
    LStream.Free();
  end;
end;

end.
