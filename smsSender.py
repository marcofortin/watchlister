###################### Imports ###################### 
import smtplib

################ Function Definition ################

# sendText(message, destNumber) sends a text message to the destination number through Gmail's server
def sendText(message : str, destNumber : str, carrier : str):
    
    # Currently only supporting Rogers and AT&T
    carriers = { 
	    'rogers':   '@pcs.rogers.com',
	       'att':   '@mms.att.net'
    }
    destNumber += carriers[carrier] # client's carrier

    # Gmail's authentification
    auth = ('--email--', '--password--')

    # Establish secure session with gmail's outgoing SMTP server
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(auth[0], auth[1])

    # Send text message through SMS gateway of destination number
    server.sendmail(auth[0], destNumber, message)
    server.quit()
