@ECHO OFF
powershell.exe -command "ls '0106\*.*' | foreach-object { $_.LastWriteTime = '01/07/2020 00:22:00'; $_.CreationTime = '01/07/2020 00:01:36' }"
PAUSE