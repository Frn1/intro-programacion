Funcion valorLeido <- LeerCantidadDeDinero ( mensaje )
	Definir valorLeido Como Real
	Escribir mensaje
	Leer valorLeido
	Mientras valorLeido < 0 Hacer
		Escribir valorLeido, " no es una cantidad de dinero v?lida. Por favor verifique su entrada."
		Escribir mensaje
		Leer valorLeido
	FinMientras
Fin Funcion

Algoritmo DescuentoPorVolumen
	Definir valorDeCompra, descuento Como Real
	valorDeCompra <- LeerCantidadDeDinero("Escriba el valor de la compra: ")
	Si valorDeCompra > 10000 Entonces
		descuento <- 20.0 / 100
	SiNo
		descuento <- 5.0 / 100
	FinSi
	
	Escribir "El valor con descuento de la compra es ", valorDeCompra * (1.0 - descuento)
FinAlgoritmo
