# Acta de Sprint Planning

**Sprint:** 1 (única iteración, duración 1 semana)
**Fecha:** [completar con la fecha real de la reunión]
**Asistentes:** Rodrigo Trujillo, Sebastián Panche, Dainer Pereira

## Sprint Goal

Entregar un MVP funcional que permita registrar equipos y estudiantes, y gestionar el ciclo completo de préstamo y devolución, validando correctamente la disponibilidad de los equipos.

## Historias comprometidas en el Sprint

| Historia | Story Points | Compromiso |
|---|---|---|
| HU01 — Registrar equipos | 3 | Comprometida |
| HU02 — Consultar equipos | 2 | Comprometida |
| HU03 — Registrar estudiantes | 3 | Comprometida |
| HU04 — Registrar préstamo | 5 | Comprometida |
| HU05 — Registrar devolución | 3 | Comprometida |
| HU06 — Consultar prestados | 5 | Meta extra (si alcanza el tiempo) |
| HU07 — Historial de préstamos | 5 | Meta extra (si alcanza el tiempo) |
| HU08 — Eliminar equipo | 3 | Fuera de este sprint |

**Total comprometido:** 16 puntos (de 29 posibles)

## Sprint Backlog — tareas técnicas y responsables

| Historia | Tarea técnica | Responsable |
|---|---|---|
| HU01, HU02 | Módulo `equipos.py`: registrar y listar equipos + persistencia JSON | Rodrigo |
| HU03 | Módulo `estudiantes.py`: registrar estudiantes + validaciones | Sebastián |
| HU04, HU05 | Módulo `prestamos.py`: registrar préstamo y devolución, validar disponibilidad | Dainer |
| Todas | `main.py`: menú principal que conecta todos los módulos | Rodrigo |
| Todas | Pruebas de cada módulo antes de integrar | Cada uno prueba su propio módulo |