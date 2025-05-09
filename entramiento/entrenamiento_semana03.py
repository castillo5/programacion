list_product = []
import os 
os.system("clear")


def add_items():
    print("esta añadiendo productos digite ")
    available = None
    name = None
    price = None
    
    items = {"name":name, "price":price, "available":available }

    for i in range(1):
        name = input("nombre: ")
        price = input("precio: ")
        available = input("disponibilida: ")
        personal_products = {}
        personal_products["name"] = name
        personal_products["price"] = price
        personal_products["available"] = available
        print(personal_products)
        list_product.append(personal_products)
    print(list_product)
    return(list_product,personal_products)


def consult_product():
    print("\nBuscar producto por nombre")
    search_name = input("Nombre del producto: ").strip().lower()
    
    for product in list_product:
        if product["name"].lower() == search_name:
            print(f"\nProducto encontrado:")
            print(f"Nombre: {product['name']}")
            print(f"Precio: ${product['price']}")
            print("Disponible:  ", product['available'])
            break
        else:
            print("no esta disponible")
            return
        
def change_price(list_product):
    print("digite el nombre del producto que desea actualizar precio")
    name_serch = input()

    for product in list_product:
        if product["name"].lower() == name_serch:
            print("producto encontrado ahora digite por que numero desea cambiar el precio")
            #print(f"precio anterior "){product["price"]} de {product["name"]}
            choice = input()
            product["price"] = choice
        else:
            print("no esta dentro de la lista")
    
  



while True:
    print("menu principal")
    print("que desea realizar:")
    print("1. añadir productos")
    print("2. consultar productos")
    print("3. actualizar precios")
    print("4. eliminar productos")
    print("5. calcular el valor total del inventario")
    choice = input("eleccion: ")
    if choice == "1":
        add_items()
    if choice == "2":
        consult_product()
    if choice == "3":
        change_price()





    answer = input("desea desertar de la operacion? [s/n]")
    if answer == "s":
        break
    
        
    