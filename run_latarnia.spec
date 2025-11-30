# -*- mode: python ; coding: utf-8 -*-
"""
PyInstaller spec file for Latarnia v6

This configuration file is used to build a standalone executable
of the Latarnia application using PyInstaller.

Usage:
    pyinstaller run_latarnia.spec
"""

import os
from pathlib import Path

# Get the project root directory
project_root = Path(SPECPATH)

# Analysis configuration
a = Analysis(
    ['run_latarnia.py'],
    pathex=[str(project_root)],
    binaries=[],
    datas=[
        ('latarnia', 'latarnia'),
        ('README_LATARNIA_V6.txt', '.'),
    ],
    hiddenimports=[
        'streamlit',
        'latarnia',
        'latarnia.core',
        'latarnia.core.logic',
        'latarnia.tools',
        'latarnia.security',
        'latarnia.runtime',
        'latarnia.runtime.webui',
        'latarnia.turbo',
        'latarnia.rag',
        'latarnia.hive',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
    noarchive=False,
)

# PYZ archive
pyz = PYZ(a.pure, a.zipped_data, cipher=None)

# Executable configuration
exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='latarnia',
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

# Collection for distribution
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='latarnia',
)
