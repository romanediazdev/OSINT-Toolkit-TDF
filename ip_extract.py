import socket
import time

def obtener_ip_de_dominio(url_objetivo: str) -> str:
    """
    Convierte el nombre de una página web (dominio) en su dirección IP real.
    """
    # 1. Limpiamos el texto. Si el usuario pega "https://www.google.com/algo", 
    # nos quedamos solo con "www.google.com"
    dominio_limpio = url_objetivo.replace("https://", "").replace("http://", "").split("/")[0]
    
    try:
        # 2. La magia de la librería socket: le pregunta a la red mundial 
        # cuál es la IP de ese nombre.
        ip_descubierta = socket.gethostbyname(dominio_limpio)
        return ip_descubierta
    
    except socket.gaierror:
        # Atajamos el error por si la página no existe o está mal escrita
        return "ERROR"

# ==========================================
# EJECUCIÓN PRINCIPAL DEL SCRIPT
# ==========================================

print("""
 🌐 EXTRACTOR DE IP (DNS RESOLVER) 🌐
""")

# Pedimos el link sospechoso o la página a investigar
objetivo = input("[>] Ingresá la página web (ej. untdf.edu.ar o facebook.com): ")

print("\n[*] Interrogando a los servidores DNS...")
time.sleep(1)

# Llamamos a nuestra función
ip_resultado = obtener_ip_de_dominio(objetivo)

# Verificamos si la función nos devolvió una IP o un error
if ip_resultado != "ERROR":
    print("\n[+] ¡OBJETIVO VULNERADO! [+]")
    print(f"[+] Dominio analizado: {objetivo}")
    print(f"[+] IP Oculta extraída: {ip_resultado}")
    print("-" * 40)
    print("💡 Tip: Copiá esta IP y pegala en tu herramienta 'rastreador_ip.py'")
else:
    print("\n[-] Error: No se pudo resolver el dominio. Verificá que la página exista y esté bien escrita.")