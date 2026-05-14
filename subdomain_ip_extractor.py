import socket
import time

def cazar_ip_real(dominio_base: str):
    """
    Busca subdominios comunes para ver si alguno filtra la IP real 
    del servidor, evadiendo la protección principal de Cloudflare.
    """
    # Lista de subdominios que los administradores suelen olvidar proteger
    subdominios = ['mail', 'ftp', 'cpanel', 'webmail', 'dev', 'test', 'admin']
    
    print(f"\n[*] Iniciando escaneo de fugas DNS para: {dominio_base}")
    print("-" * 40)
    
    for sub in subdominios:
        # Armamos el link completo (ej: mail.mercadolibre.com)
        objetivo = f"{sub}.{dominio_base}"
        
        try:
            # Intentamos resolver la IP
            ip_descubierta = socket.gethostbyname(objetivo)
            print(f"[+] VULNERABILIDAD ENCONTRADA -> {objetivo}")
            print(f"    IP Expuesta: {ip_descubierta}")
        except socket.gaierror:
            # Si el subdominio no existe, no hacemos nada y pasamos al siguiente
            print(f"[-] {objetivo} (No existe o está bloqueado)")
            pass
        
        # Pequeña pausa para no saturar la red
        time.sleep(0.5)

# --- USO DEL SCRIPT ---
print("--- ESCÁNER DE FUGAS (ANTI-CLOUDFLARE) ---")
target = input("[>] Ingresá el dominio base (ej. untdf.edu.ar sin www): ")
cazar_ip_real(target)
