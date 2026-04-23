Algoritmo RegistroDeTemperaturas
	Definir cantidadDeTemperaturas Como Entero
	cantidadDeTemperaturas <- 7
	Dimensionar temperaturas[cantidadDeTemperaturas]
	
	Para i <- 1 Hasta cantidadDeTemperaturas Hacer
		Escribir "Ingrese temperatura del día ", i, " " Sin Saltar
		Leer temperaturas[i]
	FinPara
	
	Definir seleccion Como Entero
	Definir salir Como Logico
	Definir sumaPromedio Como Real
	Definir tempMayor Como Real
	salir <- Falso
	Mientras salir == Falso Hacer
		Escribir ""
		Escribir "--- Menú ---"
		Escribir " 1. Ver todas las temperaturas"
		Escribir " 2. Ver el promedio de las temperaturas"
		Escribir " 3. Ver el día más caluroso"
		Escribir " 4. Salir"
		Escribir "Su selección " Sin Saltar
		Leer seleccion
		
		Segun seleccion Hacer
			1:
				Escribir "Las temperaturas son " Sin Saltar
				Para i<-1 Hasta cantidadDeTemperaturas Con Paso 1 Hacer
					Escribir temperaturas[i], " °C" Sin Saltar
					
					Si i <> cantidadDeTemperaturas Entonces // El último valor no lleva nada después
						Si i == cantidadDeTemperaturas - 1 Entonces
							Escribir " y " Sin Saltar // El ante-último valor usa " y "
						SiNo
							Escribir ", " Sin Saltar // Si no, usan comas
						FinSi
					FinSi
				Fin Para
			2:
				sumaPromedio <- 0.0
				Para Cada temp De temperaturas Hacer
					sumaPromedio <- temp + sumaPromedio
				FinPara
				Escribir "El promedio es ", sumaPromedio / cantidadDeTemperaturas, " °C"
			3:
				tempMayor <- temperaturas[1]
				Para Cada temp De temperaturas Hacer
					Si temp > tempMayor Entonces
						tempMayor <- temp
					FinSi
				FinPara
				Escribir "La temperatura mayor es ", tempMayor, " °C"
			4:
				Escribir "Saliendo..."
				salir <- Verdadero
			De Otro Modo:
				Escribir "No reconozco esa opción"
		FinSegun
	FinMientras
FinAlgoritmo
