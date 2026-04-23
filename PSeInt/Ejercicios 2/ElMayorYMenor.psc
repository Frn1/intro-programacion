Algoritmo ElMayorYMenor
	Definir valorMáximo, valorMínimo Como Entero
	valorMáximo <- 30
	valorMínimo <- 1
	Definir cantidadDeNumeros Como Entero
	cantidadDeNumeros <- 15
	Dimensionar nums[cantidadDeNumeros]
	Escribir "Los numeros son " Sin Saltar
	Para i<-1 Hasta cantidadDeNumeros Con Paso 1 Hacer
		nums[i] <- Azar(valorMáximo - valorMinimo) + valorMinimo
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
	
	// TODO: Esto se podría juntar con el bucle de arriba
	Definir valorMásGrande, valorMásChico Como Entero
	valorMásGrande <- valorMinimo // Inicializo este como el valor más chico para que cualquier otro valor sea más grande
	valorMásChico <- valorMáximo// Inicializo este como el valor más grande para que cualquier otro valor sea más chico
	Para i<-1 Hasta cantidadDeNumeros Con Paso 1 Hacer
		Si nums[i] > valorMásGrande Entonces
			valorMásGrande <- nums[i]
		FinSi
		Si nums[i] < valorMásChico Entonces
			valorMásChico <- nums[i]
		FinSi
	Fin Para
	Escribir "El valor más grande es ", valorMásGrande, " y el más chico es ", valorMásChico
FinAlgoritmo
