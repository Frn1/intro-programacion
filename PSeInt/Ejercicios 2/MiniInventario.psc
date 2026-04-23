Algoritmo MiniInventario
	Definir cantDeProductos Como Entero
	cantDeProductos <- 5
	Dimensionar codigosProducto[cantDeProductos], nombresProductos[cantDeProductos], cantidadesStockProducto[cantDeProductos]
	
	codigosProducto[1] <- "A125FD"
	nombresProductos[1] <- "Producto 1"
	cantidadesStockProducto[1] <- 23
	
	codigosProducto[2] <- "JE534F1"
	nombresProductos[2] <- "Producto 2"
	cantidadesStockProducto[2] <- 5
	
	codigosProducto[3] <- "PW635JF"
	nombresProductos[3] <- "Producto 3"
	cantidadesStockProducto[3] <- 0
	
	codigosProducto[4] <- "163BSD2"
	nombresProductos[4] <- "Producto 4"
	cantidadesStockProducto[4] <- 11
	
	codigosProducto[5] <- "DFUTAD2"
	nombresProductos[5] <- "Producto 5"
	cantidadesStockProducto[5] <- 2
	
	Definir correr Como Logico
	correr <- Verdadero
	
	Definir enteroIngresado Como Entero
	Definir textoIngresado Como Caracter
	Definir indiceProducto Como Entero
	Mientras correr Hacer
		Escribir ""
		Escribir "--- Menú ---"
		Escribir " 1: Mostrar inventario"
		Escribir " 2: Vender producto"
		Escribir " 3: Reponer producto"
		Escribir " 4: Salir"
		Escribir "Su selección " Sin Saltar
		Leer enteroIngresado
		
		Segun enteroIngresado Hacer
			1:
				Escribir "Este es el inventario actual:"
				Para i <- 1 Hasta cantDeProductos Hacer
					Escribir "Código: ", codigosProducto[i] Sin Saltar
					Escribir ", " Sin Saltar
					Escribir "Nombre: ", nombresProductos[i] Sin Saltar
					Escribir ", " Sin Saltar
					Escribir "Cantidad en stock: ", cantidadesStockProducto[i] Sin Saltar
					Escribir "."
				FinPara
			2:
				Escribir "Escriba el código del producto a vender " Sin Saltar
				Leer textoIngresado
				// Escribo -1 al indiceProducto ya que va a ser utilizado para
				// guardar el índice del producto en las listas. Si sigue siendo
				// -1 cuando el bucle de abajo termina, entonces no se encontró
				// el producto.
				indiceProducto <- -1
				// Buscamos el índice en la lista del código de producto ingresado
				// y lo guardamos en indiceProducto
				Para i <- 1 Hasta cantDeProductos Hacer
					Si textoIngresado == codigosProducto[i] Entonces
						indiceProducto <- i
					FinSi
				FinPara
				Si indiceProducto == -1 Entonces
					Escribir "No se encontró ese código de producto."
				SiNo
					Si cantidadesStockProducto[indiceProducto] <= 0 Entonces
						Escribir "No hay stock para ", nombresProductos[indiceProducto], "."
					SiNo
						cantidadesStockProducto[indiceProducto] <- cantidadesStockProducto[indiceProducto] - 1
						Escribir nombresProductos[indiceProducto], " vendido correctamente."
					FinSi
				FinSi
			3:
				Escribir "Escriba el código del producto a reponer " Sin Saltar
				Leer textoIngresado
				// Escribo -1 al indiceProducto ya que va a ser utilizado para
				// guardar el índice del producto en las listas. Si sigue siendo
				// -1 cuando el bucle de abajo termina, entonces no se encontró
				// el producto.
				indiceProducto <- -1
				// Buscamos el índice en la lista del código de producto ingresado
				// y lo guardamos en indiceProducto
				Para i <- 1 Hasta cantDeProductos Hacer
					Si textoIngresado == codigosProducto[i] Entonces
						indiceProducto <- i
					FinSi
				FinPara
				Si indiceProducto == -1 Entonces
					Escribir "No se encontró ese código de producto."
				SiNo
					Escribir "¿Cuanto desea reponer de ", nombresProductos[indiceProducto], "? " Sin Saltar
					Leer enteroIngresado
					cantidadesStockProducto[indiceProducto] <- cantidadesStockProducto[indiceProducto] + enteroIngresado
					Escribir nombresProductos[indiceProducto], " repuesto correctamente correctamente. Ahora hay: ", cantidadesStockProducto[indiceProducto], "."
				FinSi
			4:
				correr <- Falso
				Escribir "Adios! :3"
			De Otro Modo:
				Escribir "No reconozco esa opcion."
		Fin Segun
	FinMientras
FinAlgoritmo
