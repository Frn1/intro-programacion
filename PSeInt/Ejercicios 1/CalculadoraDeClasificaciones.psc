Funcion calificacion <- LeerNota ( mensaje )
	Escribir mensaje
	Leer calificacion
	Mientras calificacion < 0 o calificacion > 10 Hacer
		Escribir "ERROR: No se pudo haber sacado ", calificacion, ". Compruebe lo que escribio."
		Escribir mensaje
		Leer calificacion
	FinMientras
Fin Funcion

Algoritmo CalculadoraDeClasificacionFinal
	Definir cantidadDeParciales Como Entero
	cantidadDeParciales <- 3
	
	Definir sumaDeParciales Como Real
	sumaDeParciales <- 0
	Para i=1 Hasta cantidadDeParciales Hacer
		sumaDeParciales <- sumaDeParciales + LeerNota("Escriba la clasificacion de su parcial " + ConvertirATexto(i) + ": ")
	Fin Para
	Definir parciales Como Real
	parciales <- sumaDeParciales / cantidadDeParciales
	
	Definir examenFinal Como Real
	examenFinal <- LeerNota("Escriba la clasificacion de su examen final:")
	
	Definir trabajoFinal Como Real
	trabajoFinal <- LeerNota("Escriba la clasificacion de su trabajo final:")
	
	Escribir "Su clasificacion final es ", (parciales * 0.55 + examenFinal * 0.3 + trabajoFinal * 0.15)
FinAlgoritmo

