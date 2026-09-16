# Registro de Impedimentos — Sistema de Préstamo de Equipos Tecnológicos

Este documento registra los impedimentos identificados por el equipo durante el desarrollo del Sprint 1, su causa, y la solución o acción tomada.

## Impedimento 1 — Función de Sprints no habilitada en Jira

**Fecha detectado:** 15 de septiembre de 2026
**Detectado por:** Rodrigo Trujillo (Scrum Master)

**Descripción:** al crear el proyecto en Jira, la función de Sprints no estaba activada por defecto, impidiendo mover las historias del Backlog a un sprint activo e iniciar el seguimiento correspondiente.

**Causa:** ninguno de los integrantes del equipo había usado Jira previamente, por lo que se desconocía que esta función debe habilitarse manualmente desde la configuración del espacio ("Configuración del espacio → Funciones → Sprints").

**Resolución:** se ubicó la sección de configuración correspondiente y se activó la función de Sprints, permitiendo crear el "KAN Sprint 1", mover las 5 historias comprometidas, e iniciar el sprint con fecha y meta definidas.

**Estado:** ✅ Resuelto

---

## Impedimento 2 — Campo nativo de Story Points no disponible

**Fecha detectado:** 15 de septiembre de 2026
**Detectado por:** Rodrigo Trujillo, Sebastián Panche

**Descripción:** al intentar registrar la estimación de cada historia de usuario, no se encontró un campo nativo llamado "Story Points" en la configuración de campos del tipo de actividad "Historia" dentro del espacio del proyecto.

**Causa:** el campo de estimación por story points no viene incluido por defecto en este espacio de Jira, y su configuración como campo personalizado requería pasos adicionales de administración no evidentes para usuarios nuevos en la herramienta.

**Resolución:** como solución alterna, se decidió incluir los story points y la prioridad directamente en el título de cada historia (por ejemplo: "HU01 - Registrar equipos tecnológicos (3 SP - Prioridad Alta)"), manteniendo la información visible y trazable sin depender del campo nativo.

**Estado:** ✅ Resuelto (con solución alterna)

---

## Impedimento 3 — Archivos generados subidos por error al repositorio

**Fecha detectado:** 15 de septiembre de 2026
**Detectado por:** Rodrigo Trujillo

**Descripción:** en un commit inicial de integración (`main.py`), se subieron al repositorio archivos que no debían estar bajo control de versiones: la carpeta `__pycache__` (archivos compilados de Python) y la carpeta `datos/` (archivos JSON generados durante las pruebas locales).

**Causa:** no se configuró un archivo `.gitignore` desde el inicio del repositorio, antes del primer commit que incluyera código ejecutable.

**Resolución:** se creó el archivo `.gitignore` excluyendo `__pycache__/`, `*.pyc` y cualquier carpeta `datos/`, y se removieron del control de versiones los archivos ya subidos con `git rm -r --cached`, sin afectar los archivos en el disco local de cada integrante.

**Estado:** ✅ Resuelto

---

## Resumen

| # | Impedimento | Estado |
|---|---|---|
| 1 | Sprints no habilitados en Jira | ✅ Resuelto |
| 2 | Campo de Story Points no disponible | ✅ Resuelto (solución alterna) |
| 3 | Archivos generados subidos por error | ✅ Resuelto |

Ninguno de los impedimentos identificados bloqueó la entrega del sprint ni afectó el cumplimiento de las historias comprometidas.