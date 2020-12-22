import os

#Shutdown
os.system("shutdown /s /t 1")

#Sleep
os.system("rundl32.exe powrprof.dll,SetSuspendState 0,1,0")
