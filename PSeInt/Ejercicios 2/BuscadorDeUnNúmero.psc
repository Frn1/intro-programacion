Algoritmo BuscadorDeUnNúmero
	Definir cantidadDeNumeros Como Entero
	cantidadDeNumeros <- 10
	Dimensionar nums[cantidadDeNumeros]
	
	// Los números DEBEN estar ordenados de menor a mayor!
	// Si no todo se rompe!!
	nums[1] <- 3
	nums[2] <- 3
	nums[3] <- 3
	nums[4] <- 7
	nums[5] <- 10
	nums[6] <- 10
	nums[7] <- 13
	nums[8] <- 16
	nums[9] <- 18
	nums[10] <- 29
	
	Escribir "Los números son " Sin Saltar
	Para i<-1 Hasta cantidadDeNumeros Con Paso 1 Hacer
		Escribir nums[i] Sin Saltar
		
		Si i <> cantidadDeNumeros Entonces // El último valor no lleva nada después
			Si i == cantidadDeNumeros - 1 Entonces
				Escribir " y " Sin Saltar // El ante-último valor usa " y "
			SiNo
				Escribir ", " Sin Saltar // Si no, usan comas
			FinSi
		FinSi
	Fin Para
	Escribir "" // Hacemos que salte a la siguiente línea con un mensaje vacio
	
	Definir valorBuscado Como Entero
	Escribir "Escriba el valor a buscar" Sin Saltar
	Leer valorBuscado
	
	Definir seEncontró Como Logico
	seEncontró <- Falso
	Definir izq, med, der Como Entero
	izq <- 1
	der <- cantidadDeNumeros
	Mientras seEncontró == Falso Y izq <= der Hacer
		med <- izq + trunc((der - izq) / 2)
		Si nums[med] < valorBuscado Entonces
			izq <- med + 1
		SiNo
			Si nums[med] > valorBuscado Entonces
				der <- med - 1
			SiNo
				seEncontró <- Verdadero
			Fin Si
		Fin Si
	FinMientras
	
	Si seEncontró Entonces
		Escribir "Se encontró el número. Está en la posición ", med
	SiNo
		Escribir "No se encontró el número. Debería estar cerca de la posición ", med
	FinSi
FinAlgoritmo
