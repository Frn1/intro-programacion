Algoritmo CalculadoraDePorcentajesDeSexos
	Definir cantidadDeHombres, cantidadDeMujeres Como Entero
	
	Escribir "Escriba cuantos hombres hay en el grupo de estudiantes:"
	Leer cantidadDeHombres
	Mientras cantidadDeHombres < 0 Hacer
		Escribir "No puede haber ", cantidadDeHombres, " hombres. Compruebe lo que escribio."
		Escribir "Escriba cuantos hombres hay en el grupo de estudiantes:"
		Leer cantidadDeHombres
	FinMientras
	
	Escribir "Escriba cuantas mujeres hay en el grupo de estudiantes:"
	Leer cantidadDeMujeres
	Mientras cantidadDeMujeres < 0 Hacer
		Escribir "No puede haber ", cantidadDeMujeres, " mujeres. Compruebe lo que escribio."
		Escribir "Escriba cuantas mujeres hay en el grupo de estudiantes:"
		Leer cantidadDeMujeres
	FinMientras
	
	Definir cantidadDeEstudiantes Como Entero
	cantidadDeEstudiantes <- cantidadDeHombres + cantidadDeMujeres
	
	Escribir (cantidadDeHombres / cantidadDeEstudiantes) * 100, "% del grupo de estudiantes son hombres"
	Escribir (cantidadDeMujeres / cantidadDeEstudiantes) * 100, "% del grupo de estudiantes son mujeres"
FinAlgoritmo
