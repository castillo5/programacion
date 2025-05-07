#ejercicios de andre de repositorio

#Ejercicios de lógica sin condicionales ni bucles

import os
os.system('clear')

#1. Intercambio de variables
def ejercicio1():
    print("digite dos valores")
    a = int(input())
    b = int(input())
    print("los numeros que me dio fueron")
    print(f"{a} y {b}")
    print("le devuelvo")
    print(f"{b} y {a}")

#2. inverso de número de tres cifras
def ejercicio2():
    print("registra tres numeros")
    num = int(input())
    
    num_unidad = (int(num / 100))
    num_centenas = (num % 10)
    num_decena = int(num / 10)%10

    print(f"su numero normal es {num} y su nuevo numero {num_centenas}{num_decena}{num_unidad}")

# 3. Extraer hora, minuto y segundo de segundos totales
def ejercicio3():
    print("digite un numero en segundo")
    numero_usuario  = int(input())
    horas = numero_usuario * 0.000277778
    minutos = (horas - int(horas))*60
    segundos = (minutos - int(minutos))*60
    print(f"su numero en horas es {numero_usuario} que en horas es: ")
    print(f"en horas es {int(horas)}, minutos es {int(minutos)} y en segundos {int(segundos)}  ")
    
# 4. Fecha formateada
def ejercicio4():
    print("digite su fecha")
    dia = input("Dia: ")
    mes = input("Mes: ")
    año = input("Año: ")
    print(" ")    
    print("formato DD/MM/AAAA")
    print(f"{dia}/{mes}/{año}")
    print("formato AAAA-MM-DD")
    print(f"{año}-{mes}-{dia}")

# 5. Convertir temperatura (F ↔ C)
def ejercicio5():
    print("digite su temperatura en fahrenheit:")
    temp = input()
    print(f"su temperatura en faahrenheit es {temp} y en celsius es {(temp-32)*5/9}")

# 6. Cálculo de propina y cuenta total
def ejercicio6():
    print("digite el costo de su comida: ")
    cost_comida = float(input())
    respuesta = input("desea colocar propina[s/n]")
    while True:
        if respuesta == "s":
            print("cuanto desea dar propina[10/15/20]")
            propina = input()
            if propina == "10":
                print(f"su pago normal es {cost_comida} mas la propina seria {cost_comida * 0.10}")
                print("dando un total de: ", (cost_comida * 0.10)+cost_comida)
                break
            elif propina == "15":
                print(f"su pago normal es {cost_comida} mas la propina seria {cost_comida * 0.15}")
                print("dando un total de: ", (cost_comida * 0.15)+cost_comida)
                break
            elif propina == "20":
                print(f"su pago normal es {cost_comida} mas la propina seria {cost_comida * 0.20}")
                print("dando un total de: ", (cost_comida * .20)+cost_comida)
                break
            else:
                print("su respuesta no entra dentro de las opciones")
                
        
        if respuesta == "n":
            print(f"ok un gusto su pago sera solamente de: {cost_comida}")
            break
    
# 7. Extraer dígitos de un número de 4 cifras 
# revisar
def ejercicio7():
    print("digite un numero de cuatro cifras")
    numero = input()
    for i in numero:
        print(numero, end=",")


# 8. Formato de precio con dos decimales
def ejercicio8():
    print("digite un precio en float")
    num = float(input())
    print(f"su numero en moneda es ${num/100}")

#9. Conversor de minutos a días y horas
def ejercicio9():
    print("digite su numero en horas")
    minu_first = float(input())
    horas = minu_first * 0.016667
    minutos = (horas - minu_first) * 60
    segundos = (minutos - horas) * 60
    print(f"su tiempo en minutos es {minu_first} que se traduce a:")
    print(f"en horas es {horas}")
    print(f"en minutos es {minutos}")
    print(f"en segundos es {segundos}")
















print("1. Intercambio de variables")
print("2. inverso de número de tres cifras")
print("3. Extraer hora, minuto y segundo de segundos totales")
print("4. Fecha formateada")
print("5. Convertir temperatura (F ↔ C)")
print("6. Cálculo de propina y cuenta total")
print("7. Extraer dígitos de un número de 4 cifras")
print("8. Formato de precio con dos decimales")
print("9. Conversor de minutos a días y horas")

opciones = input("digite sus posibilidades: ")

if opciones == "1":
    ejercicio1()
if opciones == "2":
    ejercicio2()
if opciones == "3":
    ejercicio3()
if opciones == "4":
    ejercicio4()
if opciones == "5":
    ejercicio5()
if opciones == "6":
    ejercicio6()
if opciones == "7":
    ejercicio7()
if opciones == "8":
    ejercicio8()
if opciones == "9":
    ejercicio9()
