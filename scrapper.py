###################### Imports ###################### 
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time

################ Function Definition ################

# getStockPrice(stockTicker) retrieves the stock's real time price from TMX Money website 
#                            and returns it's value
def getStockPrice(stockTicker : str) -> float:
    
    # Set path to chromedriver
    driver = webdriver.Chrome("/Users/marcofortin/Library/chromedriver")
    
    # Open driver (TMX Money URL)
    tmxUrl = "https://money.tmx.com/en/quote/"
    tmxUrl += stockTicker
    driver.get(tmxUrl)
    time.sleep(5) # wait 5sec to load content

    # Find div tag containing price's real time price
    content = driver.page_source
    soup = BeautifulSoup(content, features="lxml") # parse
    price = 0 # initialize price
    for div in soup.findAll('div', attrs={'class':'sc-pbXLt kdiNFw'}):
        price = float(div.get_text()[1:]) # remove '$' and convert to float
        break # only want first div

    # Quit driver
    driver.quit()

    return price