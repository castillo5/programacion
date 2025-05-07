import os
os.system("clear")

#1. Nombre y edad
def ejercicio1():
    print("digite su nombre luego enter y luego su edad")
    nombre = input()
    edad = input()
    print(f"su nombre es: {nombre} y su edad es: {edad}")

#2. Suma de dos números enteros
def ejercicio2():
    print("digite un numero presione enter luego digite otro")
    num1 = int(input())
    num2 = int(input())
    print(f"sus numeros son {num1} y {num2} su resultado es {num1 + num2}")

#3. Multiplicación de decimales
def ejercicio3():
    print("digite un numero decimales presione enter luego digite otro")
    num1 = float(input())
    num2 = float(input())
    print(f"sus numeros son {num1} y {num2} su resultado es {num1 * num2}")

#4. Doble y triple
def ejercicio4():
    print("digite un numero")
    num = int(input())
    print(f"su numero es {num}, el doble de ese numero es {num * 2} y  el triple {num * 3}")

#5. Repetir palabra
def ejercicio5():
    print("digite un palabra luego presione enter y digite un numero de veces que quiere que se repita")
    palabra = input()
    repeticion = int(input())
    print(f"la repeticion de su palabra es: {palabra * repeticion}")


#6. División
def ejercicio6():
    print("digite dos numeros")
    num1 = float(input())
    num2 = float(input())
    print(f"la division del primero por el segundo es: {num1 / num2}")

#7. Letras del nombre
def ejercicio7():
    print("digite su nombre")
    nombre = input()
    print(f"la cantidad de letras de su nombre es {len(nombre)}")

#8. División entera y módulo
def ejercicio8():
    print("digite un numero presione enter y luego digite otro numero")
    num1 = float(input())
    num2 = float(input())
    print(f"la division entera de los numero es  {num1 // num2} y su residuo {num1 % num2}")

#9. Todas las operaciones
def ejercicio9():
    print("digite dos numeros")
    num1 = int(input())
    num2 = int(input())
    print(f"la suma de sus numeros {num1 + num2}")
    print(f"la resta de sus numeros {num1 - num2}")
    print(f"la multiplicacion de sus numeros {num1 * num2}")
    print(f"la division de sus numeros {num1 / num2}")

#10. Potencias con f-strings
def ejercicio10():
    print("digite un numero")
    num = int(input())
    print(f"su numero es {num}, el doble de ese numero es {num * 2} y  el triple {num * 3}")

#11. Parte entera de un decimal
def ejercicio11():
    print("digite un numero decimal")
    num = float(input())
    print(f"su numero sin decimal es {int(num)}")

#12. Mayor de edad (sin condicional)
def ejercicio12():
    print("digite su edad")
    edad = int(input())
    comprobante = edad > 18 
    print("su edad llega la mayoria de edad: ", comprobante)

#13. ¿Son iguales?
def ejercicio13():
    print("digite dos numero separados por un enter entre cada uno")
    num1 = int(input())
    num2 = int(input())
    if num1 == num2:
        print("son iguales")
    else:
        print("sus dos numeros no son iguales")

#14. ¿Mayor que?
def ejercicio14():
    print("digite dos numero separados por un enter entre cada uno")
    num1 = int(input())
    num2 = int(input())
    if num1 > num2:
        print("el primero es mayor al segundo numero")

#15. ¿Menor o igual?
def ejercicio14():
    print("digite dos numero separados por un enter entre cada uno")
    num1 = int(input())
    num2 = int(input())
    if num1 <= num2:
        print("el primero es menor o igual al segundo numero")

#16. Ambos mayores que 10
def ejercicio16():
    print("digite dos numero separados por un enter entre cada uno")
    num1 = int(input())
    num2 = int(input())
    if num1 > 10 and num2 > 10:
        print("ambos numeros son mayores a 10")
    

#17. Al menos uno mayor que 10
def ejercicio17():
    print("digite dos numero separados por un enter entre cada uno")
    num1 = int(input())
    num2 = int(input())
    if num1 > 10 or num2 > 10:
        print("almenos uno de los  numeros son mayores a 10")

#18. No son iguales
def ejercicio18():
    print("digite dos numero separados por un enter entre cada uno")
    num1 = int(input())
    num2 = int(input())
    aprobacion = not(not(num1 == num2))
    print(f"su numeros son iguales? {aprobacion}")

#19. Promedio
def ejercicio19():
    print("digite tres numeros")
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    print(f"el promedio de sus tres notas es {(num1+num2+num3)/3}")

#20. Divisible por 5
def ejercicio20():
    print("digite  numero ")
    num1 = int(input())
    if num1 % 5 == 0:
        print("su numero es divisible por 5") 
    else:
        print("su numero no es divisible")

print("1. Nombre y edad")
print("2. Suma de dos números enteros")
print("3. Multiplicación de decimales")
print("4. Doble y triple")
print("5. Repetir palabra")
print("6. División")
print("7. Letras del nombre")
print("8. División entera y módulo")
print("9. Todas las operaciones")
print("10. Potencias con f-strings")
print("11. Parte entera de un decimal")
print("12. Mayor de edad (sin condicional)")
print("13. ¿Son iguales?")
print("14. ¿Mayor que?")
print("15. ¿Menor o igual?")
print("16. Ambos mayores que 10")
print("17. Al menos uno mayor que 10")
print("18. No son iguales")
print("19. Promedio")
print("20. Divisible por 5")

eleccion = input("cual ejercicio desea ejecutar? ")
if eleccion == "1":
    ejercicio1()
if eleccion == "2":
    ejercicio2()
if eleccion == "3":
    ejercicio3()
if eleccion == "4":
    ejercicio4()
if eleccion == "5":
    ejercicio5()
if eleccion == "6":
    ejercicio6()
if eleccion == "7":
    ejercicio7()
if eleccion == "8":
    ejercicio8()
if eleccion == "9":
    ejercicio9()
if eleccion == "10":
    ejercicio10()
if eleccion == "11":
    ejercicio11()
if eleccion == "12":
    ejercicio12()
if eleccion == "13":
    ejercicio13()
if eleccion == "14":
    ejercicio14()
if eleccion == "15":
    ejercicio15()
if eleccion == "16":
    ejercicio16()
if eleccion == "17":
    ejercicio17()
if eleccion == "18":
    ejercicio18()
if eleccion == "19":
    ejercicio19()
if eleccion == "20":
    ejercicio20()

