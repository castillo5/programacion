import os
os.system("clear")


#1.Acceso exclusivo al evento


def ejercicio1():
    print("digite su edad y su invitacion para el evento")
    edad = input("edad: ")
    invitacion = input("invitacion: ")
    if edad > 21 and invitacion == "777":
        print("usted puede ingresar al evento")
    else:
        print("usted no puede ingresar al evento ")


#2. Descuento por edad o monto

def ejercicio2():
    print("digite el monto de su moto y edad")
    monto = input("monto: ")
    edad = input("edad: ")
    if monto > 100 and edad > 60:
        print("usted obtiene el descuento de su moto")
    else:
        print("usted no obtiene el descuento")

#3. Verificación para participar en un concurso internacional
def ejercicio3():
    print("digite su edad,pais y numero de documento:")
    edad = int(input("edad: "))
    pais = input("pais: ")
    cc = input("cc: ")
    if edad > 18 and edad < 30:
        if pais != "antartida":
            if cc != "0":
                print("usted cumple con todas las condiciones")
                print("puede ir al concierto")

#4. Evaluación académica de estudiante
def ejercicio4():
    print("por favor digite su notas(dos notas)")
    note1 = int(input())
    note2 = int(input())
    if note1 > 4 and note2 > 4:
        if note1 <= 6 and note2 <= 6:
            print("usted a aprobado felicidades")
        else:
            print("alguna de sus notas no es mayor o igual a 6 por lo tanto desaprobo")
    else:
        print("alguna de sus notas es menor que 4 por lo tanto desaprobo")

#5. Conexión segura en la red
def ejercicio5():
    while True:
        print("por favor digite hppts o http")
        answer01 = input()
        print("digite si el puerto es 80 o 443")
        answer02 = input()
        if answer01 == "http" or answer01 == "https":
            break
        if answer02 == "80" or answer02 == "443":
            break
        print("su respuesta no a sido valida")
    if answer01 == "https" and answer02 == "443":
        print("su conexion es segura")
    else:
        print("su conxecion no es segura")

#6. Requisitos para obtener una beca
def ejercicio6():
    while True:
        print("digite su")
        topics = int(input("materias: "))
        average = int(input("promedio: "))
        income = int(input("ingresos: "))
        if average >= 8 and topics < 3 and income <= 1500:
            print("usted puede aplicar a la beca")
            break
        else:
            print("usted no puede aspirar a la beca")
            break

#7. Acceso a atracción en parque temático
def ejercicio7():
    print("por favor ingrese estos datos")
    age = input("edad: ")
    height = input("estatura: ")
    if height > "140" and age > "10" and age < "60":
        print("usted puede ingresar")
    else:
        print("usted no puede ingresar ")
    
#8. Validación de contraseña segura
def ejercicio8():
    password = input("digite su contraseña: ")
    if len(password) > 8 and password != "123":
        print("ingresaste ")
    else:
        print("no ingresaste")



#9. Evaluación para tarjeta de crédito
#10. Horario permitido para clases

while True:
    print("1.Acceso exclusivo al evento")
    print("2. Descuento por edad o monto")
    print("3. Verificación para participar en un concurso internacional")
    print("4. Evaluación académica de estudiante")
    print("5. Conexión segura en la red")
    print("6. Requisitos para obtener una beca")
    print("7. Acceso a atracción en parque temático")
    print("8. Validación de contraseña segura")
    print("9. Evaluación para tarjeta de crédito")
    print("10. Horario permitido para clases")  
    respuesta = input("digite su eleccion preferida: ")
    if respuesta == "1":
        ejercicio1()
    if respuesta == "2":
        ejercicio2()
    if respuesta == "3":
        ejercicio3()
    if respuesta == "4":
        ejercicio4()
    if respuesta == "5":
        ejercicio5()
    if respuesta == "6":
        ejercicio6()    
    if respuesta == "7":
        ejercicio7()
    if respuesta == "8":
        ejercicio8()
    if respuesta == "9":
        ejercicio9()
    if respuesta == "10":
        ejercicio10()
    answer = input("usted desea continuar[s/n]: ")
    if answer == "n":
        print("hasta luego ")
        break
