import random

cant_digitos = 4
digitos_secretos = [random.randint(0, 9) for i in range(cant_digitos)]

while True:
    # print(f"DEBUG: {digitos_secretos}")
    caracteres_ingresados = input("Adivine el numero... ")[0:cant_digitos]

    if caracteres_ingresados == "-1":
        secreto = ""
        for d in digitos_secretos:
            secreto += str(d)
        print(f"El numero era {secreto}")
        break

    if not caracteres_ingresados.isnumeric():
        print("Eso no es un numero valido")
        continue
    elif len(caracteres_ingresados) != cant_digitos:
        print(f"Debe introducir {cant_digitos} digitos")
        continue

    # Dividimos el texto ingresado en una lista de caracteres
    caracteres: list[int | str] = list(caracteres_ingresados)
    # Lo convertimos a numeros
    for i in range(len(caracteres)):
        caracteres[i] = int(caracteres[i])
    secreto = list(digitos_secretos)
    posicion_correcta = 0
    caracter_correcto = 0
    # Vamos en el order reverso para poder ir removiendo los elementos sin hacer lios
    for i in range(cant_digitos - 1, -1, -1):
        if secreto[i] == caracteres[i]:
            secreto.pop(i)
            caracteres.pop(i)
            posicion_correcta += 1

    if posicion_correcta == cant_digitos:
        print("Ganaste!! Descubriste el código secreto!")
        break

    # Ahora utilizamos los caracteres que quedaron para calcular
    # cuantos estan en el secreto, pero no en la posicion correcta
    for c in caracteres:
        if c in secreto:
            # Lo removemos para hacer manejar duplicados correctamente
            secreto.remove(c)
            caracter_correcto += 1

    print(
        f"{posicion_correcta} correcto{'s' if posicion_correcta != 1 else ''} y {caracter_correcto} aproximado{'s' if caracter_correcto != 1 else ''}"
    )
