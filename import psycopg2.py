import psycopg2

# Datos de conexión (ajústalos según tu configuración)
conn = psycopg2.connect(
    host="localhost",          # Por defecto es 'localhost'
    database="tu_base_de_datos",  # Nombre de la base de datos
    user="postgres",          # Usuario por defecto
    password="tu_contraseña"  # Contraseña que definiste al instalar PostgreSQL
)

# Crear un cursor para ejecutar consultas
cursor = conn.cursor()

# Ejemplo: Crear una tabla
cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id SERIAL PRIMARY KEY,
        nombre VARCHAR(100),
        email VARCHAR(100) UNIQUE
    )
""")

# Guardar cambios
conn.commit()

# Cerrar conexión
cursor.close()
conn.close()