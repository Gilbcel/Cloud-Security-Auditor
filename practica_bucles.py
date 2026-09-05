# ========================================================
# 🛡️ CONTROL DE ACCESOS: LISTAS DINÁMICAS Y BUCLES
# ========================================================

# 1. Creamos una lista VACÍA de usuarios conectados
usuarios_activos = []

# 2. Añadimos elementos DINÁMICAMENTE usando .append()
# Esto simula cuando las personas van iniciando sesión en el sistema
usuarios_activos.append("gilberto_admin")
usuarios_activos.append("user_invitado")
usuarios_activos.append("attacker_99")  # Usuario sospechoso
usuarios_activos.append("maria_dev")

# 3. Definimos nuestra Blacklist de usuarios prohibidos
usuarios_bloqueados = ["attacker_99", "anonymous_user", "root_hack"]

print("========================================")
print("🔐 AUDITORÍA DE SESIONES ACTIVAS")
print("========================================\n")

# 4. El BUCLE 'for': Revisa a cada usuario que añadimos a la lista
for usuario in usuarios_activos:
    
    # 5. Condicional compuesto: ¿El usuario actual está dentro de la lista de bloqueados?
    if usuario in usuarios_bloqueados:
        print(f"❌ ¡ALERTA! Intento de acceso denegado para el usuario: {usuario}")
        print(f"🔒 Acción: Cuenta de [{usuario}] suspendida preventivamente.\n")
    else:
        print(f"✅ Acceso concedido. Usuario verificado: {usuario}")

print("========================================")
print("[+] Auditoría de usuarios finalizada.")



