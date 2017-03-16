#Cotizacion

from datetime import datetime
class cotizacion:
    'Common base class for cotizacion'
    
    def __init__(self,fecha,compra,venta):
        self.fecha = fecha
        self.compra = compra
        self.venta = venta
        
def validarFecha(fecha):
    try:
        print datetime.strptime(fecha, '%d/%m/%Y')
		
    except ValueError:
		raise ValueError("Formato incorrecto de fecha")
			
	
            
        