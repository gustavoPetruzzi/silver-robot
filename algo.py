from bs4 import BeautifulSoup
import cotizacion
import urllib2

# TODO: Ver como hacer si el usuario pone otro formato de fecha 
fecha = raw_input('Ingrese una fecha: ')
cotizacion.validarFecha(fecha)


url_adress = "http://www.bna.com.ar/Cotizador/HistoricoPrincipales?id=billetes&fecha=" + fecha +"&filtroEuro=0&filtroDolar=1"

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
	if fecha == f:
		cotizacionDia = cotizacion.cotizacion(f,e,d)	
		break;

print cotizacionDia.fecha
print cotizacionDia.compra
print cotizacionDia.venta






