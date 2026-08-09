
registros= [20.0,15.3,40.4,30.5,50.4]

def analizar_temperaturas(registros):
    minimo=min(registros)
    maximo=max(registros)
    sumaTotal= sum(registros)
    cant= len(registros)
    promedio= sumaTotal/cant
    Max,Min,Prod=[maximo, minimo,promedio]
    print(f"Temperatura Maxima: {Max}")
    print(f"Temperatura Minima: {Min}")
    print(f"Promedio de las temperaturas del registro: {Prod}")


analizar_temperaturas(registros)