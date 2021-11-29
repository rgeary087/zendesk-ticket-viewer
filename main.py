import subprocess
import getpass
import json

userEMAIL, userSUBDOMAIN, userPASSWORD = "","",""
parsed = []

def prettyPrintTicket(ID):
    print(ID)

def getUserInfo():
    global userEMAIL, userSUBDOMAIN, userPASSWORD
    userEMAIL = input('Email:')
    userSUBDOMAIN = input('Subdomain:')
    userPASSWORD = getpass.getpass('Password(hidden):')

def updateJSONFile(URL):
    #subprocess.call(['bash','curl.sh', userEMAIL, userPASSWORD])
    
    print(userPASSWORD)
    print(URL)
    data = subprocess.Popen(["curl.bat", userEMAIL, URL, userPASSWORD, "25"])
    data.communicate()

def printTicketList():
    print("\n######################################\n") 
    print("ID: \t Subject: \n")
    for ticket in parsed['tickets']:
        print(f"{ticket['id']} \t {ticket['raw_subject']}")
    print("")

def loadTicketFile():
    global parsed
    fileA = open("tickets.json", 'r')
    parsed = json.load(fileA)
    printTicketList()
    fileA.close()
    

def main():
    print("\t------ Welcome to the Greatest Zendesk Ticket Viewer You'll Ever See ------")
    getUserInfo()
    updateJSONFile(f"https://{userSUBDOMAIN}.zendesk.com/api/v2/tickets.json?page[size]")
    loadTicketFile()
    run = True

    while run:
        choice = input("What would you like to do? \n [P] - View previous page\n [N] - View next page \n [NUM] - Ticket id of ticket to view\n [Q]- Quit: \n--------------\n ")
        #choice = input("Enter P to view previous page, N to view next page, an id to view that ticket, or Q to quit: \n")
        ticketID = -1
        match choice:
            case "P":
                updateJSONFile(parsed['links']['prev'])
                printTicketList()
                continue
            case "N":
                updateJSONFile(parsed['links']['next'])
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

