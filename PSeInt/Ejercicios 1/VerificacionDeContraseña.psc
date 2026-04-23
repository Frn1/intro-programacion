Algoritmo VerificaciónDeContraseña
	Definir contraseña Como Caracter
	contraseña <- "1234"
	
	Definir contraseñaIngresada Como Caracter
	Escribir "Ingrese la contraseña: "
	Leer contraseñaIngresada
	Mientras contraseñaIngresada <> contraseña Hacer
		Escribir "Contraseña incorrecta. Vuelva a intentar: "
		Leer contraseñaIngresada
	FinMientras
	
	Escribir "Contraseña verificada. Acceso concedido."
FinAlgoritmo
