#Import library
import requests
import csv
from bs4 import BeautifulSoup
import pandas as pd

#link web yang akan dilakukan proses crawling 
response = requests.get("linkweb.com")
soup = BeautifulSoup(response.text, "html.parser")
judul_tabel = soup.find('table', class_='#classTable')
baris_tabel = judul_tabel.find_all('tr')

rows = []
columns = ['Nama kolom']

for tr in baris_tabel[1:]:
	td=tr.find_all('td')
	baris = [i.text.replace('\n', '').strip() for i in td]
	rows.append(baris)

df = pd.DataFrame(rows, columns=columns)
df.to_csv('Nama_File.csv', index=False)
