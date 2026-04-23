Algoritmo SumadorDeNúmeros
	Definir n, suma Como Real
	suma <- 0
	Escribir "Ingrese números para sumar. Ingresar 0 muestra el resultado y termina el programa."
	Repetir
		Leer n
		suma <- suma + n
		Si n <> 0 Entonces
			Escribir "Siguiente número: (Suma actual: ", suma, ". Escriba 0 para terminar)"
		FinSi
	Hasta Que n == 0
	Escribir "La suma es: ", suma
FinAlgoritmo
