# -*- mode: python ; coding: utf-8 -*-

from pathlib import Path

# This is the root directory of your project.
project_root = Path(__file__).parent.resolve()

# The name for the application and the executable.
app_name = 'my-app'

# The entry point for your application.
entry_point = str(project_root / 'src' / 'my_app' / 'main.py')

# List of data files and directories to include.
# Format: (source_path_on_disk, destination_path_in_bundle)
# Our get_asset_path function is designed to look for paths relative to the
# project root (e.g., 'src/my_app/...'). To make this work in the bundled app,
# we need to replicate this structure.
datas = [
    (str(project_root / 'src' / 'my_app' / 'qt_styles'), 'src/my_app/qt_styles'),
]

# PyInstaller analysis object.
a = Analysis(
    [entry_point],
    pathex=[str(project_root)],
    binaries=[],
    datas=datas,
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
    noarchive=False,
)

# Python Zipped Archive.
pyz = PYZ(a.pure, a.zipped_data, cipher=None)

# Executable object.
exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name=app_name,
    debug=False,
    boot_loader_options=None,
    strip=False,
    upx=True,
    console=False,  # Set to False for a GUI application on Windows
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    # TODO: Add path to an application icon file (.ico on Windows, .icns on macOS)
    # icon=str(project_root / 'assets' / 'app_icon.ico'),
)