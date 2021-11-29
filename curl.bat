@echo off
del tickets.json
curl.exe %2=%4 -v -u %1/token:%3  -o tickets.json
cls