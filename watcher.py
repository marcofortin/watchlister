###################### Imports ###################### 
from scrapper import getStockPrice
from sms import sendText
from marketTime import isMarketOpen
import json

###################### Script ######################

# Run script only if market open
if isMarketOpen():
    
    # Setup stock list from json file
    f = open('stockList.json')
    data = json.load(f)

    # For each client in client list
    for client in data['clients']:

        # For each stock in client's stock list
        for stock in client['tickers']:

            # Get stock's price
            price = getStockPrice(stock['ticker'])

            # Check if the stock is not in the given range
            if price < stock['lowerBound'] or price > stock['upperBound']:

                message = "Hello " + client["firstName"]  + ".\n" # greetings
                message += stock['ticker'] + "'s price of $" + str(price) + " is looking interesting!" # price warning
                print(message)
                sendText(message, client["phoneNumber"], client["carrier"])
