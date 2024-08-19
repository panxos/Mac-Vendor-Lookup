# Mac Vendor Lookup Pro

<p align="center">
  <img src="https://raw.githubusercontent.com/panxos/ConfServerDebian/main/panxos_logo.png" alt="Panxos Logo" width="200"/>
</p>

<p align="center">
  <a href="#descripción">Descripción</a> •
  <a href="#características">Características</a> •
  <a href="#requisitos">Requisitos</a> •
  <a href="#instalación">Instalación</a> •
  <a href="#uso">Uso</a> •
  <a href="#contribuir">Contribuir</a> •
  <a href="#licencia">Licencia</a> •
  <a href="#créditos">Créditos</a>
</p>

## Descripción

Mac Vendor Lookup Pro es una herramienta de línea de comandos potente y flexible diseñada para buscar y identificar los fabricantes de dispositivos de red basándose en sus direcciones MAC. Utiliza múltiples fuentes de datos para proporcionar información precisa y detallada.

## Características

- Búsqueda de fabricantes para múltiples direcciones MAC simultáneamente
- Soporte para entrada de direcciones MAC desde la línea de comandos o desde un archivo
- Múltiples fuentes de datos: MacVendors, MacAddress.io, y Wireshark
- Salida en formatos variados: tabla colorida, JSON, o CSV
- Manejo de configuración mediante archivo config.ini
- Sistema de logging para facilitar el debugging
- Interfaz de línea de comandos rica y flexible

## Requisitos

- Python 3.6+
- Conexión a Internet

## Instalación

1. Clone este repositorio:
   ```
   git clone https://github.com/panxos/Mac-Vendor-Lookup.git
   cd Mac-Vendor-Lookup
   ```

2. Instale las dependencias:
   ```
   pip3 install --user requests tabulate colorama
   ```

3. Configure su API key de MacAddress.io:
   Cree un archivo `config.ini` en el directorio del proyecto con el siguiente contenido:
   ```ini
   [API]
   MacAddressApiKey = SU_API_KEY_AQUI
   ```

4. Haga el script ejecutable:
   ```
   chmod +x mac-vendor-lookup-pro.py
   ```

5. Cree un enlace simbólico en /usr/local/bin para poder ejecutar el script desde cualquier ubicación:
   ```
   sudo ln -s $(pwd)/mac-vendor-lookup-pro.py /usr/local/bin/mac-vendor-lookup
   ```

## Uso

Puede usar el script desde cualquier ubicación en su terminal simplemente ejecutando:

```
mac-vendor-lookup [opciones]
```

Ejemplos de uso:

1. Para buscar múltiples direcciones MAC:
   ```
   mac-vendor-lookup -m 00:11:22:33:44:55 AA:BB:CC:DD:EE:FF
   ```

2. Para buscar direcciones MAC desde un archivo de texto:
   ```
   mac-vendor-lookup -f macs.txt
   ```

3. Para especificar el formato de salida:
   ```
   mac-vendor-lookup -m 00:11:22:33:44:55 -o json
   ```

Opciones disponibles:
- `-m, --macs`: Lista de direcciones MAC para buscar
- `-f, --file`: Archivo de texto con direcciones MAC (una por línea)
- `-o, --output`: Formato de salida (table, json, csv). Por defecto: table

## Contribuir

Las contribuciones son bienvenidas! Por favor, siéntase libre de enviar un Pull Request.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Vea el archivo `LICENSE` para más detalles.

## Créditos

Desarrollado por [Francisco Aravena](https://github.com/panxos)

---

<p align="center">
  Desarrollado con ❤️ por Francisco Aravena
</p>
