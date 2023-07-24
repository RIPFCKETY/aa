import socket , re
from socket import error
from colorama import *

with open("vless.txt", "r") as file:
    list = file.readlines()

for item in list:
    match = re.search(r'@(.+):(\d+)', item)
    if match:
        ip = match.group(1)
        port = match.group(2)
        try:
           client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
           client_socket.connect((ip, int(port)))
           client_socket.close()
           print(Fore.GREEN + f"Connection {ip}:{port} Is Ok"+Fore.WHITE+"")
        except Exception as i :
           print(Fore.RED + f"Connection {ip}:{port} Is Not Ok")
           pass
