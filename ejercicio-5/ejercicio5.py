paswd= input("ingrese una contrasenia: ")
i=0
tieneMin=False
tieneMayus=False
condicion=False
if len(paswd) >= 8 :
    while i < len(paswd):
        if paswd[i].isupper():
            tieneMayus=True
            
        if paswd[i].islower():
            tieneMin=True
            
        if  tieneMin==True and tieneMayus==True :
           condicion=True
           break
        i+=1
    if condicion==True:
     print("Contrasenia ingresada correctamente")
    else:
       print("error, la contrasenia debe tener por lo menos un caracter mayuscula y minuscula") 

else:
    print("error, la contrasenia debe tener 8 caracteres o mas")