import subprocess
import os
import getpass

#print("Hello World")

userEMAIL = input('Email:')
userSUBDOMAIN = input('Subdomain:')
userPASSWORD = getpass.getpass('Password(hidden):')

#subprocess.call(['bash','curl.sh', userNAME, userPASSWORD])
data = subprocess.Popen(["curl.bat", userEMAIL, userSUBDOMAIN, userPASSWORD])

data.communicate()

