# 🌍 IP Tracker Pro - Geolocalización Inteligente

```
██╗██████╗ ████████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗ 
██║██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
██║██████╔╝   ██║   ██████╔╝███████║██║     █████╔╝ █████╗  ██████╔╝
██║██╔═══╝    ██║   ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
██║██║        ██║   ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
╚═╝╚═╝        ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
```

## 📋 Descripción

**IP Tracker Pro** es una herramienta profesional de geolocalización que utiliza la API de **ipinfo.io** para obtener información detallada sobre direcciones IP. Diseñado con arquitectura de nivel empresarial, manejo robusto de errores y una interfaz intuitiva en terminal.

---

## ✨ Características Principales

✅ **Automatización Completa** - Sin entrada manual de tokens  
✅ **Manejo Profesional de Errores** - Excepciones controladas y timeouts  
✅ **Consulta Flexible** - Geolocaliza tu IP o cualquier otra  
✅ **Interfaz Colorida** - Salida formateada y legible en terminal  
✅ **Arquitectura POO** - Código reutilizable e integrable  
✅ **Variables de Entorno** - Seguridad mediante `.env`  

---

## 🚀 Instalación

### Requisitos Previos
- Python 3.7+
- pip (gestor de paquetes)

### Pasos de Instalación

```bash
# 1. Clona o descarga el repositorio
git clone https://github.com/tuusuario/ip-tracker-pro.git
cd ip-tracker-pro

# 2. Instala las dependencias
pip install -r requirements.txt

# 3. Configura tu token de API
echo "IPINFO_TOKEN=tu_token_aqui" > .env
```

### Obtener Token API

1. Visita [ipinfo.io](https://ipinfo.io)
2. Regístrate (plan gratuito disponible)
3. Copia tu token desde el dashboard
4. Pégalo en el archivo `.env`

---

## 💻 Uso

### Opción 1: Geolocalizar tu IP actual
```bash
python ip_tracker.py
```

### Opción 2: Geolocalizar una IP específica
```bash
python ip_tracker.py 8.8.8.8
python ip_tracker.py 1.1.1.1
python ip_tracker.py 142.251.32.14
```

### Ejemplo de Salida
```
[*] Extrayendo información de: 8.8.8.8

Ip          : 8.8.8.8
City        : Mountain View
Region      : California
Country     : US
Loc         : 37.4192,-122.0574
Org         : AS15169 Google LLC
Timezone    : America/Los_Angeles
```

---

## 📁 Estructura del Proyecto

```
ip-tracker-pro/
├── ip_tracker.py          # Script principal
├── requirements.txt       # Dependencias
├── .env.example          # Template de configuración
├── .env                  # Variables de entorno (NO SUBIR)
├── .gitignore           # Archivos ignorados en git
└── README.md            # Este archivo
```

---

## 🔧 Código Refactorizado

```python
import ipinfo
import sys
import requests
from colorama import Fore, init
import os
from dotenv import load_dotenv

# Inicializa colores
init(autoreset=True)
load_dotenv()

class IPTracker:
    def __init__(self, token=None):
        self.token = token or os.getenv("IPINFO_TOKEN")
        if not self.token:
            raise ValueError("Token no configurado. Verifica tu archivo .env")
        self.handler = ipinfo.getHandler(self.token)

    def get_public_ip(self):
        """Obtiene la IP pública actual si no se proporciona una."""
        try:
            return requests.get("https://ipify.org", timeout=5).text.strip()
        except requests.RequestException as e:
            print(f"{Fore.RED}[!] Error al obtener la IP pública: {e}")
            return None

    def fetch_details(self, ip=None):
        """Obtiene y muestra los detalles de geolocalización."""
        target_ip = ip if ip else self.get_public_ip()
        
        if not target_ip:
            return

        try:
            print(f"{Fore.CYAN}[*] Extrayendo información de: {target_ip}\n")
            details = self.handler.getDetails(target_ip)
            
            for key, value in details.all.items():
                print(f"{Fore.YELLOW}{key.capitalize():<12}: {Fore.WHITE}{value}")
                
        except Exception as e:
            print(f"{Fore.RED}[!] Error en la API de IPInfo: {e}")

if __name__ == "__main__":
    try:
        tracker = IPTracker()
        target = sys.argv[1] if len(sys.argv) > 1 else None
        tracker.fetch_details(target)
    except ValueError as e:
        print(f"{Fore.RED}[!] {e}")
        sys.exit(1)
```

---

## 🎯 Por Qué Esta Versión es Superior

| Aspecto | Antes | Después |
|--------|-------|---------|
| **Token** | Manual en código | Automático desde `.env` |
| **Errores** | Script se "rompe" | Manejo controlado |
| **Flexibilidad** | Solo IP propia | Cualquier IP |
| **Código** | Procedural | POO (reutilizable) |
| **Seguridad** | Token expuesto | Variables de entorno |
| **Formato** | Desordenado | Tabla alineada |

---

## 📦 Dependencias

```
ipinfo>=5.0.0
requests>=2.28.0
colorama>=0.4.6
python-dotenv>=0.21.0
```

---

## ⚠️ Consideraciones de Seguridad

- **Nunca** commits tu archivo `.env` con tokens reales
- Usa `.gitignore` para excluir archivos sensibles
- Regenera tokens si los expones accidentalmente
- Respeta los límites de la API (plan gratuito: 50,000 requests/mes)

---

## 🐛 Troubleshooting

**Error: "Token no configurado"**
```bash
# Asegúrate de que existe .env con:
IPINFO_TOKEN=tu_token_aqui
```

**Error: "No module named 'ipinfo'"**
```bash
pip install -r requirements.txt
```

**Timeout en la conexión**
- Verifica tu conexión a internet
- Intenta aumentar el timeout en `get_public_ip()`

---

## 📊 Casos de Uso

🔍 **Ciberseguridad** - Investigar IPs sospechosas  
📍 **Análisis Geográfico** - Mapear ubicaciones de servidores  
🛡️ **Auditoría** - Verificar ubicación de accesos  
📱 **Desarrollo** - Testing de APIs con datos reales  

---

## 📝 Licencia

MIT License - Libre para uso personal y comercial

---

## 🤝 Contribuciones

¿Encontraste un bug o tienes una idea? ¡Abre un issue o pull request!

```bash
git checkout -b feature/mi-mejora
git commit -am "Agrega mi mejora"
git push origin feature/mi-mejora
```

---

## 📞 Soporte

- 📧 Email: soporte@iptrackerpro.dev
- 🐙 GitHub Issues: [Reporta aquí](https://github.com/tuusuario/ip-tracker-pro/issues)
- 💬 Discussions: Comunidad activa

---

**Hecho con ❤️ para la comunidad de ciberseguridad**
