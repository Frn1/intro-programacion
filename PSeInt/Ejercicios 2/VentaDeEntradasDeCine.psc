Algoritmo VentaDeEntradasDeCine
	Definir cantDeAsientos Como Entero
	cantDeAsientos <- 10
	Dimensionar asientos[cantDeAsientos]
	
	Definir correr Como Logico
	correr <- Verdadero
	
	Definir entrada Como Entero
	Mientras correr Hacer
		Escribir ""
		Escribir "--- Menú ---"
		Escribir " 1: Ver asientos"
		Escribir " 2: Vender entrada"
		Escribir " 3: Salir"
		Escribir "Su seleccion " Sin Saltar
		Leer entrada
		
		Segun entrada Hacer
			1:
				Para i <- 1 Hasta cantDeAsientos Hacer
					Escribir "Asiento ", i, " está " Sin Saltar
					Si asientos[i] == 0 Entonces
						Escribir "libre"
					SiNo
						Escribir "ocupado"
					FinSi
				FinPara
			2:
				Escribir "Elija el asiento que va a vender " Sin Saltar
				Leer entrada
				
				Si entrada > 0 Y entrada <= cantDeAsientos Entonces
					Si asientos[entrada] == 0 Entonces
						asientos[entrada] = 1
						Escribir "Asiento ", entrada, " vendido correctamente."
					SiNo
						Escribir "Asiento ", entrada, " ya está ocupado."
					FinSi
				SiNo
					Escribir "Ese asiento no existe."
				FinSi
			3:
				correr <- Falso
				Escribir "Adios! :3"
			De Otro Modo:
				Escribir "No reconozco esa opcion."
		Fin Segun
	Fin Mientras
	
FinAlgoritmo
