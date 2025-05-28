# Codigo actualizado para el control de asistencia
# Autor: Bastian Olave Lagos

# Diccionario para almacenar los cursos con clases estipuladas y alumnos
cursos = {}

class funciones:

    def agregar_curso(self):
        while True:
            try:
                nombre = input("Ingresa el nombre del curso: ").strip().title()
                if nombre in cursos:
                    print("Error!\nEl Curso ya existe!")
                elif nombre == "":
                    print("Error!\nEl nombre del curso no puede estar vacio!")
                else:
                    while True:
                        try:
                            clases_totales = int(input("Ingresa la cantidad total de clases estipuladas para este curso: "))
                            if clases_totales <= 0:
                                print("Debe ser un número positivo!")
                            else:
                                break
                        except ValueError:
                            print("Error, debes ingresar un número válido!")

                    cursos[nombre] = {
                        "clases_totales": clases_totales,
                        "alumnos": []
                    }
                    print("Curso agregado con éxito!")
                    input("Presione enter para continuar...")
                    break
            except ValueError:
                input("Error, debes ingresar un nombre válido!")
                continue

    def agregar_alumno(self):
        while True:
            if not cursos:
                print("No existen cursos creados!")
                return
            print("Cursos disponibles:")
            for i, curso in enumerate(cursos, 1):
                print(f"{i}) {curso}")
            while True:
                try:
                    opcion = int(input("Selecciona el número del curso donde agregar al alumno: "))
                    lista_cursos = list(cursos.keys())
                    if opcion < 1 or opcion > len(lista_cursos):
                        print("Opción inválida")
                    else:
                        curso_elegido = lista_cursos[opcion - 1]
                        break
                except ValueError:
                    print("Error, debes ingresar un número!")
                    continue

            alumnos = cursos[curso_elegido]["alumnos"]
            while True:
                nombre_alumno = input("Ingresa el nombre del alumno: ").strip().title()
                if not nombre_alumno:
                    print("El nombre no puede estar vacío.")
                    continue

                if any(alumno["nombre"] == nombre_alumno for alumno in alumnos):
                    print("El alumno ya existe en este curso.")
                else:
                    alumnos.append({"nombre": nombre_alumno, "asistencias": []})
                    print("¡Alumno agregado al curso!")
                    break
            print("Deseas agregar otro alumno al curso? (s/n): ")
            respuesta = input().strip().lower()
            if respuesta != 's':
                break


    def agregar_asistencia(self):
        while True:
            if not cursos:
                input("No existen cursos creados!")
                return

            print("Cursos disponibles:")
            for i, curso in enumerate(cursos, 1):
                print(f"{i}) {curso}")

            while True:
                try:
                    opcion = int(input("Selecciona el número del curso donde agregar asistencia: "))
                    lista_cursos = list(cursos.keys())
                    if opcion < 1 or opcion > len(lista_cursos):
                        print("Opción inválida")
                    else:
                        curso_elegido = lista_cursos[opcion - 1]
                        break
                except ValueError:
                    print("Error, debes ingresar un número!")

            alumnos = cursos[curso_elegido]["alumnos"]
            if not alumnos:
                input("No hay alumnos en este curso")
                return

            fecha = input("Ingresa la fecha de la asistencia (dd/mm/aaaa): ").strip()
            print("Marcando asistencia para el curso", curso_elegido)
            for alumno in alumnos:
                while True:
                    estado = input(f"¿El alumno {alumno['nombre']} asistió? (s/n): ").strip().lower()
                    if estado in ["s", "n"]:
                        alumno["asistencias"].append({"fecha": fecha, "presente": estado == "s"})
                        break
                    else:
                        print("Error, ingrese 's' o 'n'")

            print("Asistencia marcada con éxito!")
            print("¿Deseas agregar asistencia a otro curso? (s/n): ")
            respuesta = input().strip().lower()
            if respuesta != 's':
                break

    def ver_porcentaje_asistencia(self):
        while True:
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

            data_curso = cursos[curso_elegido]
            alumnos = data_curso["alumnos"]
            clases_totales = data_curso["clases_totales"]

            if not alumnos:
                print(f"No hay alumnos en el curso '{curso_elegido}'.")
                return

            print(f"\nPorcentaje de asistencia - Curso: {curso_elegido} (Clases estipuladas: {clases_totales})\n")
            print("{:<20} {:<10} {:<10} {:<10}".format("Alumno", "Asistió", "Total", "%"))
            print("-" * 55)

            for alumno in alumnos:
                asistencias = alumno["asistencias"]
                total = len(asistencias)
                presentes = sum(1 for a in asistencias if a["presente"])
                porcentaje = (presentes / clases_totales * 100) if clases_totales > 0 else 0
                estado = "!" if porcentaje < 70 else ""
                print("{:<20} {:<10} {:<10} {:<5.1f}% {}".format(
                    alumno["nombre"], presentes, clases_totales, porcentaje, estado
                ))

            print("\n! indica asistencia menor al 70% respecto a las clases estipuladas.")
            print("¿Deseas ver el porcentaje de asistencia de otro curso? (s/n): ")
            respuesta = input().strip().lower()
            if respuesta != 's':
                break

