# PyInstaller demo

## PyInstaller install
Microsoft Visual C++ 2008 Redistributable Package (x86): vcredist_x86.exe
https://www.microsoft.com/en-us/download/details.aspx?id=29

create or update .../site-packages/sitecustomize.py
Add below lines: 
import sys
sys.setdefaultencoding("utf-8")

pip install pyinstaller    # include pypiwin32, pefile

## Tutorial

Create program: hello.py
c:\projectg\py2exedemo>echo print "Hello World!" > hello.py
c:\projectg\py2exedemo>python hello.py
Hello World!

Create exe:  
pyinstaller hello.py  

c:\projectg\py2exedemo>ls -R build dist
build:
hello

build/hello:
hello.exe           out00-Analysis.toc  out00-EXE.toc  out00-PKG.toc  out00-PYZ.toc  xref-hello.html
hello.exe.manifest  out00-COLLECT.toc   out00-PKG.pkg  out00-PYZ.pyz  warnhello.txt

dist:
hello

dist/hello:
Microsoft.VC90.CRT.manifest  bz2.pyd    hello.exe.manifest  msvcp90.dll  python27.dll  unicodedata.pyd
_hashlib.pyd                 hello.exe  msvcm90.dll         msvcr90.dll  select.pyd


## Note

### Norton antivirous delete created .exe file.
https://social.msdn.microsoft.com/Forums/vstudio/en-US/9817b53f-74d8-4227-9fe7-c7e603e8f0d0/visual-studio-2015-heuradvmlb?forum=visualstudiogeneral

Adding directory to exception list
https://community.norton.com/en/forums/how-add-folder-exceptions

