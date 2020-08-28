###################### Imports ###################### 
from scrapper import getStockPrice
from smsSender import sendText
from emailSender import sendEmail
from marketTime import isMarketOpen
import json

###################### Script ######################

# Run script only if market open
if isMarketOpen():
    
    # Setup stock list from json file
    f = open('clientList.json')
    data = json.load(f)

    # For each client in client list
    for client in data['clients']:

        # For each stock in client's stock list
        for stock in client['tickers']:

            # Get stock's price
            price = getStockPrice(stock['ticker'])
            print(price)

            # Make sure value is scraped
            while price == 0:
                getStockPrice(stock['ticker'])

            # Check if the stock is not in the given range
            if price < stock['lowerBound'] or price > stock['upperBound']:

                # Notify client
                message = "Hello " + client["firstName"]  + ".\n" # greetings
                message += stock['ticker'] + "'s price of $" + str(price) + " is looking interesting!" # price warning
                print(message)
                if client['preference'] == "email":
                    sendEmail(message, client["email"])
                elif client['preference'] == "sms":
                    sendText(message, client["phoneNumber"], client["carrier"])
