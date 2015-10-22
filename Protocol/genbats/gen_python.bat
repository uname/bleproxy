@echo off
cd ..
set PROTOC=..\Tools\protoc.exe
%PROTOC% --python_out=. BleProxyMsg.proto
if %errorlevel% == 0 (
	echo OK
) else (
	echo ERROR
)
