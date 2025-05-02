
"""
El programa que vas a desarrollar en este entrenamiento debe:
Determinar el estado de aprobación:
Solicitar al usuario ingresar una calificación numérica (de 0 a 100)
Evaluar si el estudiante ha aprobado o reprobado basándose en la calificación ingresada
Calcular el promedio:
Permitir al usuario ingresar una lista de calificaciones (separadas por comas)
Calcular y mostrar el promedio de las calificaciones en la lista
Contar calificaciones mayores:
Preguntar al usuario por un valor específico
Contar cuántas calificaciones en la lista son mayores que este valor
Verificar y contar calificaciones específicas
Preguntar al usuario por una calificación específica. 
Verificar si esta calificación está en la lista y contar cuántas veces aparece, utilizando
break y continue para controlar el flujo del programa.
"""

import os
os.system('clear')

def check_approval_status():
    """Determina si un estudiante aprueba basado en una calificación"""
    while True:
        try:
            grade = float(input("Ingrese una calificación numérica (0-100): "))
            if 0 <= grade <= 100:
                print("El estudiante ha APROBADO." if grade >= 60 else "El estudiante ha REPROBADO.")
                return grade
            print("¡Por favor ingrese un valor entre 0 y 100!")
        except ValueError:
            print("Entrada inválida. Debe ser un número.")

def get_grades():
    """Obtiene y valida una lista de calificaciones"""
    while True:
        try:
            input_str = input("Ingrese calificaciones separadas por comas: ")
            grades = [float(g.strip()) for g in input_str.split(',')]
            
            if all(0 <= g <= 100 for g in grades):
                return grades
            print("¡Todas las calificaciones deben estar entre 0 y 100!")
        except ValueError:
            print("Entrada inválida. Use números separados por comas.")

def count_above_value(grades):
    """Cuenta calificaciones mayores a un valor específico"""
    while True:
        try:
            threshold = float(input("Ingrese valor para comparar (0-100): "))
            if 0 <= threshold <= 100:
                above_count = sum(1 for g in grades if g > threshold)
                print(f"Calificaciones mayores que {threshold}: {above_count}")
                return
            print("¡El valor debe estar entre 0 y 100!")
        except ValueError:
            print("Entrada inválida. Ingrese un número.")

def check_specific_grade(grades):
    """Verifica y cuenta ocurrencias de una calificación específica"""
    while True:
        try:
            target = float(input("Ingrese calificación a buscar (0-100): "))
            if 0 <= target <= 100:
                count = 0
                found = False
                
                for grade in grades:
                    if grade == target:
                        count += 1
                        found = True
                        continue  # Salta a la siguiente iteración
                    # Se podría agregar más lógica aquí si fuera necesario
                
                print(f"La calificación {target} aparece {count} veces." if found 
                      else f"La calificación {target} no existe en los registros.")
                return
            print("¡La calificación debe estar entre 0 y 100!")
        except ValueError:
            print("Entrada inválida. Ingrese un número.")

def main():
    print("\n=== Sistema de Gestión de Calificaciones ===")
    #  Verificación de aprobación
    print("\n1. Verificación de estado individual")
    check_approval_status()
    #  Procesamiento de lista
    print("\n2. Procesamiento de calificaciones")
    grades = get_grades()
    average = sum(grades) / len(grades)
    print(f"Promedio calculado: {average:.2f}")
    #  Conteo comparativo
    print("\n3. Comparación contra valor de referencia")
    count_above_value(grades)
    #  Búsqueda específica
    print("\n4. Búsqueda de calificación específica")
    check_specific_grade(grades)
    # Estadísticas adicionales
    print("\nResumen estadístico:")
    print(f"Calificación más alta: {max(grades)}")
    print(f"Calificación más baja: {min(grades)}")
    print(f"Total de calificaciones: {len(grades)}")

if __name__ == "__main__":
    main()