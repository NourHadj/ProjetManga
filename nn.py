import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import os

url="https://www.scan-fr.co/manga/princess/76/1"
cle="https://www.scan-fr.co/manga/"

def Navigate(url):
    if url !="Fin du Manga":
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        ListLiens = RecupListeLiens(soup)
    return [soup, ListeLiens]

def RecupListeLiens(soup):
    Div =soup.findAll('div')[22]
    img = Div.findAll('img')
    L=[]
    for item in img:
        L.append(item['data-src'])
    return L

def Next(url):
    nexturl=""
    plouf=int(url.split('/')[5])+1
    paf=url.split('/')[4]
    nexturl=cle+paf+"/"+str(plouf)+"/"+str(1)
    heyhey=str(soop(nexturl).findAll('h1'))
    print(heyhey)
    if heyhey=='[]':
        nexturl="Fin du Manga"
    return nexturl

def soop(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup