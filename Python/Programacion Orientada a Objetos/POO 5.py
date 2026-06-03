class Ventilador:
    velocidad: int = 0

    def __init__(self) -> None:
        pass

    def apagar(self) -> None:
        self.velocidad = 0

    def encender(self) -> None:
        if self.velocidad == 0:
            self.velocidad = 1

    def subir_velocidad(self) -> None:
        if self.velocidad <= 0 or self.velocidad >= 3:
            return
        self.velocidad += 1

    def bajar_velocidad(self) -> None:
        if self.velocidad <= 0 or self.velocidad >= 3:
            return
        self.velocidad -= 1

    def esta_apagado(self) -> bool:
        return self.velocidad <= 0

    def esta_encendido(self) -> bool:
        return self.velocidad > 0

    def velocidad_actual(self) -> int | None:
        if self.esta_apagado():
            return None
        return self.velocidad
