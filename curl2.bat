@echo off
curl.exe %2 -v -u %1:%3 -o tickets.json
clear
