import os
import platform
import subprocess

if platform.system() == 'Windows':
    FAST_exe        = os.path.dirname( os.path.dirname( os.path.realpath(__file__) ) ) + os.sep + 'OF_executables' + os.sep + 'openfast.exe'
elif platform.system() == 'Darwin':
    FAST_exe        = os.path.dirname( os.path.dirname( os.path.realpath(__file__) ) ) + os.sep + 'OF_executables' + os.sep + 'openfast_mac'
else:
    FAST_exe        = os.path.dirname( os.path.dirname( os.path.realpath(__file__) ) ) + os.sep + 'OF_executables' + os.sep + 'openfast'

FAST_directory  = os.path.dirname( os.path.dirname( os.path.realpath(__file__) ) ) + os.sep + 'IEA_LB_RWT-AeroAcoustics'

FAST_InputFile  = FAST_directory + os.sep + 'IEA_LB_RWT-AeroAcoustics.fst'
exec_str = []
exec_str.append(FAST_exe)
exec_str.append(FAST_InputFile)

subprocess.call(exec_str)