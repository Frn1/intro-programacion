Algoritmo MáquinaExpendedora
	Definir cantidadDeProductos Como Entero
	cantidadDeProductos <- 5
	Dimensionar nombres[cantidadDeProductos], precios[cantidadDeProductos]
	
	nombres[1] <- "Coca-cola"
	precios[1] <- 1200
	nombres[2] <- "Pepsi"
	precios[2] <- 1100
	nombres[3] <- "7-up"
	precios[3] <- 1500
	nombres[4] <- "Fanta"
	precios[4] <- 20
	nombres[5] <- "Manaos"
	precios[5] <- 1000
	
	Escribir "--- Máquina expendedora ---"
	Escribir "Productos:"
	Para i<-1 Hasta cantidadDeProductos Con Paso 1 Hacer
		Escribir " ", i, " - ", nombres[i], ": ", precios[i], " pesos"
	Fin Para
	
	Definir productoElegido Como Entero
	Escribir "Eliga su producto " Sin Saltar
	Leer productoElegido
	
	Si productoElegido < 0 o productoElegido > cantidadDeProductos Entonces
		Escribir "Ese producto no está disponible."
	SiNo
		Escribir "" // Inserto una línea vacia
		Escribir "Usted eligió: ", nombres[productoElegido], "."
		Escribir "Debe pagar: ", precios[productoElegido], " pesos."
	FinSi
FinAlgoritmo
