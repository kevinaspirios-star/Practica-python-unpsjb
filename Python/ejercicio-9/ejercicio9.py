

class CuentaBancaria:
    def __init__(self,titular,saldo=0.0):
        self.titular=titular
        self.saldo=saldo

    def depositar(self,depositar):

        if depositar > 0:
            self.saldo=depositar
            print(f"Deposito Realizado Correctamente, Dinero actual: {self.saldo}")
        else:
            raise ValueError("El dinero a depositar es menor a 0")

    def retirar(self,retirar):

        if self.saldo>retirar:
            self.saldo-=retirar
            print(f"Retiro Realizado Correctamente, Dinero Actual: {self.saldo}")
        else:
            raise ValueError("Dinero insuficiente")
    def mostrarInfo(self):

        print(f"Titular: {self.titular}, Saldo Disponible: {self.saldo}")


cuenta1=CuentaBancaria("kevin")

cuenta1.mostrarInfo()
cuenta1.depositar(100)
cuenta1.retirar(30)

cuenta2=CuentaBancaria("Facundo",130)

cuenta2.mostrarInfo()
cuenta2.retirar(50)
cuenta2.depositar(-12)