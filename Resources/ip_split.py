import socket 
from socket import error
from colorama import *

ip_list = ['5.135.136.60:9090', '172.232.54.30:80', '172.67.70.7:80', '43.155.81.198:1081', '109.254.67.104:9090', '178.62.88.10:80', '190.93.247.25:80', '43.153.52.178:443']

for ip in ip_list:
  ip_address, port = ip.split(':')

  try:
     client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     client_socket.connect((ip_address, int(port)))
     client_socket.close()
     print(Fore.GREEN + f"Connection {ip_address}:{port} Is Ok"+Fore.WHITE+"")
  except Exception as i :
     print(Fore.RED + f"Connection {ip_address}:{port} Is Not Ok")
     pass
