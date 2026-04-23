// Calcula la cantidad de interes despues de una cantidad de meses
Algoritmo CalculadoraDeInteres
	Definir dineroInvertido, porcentajeInteres Como Real
	Definir cantidadDeMeses Como Entero
	porcentajeInteres <- 2.0 / 100.0
	
	Escribir "Escriba cuanto dinero va a invertir: "
	Leer dineroInvertido
	Mientras dineroInvertido < 0 Hacer
		Escribir "Escriba cuanto dinero va a invertir: "
		Leer dineroInvertido
	Fin Mientras
	
	Escribir "Escriba la cantidad de meses que el dinero va a estar siendo invertido: "
	Leer cantidadDeMeses
	Mientras cantidadDeMeses < 0 Hacer
		Escribir "Escriba la cantidad de meses que el dinero va a estar siendo invertido: "
		Leer cantidadDeMeses
	Fin Mientras
	
	Escribir "Despues de ", cantidadDeMeses, " mes(es), usted tendra ", dineroInvertido * (porcentajeInteres + 1.0) ^ cantidadDeMeses
FinAlgoritmo