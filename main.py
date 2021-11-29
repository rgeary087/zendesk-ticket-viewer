import subprocess
import json

userEMAIL, userSUBDOMAIN, userTOKEN = "","",""
parsed = []

def getAPI():
    global userTOKEN
    file = open("token.txt", 'r')
    userTOKEN = file.readline()


def prettyPrintTicket(ID, ticketsFile):
    data = subprocess.Popen(["curl3.bat", userEMAIL, userSUBDOMAIN, str(ID), userTOKEN])
    data.communicate()
    loadTicketFile(ticketsFile)
    printTicketList(parsed)
    if(errorCheck("ticket.json")>0):
        return -1
    loadTicketFile("ticket.json")
    ticket = parsed['ticket']

    print(f"\n\nSTATUS: {ticket['status']}\nPRIORITY: {ticket['priority']}\nID: {ticket['id']}\nCREATED AT: {ticket['created_at']}\nSUBJECT:{ticket['raw_subject']}\n\nDESCRIPTION:\n{ticket['description']}\n\n")
    return 0

def getUserInfo():
    global userEMAIL, userSUBDOMAIN
    userEMAIL = input('Email:')
    userSUBDOMAIN = input('Subdomain:')
    return userEMAIL, userSUBDOMAIN

def errorCheck(fileName):
    try:
        fileA = open(fileName, 'r')
        errorJSON = json.load(fileA)
    except:
        print("ERROR LOADING TICKETS.JSON, RETYPE IN PASSWORD")
        return 1
    try:
        print("\n\n\n\n\nERROR\n\nTITLE", errorJSON['error']['title'],"\nMESSAGE:", errorJSON['error']['message'], "\n\n")
        return 1
    except:
        try:
            print("\n\n\n\n\nERROR\n\nTITLE", errorJSON['error'],"\nMESSAGE:", errorJSON['description'], "\n\n")
            return 1
        except:
            return 0

def initJSONFile(URL: str):
    URL = URL.replace('%5B', '[')
    URL = URL.replace('%5D', ']')
    data = subprocess.Popen(["curl.bat", userEMAIL, URL, userTOKEN, "25"])
    data.communicate()

def updateJSONFile(URL: str):
    URL = URL.replace('%5B', '[')
    URL = URL.replace('%5D', ']')
    URL = URL.replace('%3D', '=')
    URL = URL.replace('&page[size]=25', '')
    print(userTOKEN)
    data = subprocess.Popen(["curl2.bat", userEMAIL, userTOKEN, URL, ""])
    data.communicate()

def printTicketList(data):
    print("\n######################################\n") 
    print("Status:\tPriority:\tID:\tSubject:\t\n")
    for ticket in data['tickets']:
        print(f"{ticket['status']}\t{ticket['priority']}\t{ticket['id']}\t{ticket['raw_subject']}")
    print("")

def loadTicketFile(fileName):
    global parsed
    parsed = None
    fileA = open(fileName, 'r')
    parsed = json.load(fileA)
    fileA.close()
    

def main():
    print("\n\n\t------ Welcome to the Greatest Zendesk Ticket Viewer You'll Ever See ------\n")
    getAPI()
    while True:
        getUserInfo()
        initJSONFile(f"https://{userSUBDOMAIN}.zendesk.com/api/v2/tickets.json?page[size]")
        if(errorCheck("tickets.json") == 0):
            break;
    
    loadTicketFile("tickets.json")
    printTicketList(parsed)
    run = True

    while run:
        choice = input("What would you like to do? \n [P] - View previous page\n [N] - View next page \n [NUM] - Ticket id of ticket to view\n [Q]- Quit: \n--------------\n ")
        #choice = input("Enter P to view previous page, N to view next page, an id to view that ticket, or Q to quit: \n")
        ticketID = -1
        match choice:
            case "P":
                loadTicketFile("tickets.json")
                updateJSONFile(parsed['links']['prev'])
                errorCheck("tickets.json")
                loadTicketFile("tickets.json")
                printTicketList(parsed)
                continue
            case "N":
                loadTicketFile("tickets.json")
                if parsed['meta']['has_more']:
                    updateJSONFile(parsed['links']['next'])
                    errorCheck("tickets.json")
                    loadTicketFile("tickets.json")
                else:
                    print("\n Reached end of list!")
                printTicketList(parsed)
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
                
                prettyPrintTicket(ticketID, "tickets.json") 
          

if(__name__=="__main__"):
    main()
