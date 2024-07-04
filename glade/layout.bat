set GLADE_USE_OPENGL=no

rem ************  Substitute your actual glade installation dir ****

rem set GLADE_HOME=C:\installation\Glade_Layout\glade_5_0_48

set GLADE_HOME=C:\glade6_win64\glade6_win64

rem ****************************************************************

rem set PYTHONPATH=%PYTHONHOME%;%GLADE_HOME%;.
rem set PYTHONHOME=%GLADE_HOME%\Python38
set PATH=%GLADE_HOME%;%PATH%
set PYTHONPATH=%GLADE_HOME%;.


set GLADE_LOGFILE_DIR=.
set HOME=.

del .\*.log

start /b glade
