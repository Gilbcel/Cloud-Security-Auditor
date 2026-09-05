import sqlite3

# 1. Nos conectamos a la base de datos (si el archivo no existe, lo crea solo)
conexion = sqlite3.connect("servidor_seguridad.db")
cursor = conexion.cursor()

# 2. Comando SQL: Crear una tabla de registros de accesos (Logs)
# Especificamos las columnas: ID, usuario, dirección IP, y si el acceso fue exitoso
cursor.execute("""
CREATE TABLE IF NOT EXISTS logs_acceso (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario TEXT,
    ip TEXT,
    exitoso INTEGER
)
""")

# 3. Comando SQL: Insertar datos de prueba en la tabla
# (Borramos datos previos para no duplicar en cada prueba)
cursor.execute("DELETE FROM logs_acceso")

cursor.execute("INSERT INTO logs_acceso (usuario, ip, exitoso) VALUES ('gilberto_admin', '192.168.1.5', 1)")
cursor.execute("INSERT INTO logs_acceso (usuario, ip, exitoso) VALUES ('user_invitado', '10.0.0.15', 1)")
cursor.execute("INSERT INTO logs_acceso (usuario, ip, exitoso) VALUES ('root_hack', '185.40.3.12', 0)")
cursor.execute("INSERT INTO logs_acceso (usuario, ip, exitoso) VALUES ('root_hack', '185.40.3.12', 0)")
cursor.execute("INSERT INTO logs_acceso (usuario, ip, exitoso) VALUES ('maria_dev', '192.168.1.20', 1)")

# Guardamos los datos insertados
conexion.commit()

print("========================================")
print("🛡️  CONSULTA SQL: DETECTANDO INTRUSOS")
print("========================================\n")

# 4. Tu primera consulta SQL avanzada: Buscaremos accesos fallidos (exitoso = 0)
# El comando SELECT extrae información específica usando filtros (WHERE)
query_sql = "SELECT usuario, ip FROM logs_acceso WHERE exitoso = 0"
cursor.execute(query_sql)

# Recuperamos las filas encontradas
alertas = cursor.fetchall()

# Mostramos los resultados
for alerta in alertas:
    print(f"⚠️  ALERTA: Intento de inicio de sesión FALLIDO detectado!")
    print(f"   👤 Usuario atacante: {alerta[0]}")
    print(f"   🌐 Dirección IP origen: {alerta[1]}\n")

# Cerramos la conexión de forma limpia
conexion.close()

