# Casos de Prueba — Sistema de Préstamo de Equipos Tecnológicos

Este documento recopila los casos de prueba ejecutados durante el desarrollo de cada módulo, y la prueba de integración final del sistema completo a través de `main.py`.

## Módulo: equipos.py

| # | Descripción | Pasos | Resultado esperado | Resultado obtenido | Estado |
|---|---|---|---|---|---|
| 1 | Registrar equipo válido | Registrar equipo con código, tipo, marca y modelo completos | El equipo se guarda con estado "disponible" | Equipo registrado correctamente | ✅ Pasó |
| 2 | Registrar equipo con código duplicado | Registrar dos veces un equipo con el mismo código | El sistema rechaza el segundo registro | "Error: ya existe un equipo con el código..." | ✅ Pasó |
| 3 | Listar equipos registrados | Consultar el listado con al menos un equipo guardado | Se muestra el equipo con su estado | Equipo mostrado correctamente con estado | ✅ Pasó |
| 4 | Buscar equipo inexistente | Buscar un código que no existe en el sistema | La función devuelve `None`, sin errores | Devolvió `None` sin fallar | ✅ Pasó |
| 5 | Eliminar equipo prestado | Intentar eliminar un equipo cuyo estado es "prestado" | El sistema rechaza la eliminación | "Error: no se puede eliminar un equipo que está prestado" | ✅ Pasó |
| 6 | Eliminar equipo disponible | Eliminar un equipo cuyo estado es "disponible" | El equipo se elimina y ya no aparece en el listado | Equipo eliminado, listado vacío tras la prueba | ✅ Pasó |

## Módulo: estudiantes.py

| # | Descripción | Pasos | Resultado esperado | Resultado obtenido | Estado |
|---|---|---|---|---|---|
| 7 | Registrar estudiante válido | Registrar estudiante con documento, nombre, correo y programa | El estudiante se guarda correctamente | "Estudiante Maria Lopez registrado correctamente" | ✅ Pasó |
| 8 | Registrar estudiante con documento duplicado | Registrar dos veces un estudiante con el mismo documento | El sistema rechaza el segundo registro | "Error: ya existe un estudiante con el documento..." | ✅ Pasó |
| 9 | Buscar estudiante inexistente | Buscar un documento que no existe | La función devuelve `None`, sin errores | Devolvió `None` sin fallar | ✅ Pasó |

## Módulo: prestamos.py

| # | Descripción | Pasos | Resultado esperado | Resultado obtenido | Estado |
|---|---|---|---|---|---|
| 10 | Registrar préstamo válido | Prestar un equipo disponible a un estudiante existente | El préstamo se registra y el equipo pasa a "prestado" | "Préstamo registrado: equipo EQ300 -> estudiante 2005" | ✅ Pasó |
| 11 | Prestar un equipo inexistente | Intentar prestar un código de equipo que no existe | El sistema rechaza la operación | "Error: equipo no encontrado" | ✅ Pasó |
| 12 | Prestar un equipo ya prestado | Intentar prestar un equipo cuyo estado ya es "prestado" | El sistema rechaza la operación | "Error: el equipo no está disponible" | ✅ Pasó |
| 13 | Registrar devolución válida | Devolver un equipo con préstamo activo | El préstamo se marca "devuelto" y el equipo vuelve a "disponible" | "Devolución registrada para el equipo EQ300" | ✅ Pasó |
| 14 | Devolver equipo sin préstamo activo | Intentar devolver un equipo que no tiene préstamo activo | El sistema rechaza la operación | "Error: no hay un préstamo activo para el equipo..." | ✅ Pasó |
| 15 | Consultar historial de préstamos | Consultar el historial tras un ciclo completo de préstamo y devolución | Se muestra el registro con ambas fechas | "[DEVUELTO] Equipo EQ300 - Estudiante 2005 - Prestado: 2026-09-15 19:29 - Devuelto: 2026-09-15 19:29" | ✅ Pasó |

## Prueba de integración — main.py (flujo completo)

Prueba ejecutada de principio a fin sobre el sistema integrado, confirmando que los tres módulos se comunican correctamente a través del menú principal.

| # | Paso del menú | Datos de prueba | Resultado obtenido | Estado |
|---|---|---|---|---|
| 16 | Opción 1 — Registrar equipo | EQ300, Portátil, Asus, Inspiron 15 | Equipo registrado correctamente | ✅ Pasó |
| 17 | Opción 3 — Registrar estudiante | Documento 2005, Maria Lopez, Ingeniería de Software | Estudiante registrado correctamente | ✅ Pasó |
| 18 | Opción 5 — Registrar préstamo | Equipo EQ300, estudiante 2005 | Préstamo registrado: equipo EQ300 -> estudiante 2005 | ✅ Pasó |
| 19 | Opción 6 — Registrar devolución | Equipo EQ300 | Devolución registrada para el equipo EQ300 | ✅ Pasó |
| 20 | Opción 8 — Consultar historial | — | Se muestra el registro completo del ciclo préstamo-devolución | ✅ Pasó |

## Resumen

- **Total de casos ejecutados:** 20
- **Casos exitosos:** 20
- **Casos fallidos:** 0
- **Cobertura:** las 5 historias de usuario comprometidas en el sprint (HU01-HU05) fueron validadas tanto a nivel de módulo individual como en integración completa a través de `main.py`.