import socket
import os
from tqdm import tqdm
from colorama import Fore, Style

ascii_art = """
 .oooooo..o   .oooooo.         .o.       ooooo      ooo oooooooooooo ooooooooooooo 
d8P'    `Y8  d8P'  `Y8b       .888.      `888b.     `8' `888'     `8 8'   888   `8 
Y88bo.      888              .8"888.      8 `88b.    8   888              888      
 `"Y8888o.  888             .8' `888.     8   `88b.  8   888oooo8         888      
     `"Y88b 888            .88ooo8888.    8     `88b.8   888    "         888      
oo     .d8P `88b    ooo   .8'     `888.   8       `888   888       o      888      
8""88888P'   `Y8bood8P'  o88o     o8888o o8o        `8  o888ooooood8     o888o     """

bienvenida = """
[+] Bienvenido a Scanet! 
[+] Una herramienta de escaneo de red, dispositivos, puertos y servicios.
[+] Versión: 1.0
[+] Desarrollado al 100% con Python.
[+] Creado por Daniel Escamilla"""

print(Fore.MAGENTA + Style.BRIGHT + ascii_art + "\n" + bienvenida + Style.RESET_ALL +"\n")

def validar_ip(ip):
    octetos = ip.split(".")
    if len(octetos) != 4:
        return False
    for octeto in octetos:
        if not (0 <= int(octeto) <= 255):
            return False
    return ip

def pedir_ip():
    while True:
        ip_usuario = input("Ingresa una dirección IP: ")
        if validar_ip(ip_usuario):
            print("La dirección IP es válida.")
            return ip_usuario 
        else:
            print("La dirección IP no es válida. Intenta nuevamente.")

def validar_port(port):
    if 1 <= int(port) <= 65535:
        return int(port)
    else:
        return False

def pedir_port():
    while True:
        port_usuario = input("Ingresa un puerto (1-65535): ")
        if validar_port(port_usuario):
            return port_usuario 
        else:
            print("El puerto no es válido. Intenta nuevamente.")

def escanear_red():
    print("Escaneando las redes...")
    resultado = os.popen("arp -a").read()
    print(resultado)

def escanear_ip():
    print("[+] Dirección IP a escanear.")
    target_ip = validar_ip(pedir_ip())
    print("[+] Puerto desde el que se iniciará el escaneo.")
    first_port = validar_port(pedir_port())
    print("[+] Puerto en el que finalizará el escaneo.")
    last_port = validar_port(pedir_port())

    if first_port > last_port:
        first_port, last_port = last_port, first_port

    if first_port == last_port:
        last_port += 1

    if first_port == last_port == 65535:
        first_port -= 1

    print(f"\n[+] Escaneando la IP: {target_ip} desde el puerto {first_port} hasta {last_port}...\n")
    open_ports = []
    for port in tqdm(range(first_port, last_port + 1)):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.1)
        resultado = s.connect_ex((target_ip, port))
        if resultado == 0:
            try:
                service = socket.getservbyport(port)
            except:
                service = "Desconocido"
            print(f"\nPuerto: {Fore.MAGENTA}{port}{Style.RESET_ALL} | Servicio: {Fore.MAGENTA}{service}{Style.RESET_ALL}")
            open_ports.append((port, service))
        s.close()
    print("[+] Escaneo completado con éxito!")
    return target_ip, open_ports

