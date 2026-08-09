costoPasaje=int(input("ingrese el costo estimado del Pasaje: "))

alojmientoXnoche=int(input("costo de alojamiento por noche: "))

cantNoches=int(input("Cantidad de noches que durara el viaje: "))

dineroDisp=int(input("ingrese su Dinero disponible: "))

costoTotal=costoPasaje+ (alojmientoXnoche * cantNoches)

if costoTotal<= dineroDisp :
 print(f"El costo total del vieja es: {costoTotal}")
else:
 print(f"Dinero insuficiente: {costoTotal} mayor a {dineroDisp}")