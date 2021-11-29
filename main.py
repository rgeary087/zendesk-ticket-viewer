import subprocess
import getpass
import json

userEMAIL, userSUBDOMAIN, userPASSWORD = "","",""
parsed = []

def getUserInfo():
    global userEMAIL, userSUBDOMAIN, userPASSWORD
    userEMAIL = input('Email:')
    userSUBDOMAIN = input('Subdomain:')
    userPASSWORD = getpass.getpass('Password(hidden):')

#subprocess.call(['bash','curl.sh', userNAME, userPASSWORD])
#data = subprocess.Popen(["curl.bat", userEMAIL, userSUBDOMAIN, userPASSWORD])

#data.communicate()
def printTicketList():
    for ticket in parsed['tickets']:
        print(f"ID: {ticket['id']} SUB: {ticket['raw_subject']}")

def loadTicketFile():
    global parsed
    fileA = open("tickets.json", 'r')
    parsed = json.load(fileA)
    printTicketList()
    fileA.close()
    

def main():
    getUserInfo()
    loadTicketFile()
    run = True

    while run:
        print("######################################")
        choice = input("Enter P to view previous page, N to view next page, an id to view that ticket, or Q to quit: \n")
        ticketID = -1
        match choice:
            case "P":
                printTicketList()
                continue
            case "N":
                printTicketList()
                continue
            case "Q":
                print("Thank you for using the Ticket Viewer!")
                quit()
            case _:
                try:
                    ticketID = int(choice)
                except:
                    print("Improper variable entered")
                    continue
                print(ticketID)    

if(__name__=="__main__"):
    main()

