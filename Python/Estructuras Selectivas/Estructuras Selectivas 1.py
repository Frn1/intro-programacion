def ejercicio1():
    precio_por_boleto = float(input("Ingresa el precio por boleto: "))
    cantidad = int(input("Ingresa la cantidad de boletos: "))
    
    if cantidad >= 5:
        print("No se puede realizar esa venta.")
        return
    
    print(f"{cantidad} boleto(s) = ${precio_por_boleto * cantidad}")
    
if __name__ == "__main__":
    ejercicio1()