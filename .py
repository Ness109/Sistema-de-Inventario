inventario = []

# Función para agregar un producto
def agregar_producto():
    nombre = input("Nombre del producto: ")
    cantidad = int(input("Cantidad: "))
    precio = float(input("Precio: "))
    
    producto = {
        "nombre": nombre,
        "cantidad": cantidad,
        "precio": precio
    }
    
    inventario.append(producto)
    print("Producto agregado con éxito.\n")

# Función para ver todo el inventario
def mostrar_inventario():
    if not inventario:
        print("El inventario está vacío.\n")
    else:
        print("\nInventario:")
        for i, producto in enumerate(inventario, start=1):
            print(f"{i}. {producto['nombre']} - {producto['cantidad']} unidades - ${producto['precio']}")
        print()

# Función para buscar un producto
def buscar_producto():
    nombre = input("Nombre del producto a buscar: ")
    encontrado = False
    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            print(f"Encontrado: {producto['nombre']} - {producto['cantidad']} unidades - ${producto['precio']}\n")
            encontrado = True
            break
    if not encontrado:
        print("Producto no encontrado.\n")

# Función para actualizar cantidad o precio de un producto
def actualizar_producto():
    nombre = input("Nombre del producto a actualizar: ")
    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            print(f"Producto encontrado: {producto['nombre']} - {producto['cantidad']} unidades - ${producto['precio']}")
            nueva_cantidad = input("Nueva cantidad (deja en blanco para no cambiar): ")
            nuevo_precio = input("Nuevo precio (deja en blanco para no cambiar): ")

            if nueva_cantidad:
                producto["cantidad"] = int(nueva_cantidad)
            if nuevo_precio:
                producto["precio"] = float(nuevo_precio)
                
            print("Producto actualizado con éxito.\n")
            return
    print("Producto no encontrado.\n")

# Función para eliminar un producto
def eliminar_producto():
    nombre = input("Nombre del producto a eliminar: ")
    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            inventario.remove(producto)
            print("Producto eliminado con éxito.\n")
            return
    print("Producto no encontrado.\n")

# Menú principal
def menu():
    while True:
        print("=== MENÚ DE INVENTARIO ===")
        print("1. Agregar producto")
        print("2. Ver inventario")
        print("3. Buscar producto")
        print("4. Actualizar producto")
        print("5. Eliminar producto")
        print("6. Salir")
        
        opcion = input("Selecciona una opción (1-6): ")
        print()
        
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            mostrar_inventario()
        elif opcion == "3":
            buscar_producto()
        elif opcion == "4":
            actualizar_producto()
        elif opcion == "5":
            eliminar_producto()
        elif opcion == "6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.\n")

# Iniciar el programa
menu()
