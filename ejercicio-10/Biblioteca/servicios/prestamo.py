from Biblioteca.modelos.libro import Libro

class Prestamo:
    def __init__(self):
        pass

    def prestar(self,libro:Libro):

        if libro.disponible==True:
            libro.disponible=False
            print("Prestamos realizado")
        else:
            print(f"El Libro {libro.titulo} no esta disponible")

    def devolucion(self,libro:Libro):

        if libro.disponible==False:
            libro.disponible=True
            print("El libro fue devuelto con exito")
        else:
            print(f"El libro {libro.titulo} ya figuraba como disponible")

    def estadoActual(self,libro:Libro):

        if libro.disponible==True:
            print("Estado: Disponible")
        else:
            print("Estado: No Disponible")

        print(f"Libro: {libro.titulo}")
        print(f"Autor: {libro.autor}")
        print(f"Isbn: {libro.isbn}")

