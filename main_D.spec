# -*- mode: python ; coding: utf-8 -*-

block_cipher = None
added_files =[( 'data', 'data')]

a = Analysis(['main.py'],
             pathex=['D:\\Personal\\Desktop\\skxxgj\\SCSG\\py\\SC_CALCUL'],
             binaries=[],
             datas=added_files,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='鼠笼风电机组电驱系统设计工具_V1_0',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='test.ico')

