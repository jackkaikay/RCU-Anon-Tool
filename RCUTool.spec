# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['RCUTool.py'],
             pathex=['C:\\Users\\jkay\\Desktop\\RCU-Anon-Tool'],
             binaries=[],
             datas=[('Dependencies/DeprivationBand.txt','Dependencies'), 
			 ('Dependencies/RCU2.ico','Dependencies'), 
			 ('Dependencies/Banner.png','Dependencies'),
			 ('Dependencies/Banner2.png','Dependencies')],
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
          name='RCUTool',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
