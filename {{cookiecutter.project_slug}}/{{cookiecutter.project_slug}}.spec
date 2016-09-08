# -*- mode: python -*-

# pyinstaller configuration

block_cipher = None

import {{ cookiecutter.project_slug }}



a = Analysis(['scripts\\{{ cookiecutter.project_slug }}'],
             pathex=['{{ cookiecutter.project_slug }}'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=['matplotlib', 'PyQt4', 'PySide', '_tkinter'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='{{ cookiecutter.project_slug }}-{}'.format({{ cookiecutter.project_slug }}.__version__),
          debug=False,
          strip=False,
          upx=True,
          console=True )
