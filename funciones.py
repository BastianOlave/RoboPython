cursos={} #Diccionario para almacenar los cursos

class funciones:

    def agregar_curso(self):
        nombre = input("Ingresa el nombre del curso: ").strip().title()
        if nombre in cursos:
            print("Error!\nEl Curso ya existe!")
        else:
            cursos[nombre]=[]
            print("Curso agregado con exito!")
        input("Presione enter para continuar...")

    def agregar_alumno(self):
        if not cursos:
            print("No existen cursos creados!")
            return
        print("Curso disponible: ")
        for i, curso in enumerate(cursos, 1):
            print(f"{i}){curso}")
        try:
            opcion=int(input("Seleccion el numero del curso donde agregar a alumno: "))
            lista_cursos=list(cursos.keys())
            if opcion<1 or opcion>len(lista_cursos):
                input("Opcion invalida")
                return
            curso_elegido=lista_cursos[opcion-1]
        except ValueError:
            input("Error, debes ingresar un numero!")
            return 
        nombre_alumno=input("Ingresa el nombre del alumno: ").strip().title()
        alumnos=cursos[curso_elegido]
        for alumno in alumnos:
            if alumno["nombre"]==nombre_alumno:
                input("El alumno ya existe en este curso")
                return
        alumnos.append({"nombre": nombre_alumno, "asistencias": []})
        print("Alumno agregado al curso!")
        input("Presione enter para continuar...")

    def agregar_asistencia(self):
        if not cursos:
            input("No existen cursos creados!")
            return
        print("Cursos disponibles: ")
        for i, curso in enumerate(cursos, 1):
            print(f"{i}){curso}")
        try:
            opcion=int(input("Seleccion el numero del curso donde agregar asistencia: "))
            lista_cursos=list(cursos.keys())
            if opcion<1 or opcion>len(lista_cursos):
                input("Opcion invalida")
                return
            curso_elegido=lista_cursos[opcion-1]
        except ValueError:
            input("Error, debes ingresar un numero!")
            return
        alumnos=cursos[curso_elegido]
        if not alumnos:
            input("No hay alumnos en este curso")
            return
        fecha=input("Ingresa la fecha de la asistencia (dd/mm/aaaa): ").strip()
        print("Marcando asistencia oara el curso ", curso_elegido)
        for alumno in alumnos:
            while True:
                estado=input(f"El alumno {alumno['nombre']} asistió? (s/n): ").strip().lower()
                if estado in ["s", "n"]:
                    if estado=="s":
                        alumno["asistencias"].append({"fecha": fecha, "presente": True})
                    else:
                        alumno["asistencias"].append({"fecha": fecha, "presente": False})
                    break
                else:
                    print("Error, ingrese s o n")
        print("Asistencia marcada con exito!")
        input("Presione enter para continuar...")

    def ver_porcentaje_asistencia(self):
        if not cursos:
            input("No hay cursos creados.")
            return
        print("Cursos disponibles:")
        for i, curso in enumerate(cursos, 1):
            print(f"{i}) {curso}")

        try:
            opcion = int(input("Selecciona el número del curso que quieres revisar: "))
            lista_cursos = list(cursos.keys())
            if opcion < 1 or opcion > len(lista_cursos):
                print("Opción inválida.")
                return
            curso_elegido = lista_cursos[opcion - 1]
        except ValueError:
            print("Entrada inválida.")
            return
        alumnos = cursos[curso_elegido]
        if not alumnos:
            print(f"No hay alumnos en el curso '{curso_elegido}'.")
            return
        print(f"\nPorcentaje de asistencia - Curso: {curso_elegido}\n")
        print("{:<20} {:<10} {:<10} {:<10}".format("Alumno", "Asistió", "Total", "%"))
        print("-" * 55)
        for alumno in alumnos:
            asistencias = alumno["asistencias"]
            total = len(asistencias)
            presentes = sum(1 for a in asistencias if a["presente"])
            porcentaje = (presentes / total * 100) if total > 0 else 0
            estado = "!" if porcentaje < 70 else ""
            print("{:<20} {:<10} {:<10} {:<5.1f}% {}".format(alumno['nombre'], presentes, total, porcentaje, estado))
        print("\n! indica asistencia menor al 70%.")
        input("Presione enter para continuar...")

    

        