from bs4 import BeautifulSoup
import urllib2
fecha = "21/11/2016" #Aca valido la fecha
url_adress = "http://www.bna.com.ar/Cotizador/HistoricoPrincipales?id=billetes&fecha=" + fecha+"&filtroEuro=0&filtroDolar=1"

page = urllib2.urlopen(url_adress)

soup = BeautifulSoup(page, "html.parser")
table = soup.find('tbody')
rows = table.find_all('tr')
for tr in rows:
#Aca creo la lista con las cotizaciones.
    cols = tr.find_all('td')
    p = cols[0].text.strip()
    d = cols[1].text.strip()
    e = cols[2].text.strip()
    f = cols[3].text.strip()
    print(p)
    print(d)
    print(e)
    print(f)






