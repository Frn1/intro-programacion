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

Algoritmo CalculadoraDeBono
	Definir sueldo Como Real
	Definir bono Como Real
	bono <- 25.0 / 100.0
	
	sueldo <- LeerCantidadDeDinero("Introduzca su sueldo: ")
	
	Escribir "El sueldo más bono es: ", sueldo * (1.0 + bono)
FinAlgoritmo
