# Cloud Security Auditor 🛡️☁️

**Cloud Security Auditor** es una herramienta automatizada de gestión de la postura de seguridad en la nube (CSPM). Está diseñada para escanear y analizar la infraestructura de **Amazon Web Services (AWS)** en busca de vulnerabilidades críticas, configuraciones erróneas y brechas de seguridad que puedan exponer datos sensibles.

## 🚀 Características principales
* **Escaneo de AWS S3 Buckets:** Identifica buckets configurados como públicos que puedan estar exponiendo archivos o credenciales de acceso por error.
* **Auditoría de Firewalls (Security Groups):** Detecta configuraciones de cortafuegos peligrosas, como el puerto de administración SSH (22) abierto globalmente a Internet (`0.0.0.0/0`).
* **Reportes Estructurados:** Genera auditorías detalladas en formato JSON limpio con niveles de severidad (CRITICAL, HIGH, etc.) para una rápida mitigación.

## 🛠️ Requisitos previos
* **Python 3.x** instalado en tu sistema.
* Credenciales de AWS configuradas (en caso de integrarse con el SDK de AWS / `boto3`).

## 🔧 Instalación y Uso

1. Clona este repositorio en tu máquina local:
   ```bash
   git clone git@github.com:Gilbcel/Cloud-Security-Auditor.git
   cd Cloud-Security-Auditor
   ```

2. Ejecuta el auditor de seguridad directamente desde la terminal:
   ```bash
   python3 cloud_auditor.py
   ```

## 📊 Ejemplo de Reporte
Al finalizar el análisis, la herramienta despliega un reporte estructurado en la consola:

```json
================ CLOUD AUDIT REPORT ================
{
    "status": "COMPLETED",
    "total_vulnerabilities": 2,
    "vulnerabilities": [
        {
            "resource": "backup-credentials-2026",
            "type": "AWS_S3_BUCKET",
            "severity": "CRITICAL",
            "finding": "Bucket público expone posibles credenciales de acceso."
        }
    ]
}
====================================================
```

