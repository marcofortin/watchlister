###################### Imports ###################### 
from datetime import datetime

################ Function Definition ################

# isMarketOpen() returns true if the stock market is currently opened (9:30 to 16:30)
def isMarketOpen() -> bool:

    now = datetime.now() # get current date and time
    isWeek = (now.weekday() != 5 and now.weekday() != 6) # not saturday nor sunday
    isBetween = (now.hour > 9 and now.hour < 16) # 10:00-16:00
    justPastOpen = (now.hour == 9 and now.minute >= 30) # 9:30-9:59
    justBeforeClose = (now.hour == 16 and now.minute < 30) # 16:00-16:29
    return isWeek and (isBetween or justPastOpen or justBeforeClose)