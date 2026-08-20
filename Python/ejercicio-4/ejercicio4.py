numero= int(input("ingrese un numero para realizar la conversion: "))

escala= int(input("ingrese la escala original del numero anteriormente ingresado (1 Celsius o 2 Fahrenheit): "))

def get_Celsius_(numero):
    convert= (numero - 32) / 1.8
    print( f"Conversion a Celsius echa: {convert}")

def get_Fahrenheit_(numero):
    convert= (numero * 1.8) + 32
    print( f"Conversion a Fahrenheit echa: {convert}")

if escala == 1 :
    get_Celsius_(numero)
elif escala == 2 :
    get_Fahrenheit_(numero)