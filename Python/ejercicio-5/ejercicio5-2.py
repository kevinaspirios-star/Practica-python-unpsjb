CLAVE_CORRECTA="Admin1234"
INTENTOS=3
i=1
while i<= 3:
    paswd=input("ingrese su contrasenia para iniciar sesion: ")

    if paswd== CLAVE_CORRECTA:
        print("Contrasenia correcta")
        break
    elif i<=INTENTOS:
        print(f"Contrasenia incorrecta,cantidad de intentos restantes: {INTENTOS-i}")
        if INTENTOS-i ==0:
            print("intentos agotados, Cuenta Bloqueada")
    i+=1