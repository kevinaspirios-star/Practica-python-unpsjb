from Biblioteca.modelos.libro import Libro
from Biblioteca.servicios.prestamo import Prestamo

libro1=Libro("Pinocho","Gaston",978)

prestamo1=Prestamo()

prestamo1.prestar(libro1)
prestamo1.estadoActual(libro1)
prestamo1.devolucion(libro1)
prestamo1.estadoActual(libro1)