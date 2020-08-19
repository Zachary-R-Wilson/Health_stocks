import pandas as pd
from scrape import get_stock
import sqlite3

# create a connection and a cursor for sqlite
conn = sqlite3.connect('health.db')
c = conn.cursor()
# links to google finance for a given company
cvs_link = 'https://www.google.com/search?q=NYSE:CVS&tbm=fin&stick=H4sIAAAAAAAAAONgecRoyi3w8sc9YSmdSWtOXmNU4-IKzsgvd80rySypFJLgYoOy-KR4uLj0c_UNzKtySjLSeBaxcvhFBrtaOYcFAwBcjq1kRQAAAA#scso=__Eo9X6KVKoTWtQbskYu4DA1:0'
wba_link = 'https://www.google.com/search?tbm=fin&q=NASDAQ%3A%20WBA#scso=_Pks9X7WRIYSGtQbCpb3QCg1:0'
mck_link = 'https://www.google.com/search?tbm=fin&q=NYSE%3A%20MCK#scso=_T0s9X-mPC-qD9PwP2fan0A81:0'
# list to make it easier to call the links above
link_list = [cvs_link,wba_link,mck_link]
# create a dataframe to store the data
stock_df = pd.DataFrame(columns=["company","open_price","close_price","high","low","date"])
# call the get_stock function from scrape.py to fill the stock_df with the current data for today
for link in link_list:
    stock_df = stock_df.append(get_stock(link),ignore_index=True)

# save the data to the sqlite db, health.db, and commit the changes to the file
stock_df.to_sql('health', con=conn, if_exists='append',index=False)
conn.commit()