// Calcula el sueldo de un mes
Algoritmo CalculadoraDeSueldo
	Definir sueldoMensual, porcentajeBonusPorVenta Como Real
	Definir cantidadDeVentas Como Entero
	cantidadDeVentas <- 3
	porcentajeBonusPorVenta <- 10.0 / 100.0
	
	Escribir "Ingrese su sueldo mensual: "
	Leer sueldoMensual
	Mientras sueldoMensual < 0 Hacer
		Escribir "Ingrese su sueldo mensual: "
		Leer sueldoMensual
	Fin Mientras
	
	Definir sueldoBonusPorVentas Como Real
	sueldoBonusPorVentas <- sueldoMensual * porcentajeBonusPorVenta * cantidadDeVentas
	
	Escribir "Bonus por ", cantidadDeVentas, " venta(s): ", sueldoBonusPorVentas
	Escribir "Total este mes: ", sueldoMensual + sueldoBonusPorVentas
FinAlgoritmo