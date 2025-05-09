list_product = []  # Lista global para almacenar los productos

def add_items():
    print("\n--- Añadir Producto ---")
    name = input("Nombre del producto: ").strip().title()
    price = float(input("Precio: $"))
    available = input("¿Disponible? (s/n): ").lower() == "s"
    
    new_product = {
        "nombre": name,
        "precio": price,
        "disponible": available
    }
    
    list_product.append(new_product)
    print(f"✅ {name} añadido correctamente!")

def consult_product():
    print("\n--- Consultar Producto ---")
    search_name = input("Nombre del producto a buscar: ").strip().title()
    
    found = False
    for product in list_product:
        if product["nombre"] == search_name:
            print(f"\nNombre: {product['nombre']}")
            print(f"Precio: ${product['precio']:.2f}")
            print(f"Disponible: {'Sí' if product['disponible'] else 'No'}")
            found = True
            break
    
    if not found:
        print("❌ Producto no encontrado")

def change_price():
    print("\n--- Actualizar Precio ---")
    product_name = input("Nombre del producto: ").strip().title()
    
    for product in list_product:
        if product["nombre"] == product_name:
            new_price = float(input("Nuevo precio: $"))
            product["precio"] = new_price
            print(f"✅ Precio actualizado a ${new_price:.2f}")
            return
    
    print("❌ Producto no encontrado")

def delete_product():
    print("\n--- Eliminar Producto ---")
    product_name = input("Nombre del producto a eliminar: ").strip().title()
    
    for index, product in enumerate(list_product):
        if product["nombre"] == product_name:
            del list_product[index]
            print(f"✅ Producto eliminado")
            return
    
    print("❌ Producto no encontrado")

def calculate_total():
    total = sum(product["precio"] for product in list_product)
    print(f"\n💰 Valor total del inventario: ${total:.2f}")

while True:
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Añadir productos")
    print("2. Consultar productos")
    print("3. Actualizar precios")
    print("4. Eliminar productos")
    print("5. Calcular valor total")
    print("6. Salir")
    
    choice = input("\nElección: ").strip()
    
    if choice == "1":
        add_items()
    elif choice == "2":
        consult_product()
    elif choice == "3":
        change_price()
    elif choice == "4":
        delete_product()
    elif choice == "5":
        calculate_total()
    elif choice == "6":
        print("\n¡Hasta luego! 👋")
        break
    else:
        print("❌ Opción inválida. Intente nuevamente.")
    
    # Opcional: Preguntar si desea continuar después de cada operación
    if choice != "6":
        cont = input("\n¿Desea realizar otra operación? (s/n): ").lower()
        if cont != "s":
            print("\n¡Hasta luego! 👋")
            break