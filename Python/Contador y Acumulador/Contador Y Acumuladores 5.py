def ejercicio5():
    menores = 0
    suma_edad_menores = 0
    adultos = 0
    suma_edad_adultos = 0
    while True:
        edad = int(input("Ingrese la edad: "))
        if edad == -1:
            break
        if edad < 0 or edad > 100:
            continue
        
        if edad < 18:
            menores += 1
            suma_edad_menores += edad
        else:
            adultos += 1
            suma_edad_adultos += edad
    
    if menores == 0:
        print(f"Hay {menores} menores")
    else:
        print(f"Hay {menores} menores, con edad promedio {suma_edad_menores / menores}")
    
    if adultos == 0:
        print(f"Hay {adultos} adultos")
    else:
        print(f"Hay {adultos} adultos, con edad promedio {suma_edad_adultos / adultos}")
    
if __name__ == "__main__":
    ejercicio5()