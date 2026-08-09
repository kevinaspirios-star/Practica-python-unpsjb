
precio_base=int(input("ingrese el precio base del producto: "))

vip=int(input("es vip? ingrese 1(si), 2(no): "))
es_vip=False
def calcular_precio_final(precio_base,porcentaje_descuento=10,es_vip=False):
    precioCon_descuento=precio_base
    precioCon_descuento-=precio_base * (porcentaje_descuento/100)
    if es_vip==True:
        precioCon_descuento -= precio_base * (5/100)
        print(f"Precio con descuento normal y vip incluido es: {precioCon_descuento}")
        return
    print(f"Precio con descuento normal es: {precioCon_descuento}")

if precio_base >0:
    if vip==1:
     calcular_precio_final(precio_base,es_vip=True)
    elif vip==2:
     calcular_precio_final(precio_base)
else:
   raise ValueError("El precio base debe ser mayor a 0")
