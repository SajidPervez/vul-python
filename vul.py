import sys, os, io
import logging, random

class ForifyScanTest(object):
    def __init__(self, password):
        self.password = password
		
    def testHardCodedPassword(self):
        #Fortify Test - Password Management: Hardcoded Password
        password = "password"
        logging.warning(password)
		
    def testAccessControlDatabase(self, request, id):
        #Fortify Test - Access Control:Database
        #id = request.GET['id']
        c = db.cursor()
        stmt = c.execute("SELECT * FROM invoices WHERE id = %s", id)

    def testPoorLoggingPractice(self):
        #Fortify Test - Poor Logging Practice: Use of a System Output Stream
        sys.stdout.write("hello world")
		
    def testPrivacyViolation(self,password):
        #Fortify Test - Privacy Violation
        logging.warning(password)
		
    def testInsecureRandomness(self,baseURL):
        #Fortify Test - Insecure Randomness
        randNum = random.random()
        receiptURL = baseURL + randNum + ".html"
        return receiptURL
		
    def testInsecureRandomnessHardcodedSeeds(self,baseURL):
        #Fortify Test - Insecure Randomness: Hardcoded Seeds
        randNum = random.seed(123456)
        receiptURL = baseURL + randNum + ".html"
        return receiptURL
