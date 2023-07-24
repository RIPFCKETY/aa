import requests
import re as rr

def get():
 try:
    URLs = [
        'https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks4.txt',
        'https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt',
        'https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt',
        'https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt',
        'https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt',
        'https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt',
        'https://raw.githubusercontent.com/HyperBeats/proxy-list/main/https.txt',
        'https://raw.githubusercontent.com/HyperBeats/proxy-list/main/socks4.txt',
        'https://raw.githubusercontent.com/HyperBeats/proxy-list/main/socks5.txt',
        'https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/socks4/socks4.txt',
        'https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/socks5/socks5.txt',
        'https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/https/https.txt',
        'https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/http/http.txt'
    ]

    for URL in URLs:
        response = requests.get(URL, allow_redirects=True)
        content = response.content.decode('utf-8')

        with open('VPD/proxy/proxy.txt', 'a', encoding='utf-8') as file:
            file.write(content + '\n')

        response = requests.get("https://raw.githubusercontent.com/yebekhe/TelegramV2rayCollector/main/sub/vless", allow_redirects=True)
        content = response.content.decode('utf-8')
        with open('VPD/proxy/vless.txt', 'a', encoding='utf-8') as file:
            file.write(content + '\n')
        response = requests.get("https://raw.githubusercontent.com/yebekhe/TelegramV2rayCollector/main/sub/reality", allow_redirects=True)
        content = response.content.decode('utf-8')
        with open('VPD/proxy/reality.txt', 'a', encoding='utf-8') as file:
            file.write(content + '\n')

    with open("VPD/proxy/vless.txt", "r", encoding='utf-8') as file:
        listvless = file.readlines()

    for item1 in listvless:
        match = rr.search(r'@(.+):(\d+)', item1)
        if match:
            ip = match.group(1)
            port = match.group(2)
            with open("VPD/proxy/proxy.txt", "a", encoding='utf-8') as file:
                file.write(ip + ":" + port + "\n")

    with open("VPD/proxy/reality.txt", "r", encoding='utf-8') as file:
        listreality = file.readlines()

    for item2 in listreality:
        match = rr.search(r'@(.+):(\d+)', item2)
        if match:
            ip = match.group(1)
            port = match.group(2)
            with open("VPD/proxy/proxy.txt", "a", encoding='utf-8') as file:
                file.write(ip + ":" + port + "\n")
    with open("VPD/proxy/all.txt", "r") as file: listall = file.readlines()
    formatted_list = ''.join(listall) 
    with open("VPD/proxy/proxy.txt", "a") as file: file.write(formatted_list)
 except:
     pass
 