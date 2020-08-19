import pandas as pd
from scrape import get_stock
from sqlalchemy import create_engine
engine = create_engine('sqlite://', echo=False)

#links to google finance for a given company
cvs_link = 'https://www.google.com/search?q=NYSE:CVS&tbm=fin&stick=H4sIAAAAAAAAAONgecRoyi3w8sc9YSmdSWtOXmNU4-IKzsgvd80rySypFJLgYoOy-KR4uLj0c_UNzKtySjLSeBaxcvhFBrtaOYcFAwBcjq1kRQAAAA#scso=__Eo9X6KVKoTWtQbskYu4DA1:0'
wba_link = 'https://www.google.com/search?tbm=fin&q=NASDAQ%3A%20WBA#scso=_Pks9X7WRIYSGtQbCpb3QCg1:0'
mck_link = 'https://www.google.com/search?tbm=fin&q=NYSE%3A%20MCK#scso=_T0s9X-mPC-qD9PwP2fan0A81:0'

link_list = [cvs_link,wba_link,mck_link]

stock_df = pd.DataFrame(columns=["company","open_price","close_price","high","low","date"])

for link in link_list:
    stock_df = stock_df.append(get_stock(link),ignore_index=True)

stock_df.to_sql()