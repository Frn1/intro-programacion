Algoritmo NotasDeAlumnos
	Definir cantidadDeAlumnos, cantMaximaDeAlumnos Como Entero
	cantidadDeAlumnos <- 0
	cantMaximaDeAlumnos <- 10
	Dimensionar nombres[cantMaximaDeAlumnos], notas1[cantMaximaDeAlumnos], notas2[cantMaximaDeAlumnos]
	
	Definir correr Como Logico
	correr <- Verdadero
	
	Definir entrada Como Entero
	Definir nombre Como Caracter
	Definir notaIngresada Como Real
	Mientras correr Hacer
		Escribir ""
		Escribir "--- Menú ---"
		Escribir " 1: Registrar nuevo alumno"
		Escribir " 2: Mostrar promedio de todos los alumnos"
		Escribir " 3: Salir"
		Escribir "Su seleccion " Sin Saltar
		Leer entrada
		
		Segun entrada Hacer
			1:
				Si cantidadDeAlumnos < cantMaximaDeAlumnos Entonces
					cantidadDeAlumnos <- cantidadDeAlumnos + 1
					Escribir "Introduzca el nombre del alumno " Sin Saltar
					Leer nombre
					nombres[cantidadDeAlumnos] <- nombre
					
					Escribir "Introduzca la nota 1 del alumno " Sin Saltar
					Leer notaIngresada
					notas1[cantidadDeAlumnos] <- notaIngresada
					
					Escribir "Introduzca la nota 2 del alumno " Sin Saltar
					Leer notaIngresada
					notas2[cantidadDeAlumnos] <- notaIngresada
					
					Escribir "Alumno ", nombre, " registrado correctamente."
				SiNo
					Escribir "No se pueden agregar más de ", cantMaximaDeAlumnos, " alumnos."
				FinSi
			2:
				Si cantidadDeAlumnos == 0 Entonces
					Escribir "No hay ningun alumno registrado!"
				SiNo
					Escribir "Estos son los promedios:"
					Para i <- 1 Hasta cantidadDeAlumnos Hacer
						Escribir nombres[i], " - Promedio: ", (notas1[i] + notas2[i]) / 2
					FinPara
				FinSi
			3:
				correr <- Falso
				Escribir "Adios! :3"
			De Otro Modo:
				Escribir "No reconozco esa opcion."
		Fin Segun
	FinMientras
FinAlgoritmo
