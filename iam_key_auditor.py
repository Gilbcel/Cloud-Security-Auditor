import boto3
from datetime import datetime, timezone

DIAS_LIMITE = 90

def auditar_llaves_iam():
    client = boto3.client('iam')
    print("=" * 60)
    print("🔍 INICIANDO AUDITORÍA DE LLAVES DE ACCESO IAM (AWS)")
    print("=" * 60)
    
    try:
        usuarios = client.list_users()
        tiempo_actual = datetime.now(timezone.utc)
        llaves_viejas_detectadas = 0

        for usuario in usuarios['Users']:
            nombre_usuario = usuario['UserName']
            llaves = client.list_access_keys(UserName=nombre_usuario)
            
            for llave in llaves['AccessKeyMetadata']:
                id_llave = llave['AccessKeyId']
                estado = llave['Status']
                fecha_creacion = llave['CreateDate']
                antiguedad_dias = (tiempo_actual - fecha_creacion).days
                
                if estado == 'Active':
                    if antiguedad_dias > DIAS_LIMITE:
                        print(f"🔴 ALERTA: El usuario [{nombre_usuario}] tiene una llave activa VIEJA.")
                        print(f"   🔹 ID Llave: {id_llave} | Edad: {antiguedad_dias} días")
                        llaves_viejas_detectadas += 1
                    else:
                        print(f"🟢 OK: Usuario [{nombre_usuario}] | Llave: {id_llave} | Edad: {antiguedad_dias} días.")
                        
        print("=" * 60)
        print(f"📊 RESUMEN: Se encontraron {llaves_viejas_detectadas} llaves vencidas.")
        print("=" * 60)

    except Exception as e:
        print(f"❌ Error al conectar con AWS: {e}")

if __name__ == "__main__":
    auditar_llaves_iam()
