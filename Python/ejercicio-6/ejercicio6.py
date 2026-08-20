print("MENU")
print("1.Calcular la suma de los primeros N numeros naturales.")
print("2.Encontrar todos los Numeros divisibles por 3 en un rango determinado por usted")
print("3.Salir")
opcion=int (input("que operacion desea realizar: "))
def _sumaDeNaturales_(N):
    sumas=1
    for i in range(N):
        sumas += 1
        result=N * sumas // 2
    print(f"resultado de la suma de los Primeros numeros naturales: {result}")

def _numerosDivisiblesX3_(N):
    for i in range(N):
        if i%3==0:
            print(f"El numero {i} es divisible por 3")
    
match opcion:
    case 1:
        N=int(input("Ingrese el numero para calcular la suma de sus primeros numeros naturales: "))
        _sumaDeNaturales_(N)
    case 2:
        N=int(input("Ingrese el Rango en el que se buscaran todos los numeros divisibles por 3: "))
        _numerosDivisiblesX3_(N)
    case 3:
        print("Fin del Programa")

