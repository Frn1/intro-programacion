class Empleado:
    def __init__(self, legajo: float, categoria: int, salario: float):
        self.legajo = legajo
        self.categoria = categoria
        self.salario = salario

def desafio():
    cantidad = int(input("Introduzca la cantidad de empleados: "))
    if cantidad <= 0:
        return
    
    empleados: list[Empleado] = []
    
    print()
    for i in range(cantidad):
        legajo = float(input(f"Introduzca la cantidad de años de legajo del empleado {i + 1}: "))
        categoria = int(input(f"Introduzca la categoría del empleado {i + 1}: "))
        salario = float(input(f"Introduzca el salario del empleado {i + 1}: "))
        print()
        empleados.append(Empleado(legajo, categoria, salario))
    
    total_salarios = 0.0
    cantidad_empleados_que_ganan_mas_de_200000 = 0
    cantidad_empleados_que_ganan_menos_de_50000_con_categoria_3 = 0    
    empleado_con_mayor_salario: Empleado = None
    sueldo_mas_bajo: float = None
    total_salario_por_categoria = {
        1: 0.0,
        2: 0.0,
        3: 0.0,
    }
    for empleado in empleados:
        total_salarios += empleado.salario
        if empleado.salario > 200000:
            cantidad_empleados_que_ganan_mas_de_200000 += 1
        if empleado.salario < 50000 and empleado.categoria == 3:
            cantidad_empleados_que_ganan_menos_de_50000_con_categoria_3 += 1
        if empleado_con_mayor_salario == None or empleado.salario > empleado_con_mayor_salario.salario:
            empleado_con_mayor_salario = empleado
        if sueldo_mas_bajo == None or empleado.salario < sueldo_mas_bajo:
            sueldo_mas_bajo = empleado.salario
        total_salario_por_categoria[empleado.categoria] += empleado.salario 
    salario_promedio = total_salarios / len(empleados) 
    
    print("--- Informe ---")
    print(f"Total de salarios: ${total_salarios}")
    print(f"Cantidad de empleados que ganan más de $200000: {cantidad_empleados_que_ganan_mas_de_200000}")
    print(f"Cantidad de empleados que ganan menos de $50000 y son de categoría 3: {cantidad_empleados_que_ganan_menos_de_50000_con_categoria_3}")
    print(f"Legajo del empleado con mayor salario: {empleado_con_mayor_salario.legajo}")
    print(f"Sueldo más bajo: ${sueldo_mas_bajo}")
    print(f"Total de salarios de categoría 1: ${total_salario_por_categoria[1]}")
    print(f"Total de salarios de categoría 2: ${total_salario_por_categoria[2]}")
    print(f"Total de salarios de categoría 3: ${total_salario_por_categoria[3]}")
    print(f"Salario promedio: ${salario_promedio}")
if __name__ == "__main__":
    desafio()