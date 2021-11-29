@echo off
del ticket.json
curl.exe https://%2.zendesk.com/api/v2/tickets/%3.json -v -u %1/token:%4 -o ticket.json
cls
