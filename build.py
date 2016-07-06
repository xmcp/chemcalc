import sys
import os,shutil
from cx_Freeze import setup, Executable
base = None
if sys.platform == 'win32':
    base = 'Win32GUI'
executables = [Executable(script='LXcalc.py',
               base=base,
               targetName="LXcalc.exe",
               compress=True),]
setup(name='LXcalc',
      version='1.0',
      description='LiangXin Calculator',
      executables=executables,
      options={'build_exe':{
          'optimize':2,
          'include_msvcr':True,
          'include_files':['chem_weight.py','chemcalc.py','chemparser.py'],
          'excludes':'chem_weight,chemcalc,chemparser','includes':'ply.lex,ply.yacc,fractions,collections',
      }},)

print('===== CLEANING UP =====')

#os.remove('build/exe.win32-3.4/unicodedata.pyd')
os.remove('build/exe.win32-3.4/_socket.pyd')
os.remove('build/exe.win32-3.4/_hashlib.pyd')
os.remove('build/exe.win32-3.4/_ssl.pyd')
shutil.rmtree('build/exe.win32-3.4/tcl/tzdata')
shutil.rmtree('build/exe.win32-3.4/tcl/msgs')
shutil.rmtree('build/exe.win32-3.4/tcl/encoding')
shutil.rmtree('build/exe.win32-3.4/tk/demos')
shutil.rmtree('build/exe.win32-3.4/tk/images')
shutil.rmtree('build/exe.win32-3.4/tk/msgs')

os.rename('build/exe.win32-3.4','build/LXcalc-exe.win32-3.4')

print('===== DONE =====')

