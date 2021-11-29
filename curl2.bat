@echo off
del tickets.json
curl.exe "%3=%4==&page[size]=25" -v -u %1/token:%2 -o tickets.json
cls
