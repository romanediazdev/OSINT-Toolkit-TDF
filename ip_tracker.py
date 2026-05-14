import urllib.request
import json
import time
from urllib.error import URLError

def obtener_datos_ip(ip_objetivo: str) -> dict:
    """
    Se conecta a la API de geolocalización pidiendo campos de seguridad extra
    (incluyendo detección de VPN/Proxy y Hosting).
    """
    # URL actualizada con los campos extra de seguridad
    url = f"http://ip-api.com/json/{ip_objetivo}?fields=status,country,regionName,city,lat,lon,isp,org,query,proxy,hosting"
    
    cabecera = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    
    peticion = urllib.request.Request(url, headers=cabecera)
    respuesta = urllib.request.urlopen(peticion)
    
    return json.loads(respuesta.read())

def generar_reporte(datos: dict) -> str:
    """
    Toma los datos extraídos y crea un archivo de texto con el informe completo.
    """
    ip_analizada = datos.get('query', 'Desconocida')
    nombre_archivo = f"Evidencia_IP_{ip_analizada.replace('.', '_')}.txt"
    
    # Variables de seguridad
    es_proxy = datos.get("proxy", False)
    es_hosting = datos.get("hosting", False)
    
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        archivo.write("=========================================\n")
        archivo.write("      REPORTE DE INTELIGENCIA OSINT      \n")
        archivo.write("=========================================\n\n")
        archivo.write(f"[+] IP RASTREADA: {ip_analizada}\n")
        archivo.write(f"[+] PAÍS: {datos.get('country')}\n")
        archivo.write(f"[+] CIUDAD/PROVINCIA: {datos.get('city')}, {datos.get('regionName')}\n")
        archivo.write(f"[+] PROVEEDOR (ISP): {datos.get('isp')}\n")
        archivo.write(f"[+] ORGANIZACIÓN: {datos.get('org')}\n")
        archivo.write(f"[+] COORDENADAS GPS: {datos.get('lat')}, {datos.get('lon')}\n\n")
        
        archivo.write("--- ANÁLISIS DE SEGURIDAD ---\n")
        if es_proxy or es_hosting:
            archivo.write("[!] ALERTA: La conexión está ruteada mediante Proxy/VPN o Datacenter.\n")
            archivo.write("[!] La ubicación geográfica mostrada pertenece al servidor, no al usuario final.\n")
        else:
            archivo.write("[+] Conexión limpia. No se detectaron escudos o VPNs comerciales.\n")
            
        archivo.write("\n=========================================\n")
        archivo.write("Extracción finalizada con éxito.\n")
        
    return nombre_archivo

# ==========================================
# EJECUCIÓN PRINCIPAL DEL SCRIPT
# ==========================================

banner = """
 ╦╔═╗  ╔╦╗╦═╗╔═╗╔═╗╦╔═╔═╗╦═╗
 ║╠═╝   ║ ╠╦╝╠═╣║  ╠╩╗║╣ ╠╦╝
 ╩╩     ╩ ╩╚═╩ ╩╚═╝╩ ╩╚═╝╩╚═
  --- RIO GRANDE, TIERRA DEL FUEGO ---
        Módulo de Rastreo IP v2.0
"""
print(banner)
print("Dejá en blanco y presioná Enter para rastrear tu propia conexión.")
objetivo = input("[>] IP a investigar (Ej: 8.8.8.8): ")

print("\n[*] Iniciando módulo de rastreo geolocalizado...")
time.sleep(1)
print("[*] Evadiendo firewalls y cruzando bases de datos públicas...")
time.sleep(1.5)

try:
    resultados = obtener_datos_ip(objetivo)
    
    if resultados.get("status") == "success":
        print("\n[+] ¡Rastreo Exitoso! Analizando datos de seguridad...")
        time.sleep(1)
        
        # Evaluamos la seguridad en la consola
        es_proxy = resultados.get("proxy", False)
        es_hosting = resultados.get("hosting", False)
        
        if es_proxy or es_hosting:
            print("\n[!] ALERTA ROJA: LA UBICACIÓN PUEDE SER FALSA [!]")
            print("[!] La IP pertenece a un Datacenter, VPN o Escudo (Cloudflare/AWS).")
            print("[!] La ubicación que ves es donde está el servidor, no el objetivo real.")
        else:
            print("\n[+] Conexión residencial detectada (IP limpia).")
            
        # Generamos el reporte
        archivo_creado = generar_reporte(resultados)
        
        print(f"\n[+] Reporte exportado y guardado como: '{archivo_creado}'")
        print("[!] Revisá la carpeta actual en VS Code para ver la evidencia.")
    else:
        print("\n[-] Error: La dirección IP no es válida o es privada.")

except URLError:
    print("\n[-] Error crítico: No hay conexión a internet o el servidor bloqueó la solicitud.")
except Exception as e:
    print(f"\n[-] Ocurrió un error inesperado: {e}")