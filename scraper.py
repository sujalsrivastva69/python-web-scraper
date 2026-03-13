
import requests
from bs4 import BeautifulSoup
import sqlite3

Url = input("Enter Website Url :")
responce = requests.get(Url)
soup = BeautifulSoup(responce.text,"html.parser")

heading = soup.find_all("h2")
links = soup.find_all("a")
conn = sqlite3.connect("database.db")
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS pages(title TEXT)")

for h in heading:
    title = h.text
    print(title)


    cur.execute("INSERT INTO pages (title) VALUES(?)", (title, ))
for link in links:
    print(link.get('href'))
conn.commit()
conn.close