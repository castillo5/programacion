
"""
Ejercicio 1: Formatear nombre completo

Descripción:
Crea una función llamada formatear_nombre que reciba tres cadenas de texto: nombre, segundo_nombre y apellido.
La función debe devolver una sola cadena que contenga los tres nombres, cada uno con la primera letra en mayúscula 
y el resto en minúscula, separados por espacios.
Ejemplo:
formatear_nombre("juan", "carlos", "perez") → "Juan Carlos Perez"

Ejercicio 2: Convertir salario de COP a USD

Descripción:
Escribe una función llamada convertir_a_usd que reciba dos parámetros:
    salario_cop (float): el salario en pesos colombianos.
    tasa (float): la tasa de conversión de pesos a dólares.
La función debe devolver el valor del salario convertido a dólares, utilizando la fórmula:
salario_usd = salario_cop / tasa
Ejemplo:
convertir_a_usd(5000000, 4000) → 1250.0

Ejercicio 3: Verificar contraseña segura

Descripción:

Crea una función llamada es_contrasena_segura que reciba un texto (string) como parámetro y devuelva
 True si la contraseña es segura, o False si no lo es.
Una contraseña se considera segura si cumple con lo siguiente:
    Tiene al menos 8 caracteres.
    Contiene al menos una letra mayúscula.
    Contiene al menos un número.
"""
"""
# funcion del ejercicio 1
def format_name(name,last_name,second_name):
    name = name.capitalize()
    last_name = last_name.capitalize()
    second_name = second_name.capitalize()
    return f"{name} {last_name} {second_name}"


name = input("Ingrese su nombre: ") 
last_name = input("Ingrese su apellido: ")
second_name = input("Ingrese su segundo nombre: ")
print(format_name(name,last_name,second_name))

# funcion del ejercicio 2

def convert_to_usd(money_co,conversion_rate):
    return money_co/conversion_rate


money_co = float(input("Ingrese su salario en pesos colombianos: "))
conversion_rate = float(input("Ingrese la tasa de conversion: "))
print(f"Su salario en dolares es: {convert_to_usd(money_co,conversion_rate)}")
"""
import os
os.system('clear')
# funcion del ejercicio 3

def number_variable(pasword):
    for i in range(len(password)):
        print("es para que la variable verifique hacer")
        pasword = int(pasword)
        if pasword == int(pasword):
            number_checkic = True
    return(number_checkic)



while True:
    password = input("introduce una contraseña: ")
    for i in range(len(password)):
        caracter = password[i]
        print(f"Índice: {i}, Carácter: {caracter}")
        if caracter == upper(caracter):
            capitalization_checkic = True
            break
        
    if len(password) > 8:
        if capitalization_checkic == True:
           if number_variable == True:
              print("felicidades tu contraseña es segura")
              break
        else:
            print("no hay un mayuscula, intente denuevo")
    else:
        print("muy pocos caracteres, intente denuevo")
    
