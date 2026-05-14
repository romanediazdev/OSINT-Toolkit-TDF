import urllib.request
from urllib.error import URLError, HTTPError
import time

def desenmascarar_link(url_sospechosa: str) -> str:
    """
    Sigue la ruta de un link acortado o enmascarado para revelar 
    el destino final (IP Logger o Phishing) sin activar scripts maliciosos.
    """
    # Verificamos que el usuario haya puesto "http" al principio
    if not url_sospechosa.startswith('http'):
        url_sospechosa = 'http://' + url_sospechosa
        
    try:
        # Nos disfrazamos de navegador
        cabecera = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        peticion = urllib.request.Request(url_sospechosa, headers=cabecera)
        
        # Al conectarse, Python sigue automáticamente las redirecciones ocultas
        # pero NO ejecuta los códigos maliciosos de la página.
        respuesta = urllib.request.urlopen(peticion)
        
        # El método geturl() nos dice exactamente en qué página aterrizamos al final
        destino_real = respuesta.geturl()
        return destino_real
        
    except HTTPError as e:
        return f"ERROR: El servidor rechazó la conexión (Código {e.code}). Puede estar dado de baja."
    except URLError:
        return "ERROR: No se pudo conectar. El link no existe o tu internet falla."

# ==========================================
# EJECUCIÓN PRINCIPAL DEL SCRIPT
# ==========================================

print("""
 🛡️  ANALIZADOR FORENSE DE ENLACES (ANTI-SPOOFING) 🛡️
------------------------------------------------------
Analiza links cortos (bit.ly, tinyurl) o enmascarados 
para revelar la trampa sin exponer tu IP local.
""")

objetivo = input("[>] Pegá el link sospechoso acá: ")

print("\n[*] Rastreando redirecciones de red...")
time.sleep(1)

# Llamamos a la función
resultado_final = desenmascarar_link(objetivo)

print("-" * 50)
if "ERROR" in resultado_final:
    print(resultado_final)
else:
    print(f"[!] LINK ORIGINAL INGRESADO: {objetivo}")
    print(f"[+] DESTINO REAL DESCUBIERTO: {resultado_final}")
    
    # Lógica extra para alertar sobre IP loggers conocidos
    if "grabify.link" in resultado_final or "iplogger.org" in resultado_final:
        print("\n[!!!] ALERTA ROJA: SE DETECTÓ UN IP LOGGER [!!!]")
        print("Este link fue diseñado para robar tu ubicación y datos de conexión.")
print("-" * 50)