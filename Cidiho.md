import ipinfo
import sys
import requests

# Obtiene la IP pública actual del sistema
response = requests.get("https://ipify.org")
ip_address = response.text

# Pide el token de acceso manualmente
access_token = input("Ingresa el token => ")

# Configura el handler de ipinfo
handler = ipinfo.getHandler(access_token)

# Obtiene los detalles de la IP detectada
details = handler.getDetails(ip_address)

# Itera sobre todos los ítems y los imprime
for key, value in details.all.items():
    print(f"{key}:{value}")
Usa el código con precaución.Detalles a tener en cuenta:Dependencias: Para que funcione, necesitas instalar las librerías con: pip install ipinfo requests.API Key: Necesitas una cuenta en ipinfo.io para obtener el token que el programa pide por consola.Uso: Este script es ideal para la fase de Reconocimiento (OSINT), ya que te da la ubicación física, el ISP (proveedor de internet) y las coordenadas de una IP.
