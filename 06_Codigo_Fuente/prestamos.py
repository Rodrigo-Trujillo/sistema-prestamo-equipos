from datetime import datetime
from archivos import cargar, guardar, siguiente_id
from equipos import buscar_equipo_por_codigo, actualizar_estado_equipo
from estudiantes import buscar_estudiante_por_documento

RUTA_PRESTAMOS = "datos/prestamos.json"

def registrar_prestamo(codigo_equipo, documento_estudiante):
    equipo = buscar_equipo_por_codigo(codigo_equipo)
    if not equipo:
        print("Error: equipo no encontrado.")
        return None
    if equipo["estado"] != "disponible":
        print(f"Error: el equipo {codigo_equipo} no está disponible (estado actual: {equipo['estado']}).")
        return None

    estudiante = buscar_estudiante_por_documento(documento_estudiante)
    if not estudiante:
        print("Error: estudiante no encontrado.")
        return None

    prestamos = cargar(RUTA_PRESTAMOS)
    nuevo = {
        "id": siguiente_id(prestamos),
        "codigo_equipo": codigo_equipo,
        "documento_estudiante": documento_estudiante,
        "fecha_prestamo": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "fecha_devolucion": None,
        "estado": "activo"
    }
    prestamos.append(nuevo)
    guardar(RUTA_PRESTAMOS, prestamos)
    actualizar_estado_equipo(codigo_equipo, "prestado")
    print(f"Préstamo registrado: equipo {codigo_equipo} -> estudiante {documento_estudiante}.")
    return nuevo

def registrar_devolucion(codigo_equipo):
    prestamos = cargar(RUTA_PRESTAMOS)
    prestamo = next((p for p in prestamos if p["codigo_equipo"] == codigo_equipo and p["estado"] == "activo"), None)
    if not prestamo:
        print(f"Error: no hay un préstamo activo para el equipo {codigo_equipo}.")
        return False

    prestamo["estado"] = "devuelto"
    prestamo["fecha_devolucion"] = datetime.now().strftime("%Y-%m-%d %H:%M")
    guardar(RUTA_PRESTAMOS, prestamos)
    actualizar_estado_equipo(codigo_equipo, "disponible")
    print(f"Devolución registrada para el equipo {codigo_equipo}.")
    return True

def listar_prestamos_activos():
    prestamos = cargar(RUTA_PRESTAMOS)
    activos = [p for p in prestamos if p["estado"] == "activo"]
    if not activos:
        print("No hay préstamos activos.")
        return
    for p in activos:
        print(f"Equipo {p['codigo_equipo']} prestado a {p['documento_estudiante']} desde {p['fecha_prestamo']}")

def listar_historial_prestamos():
    prestamos = cargar(RUTA_PRESTAMOS)
    if not prestamos:
        print("No hay préstamos registrados.")
        return
    for p in prestamos:
        print(f"[{p['estado'].upper()}] Equipo {p['codigo_equipo']} - Estudiante {p['documento_estudiante']} - Prestado: {p['fecha_prestamo']} - Devuelto: {p['fecha_devolucion']}")