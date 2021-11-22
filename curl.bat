@echo off
Rem curl.exe -u %1:%3 https://%2.zendesk.com/api/v2/users/me.json
curl.exe https://%2.zendesk.com/api/v2/imports/tickets/create_many.json -v -u %1:%3  -X POST -d @tickets.json -H "Content-Type:application/json" 