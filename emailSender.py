###################### Imports ###################### 
import smtplib
from email.message import EmailMessage

################ Function Definition ################

# sendEmail(message, destEmail) sends an email to the destination email through Gmail's server
def sendEmail(message : str, destEmail : str):

    # setup email
    msg = EmailMessage()
    msg.set_content(message)
    msg['Subject'] = "Watchlister Alert"
    msg['From'] = "mofthecoder@gmail.com"
    msg['To'] = destEmail

    # Gmail's authentification
    auth = ('--email--', '--password--')

    # Establish secure session with gmail's outgoing SMTP server
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(auth[0], auth[1])

    # Send the message
    server.send_message(msg)
