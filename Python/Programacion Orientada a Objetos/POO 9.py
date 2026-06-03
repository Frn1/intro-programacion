class Coche:
    kilometraje: float = 0.0

    def conducir(self, distancia: float):
        if distancia <= 0:
            return
        self.kilometraje += distancia
