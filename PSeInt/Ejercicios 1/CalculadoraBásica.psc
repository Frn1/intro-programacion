Algoritmo CalculadoraBásica
	Definir n1, n2 Como Real
	Definir selección Como Entero
	
	Escribir "--- Operaciones ---"
	Escribir "  1. Sumar"
	Escribir "  2. Restar"
	Escribir "  3. Multiplicar"
	Escribir "  4. Dividir"
	Escribir "Eliga su operación:"
	Leer selección
	
	Si selección < 1 o selección > 4 Entonces
		Escribir selección, " no es una operación válida"
	SiNo
		Escribir "Escriba su primer número: "
		Leer n1
		Escribir "Escriba su segundo número: "
		Leer n2
		
		Segun selección Hacer
			1: // Suma
				Escribir "Su resultado es ", n1 + n2
			2: // Resta
				Escribir "Su resultado es ", n1 - n2
			3: // Multiplicación
				Escribir "Su resultado es ", n1 * n2
			4: // División
				Si n2 == 0 Entonces
					Escribir "ERROR: No se puede dividir por 0"
				SiNo
					Escribir "Su resultado es ", n1 / n2
				FinSi
			De Otro Modo:
				// No se puede llegar 
		Fin Segun
	FinSi
	
FinAlgoritmo
