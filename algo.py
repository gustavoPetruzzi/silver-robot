from bs4 import BeautifulSoup
import urllib2

url_adress = "http://www.bna.com.ar/Cotizador/HistoricoPrincipales?id=billetes&fecha=09/03/2017&filtroEuro=0&filtroDolar=1"

page = urllib2.urlopen(url_adress)

soup = BeautifulSoup(page, "html.parser")
table = soup.find('tbody')
rows = table.find_all('tr')
for tr in rows:
    cols = tr.find_all('td')
    p = cols[0].text.strip()
    d = cols[1].text.strip()
    e = cols[2].text.strip()
    f = cols[3].text.strip()
    print(p)
    print(d)
    print(e)
    print(f)






