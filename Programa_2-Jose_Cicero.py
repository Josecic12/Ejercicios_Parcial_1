def crear_arreglos(tamano):
    productos = []
    precios = []
    
    for i in range(tamano):
        producto = input(f"Ingrese el nombre del producto {i+1}: ")
        precio = float(input(f"Ingrese el precio del producto {producto}: "))
        productos.append(producto)
        precios.append(precio)
    
    return productos, precios

def mostrar_productos_y_precios(productos, precios):
    print("\nLista de productos y sus precios:")
    for i in range(len(productos)):
        print(f"Producto: {productos[i]}, Precio: ${precios[i]:.2f}")

def main():
    tamano = int(input("Ingrese el número de productos: "))
    
    productos, precios = crear_arreglos(tamano)
    
    mostrar_productos_y_precios(productos, precios)

if __name__ == "__main__":
    main()
