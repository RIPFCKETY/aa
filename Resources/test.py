import requests , re , socket
def get():           
           URLvless = 'https://raw.githubusercontent.com/yebekhe/TelegramV2rayCollector/main/sub/vless'
           ve = requests.get(URLvless, allow_redirects=True)
           open('VPD/proxy/vless.txt', 'wb').write(ve.content)
           URLreality = 'https://raw.githubusercontent.com/yebekhe/TelegramV2rayCollector/main/sub/reality'
           re = requests.get(URLreality, allow_redirects=True)
           open('VPD/proxy/reality.txt', 'wb').write(re.content)
           URLSo4 = 'https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks4.txt'
           so4 = requests.get(URLSo4, allow_redirects=True)
           open('VPD/proxy/socks4.txt', 'wb').write(so4.content)
           URLSo5 = 'https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks4.txt'
           so5 = requests.get(URLSo5, allow_redirects=True)
           open('VPD/proxy/socks5.txt', 'wb').write(so5.content)
           URLhttp= 'https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt'
           http = requests.get(URLhttp, allow_redirects=True)
           open('VPD/proxy/http.txt', 'wb').write(http.content)
           URLSo4_2= 'https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt'
           so4_2 = requests.get(URLSo4_2, allow_redirects=True)
           open('VPD/proxy/socks4_2.txt', 'wb').write(so4_2.content)
           URLSo5_2= 'https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt'
           so5_2 = requests.get(URLSo5_2, allow_redirects=True)
           open('VPD/proxy/socks5_2.txt', 'wb').write(so5_2.content)
           URLhttp2= 'https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt'
           http2 = requests.get(URLhttp2, allow_redirects=True)
           open('VPD/proxy/httpS.txt', 'wb').write(http2.content)
           URLhttp3= 'https://raw.githubusercontent.com/HyperBeats/proxy-list/main/https.txt'
           http3 = requests.get(URLhttp3, allow_redirects=True)
           open('VPD/proxy/httpS2.txt', 'wb').write(http3.content)
           URLSo4_3= 'https://raw.githubusercontent.com/HyperBeats/proxy-list/main/socks4.txt'
           so4_3 = requests.get(URLSo4_3, allow_redirects=True)
           open('VPD/proxy/socks4_3.txt', 'wb').write(so4_3.content)
           URLSo5_3= 'https://raw.githubusercontent.com/HyperBeats/proxy-list/main/socks5.txt'
           so5_3 = requests.get(URLSo5_3, allow_redirects=True)
           open('VPD/proxy/socks5_3.txt', 'wb').write(so5_3.content)
           URLAll= 'https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt'
           all = requests.get(URLAll, allow_redirects=True)
           open('VPD/proxy/all.txt', 'wb').write(all.content)
           URLSo4_4= 'https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/socks4/socks4.txt'
           so4_4 = requests.get(URLSo4_4, allow_redirects=True)
           open('VPD/proxy/socks4_4.txt', 'wb').write(so4_4.content)
           URLSo5_4= 'https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/socks5/socks5.txt'
           so5_4 = requests.get(URLSo5_4, allow_redirects=True)
           open('VPD/proxy/https3.txt', 'wb').write(so5_4.content)
           URLHttp4= 'https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/https/https.txt'
           Http4 = requests.get(URLHttp4, allow_redirects=True)
           open('VPD/proxy/Https4.txt', 'wb').write(Http4.content)
           URLHttp5= 'https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/http/http.txt'
           Http5 = requests.get(URLHttp5, allow_redirects=True)
           open('VPD/proxy/Https4.txt', 'wb').write(Http5.content)

get()
# URLSo4 = 'https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks4.txt'
# so4 = requests.get(URLSo4, allow_redirects=True)
# open('socks4.txt', 'wb').write(so4.content)
# from socket import error
# URLvless = 'https://raw.githubusercontent.com/yebekhe/TelegramV2rayCollector/main/sub/vless'
# r = requests.get(URLvless, allow_redirects=True)
# open('vless.txt', 'wb').write(r.content)
# URLreality = 'https://raw.githubusercontent.com/yebekhe/TelegramV2rayCollector/main/sub/reality'
# r = requests.get(URLreality, allow_redirects=True)
# open('reality.txt', 'wb').write(r.content)
# with open("vless.txt", "r") as file:
#                  listVLESS = file.readlines()
# with open("reality.txt", "r") as file:
#                  listREALITY = file.readlines()
# with open ("proxy.txt" , "a") as proxy:
#                          proxy.truncate(0)
# for item in listVLESS:
#                 match = re.search(r'@(.+):(\d+)', item)
#                 if match:
#                   ip = match.group(1)
#                   port = match.group(2)
#                   try:
#                      client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#                      client_socket.connect((ip, int(port)))
#                      client_socket.close()
#                      #await client.edit_message_text(message_id=call.message.id , chat_id=call.message.chat.id , text=f"𝐂𝐨𝐧𝐧𝐞𝐜𝐭𝐢𝐨𝐧 {ip}:{port} 𝐈𝐬 𝐎𝐤 ✅")
                     
#                      with open ("proxy.txt" , "a") as proxy: 
#                          proxy.write(ip+":"+port+"\n")
#                   except Exception as i :
#                      #await client.edit_message_text(message_id=call.message.id , chat_id=call.message.chat.id , text=f"𝐂𝐨𝐧𝐧𝐞𝐜𝐭𝐢𝐨𝐧 {ip}:{port} 𝐈𝐬 𝐍𝐨𝐭 𝐎𝐤 ❌")
#                      pass
# for item2 in listREALITY:
#                 match = re.search(r'@(.+):(\d+)', item2)
#                 if match:
#                   ip = match.group(1)
#                   port = match.group(2)
#                   try:
#                      client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#                      client_socket.connect((ip, int(port)))
#                      client_socket.close()
#                     # await client.edit_message_text(message_id=call.message.id , chat_id=call.message.chat.id , text=f"𝐂𝐨𝐧𝐧𝐞𝐜𝐭𝐢𝐨𝐧 {ip}:{port} 𝐈𝐬 𝐎𝐤 ✅")
#                      with open ("proxy.txt" , "a") as proxy:
#                          proxy.write(ip+":"+port+"\n")
#                   except Exception as i :
#                   #   await client.edit_message_text(message_id=call.message.id , chat_id=call.message.chat.id , text=f"𝐂𝐨𝐧𝐧𝐞𝐜𝐭𝐢𝐨𝐧 {ip}:{port} 𝐈𝐬 𝐍𝐨𝐭 𝐎𝐤 ❌")
#                      pass