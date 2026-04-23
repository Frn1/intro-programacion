// Calcula el total con descuento desde un subtotal
Algoritmo CalculadoraDeDescuento
	Definir descuento, subtotal Como Real
	descuento <- 15.0 / 100.0
	
	Escribir "Escriba su subtotal: "
	Leer subtotal
	Mientras subtotal < 0 Hacer
		Escribir "Escriba su subtotal: "
		Leer subtotal
	FinMientras
	
	// subtotal * (1.0 - descuento) = subtotal - subtotal * descuento
	Escribir "Su total es: ", subtotal * (1.0 - descuento)
FinAlgoritmo
