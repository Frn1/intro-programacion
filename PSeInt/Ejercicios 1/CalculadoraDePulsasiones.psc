Algoritmo CallculadoraDePulsasiones
	Definir edad Como Real
	Escribir "Escriba su edad:"
	Leer edad
	
	Definir pulsasiones Como Real
	pulsasiones <- redon((220 - edad) / 10)
	Escribir "Por cada 10 segundos de ejercicio, debería tener ", pulsasiones, " pulsasiones"
FinAlgoritmo
