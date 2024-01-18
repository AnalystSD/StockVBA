# -*- coding: utf-8 -*-

from IPython.utils.text import get_text_list
from bs4 import BeautifulSoup
import requests
import time
import datetime
import smtplib
import datetime
import csv

url ='https://finance.yahoo.com/most-active/'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}
page = requests.get(url, headers=headers)

soup1 = BeautifulSoup(page.content, "html.parser")
soup2 = BeautifulSoup(soup1.prettify(),"html.parser")

stocks = soup2.find_all('tr',class_="simpTblRow")
cur = datetime.date.today()
curf = cur.strftime('%d/%m/%y')
tim = datetime.datetime.now()
tim2 = tim.strftime('%H:%M%p %Z')

header = ['Name','Price','Change','Volume','Market Cap','Date','Time']
with open('YahooMostActiveWS.csv','w',newline='',encoding='UTF8') as f:
  writer = csv.writer(f)
  writer.writerow(header)
  for a in stocks:
    sname = a.find("td",{"aria-label": "Name"}).text.strip()
    sprice = a.find("td",{"aria-label": "Price (Intraday)"}).text.strip()
    schange = a.find("td",{"aria-label": "Change"}).text.strip()
    svolume = a.find("td",{"aria-label": "Volume"}).text.strip()[:-1]
    smarketc = a.find("td",{"aria-label": "Market Cap"}).text.strip()[:-1]
    data = [sname,sprice,schange,svolume,smarketc,curf,tim2]

    writer.writerow(data)
    print(sname,sprice,schange,svolume,smarketc,curf,tim2)