@echo off
Rem curl.exe -u %1:%3 https://%2.zendesk.com/api/v2/users/me.json
Rem curl.exe https://%2.zendesk.com/api/v2/imports/tickets/create_many.json -v -u %1:%3  -X POST -d @tickets.json -H "Content-Type:application/json" 
echo curl.exe %2 -v -u %1:%3 -o tickets.json
curl.exe -B %2=%4 -v -u %1:%3 
Rem -o tickets.json 