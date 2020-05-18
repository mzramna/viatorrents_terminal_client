from bs4 import BeautifulSoup
import requests
url="https://viatorrents.com/x-men-classico-download-via-torrent/"
source=requests.get(url).text
bs=BeautifulSoup(source,"lxml")
teste=bs.find(id="lista_download")
print(teste.prettify())
bs=BeautifulSoup(teste.prettify(),"lxml")
teste=bs.find_all('a')
print(teste)

for i in teste:
    print(i['href'])