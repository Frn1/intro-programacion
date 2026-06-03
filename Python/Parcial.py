def calcular_comision(monto: float, cat: int | str):
    match cat:
        case 0 | "A" | "a":
            return monto * 0.10
        case 1 | "B" | "b":
            return monto * 0.15
        case 2 | "C" | "c":
            return monto * 0.20
        case _:
            raise Exception("Categoría no reconocida")


class Vendedor:
    def __init__(self, legajo: int, categoria: int, total_ventas: float) -> None:
        self.legajo = legajo
        self.categoria = categoria
        self.total_ventas = total_ventas
        pass

    def comision(self) -> float:
        # Esto llama a la funcion calcular_comision definida arriba
        return calcular_comision(self.total_ventas, self.categoria)


def parcial(cantidad_vendedores: int):
    # Creamos la lista de vendedores
    vendedores: list[Vendedor] = []

    for i in range(cantidad_vendedores):
        legajo = 0
        while True:
            entrada = input(f"Ingrese el legajo del vendedor {i + 1}: ").strip()
            if entrada.isnumeric():
                legajo = int(entrada)
                if legajo < 0:
                    print("Legajo no puede ser negativo, pruebe de nuevo.")
                else:
                    break  # El legajo es válido! salimos del while
            else:
                print("Legajo invalido, pruebe de nuevo.")

        print("")  # Linea vacia porque se ve lindo :3

        categoria = -1
        while True:
            entrada = (
                input(f"Ingrese la categoría del vendedor {i + 1}: ").strip().upper()
            )
            match entrada:
                case "A":
                    categoria = 0  # Categoria A = 0
                    break  # La categoria es válida! salimos del while
                case "B":
                    categoria = 1  # Categoria B = 1
                    break  # La categoria es válida! salimos del while
                case "C":
                    categoria = 2  # Categoria C = 2
                    break  # La categoria es válida! salimos del while
                case _:
                    print("Categoría no encontrada, pruebe de nuevo.")

        print("")  # Linea vacia porque se ve lindo :3

        total_ventas = -1
        while True:
            entrada = (
                input(f"Ingrese el total de ventas del vendedor {i + 1}: ")
                .strip()
                .upper()
            )
            if entrada.isdecimal():
                total_ventas = float(entrada)
                if total_ventas < 0:
                    print("El total de ventas no puede ser negativo, pruebe de nuevo.")
                else:
                    break  # El total es válido! salimos del while
            else:
                print("Total de ventas invalido, pruebe de nuevo.")

        print("")  # Linea vacia porque se ve lindo :3

        # Creamos el vendedor y lo sumamos a la lista
        vendedores.append(Vendedor(legajo, categoria, total_ventas))

    if len(vendedores) == 0:
        print("No se introdujeron vendedores")
        return

    total_comisiones = 0.0
    vendedor_con_mas_ventas = (
        None  # Empieza como None porque no guardamos la info de ningun vendedor todavia
    )
    for vendedor in vendedores:
        comision = vendedor.comision()
        total_comisiones += comision
        if vendedor_con_mas_ventas is not None:
            if vendedor.total_ventas > vendedor_con_mas_ventas.total_ventas:
                vendedor_con_mas_ventas = vendedor
        else:
            vendedor_con_mas_ventas = vendedor

    # Chequeo de sanidad para asegurarnos que encontramos el vendedor con mas ventas
    # Si no, esto deberia tirar un error
    assert vendedor_con_mas_ventas is not None

    print(f"Total de comisiones a pagar: {total_comisiones:.2f}")
    print(
        f"Legajo del vendedor con más total de ventas: {vendedor_con_mas_ventas.legajo}"
    )


if __name__ == "__main__":
    cant_vendedores = int(input("Ingrese la cantidad de vendedores: "))
    print("")  # Linea vacia porque se ve lindo :3
    parcial(cant_vendedores)
