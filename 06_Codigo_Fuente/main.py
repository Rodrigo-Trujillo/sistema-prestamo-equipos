from equipos import registrar_equipo, listar_equipos, eliminar_equipo
from estudiantes import registrar_estudiante, listar_estudiantes
from prestamos import registrar_prestamo, registrar_devolucion, listar_prestamos_activos, listar_historial_prestamos

def menu_principal():
    while True:
        print("\n===== SISTEMA DE PRÉSTAMO DE EQUIPOS TECNOLÓGICOS =====")
        print("1. Registrar equipo")
        print("2. Listar equipos")
        print("3. Registrar estudiante")
        print("4. Listar estudiantes")
        print("5. Registrar préstamo")
        print("6. Registrar devolución")
        print("7. Consultar préstamos activos")
        print("8. Consultar historial de préstamos")
        print("9. Eliminar equipo")
        print("0. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            codigo = input("Código del equipo: ").strip()
            tipo = input("Tipo (Portátil/Videobeam/Tablet/etc): ").strip()
            marca = input("Marca: ").strip()
            modelo = input("Modelo: ").strip()
            registrar_equipo(codigo, tipo, marca, modelo)

        elif opcion == "2":
            listar_equipos()

        elif opcion == "3":
            documento = input("Documento del estudiante: ").strip()
            nombre = input("Nombre completo: ").strip()
            correo = input("Correo: ").strip()
            programa = input("Programa académico: ").strip()
            registrar_estudiante(documento, nombre, correo, programa)

        elif opcion == "4":
            listar_estudiantes()

        elif opcion == "5":
            codigo = input("Código del equipo a prestar: ").strip()
            documento = input("Documento del estudiante: ").strip()
            registrar_prestamo(codigo, documento)

        elif opcion == "6":
            codigo = input("Código del equipo a devolver: ").strip()
            registrar_devolucion(codigo)

        elif opcion == "7":
            listar_prestamos_activos()

        elif opcion == "8":
            listar_historial_prestamos()

        elif opcion == "9":
            codigo = input("Código del equipo a eliminar: ").strip()
            eliminar_equipo(codigo)

        elif opcion == "0":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    menu_principal()