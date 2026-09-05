import json

def auditar_entorno_cloud():
    print("[+] Iniciando auditoría de postura de seguridad en la nube (CSPM)...")
    
    # Simulamos la configuración de una infraestructura cloud para auditar
    infraestructura_simulada = {
        "aws_s3_buckets": [
            {"name": "production-data", "public_access": False},
            {"name": "public-assets", "public_access": True},
            {"name": "backup-credentials-2026", "public_access": True} # <- ¡Falla crítica!
        ],
        "security_groups": [
            {"id": "sg-100", "port": 80, "cidr": "0.0.0.0/0", "status": "SAFE"},
            {"id": "sg-200", "port": 22, "cidr": "0.0.0.0/0", "status": "DANGER"} # <- SSH abierto al mundo
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
            
    # 2. Auditar puertos de administración expuestos
    for sg in infraestructura_simulada["security_groups"]:
        if sg["port"] == 22 and sg["cidr"] == "0.0.0.0/0":
            reporte_hallazgos.append({
                "resource": sg["id"],
                "type": "AWS_SECURITY_GROUP",
                "severity": "HIGH",
                "finding": "Puerto de administración SSH (22) abierto globalmente a Internet."
            })
            
    # Mostrar resultados
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
