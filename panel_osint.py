import os
import time

def mostrar_menu():
    # Esta línea es un truco para limpiar la pantalla cada vez que volvemos al menú.
    # Usa 'cls' en Windows y 'clear' si algún día lo corrés en Linux.
    os.system('cls' if os.name == 'nt' else 'clear')
    
    banner = """
 ╦╔═╗  ╔╦╗╦═╗╔═╗╔═╗╦╔═╔═╗╦═╗
 ║╠═╝   ║ ╠╦╝╠═╣║  ╠╩╗║╣ ╠╦╝
 ╩╩     ╩ ╩╚═╩ ╩╚═╝╩ ╩╚═╝╩╚═
 🛡️  OSINT TOOLKIT TDF - PANEL DE CONTROL 🛡️
--------------------------------------------------
[1] Rastreador Geográfico (ip_tracker.py)
[2] Resolutor DNS Estático (ip_extract.py)
[3] Escáner de Fugas DNS (subdomain_ip_extractor.py)
[4] Analizador Forense (domain_unmasker.py)
[0] Salir del Panel
--------------------------------------------------
    """
    # Para que se vea verde (solo si lo corrés directo en PowerShell)
    print("\033[92m" + banner + "\033[0m")

# ==========================================
# MOTOR DEL MENÚ PRINCIPAL
# ==========================================

# El bucle while True mantiene el programa vivo hasta que le digamos "break"
while True:
    mostrar_menu()
    opcion = input("[root@romanediazdev]~# Seleccione un módulo a ejecutar: ")

    if opcion == "1":
        print("\n[*] Iniciando Rastreador Geográfico...\n")
        time.sleep(1)
        # Acá le damos la orden a tu Windows de que corra el otro archivo
        os.system("python ip_tracker.py")
        input("\n[!] Presioná ENTER para volver al menú principal...")
        
    elif opcion == "2":
        print("\n[*] Iniciando Resolutor DNS Estático...\n")
        time.sleep(1)
        os.system("python ip_extract.py")
        input("\n[!] Presioná ENTER para volver al menú principal...")
        
    elif opcion == "3":
        print("\n[*] Iniciando Escáner de Fugas DNS...\n")
        time.sleep(1)
        os.system("python subdomain_ip_extractor.py")
        input("\n[!] Presioná ENTER para volver al menú principal...")
        
    elif opcion == "4":
        print("\n[*] Iniciando Analizador Forense...\n")
        time.sleep(1)
        os.system("python domain_unmasker.py")
        input("\n[!] Presioná ENTER para volver al menú principal...")
        
    elif opcion == "0":
        print("\n[*] Cerrando OSINT Toolkit. ¡Nos vemos en la terminal!\n")
        time.sleep(1)
        break # Esto rompe el bucle infinito y cierra el programa
        
    else:
        print("\n[-] Opción no válida. Por favor, ingresá un número del 0 al 4.")
        time.sleep(1.5)