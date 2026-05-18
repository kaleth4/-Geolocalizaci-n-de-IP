import requests


def geolocalizar_ip(ip_o_dominio):
    # API gratuita que no requiere llave de acceso (hasta 45 peticiones por minuto)
    url = f"http://ip-api.com{ip_o_dominio}?fields=status,message,country,countryCode,regionName,city,zip,lat,lon,timezone,isp,org,as,query"

    try:
        # Hacer la consulta a la API
        respuesta = requests.get(url)
        datos = respuesta.json()

        # Verificar si la API respondió correctamente
        if datos.get("status") == "success":
            print(f"=== Datos de la IP / Dominio / Host ===")
            print(f"Dirección IP:      {datos.get('query')}")
            print(f"AS Number (ASN):   {datos.get('as')}")
            print(f"Organización:      {datos.get('org')}")
            print(f"ISP:               {datos.get('isp')}")
            print(f"País:              {datos.get('country')} ({datos.get('countryCode')})")
            print(f"Región/Estado:     {datos.get('regionName')}")
            print(f"Ciudad:            {datos.get('city')}")
            print(f"Código ZIP:        {datos.get('zip')}")
            print(f"Zona Horaria:      {datos.get('timezone')}")
            print(f"Latitud:           {datos.get('lat')}")
            print(f"Longitud:          {datos.get('lon')}")

            # Enlace de mapa equivalente al de la web
            lat, lon = datos.get("lat"), datos.get("lon")
            print(
                f"Mapa (Google):     https://google.com{lat},{lon}"
            )
        else:
            print(f"Error al localizar: {datos.get('message')}")

    except Exception as e:
        print(f"Error de conexión: {e}")


# Ejemplo de uso con la IP de tu consulta anterior
geolocalizar_ip("181.53.96.99")
