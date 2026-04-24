def ejercicio3():
    cantidad_de_alumnos = int(input("Ingrese la cantidad de alumnos que rindieron el examen: "))
    if cantidad_de_alumnos <= 0:
        print("Ningún alumno rindió el examen.")
        return
    
    suma_promedio = 0.0
    for i in range(cantidad_de_alumnos):
        suma_promedio += float(input(f"Ingrese la nota del alumno {i + 1}: "))
        
    print(f"El promedio es {suma_promedio / cantidad_de_alumnos}")
    
if __name__ == "__main__":
    ejercicio3()