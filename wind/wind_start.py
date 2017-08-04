from WindPy import *
from datetime import datetime

start = datetime(2017,7,25)
end = datetime(2017,7,31)

w.start()
print(w.wsd('090007.IB','close',start,end,'Priceadj=F;tradingcalendar=NIB'))