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