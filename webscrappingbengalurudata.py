import requests

import csv

from bs4 import BeautifulSoup as bs
url=requests.get("https://rates.goldenchennai.com/vegetable-price/bangalore-vegetable-price-today/")
soup=bs(url.content,'html.parser')
filename='13April2021.csv'
csv_writer=csv.writer(open(filename,'w'))
# run a for loop to extract the table data ad store it in csv file

for tr in soup.find_all('tr'):
    data = []
    # for extracting the  th
    for th in tr.find_all('th'):
        data.append(th.text)

    if data:
        print("Inserting headers:{}".format(','.join(data)))
        csv_writer.writerow(data)
        continue

    # for scraping the actual table data values

    for td in tr.find_all('td'):
        data.append(td.text.strip())
    if data:
        print("Inserting Table Data:{}".format(','.join(data)))
        csv_writer.writerow(data)
