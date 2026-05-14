# OSINT Toolkit TDF - Prototipo de Auditoría de Red

Este repositorio contiene una suite de herramientas desarrolladas en **Python** enfocadas en la recolección de inteligencia de fuentes abiertas (OSINT) y el análisis de infraestructura de red. Este proyecto fue desarrollado como parte de mi formación técnica en el **Centro Politécnico Superior Malvinas Argentinas (Río Grande, Tierra del Fuego)**.

## Herramientas Incluidas

El toolkit se divide en cuatro módulos principales, cada uno diseñado para una etapa específica de una investigación digital:

### 1. [ip_tracker.py](cite: ip_tracker.py) - Rastreador Geográfico Avanzado
Módulo principal de geolocalización que consulta APIs de inteligencia para obtener datos precisos de una dirección IP.
* **Detección de Escudos:** Identifica automáticamente si la IP pertenece a un Proxy, VPN o a un centro de datos (Hosting) como Cloudflare o AWS.
* **Reportes Automáticos:** Genera un archivo `.txt` detallado con coordenadas GPS, ISP y organización, incluyendo advertencias de seguridad si la ubicación es potencialmente falsa.

### 2. [ip_extract.py](cite: ip_extract.py) - Resolutor DNS Estático
Herramienta fundamental para la fase de reconocimiento inicial.
* **Limpieza de Datos:** Utiliza manipulación de strings para procesar URLs crudas y extraer el dominio puro.
* **Resolución de Host:** Emplea la librería nativa `socket` para interrogar a los servidores DNS y obtener la IP pública de cualquier sitio web.

### 3. [subdomain_ip_extractor.py](cite: subdomain_ip_extractor.py) - Escáner de Fugas DNS
Diseñado específicamente para evadir protecciones de servicios de borde como Cloudflare.
* **Detección de Fugas:** Realiza un escaneo sobre subdomains comunes (`mail`, `ftp`, `dev`, etc.) para encontrar configuraciones incorrectas que expongan la IP real del servidor de origen.

### 4. [domain_unmasker.py](cite: domain_unmasker.py) - Analizador Forense de Enlaces
Herramienta de seguridad defensiva para analizar enlaces sospechosos o enmascarados.
* **Anti-Spoofing:** Sigue la cadena de redirecciones HTTP sin ejecutar scripts maliciosos en el navegador del analista.
* **Identificación de Amenazas:** Detecta específicamente si el destino final es un servicio de IP Logging conocido (como Grabify o iplogger).

## Instalación y Uso

Este toolkit fue desarrollado utilizando únicamente **librerías nativas de Python 3.x**, por lo que no requiere la instalación de dependencias externas (`pip`), lo que lo hace ideal para entornos de auditoría rápidos y seguros.

1. Clonar el repositorio.
2. Ejecutar cualquier módulo desde la terminal:
   ```bash
   python ip_tracker.py
