
# Installation at Windows

python, pip, virtualenv, virutalenvwrapper-win

reference:
https://github.com/davidmarble/virtualenvwrapper-win


# Virtual environment

C:\projectg> mkvirtualenv py2exedemo

C:\Users\i55956\Envs is not a directory, creating
New python executable in C:\Users\i55956\Envs\py2exedemo\Scripts\python.exe
Installing setuptools, pip, wheel...done.

(py2exedemo) c:\projectg>

# Working directory

C:\projectg> mkdir c:\projectg\py2exedemo
C:\projectg> cd py2exedemo
setprojectdir .

"c:\projectg\py2exedemo" is now the project directory for
virtualenv "C:\Users\i55956\Envs\py2exedemo"

"c:\projectg\py2exedemo" added to
C:\Users\i55956\Envs\py2exedemo\Lib\site-packages\virtualenv_path_extensions.pth

# Deactivate
(py2exedemo) c:\projectg\py2exedemo>deactivate

c:\projectg\py2exedemo>


# Workon
c:\projectg\py2exedemo> workon py2exedemo
c:\projectg\py2exedemo>workon py2exedemo
(py2exedemo) c:\projectg\py2exedemo>

# Main Commands
mkvirtualenv [mkvirtualenv-options] [virtualenv-options] <name>

mkvirtualenv options:
-h
-a project_path		Associating existing path as project directory
-i package          Install package in new environment. can be repeated.
-r requirement_file	Requirement_file is passwd to pip install -r requirement_file

listvirtualenv
rmvirtualenv
workon <name>
deactivate
add2virtualenv <file-or-path>  Add to virutalenv_path_extensions.pth for PYTHONPATH

# Convenience Commands
cdproject
cdsitepackages
cdvirtualenv
lssitepackages
mkproject       Create a project dir in PROJECT_HOME, virtualenv in WORKON_HOME.
				Automatically assocaite project path with environment.
setprojectdir  	<full or relative_path>   Add or create project dir and add2virtualenv
toggleglobalsitepackages   toggle the global site-packages in the PYTHONPATH
whereis <file>  The locations of an executable file on %PATH%
virtualenvwrapper  Print a list of commands














