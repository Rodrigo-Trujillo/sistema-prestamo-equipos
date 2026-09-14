from archivos import cargar, guardar, siguiente_id

RUTA_ESTUDIANTES = "datos/estudiantes.json"

def registrar_estudiante(documento, nombre, correo, programa):
    if not documento or not nombre or not correo or not programa:
        print("Error: todos los campos son obligatorios.")
        return None

    estudiantes = cargar(RUTA_ESTUDIANTES)

    if any(e["documento"] == documento for e in estudiantes):
        print(f"Error: ya existe un estudiante con el documento {documento}.")
        return None

    nuevo = {
        "id": siguiente_id(estudiantes),
        "documento": documento,
        "nombre": nombre,
        "correo": correo,
        "programa": programa
    }
    estudiantes.append(nuevo)
    guardar(RUTA_ESTUDIANTES, estudiantes)
    print(f"Estudiante {nombre} registrado correctamente.")
    return nuevo

def listar_estudiantes():
    estudiantes = cargar(RUTA_ESTUDIANTES)
    if not estudiantes:
        print("No hay estudiantes registrados.")
        return
    for e in estudiantes:
        print(f"[{e['id']}] {e['documento']} - {e['nombre']} - {e['correo']} - {e['programa']}")

def buscar_estudiante_por_documento(documento):
    estudiantes = cargar(RUTA_ESTUDIANTES)
    for e in estudiantes:
        if e["documento"] == documento:
            return e
    return None
