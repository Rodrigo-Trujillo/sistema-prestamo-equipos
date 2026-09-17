# Sistema de Préstamo de Equipos Tecnológicos

MVP desarrollado en Python aplicando la metodología Scrum, para gestionar el préstamo de equipos tecnológicos a estudiantes de una institución educativa.

## Equipo

- **Rodrigo Trujillo** — Scrum Master / Developer
- **Sebastián Panche** — Product Owner / Developer
- **Dainer Pereira** — Developer

## Estructura del repositorio

- `01_Product_Backlog/` — Historias de usuario y criterios de aceptación
- `02_Sprint_Planning/` — Acta de planeación del sprint
- `03_Tablero/` — Evidencias del tablero de gestión
- `04_Daily_Scrum/` — Registro diario de avance
- `05_Impedimentos/` — Registro de bloqueos del equipo
- `06_Codigo_Fuente/` — Código fuente del sistema
- `07_Pruebas/` — Casos de prueba y resultados
- `08_Sprint_Review/` — Evidencia de la revisión del sprint
- `09_Retrospectiva/` — Acta de retrospectiva
- `10_Videos/` — Videos de sustentación y demo

## Requisitos funcionales

- Registrar equipos tecnológicos
- Consultar equipos registrados
- Registrar estudiantes
- Registrar préstamo de equipo
- Registrar devolución de equipo

## Cómo ejecutar

Requisitos: Python 3.10 o superior. No requiere librerías externas, solo la librería estándar (`json`, `os`, `datetime`).

1. Clona el repositorio:

   ```bash
   git clone https://github.com/Rodrigo-Trujillo/sistema-prestamo-equipos.git
   cd sistema-prestamo-equipos/06_Codigo_Fuente
   ```

2. Ejecuta el programa:

   ```bash
   python main.py
   ```

3. Usa el menú en consola para registrar equipos, estudiantes, préstamos y devoluciones. Los datos se guardan automáticamente en archivos JSON dentro de la carpeta `datos/` (excluida del control de versiones).
