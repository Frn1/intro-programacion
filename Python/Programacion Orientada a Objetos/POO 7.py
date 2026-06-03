class Celular:
    bateria: float = 100.0

    def __init__(self) -> None:
        pass

    def hacer_llamada(self, minutos: float):
        self.bateria -= minutos
        if self.bateria < 0.0:
            self.bateria = 0

    def cargar(self):
        self.bateria = 100
