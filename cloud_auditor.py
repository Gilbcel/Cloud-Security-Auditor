import json
import sqlite3  # Cambiado psycopg2 por la librería nativa sqlite3

def guardar_en_sqlite(resource_name, port_number, status):
    """Guarda automáticamente el hallazgo crítico en la base de datos SQLite local."""
    try:
        # Nos conectamos directamente al archivo físico que subiste a tu repositorio
        conexion = sqlite3.connect("servidor_seguridad.db")
        cursor = conexion.cursor()
        
        # Insertamos el hallazgo utilizando parámetros seguros (?) para evitar SQL Injection
        query = """INSERT INTO security_groups (resource_name, port_number, status) 
                   VALUES (?, ?, ?);"""
        cursor.execute(query, (resource_name, port_number, status))
        
        conexion.commit()
        cursor.close()
        conexion.close()
        print(f"💾 [DB] Hallazgo [{resource_name}] registrado en SQLite.")
    except Exception as e:
        print(f"❌ [DB] Error al conectar o guardar en SQLite: {e}")

def auditar_entorno_cloud():
    print("[+] Iniciando auditoría de postura de seguridad en la nube (CSPM)...")
    
    infraestructura_simulada = {
        "aws_s3_buckets": [
            {"name": "production-data", "public_access": False},
            {"name": "public-assets", "public_access": True},
            {"name": "backup-credentials-2026", "public_access": True} 
        ],
        "security_groups": [
            {"id": "sg-100", "port": 80, "cidr": "0.0.0.0/0", "status": "SAFE"},
            {"id": "sg-200", "port": 22, "cidr": "0.0.0.0/0", "status": "DANGER"} 
        ]
    }
    
    reporte_hallazgos = []
    
    # 1. Auditar almacenamiento expuesto
    for bucket in infraestructura_simulada["aws_s3_buckets"]:
        if bucket["public_access"] and "credential" in bucket["name"]:
            reporte_hallazgos.append({
                "resource": bucket["name"],
                "type": "AWS_S3_BUCKET",
                "severity": "CRITICAL",
                "finding": "Bucket público expone posibles credenciales de acceso."
            })
            # ENLACE DB: Cambiado para usar la función adaptada a SQLite
            guardar_en_sqlite(bucket["name"], 443, "VULNERABLE")
            
    # 2. Auditar puertos de administración expuestos
    for sg in infraestructura_simulada["security_groups"]:
        if sg["port"] == 22 and sg["cidr"] == "0.0.0.0/0":
            reporte_hallazgos.append({
                "resource": sg["id"],
                "type": "AWS_SECURITY_GROUP",
                "severity": "HIGH",
                "finding": "Puerto de administración SSH (22) abierto globalmente a Internet."
            })
            # ENLACE DB: Cambiado para usar la función adaptada a SQLite
            guardar_en_sqlite(sg["id"], sg["port"], "VULNERABLE")
            
    generar_reporte(reporte_hallazgos)

def generar_reporte(hallazgos):
    payload_auditoria = {
        "status": "COMPLETED",
        "total_vulnerabilities": len(hallazgos),
        "vulnerabilities": hallazgos
    }
    print("\n================ CLOUD AUDIT REPORT ================")
    print(json.dumps(payload_auditoria, indent=4))
    print("====================================================\n")
    print("[+] Auditoría finalizada. Reporte generado de forma exitosa.")

if __name__ == "__main__":
    auditar_entorno_cloud()

            
