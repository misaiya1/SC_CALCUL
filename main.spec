# -*- mode: python ; coding: utf-8 -*-

block_cipher = None
added_files = [('D:\\Personal\\Desktop\\skxxgj\\py\\DF_CALCUL\\pptx', 'pptx' )]
           # ('D:\\Personal\\Desktop\\skxxgj\\py\\DF_CALCUL\\res\\default.pptxo', 'res\\default.pptx' )]

a = Analysis(['main.py'],
             pathex=['D:\\Personal\\Desktop\\skxxgj\\py\\DF_CALCUL'],
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
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='test.ico')