def escaneo_comun(target_ip):
    puertos_comunes = [
        20, 21,     # FTP (File Transfer Protocol)
        22,         # SSH (Secure Shell)
        23,         # Telnet
        25,         # SMTP (Simple Mail Transfer Protocol)
        53,         # DNS (Domain Name System)
        67, 68,     # DHCP (Dynamic Host Configuration Protocol)
        69,         # TFTP (Trivial File Transfer Protocol)
        80,         # HTTP (HyperText Transfer Protocol)
        110,        # POP3 (Post Office Protocol v3)
        123,        # NTP (Network Time Protocol)
        137, 138, 139,  # NetBIOS
        143,        # IMAP (Internet Message Access Protocol)
        161, 162,   # SNMP (Simple Network Management Protocol)
        389,        # LDAP (Lightweight Directory Access Protocol)
        443,        # HTTPS (Secure HTTP)
        445,        # SMB (Server Message Block)
        465,        # SMTPS (SMTP over SSL)
        514,        # Syslog
        587,        # SMTP (Email submission)
        636,        # LDAPS (Secure LDAP)
        873,        # Rsync
        990, 991,   # FTPS (Secure FTP)
        993,        # IMAPS (IMAP over SSL)
        995,        # POP3S (POP3 over SSL)
        1080,       # SOCKS Proxy
        1433, 1434, # Microsoft SQL Server
        1521,       # Oracle Database
        1723,       # PPTP (Point-to-Point Tunneling Protocol)
        1883, 8883, # MQTT (Message Queuing Telemetry Transport)
        2049,       # NFS (Network File System)
        2181,       # Apache Zookeeper
        3306,       # MySQL
        3389,       # RDP (Remote Desktop Protocol)
        5432,       # PostgreSQL
        5900,       # VNC (Virtual Network Computing)
        6379,       # Redis
        6667,       # IRC (Internet Relay Chat)
        7000,       # Kademlia
        8080,       # Alternative HTTP
        8443,       # HTTPS (Alternative)
        9000,       # SonarQube, PHP-FPM
        9092,       # Kafka
        9200,       # Elasticsearch
        11211,      # Memcached
        27017,      # MongoDB
    ]

    print(f"\n[+] Escaneando la IP: {target_ip} desde el puerto {puertos_comunes[0]} hasta {puertos_comunes[-1]}...\n")
    open_ports = []
    for port in tqdm(puertos_comunes):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.1)
        resultado = s.connect_ex((target_ip, port))
        if resultado == 0:
            try:
                service = socket.getservbyport(port)
            except:
                service = "Desconocido"
            print(f"\nPuerto: {Fore.MAGENTA}{port}{Style.RESET_ALL} | Servicio: {Fore.MAGENTA}{service}{Style.RESET_ALL}")
            open_ports.append((port, service))
        s.close()
    print("[+] Escaneo completado con éxito!")
    return target_ip, open_ports

def generar_txt(target_ip, open_ports):
    print("\n[+] Generando archivo txt...\n")
    with open("scanet.txt", "w") as f:
        f.write("[+] Resgistro del escaneo al dispositivo con dirección IP: " + target_ip + "\n")
        for port, service in open_ports:
            f.write(f"Puerto {port}: {service}\n")
    print("[+] Archivo generado con éxito!")

def menu():
    try:
        while True:
            opcion =int(input("""
    - Pulsa el número previo a la tarea que desea realizar:

        1) Escanear las redes a las que está conectada tu máquina.
        2) Escanear una dirección IP que introduzcas en un rango de puertos que desees.
        3) Generar archivo .txt con escaneo de la dirección IP que introduzcas en el rango de puertos que desees.
        4) Generar archivo .txt con escaneo de puertos comunes de la dirección IP que introduzcas.
        5) Salir del programa. :(
    """ + "\n"))

            print("\n")

            if opcion == 1:
                escanear_red()
            elif opcion == 2:
                ip, puertos_abiertos = escanear_ip()
            elif opcion == 3:
                ip, puertos_abiertos = escanear_ip()  # Escanea y obtiene la IP con los puertos abiertos
                generar_txt(ip, puertos_abiertos)
            elif opcion == 4:
                ip, puertos_abiertos = escaneo_comun(validar_ip(pedir_ip()))  # Escanea y obtiene la IP con los puertos abiertos
                generar_txt(ip, puertos_abiertos)
            elif opcion == 5:
                print(Fore.MAGENTA + Style.BRIGHT + ascii_art + "\n")
                print(Fore.MAGENTA + Style.BRIGHT + "Gracias por usar Scanet!" + Style.RESET_ALL+"\n")
                print("🔗 GitHub: https://github.com/daniescamilla"+"\n")
                break
    except KeyboardInterrupt:
        print(Fore.MAGENTA + Style.BRIGHT + ascii_art + "\n")
        print(Fore.MAGENTA + Style.BRIGHT + "Gracias por usar Scanet!" + Style.RESET_ALL+"\n")
        print("🔗 GitHub: https://github.com/daniescamilla"+"\n")
menu()