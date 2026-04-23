Algoritmo InversorDeNumeros
	Definir cantidadDeNumeros Como Entero
	cantidadDeNumeros <- 10
	Dimensionar nums[cantidadDeNumeros]
	Escribir "Ingrese los ", cantidadDeNumeros, " numeros"
	Para i<-1 Hasta cantidadDeNumeros Con Paso 1 Hacer
		Leer nums[i]
	Fin Para
	Escribir "El orden opuesto es:"
	Para i<-cantidadDeNumeros Hasta 1 Con Paso -1 Hacer
		Escribir nums[i]
	Fin Para
FinAlgoritmo
