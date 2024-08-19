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
  <a href="#configuración-como-comando-de-consola">Configuración como Comando de Consola</a> •
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
- Instalación automática de dependencias
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

2. (Opcional) Cree y active un entorno virtual:
   ```
   python3 -m venv venv
   source venv/bin/activate  # En Windows use `venv\Scripts\activate`
   ```

3. Instale las dependencias:
   ```
   pip install -r requirements.txt
   ```

4. Configure su API key de MacAddress.io:
   Cree un archivo `config.ini` en el directorio del proyecto con el siguiente contenido:
   ```ini
   [API]
   MacAddressApiKey = SU_API_KEY_AQUI
   ```

## Uso

Puede usar el script de las siguientes maneras:

1. Para buscar múltiples direcciones MAC desde la línea de comandos:
   ```
   python3 mac-vendor-lookup-pro.py -m 00:11:22:33:44:55 AA:BB:CC:DD:EE:FF
   ```

2. Para buscar direcciones MAC desde un archivo de texto:
   ```
   python3 mac-vendor-lookup-pro.py -f macs.txt
   ```

3. Para especificar el formato de salida:
   ```
   python3 mac-vendor-lookup-pro.py -m 00:11:22:33:44:55 -o json
   ```

Opciones disponibles:
- `-m, --macs`: Lista de direcciones MAC para buscar
- `-f, --file`: Archivo de texto con direcciones MAC (una por línea)
- `-o, --output`: Formato de salida (table, json, csv). Por defecto: table

## Configuración como Comando de Consola

Para poder ejecutar `mac-vendor-lookup-pro` desde cualquier ubicación en la terminal, siga estos pasos:

1. Asegúrese de que el script tenga permisos de ejecución:
   ```
   chmod +x /ruta/completa/a/mac-vendor-lookup-pro.py
   ```

2. Cree un alias en su archivo de configuración de shell (por ejemplo, `.bashrc` o `.zshrc`):
   ```
   echo 'alias mac-vendor-lookup="python3 /ruta/completa/a/mac-vendor-lookup-pro.py"' >> ~/.bashrc
   ```

3. Recargue su configuración de shell:
   ```
   source ~/.bashrc
   ```

Ahora puede usar el comando `mac-vendor-lookup` desde cualquier ubicación en su terminal.

Alternativamente, puede crear un enlace simbólico en un directorio que esté en su PATH:

```
sudo ln -s /ruta/completa/a/mac-vendor-lookup-pro.py /usr/local/bin/mac-vendor-lookup
```

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
