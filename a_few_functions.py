from datetime import datetime as dt
from datetime import date as dte


def returndate():
    today = dte.today()
    d2 = today.strftime("%A, %B %d, %Y")
    return d2

def returntime():
    now = dt.now()
    dt_string = now.strftime("%H:%M")
    return(dt_string)
