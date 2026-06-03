class CuentaBancaria:
    saldo: float = 0

    def __init__(self) -> None:
        pass

    def depositar(self, cantidad: float):
        if cantidad <= 0:
            return
        self.saldo += cantidad

    def retirar(self, cantidad: float):
        if cantidad <= 0:
            return
        if self.saldo < cantidad:
            return  # No hay suficiente dinero para retirar
        self.saldo -= cantidad
