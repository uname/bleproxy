@echo off
cd ..
set TMP_PROTO=BleProxyMsg_Java.proto
cat JavaHead.txt > %TMP_PROTO%
cat BleProxyMsg.proto >> %TMP_PROTO%
set PROTOC=..\Tools\protoc.exe
%PROTOC% --java_out=. %TMP_PROTO%
if %errorlevel% == 0 (
	echo OK
) else (
	echo ERROR
)

del /Q %TMP_PROTO%
