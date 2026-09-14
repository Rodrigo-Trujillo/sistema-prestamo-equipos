# Product Backlog — Sistema de Préstamo de Equipos Tecnológicos

## HU01 — Registrar equipos tecnológicos
**Como** administrador, **quiero** registrar equipos tecnológicos **para** mantener actualizado el inventario.
**Prioridad:** Alta | **Story Points:** 3

**Criterios de aceptación:**
- El sistema permite registrar un equipo con código, tipo, marca, modelo y estado.
- No permite registrar campos vacíos ni un código de equipo duplicado.
- El equipo queda guardado y disponible para consultarlo después.

## HU02 — Consultar equipos registrados
**Como** administrador, **quiero** consultar los equipos registrados **para** ver su disponibilidad.
**Prioridad:** Alta | **Story Points:** 2

**Criterios de aceptación:**
- El sistema muestra el listado completo de equipos registrados.
- Cada equipo se muestra junto con su estado de disponibilidad (disponible / prestado).
- Si no hay equipos registrados, el sistema informa que el inventario está vacío.

## HU03 — Registrar estudiantes
**Como** administrador, **quiero** registrar estudiantes **para** poder asociarlos a un préstamo.
**Prioridad:** Alta | **Story Points:** 3

**Criterios de aceptación:**
- El sistema permite registrar un estudiante con documento, nombre, correo y programa académico.
- No permite registrar un estudiante con documento duplicado ni con campos vacíos.
- El estudiante queda guardado y disponible para asociarlo a un préstamo.

## HU04 — Registrar préstamo de un equipo a un estudiante
**Como** administrador, **quiero** registrar el préstamo de un equipo **para** llevar control de quién lo tiene.
**Prioridad:** Alta | **Story Points:** 5

**Criterios de aceptación:**
- El sistema valida que el estudiante y el equipo existan antes de registrar el préstamo.
- Solo permite prestar un equipo si su estado es "disponible".
- Al confirmar el préstamo, el estado del equipo cambia automáticamente a "prestado".

## HU05 — Registrar devolución de un equipo
**Como** administrador, **quiero** registrar la devolución de un equipo **para** liberarlo y que quede disponible de nuevo.
**Prioridad:** Alta | **Story Points:** 3

**Criterios de aceptación:**
- El sistema valida que exista un préstamo activo para ese equipo antes de procesar la devolución.
- Al confirmar la devolución, el estado del equipo vuelve automáticamente a "disponible".
- No permite devolver un equipo que no tenga un préstamo activo registrado.

## HU06 — Consultar equipos actualmente prestados
**Como** administrador, **quiero** consultar qué equipos están prestados **para** saber cuáles no están disponibles.
**Prioridad:** Media | **Story Points:** 5

**Criterios de aceptación:**
- El sistema muestra únicamente los equipos cuyo estado sea "prestado".
- Cada resultado muestra a qué estudiante fue prestado.
- Si no hay equipos prestados, el sistema informa que no hay préstamos activos.

## HU07 — Consultar historial de préstamos realizados
**Como** administrador, **quiero** consultar el historial completo de préstamos **para** llevar trazabilidad del uso de los equipos.
**Prioridad:** Media | **Story Points:** 5

**Criterios de aceptación:**
- El sistema muestra todos los préstamos registrados, incluyendo los ya devueltos.
- Cada registro muestra equipo, estudiante y estado (activo / devuelto).
- El historial se mantiene aunque el préstamo ya haya sido devuelto.

## HU08 — Eliminar un equipo del inventario
**Como** administrador, **quiero** eliminar un equipo del inventario **para** dar de baja equipos dañados o fuera de uso.
**Prioridad:** Baja | **Story Points:** 3

**Criterios de aceptación:**
- El sistema permite eliminar un equipo solo si su estado es "disponible" (no si está prestado).
- El sistema pide confirmación antes de eliminar.
- Una vez eliminado, el equipo ya no aparece en el listado ni puede ser prestado.