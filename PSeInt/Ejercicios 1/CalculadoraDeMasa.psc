Algoritmo CalculadoraDeMasa
	Definir presión, volumen, temperatura Como Real
	Definir masa Como Real
	
	Escribir "Introduzca la presión: "
	Leer presión
	Escribir "Introduzca el volumen: "
	Leer volumen
	Escribir "Introduzca la temperatura: " 
	Leer temperatura
	
	masa <- (presión * volumen) / (0.37 * (temperatura + 460))
	Escribir "Masa = ", masa
FinAlgoritmo
