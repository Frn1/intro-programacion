class Libro:
    prestado: bool = False

    def __init__(self) -> None:
        pass

    def prestar(self):
        if self.prestado:
            print("Este libro ya está prestado!")
            return
        self.prestado = True

    def devolver(self):
        if not self.prestado:
            print("Este libro no fue prestado!")
            return
        self.prestado = False
