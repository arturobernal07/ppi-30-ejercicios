class Cuentabancaria:
    def __init__(self, titular, saldo=0):
        self.__titular = titular
        self.__saldo = saldo

    def dep(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Depósito exitoso de ${cantidad}.")
        else:
            print("No se pueden depositar cantidades negativas")

    def ret(self, cantidad):
        if cantidad <= 0:
            print("No se pueden retirar cantidades negativas o cero")
        elif cantidad > self.__saldo:
            print("Fondo insuficiente")
        else:
            self.__saldo -= cantidad
            print(f"Retiro exitoso de ${cantidad}.")

    def consultar_titular(self):
        return self.__titular

    def consultar_saldo(self):
        return self.__saldo



if __name__ == "__main__":
    cuenta = Cuentabancaria("Luis Arturo", 500)
    print(f"Titular: {cuenta.consultar_titular()}")
    print(f"Saldo ${cuenta.consultar_saldo()}")
''
    cuenta.dep(300)
    cuenta.ret(200)
    cuenta.ret(1000)
    cuenta.dep(-50)
    print(f"Saldo final: ${cuenta.consultar_saldo()}")