# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['delphivclexecutable.py'],
    pathex=[],
    binaries=[],
    datas=[(r"C:\Users\lmbelo\AppData\Local\Programs\Python\Python311\Lib\site-packages\delphivcl", "delphivcl")],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='delphivclexecutable',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='delphivclexecutable',
)
