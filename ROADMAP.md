ROADMAP - ModulosPython

Objetivo: Implementar y verificar todos los ejercicios por módulo siguiendo las directrices de cada "subject" (PDF) en cada módulo. Trabajaré módulo por módulo, ejercicio por ejercicio, documentando la implementación, pruebas y comprobaciones.

Estructura y estado inicial

- Module 00: Parcialmente implementado. Revisar `en.subject` y terminar `ex0`..`ex7`.
- Module 01: Parcialmente implementado. Revisar `en.subject` y terminar `ex0`..`ex6`.
- Module 02..10: Implementaciones añadidas en esta sesión; revisar cada `en.subject` correspondiente para validar cumplimiento.

Nota: Muchos ejercicios ya contienen implementaciones y ejemplos; esta hoja de ruta sirve para asegurar cobertura, linters, tipos y verificación funcional.

Flujo de trabajo por módulo

1. Leer `en.subject*.pdf` del módulo y extraer requisitos, casos borde y comportamiento esperado.
2. Implementar o revisar cada ejercicio `ft_*.py` siguiendo el subject: mantener `print` si el enunciado lo pide, o `return` para funciones destinables a tests.
3. Añadir bloque `if __name__ == "__main__":` con ejemplos reproducibles y comentarios de entrada/salida.
4. Ejecutar con `run_all_mains.py` y corregir errores de importación/ejecución.
5. Ejecutar linters: `flake8` (excluir `.venv`) y `mypy` (`--ignore-missing-imports`) y arreglar avisos críticos.
6. Documentar el ejercicio en su `README.md` breve (propósito, usage, ejemplos) y marcar completado en este ROADMAP.

Checklist de aceptación por ejercicio

- Implementación que satisface el subject.
- Ejemplo en `__main__` que demuestra el comportamiento esperado.
- Pasa lint básico sin errores críticos (E402, E731, F401, F841 corregidos cuando afectan claridad).
- Si aplica, tipos básicos con `mypy` (sin errores importantes) o excepción documentada.


Cómo proceder ahora (pasos inmediatos)

1. Crear/actualizar `.flake8` en la raíz para excluir `.venv` y ajustar `max-line-length = 120`.
2. Auditar y corregir import/ejecución: asegurar que `run_all_mains.py` ejecuta cada `ex*/ft_*.py` con `cwd` y `PYTHONPATH` adecuados.
3. Corregir avisos críticos de `flake8` en los ficheros del proyecto que afectan ejecución o claridad (E402, E731, F401, F841, E501 cuando razonable).
4. Ejecutar `mypy` y documentar excepciones o ajustar tipos mínimos.
5. Inicializar repositorio Git local si el usuario lo confirma, crear rama `fix/runner-imports`, y commitear los cambios.
6. (Opcional) Crear repo remoto en GitHub y `git push` si el usuario otorga acceso/URL.

Estimación y prioridades

- Prioridad alta (inmediata): arreglar import/syntax que impiden ejecución completa del runner.
- Prioridad media: linters y tipos para mejorar mantenibilidad.
- Prioridad baja: estilizado fino y reformatación extensa (se puede delegar a una PR adicional).

Contacto y preferencias

Si quieres que aplique una convención global (por ejemplo, convertir todas las implementaciones a `return` para facilitar tests), indícalo ahora; de lo contrario seguiré el enunciado de cada subject.

Registro de estado

- `run_all_mains.py`: parcheado para ejecutar con `cwd` y `PYTHONPATH` (ver historial de commits locales pendientes).
- Linting: `flake8` y `mypy` ejecutados; quedan avisos documentados en la carpeta raíz (ejecutar `flake8 . --exclude=.venv`).

-- Fin del ROADMAP actualizado --
