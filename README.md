# postgreSql

Este proyecto es una API REST construida con **FastAPI** y utiliza **PostgreSQL** como base de datos. La conexión a la base de datos se realiza mediante el paquete [`psycopg`](https://www.psycopg.org/).

## Requisitos

- Python 3.12
- PostgreSQL
- pip

## Instalación

1. **Crea y activa un entorno virtual:**
   ```sh
   python -m venv venv
   source venv/Scripts/activate  # En Windows
   ```

2. **Instala las dependencias:**
   ```sh
   pip install fastapi psycopg-binary uvicorn autopep8
   ```

3. **Configura la base de datos:**
   - Crea una base de datos llamada `Fast_api` en PostgreSQL.
   - Crea la tabla `users`:
     ```sql
     CREATE TABLE users (
         id SERIAL PRIMARY KEY,
         username VARCHAR(100),
         phone VARCHAR(20)
     );
     ```

5. **Configura las credenciales de conexión** en `model/user_connection.py` si es necesario.

## Ejecución

Inicia el servidor de desarrollo con:

```sh
uvicorn main:app --reload
```

La API estará disponible en [http://localhost:8000](http://localhost:8000).

La API para utilizar las funciones esta disponible en [http://localhost:8000/docs](http://localhost:8000/docs).


## Notas

- Asegúrate de tener el intérprete de Python correcto seleccionado en VS Code.
- Si tienes problemas con la instalación de paquetes, revisa la versión de Python y el entorno virtual.

---

**Autor:** [Nicolás Arévalo Fajardo]  
**Fecha:** 09/06/2025.