# 🌐 Geolocalizador de Direcciones IP y Dominios

Este es un script sencillo en **Python** que permite obtener la información geográfica y técnica de cualquier dirección IP pública o nombre de dominio (como `google.com`). El script consume una API de geolocalización gratuita y muestra los datos formateados directamente en la terminal, incluyendo un enlace directo a Google Maps.

## 🚀 Características

* **Información Completa:** Obtiene IP, ASN, ISP, País, Ciudad, Región, Código Postal y Zona Horaria.
* **Coordenadas Exactas:** Extrae la latitud y longitud estimadas.
* **Enlace a Mapa:** Genera un enlace interactivo para visualizar la ubicación en Google Maps.
* **Soporte Dual:** Funciona tanto con direcciones IP (IPv4) como con nombres de dominio.

## 📋 Requisitos Previos

Antes de ejecutar el script, asegúrate de tener instalado Python (versión 3.x o superior) y el administrador de paquetes `pip`.

## 🛠️ Instalación

1. Clona este repositorio o descarga el archivo del script:
   ```bash
   git clone https://github.com
   cd tu-repositorio
   ```

2. Instala la librería externa `requests` requerida para realizar las consultas web:
   ```bash
   pip install requests
   ```

## 💻 Uso

1. Abre el archivo del script (`geoloc.py` o el nombre que hayas elegido) y modifica la línea final con la IP o dominio que deseas buscar:
   ```python
   geolocalizar_ip("181.53.96.99")
   ```

2. Ejecuta el script desde tu terminal:
   ```bash
   python geoloc.py
   ```

### Ejemplo de Salida en Terminal

```text
=== Datos de la IP / Dominio / Host ===
Dirección IP:      181.53.96.99
AS Number (ASN):   AS10620 Telmex Colombia S.A.
Organización:      Telmex Colombia S.A.
ISP:               Telmex Colombia S.A.
País:              Colombia (CO)
Región/Estado:     Cundinamarca
Ciudad:            Cota
Código ZIP:        250010
Zona Horaria:      America/Bogota
Latitud:           4.8095
Longitud:          -74.0982
Mapa (Google):     https://google.com
```

## ⚙️ Detalles de la API

Este script utiliza la API pública y gratuita de [ip-api.com](http://ip-api.com). 
* **Limitaciones:** La versión gratuita permite un máximo de **45 peticiones por minuto** desde la misma dirección IP. Si excedes este límite, las peticiones serán bloqueadas temporalmente hasta que se restablezca el contador.
* **Uso comercial:** No está permitido el uso comercial con el endpoint gratuito.

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Siéntete libre de modificarlo y adaptarlo a tus necesidades.
