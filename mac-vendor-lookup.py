#!/usr/bin/env python3

import sys
import os
import argparse
import logging
import json
import csv
from io import StringIO
from configparser import ConfigParser
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import List, Tuple, Dict

import requests
from tabulate import tabulate
from colorama import Fore, Style, init

# Configuración inicial
init(autoreset=True)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_config() -> ConfigParser:
    config = ConfigParser()
    config_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'config.ini')
    if os.path.exists(config_file):
        config.read(config_file)
    else:
        config['API'] = {'MacAddressApiKey': 'YOUR_API_KEY'}
        with open(config_file, 'w') as f:
            config.write(f)
        logging.warning(f"Archivo de configuración creado en {config_file}. Por favor, actualiza la API key.")
    return config

CONFIG = load_config()

def print_banner() -> None:
    banner = '''
    ██████╗ ██╗  ██╗███╗   ██╗██╗  ██╗ ██████╗ ███████╗
    ██╔══██╗██║  ██║████╗  ██║╚██╗██╔╝██╔═████╗╚══███╔╝
    ██████╔╝███████║██╔██╗ ██║ ╚███╔╝ ██║██╔██║  ███╔╝ 
    ██╔═══╝ ╚════██║██║╚██╗██║ ██╔██╗ ████╔╝██║ ███╔╝  
    ██║          ██║██║ ╚████║██╔╝ ██╗╚██████╔╝███████╗
    ╚═╝          ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝
                                                       
    GitHub: https://github.com/panxos
    Author: Francisco Aravena
    '''
    print(banner)

def clean_mac(mac_address: str) -> str:
    return ''.join(c for c in mac_address if c.isalnum()).upper()

def get_mac_vendor_macvendors(mac_prefix: str) -> Tuple[str, str]:
    url = f'https://api.macvendors.com/{mac_prefix}'
    try:
        response = requests.get(url, timeout=5)
        return "MacVendors", response.text if response.status_code == 200 else "No encontrado"
    except requests.RequestException as e:
        logging.error(f"Error al consultar MacVendors: {e}")
        return "MacVendors", "Error de conexión"

def get_mac_vendor_macaddress(mac_prefix: str) -> Tuple[str, str]:
    api_key = CONFIG['API'].get('MacAddressApiKey', 'YOUR_API_KEY')
    url = f'https://api.macaddress.io/v1?apiKey={api_key}&output=vendor&search={mac_prefix}'
    try:
        response = requests.get(url, timeout=5)
        return "MacAddress.io", response.text if response.status_code == 200 else "No encontrado"
    except requests.RequestException as e:
        logging.error(f"Error al consultar MacAddress.io: {e}")
        return "MacAddress.io", "Error de conexión"

def get_mac_vendor_wireshark(mac_prefix: str) -> Tuple[str, str]:
    url = f'https://www.wireshark.org/tools/oui-lookup.html?query={mac_prefix}'
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            import re
            match = re.search(r'<td>([^<]+)</td>', response.text)
            return "Wireshark", match.group(1) if match else "No encontrado"
        return "Wireshark", "No encontrado"
    except requests.RequestException as e:
        logging.error(f"Error al consultar Wireshark: {e}")
        return "Wireshark", "Error de conexión"

def get_all_vendors(mac_address: str) -> List[Tuple[str, str]]:
    mac_prefix = clean_mac(mac_address)[:6]
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = [
            executor.submit(get_mac_vendor_macvendors, mac_prefix),
            executor.submit(get_mac_vendor_macaddress, mac_prefix),
            executor.submit(get_mac_vendor_wireshark, mac_prefix)
        ]
        results = [future.result() for future in as_completed(futures)]
    return results

def colorize_result(result: str) -> str:
    if "No encontrado" in result:
        return Fore.YELLOW + result + Style.RESET_ALL
    elif "Error" in result:
        return Fore.RED + result + Style.RESET_ALL
    else:
        return Fore.GREEN + result + Style.RESET_ALL

def process_mac(mac: str) -> Tuple[str, List[Tuple[str, str]]]:
    results = get_all_vendors(mac)
    return mac, [(source, colorize_result(vendor)) for source, vendor in results]

def output_results(results: Dict[str, List[Tuple[str, str]]], output_format: str) -> None:
    if output_format == 'table':
        for mac, vendors in results.items():
            print(f"\nResultados para la MAC: {Fore.CYAN}{mac}{Style.RESET_ALL}")
            headers = [Fore.BLUE + "Fuente" + Style.RESET_ALL, Fore.BLUE + "Fabricante" + Style.RESET_ALL]
            table = tabulate(vendors, headers=headers, tablefmt="fancy_grid")
            print(table)
    elif output_format == 'json':
        json_results = {mac: dict(vendors) for mac, vendors in results.items()}
        print(json.dumps(json_results, indent=2))
    elif output_format == 'csv':
        output = StringIO()
        writer = csv.writer(output)
        writer.writerow(['MAC', 'Fuente', 'Fabricante'])
        for mac, vendors in results.items():
            for source, vendor in vendors:
                writer.writerow([mac, source, vendor])
        print(output.getvalue())

def main():
    print_banner()

    parser = argparse.ArgumentParser(description='Buscar fabricantes de direcciones MAC.')
    parser.add_argument('-m', '--macs', nargs='+', help='Lista de direcciones MAC para buscar')
    parser.add_argument('-f', '--file', help='Archivo de texto con direcciones MAC (una por línea)')
    parser.add_argument('-o', '--output', choices=['table', 'json', 'csv'], default='table', help='Formato de salida')
    args = parser.parse_args()

    macs = []
    if args.macs:
        macs.extend(args.macs)
    if args.file:
        try:
            with open(args.file, 'r') as f:
                macs.extend([line.strip() for line in f if line.strip()])
        except FileNotFoundError:
            logging.error(f"No se pudo encontrar el archivo {args.file}")
            sys.exit(1)

    if not macs:
        logging.error("Debe proporcionar al menos una dirección MAC o un archivo con direcciones MAC")
        sys.exit(1)

    results = {}
    with ThreadPoolExecutor() as executor:
        future_to_mac = {executor.submit(process_mac, mac): mac for mac in macs}
        for future in as_completed(future_to_mac):
            mac = future_to_mac[future]
            try:
                mac, vendors = future.result()
                results[mac] = vendors
            except Exception as exc:
                logging.error(f'{mac} generó una excepción: {exc}')

    output_results(results, args.output)

if __name__ == "__main__":
    main()
