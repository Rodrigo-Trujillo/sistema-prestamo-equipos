from archivos import cargar, guardar, siguiente_id

RUTA_EQUIPOS = "datos/equipos.json"

def registrar_equipo(codigo, tipo, marca, modelo):
    if not codigo or not tipo or not marca or not modelo:
        print("Error: todos los campos son obligatorios.")
        return None

    equipos = cargar(RUTA_EQUIPOS)

    if any(e["codigo"] == codigo for e in equipos):
        print(f"Error: ya existe un equipo con el código {codigo}.")
        return None

    nuevo = {
        "id": siguiente_id(equipos),
        "codigo": codigo,
        "tipo": tipo,
        "marca": marca,
        "modelo": modelo,
        "estado": "disponible"
    }
    equipos.append(nuevo)
    guardar(RUTA_EQUIPOS, equipos)
    print(f"Equipo {codigo} registrado correctamente.")
    return nuevo

def listar_equipos():
    equipos = cargar(RUTA_EQUIPOS)
    if not equipos:
        print("No hay equipos registrados.")
        return
    for e in equipos:
        print(f"[{e['id']}] {e['codigo']} - {e['tipo']} {e['marca']} {e['modelo']} - Estado: {e['estado']}")


def buscar_equipo_por_codigo(codigo):
    equipos = cargar(RUTA_EQUIPOS)
    for e in equipos:
        if e["codigo"] == codigo:
            return e
    return None

def actualizar_estado_equipo(codigo, nuevo_estado):
    equipos = cargar(RUTA_EQUIPOS)
    for e in equipos:
        if e["codigo"] == codigo:
            e["estado"] = nuevo_estado
            guardar(RUTA_EQUIPOS, equipos)
            return True
    return False

def eliminar_equipo(codigo):
    equipos = cargar(RUTA_EQUIPOS)
    equipo = next((e for e in equipos if e["codigo"] == codigo), None)
    if not equipo:
        print("Error: equipo no encontrado.")
        return False
    if equipo["estado"] != "disponible":
        print("Error: no se puede eliminar un equipo que está prestado.")
        return False
    equipos = [e for e in equipos if e["codigo"] != codigo]
    guardar(RUTA_EQUIPOS, equipos)
    print(f"Equipo {codigo} eliminado.")
    return True