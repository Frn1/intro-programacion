def ejercicio2():
    meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
    numero_mes = int(input("Introduzca el número del mes: ")) - 1
    if numero_mes < 0 or numero_mes >= len(meses):
        print("Ese mes no existe")
        return
    print(f"Ese mes es {meses[numero_mes]}")

if __name__ == "__main__":
    ejercicio2()