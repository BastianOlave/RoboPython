# Codigo main para el control de asistencia de clases
# Bastian Olave Lagos

from os import system
from funciones import *


# func es una instancia de la clase funciones
# que contiene todos los metodos para el control de asistencia
func=funciones()


# Se crea un bucle infinito con el menu
while True:
        try:
            system('cls')
            print("\n\t\t\t\t\t\tControl de Asistencia de Clases")
            opcion=int(input("Ingresa una opción:\n\n"
                     "1) Agregar Curso\n"
                     "2) Agregar Alumno\n"
                     "3) Marcar Asistencia\n"
                     "4) Ver porcentaje de asistencia\n"
                     "5) Salir\n"
                     "-> "))
            if opcion==1:
                func.agregar_curso()
            elif opcion==2:
                func.agregar_alumno()
            elif opcion==3:
                 func.agregar_asistencia()
            elif opcion==4:
                 func.ver_porcentaje_asistencia()
            elif opcion==5:
                input("Saliendo del sistema...")
                break
            else:
                 input("Por favor, ingresa una de las opciones")
        except ValueError:
             input("Por favor, ingrese un numero del 1 al 5.")






