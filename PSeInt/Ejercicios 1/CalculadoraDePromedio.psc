Funcion nota <- IngresarNota ( mensaje ) 
	Escribir mensaje
	Leer nota
	Mientras nota < 0 o nota > 10 Hacer
		Escribir "Esa no es una nota válida. Por favor verifique su entrada."
		Escribir mensaje
		Leer nota
	FinMientras
FinFuncion

Funcion promedio <- CalcularPromedio ( nombre, cantidadDeTareas, porcentajePorExamenFinal )
	promedio <- 0
	Escribir "--- Notas para ", nombre, " ---"
	Para i<-1 Hasta cantidadDeTareas Con Paso 1 Hacer
		promedio <- promedio + IngresarNota ( "Ingrese la nota de la tarea " + ConvertirATexto(i) + " de " + nombre + ": " ) * (1.0 - porcentajePorExamenFinal) / cantidadDeTareas
	Fin Para
	promedio <- promedio + IngresarNota( "Ingrese la nota del examen final" + " de " + nombre + ": " ) * porcentajePorExamenFinal
	Escribir "Su promedio para ", nombre, " es ", promedio
Fin Funcion

Algoritmo CalculadoraDePromedio
	Definir cantidadDeMaterias Como Entero
	cantidadDeMaterias <- 3
	Dimensionar nombres[cantidadDeMaterias], tareasPorMateria[cantidadDeMaterias], porcentajePorExamenFinal[cantidadDeMaterias]
	
	nombres[1] = "Matemáticas"
	tareasPorMateria[1] = 3
	porcentajePorExamenFinal[1] = 90.0 / 100.0
	
	nombres[2] = "Física"
	tareasPorMateria[2] = 2
	porcentajePorExamenFinal[2] = 80.0 / 100.0
	
	nombres[3] = "Química"
	tareasPorMateria[3] = 3
	porcentajePorExamenFinal[3] = 85.0 / 100.0
	
	Definir sumaTotal Como Real
	sumaTotal <- 0
	Para i<-1 Hasta 3 Con Paso 1 Hacer
		sumaTotal <- sumaTotal + CalcularPromedio(nombres[i], tareasPorMateria[i], porcentajePorExamenFinal[i])
		Escribir ""
	Fin Para
	
	Escribir "Su promedio general es ", sumaTotal / cantidadDeMaterias
FinAlgoritmo

