Algoritmo CargaCondicionada
	Definir cantidadMáxima, cantidadIntroducida Como Entero
	cantidadMáxima <- 20
	cantidadIntroducida <- 0
	Dimensionar valoresIntroducidos[cantidadMáxima]
	
	Escribir "Ingrese hasta ", cantidadMáxima, " valores. O ingrese un valor negativo para terminar antes."
	
	Definir valorIngresado Como Real
	Definir seguirRecibiendoValores Como Logico
	seguirRecibiendoValores <- Verdadero
	Mientras cantidadIntroducida < cantidadMáxima Y seguirRecibiendoValores Hacer
		Escribir "Ingrese el valor ", cantidadIntroducida + 1, " " Sin Saltar
		Leer valorIngresado
		Si valorIngresado < 0 Entonces
			seguirRecibiendoValores <- Falso
		SiNo
			cantidadIntroducida <- cantidadIntroducida + 1
			valoresIntroducidos[cantidadIntroducida] = valorIngresado
		FinSi
	FinMientras
	
	Si cantidadIntroducida == cantidadMáxima Entonces
		Escribir "Ya no entran más valores."
	FinSi
	
	Si cantidadIntroducida == 0 Entonces
		Escribir "No se ingresaron valores."
	SiNo
		Definir suma Como Real
		suma <- 0
		Para i<-1 Hasta cantidadIntroducida Con Paso 1 Hacer
			suma <- suma + valoresIntroducidos[i]
		Fin Para
		Escribir "" // Línea vacia
		Escribir "El promedio es ", suma / cantidadIntroducida
	FinSi
FinAlgoritmo
