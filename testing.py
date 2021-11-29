import main
import unittest
import os

#Passing Tests

properToken = "ENTER TOKEN HERE"

class API_CONNECTION_SUCCESS_TESTS(unittest.TestCase):
    def test_init_JSON_method(self):
        main.userEMAIL = "rgeary087@gmail.com"
        main.userSUBDOMAIN = "zccrgeary"
        main.userTOKEN = properToken
        main.initJSONFile(f"https://{main.userSUBDOMAIN}.zendesk.com/api/v2/tickets.json?page[size]")
        self.assertEqual(main.errorCheck("tickets.json"), 0)
    def test_get_ticket_ID(self):
        main.userEMAIL = "rgeary087@gmail.com"
        main.userSUBDOMAIN = "zccrgeary"
        main.userTOKEN = properToken
        self.assertEqual(main.prettyPrintTicket(1, "ticketsTEST.json"), 0)
    def test_get_next_link(self):
        main.userEMAIL = "rgeary087@gmail.com"
        main.userSUBDOMAIN = "zccrgeary"
        main.userTOKEN = properToken
        main.loadTicketFile("ticketsTEST.json")
        main.updateJSONFile(main.parsed['links']['next'])
        self.assertEqual(main.errorCheck("tickets.json"),0)

class API_CONNECTION_FAILURE_TESTS(unittest.TestCase):
    
    def test_init_JSON_method(self):
        main.userEMAIL = "aa"
        main.userSUBDOMAIN = "aa"
        main.userTOKEN = "asjbdf"
        main.initJSONFile(f"https://{main.userSUBDOMAIN}.zendesk.com/api/v2/tickets.json?page[size]")
        self.assertEqual(main.errorCheck("tickets.json"), 1)
    def test_get_ticket_ID(self):
        main.userEMAIL = "aa"
        main.userSUBDOMAIN = "aa"
        main.userTOKEN = "asjbdf"
        self.assertEqual(main.prettyPrintTicket(-1, "ticketsTEST.json"), -1)
if __name__ == '__main__':
    unittest.main()
