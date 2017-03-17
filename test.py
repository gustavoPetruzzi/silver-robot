# test

import cotizacion

print cotizacion.validarFecha("1/1/1991")
#Pruebo si me instancia bien el objeto
cotizacionDia = cotizacion.cotizacion("21/11/1991", 15.49, 19)
print isinstance(cotizacionDia, cotizacion.cotizacion)