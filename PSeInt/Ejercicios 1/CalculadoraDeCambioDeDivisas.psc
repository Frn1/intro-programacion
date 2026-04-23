Funcion valorLeido <- LeerCantidadDeDinero ( mensaje )
	Definir valorLeido Como Real
	Escribir mensaje
	Leer valorLeido
	Mientras valorLeido < 0 Hacer
		Escribir valorLeido, " no es una cantidad de dinero válida. Por favor verifique su entrada."
		Escribir mensaje
		Leer valorLeido
	FinMientras
Fin Funcion


Algoritmo CalculadoraDeCambioDeDivisas
	Definir bolívares, dólasres Como Real
	Definir divisaBolivaresADolares Como Real
	
	bolívares <- LeerCantidadDeDinero("Escriba la cantidad de bolívares a convertir")
	divisaBolivaresADolares <- LeerCantidadDeDinero("Escriba la divisa de cambio de bolívares a dólares")
	dólares <- bolívares * divisaBolivaresADolares
	
	Escribir bolívares, " bolivar(es)=", dólares, " dolar(es)"
FinAlgoritmo
