from logging import exception
from logging import exception
import requests, colorama, secrets, random, threading, os
from httpx import Client
from httpx_socks import SyncProxyTransport
from hfuck import Bypass
from colorama import Fore, init, Style
from string import ascii_letters
from random import choice
import time             
import json

fingerprint = requests.get("https://discord.com/api/v9/experiments").json()['fingerprint']
cookie = requests.get("https://discord.com/register").headers['set-cookie']
sep = cookie.split(";")
sx = sep[0]
sx2 = sx.split("=")
dfc = sx2[1]
split = sep[6]
split2 = split.split(",")
split3 = split2[1]
split4 = split3.split("=")
sdc = split4[1]

with open('config.json') as config_file:
    data = json.load(config_file)

with open("name.txt", "r") as file:
    text = file.read()
    words = list(map(str, text.split()))

    print(random.choice(words)) 

invite = data['invite']
username = data['username']

tokens = open("tokens.txt", "a")
proxies = open("proxies.txt").read().splitlines()
genned = 0
bypassed = 0
maxThreads = 100000    
color = f"{Fore.CYAN}{Style.BRIGHT}"


os.system("cls & title Menu")
print(f"{Fore.LIGHTRED_EX}Tool Made By uuid#0002  &  ᴜʀ | ᴅᴀᴅᴅʏ#2678 ( it's a REMAKE )") 
print(f"""{Fore.LIGHTRED_EX}
 ▄▄▄▄    ▒█████  ▄▄▄█████▓▄▄▄█████▓ ██▓ ███▄    █   ▄████      ▄████ ▓█████  ███▄    █ 
▓█████▄ ▒██▒  ██▒▓  ██▒ ▓▒▓  ██▒ ▓▒▓██▒ ██ ▀█   █  ██▒ ▀█▒    ██▒ ▀█▒▓█   ▀  ██ ▀█   █ 
▒██▒ ▄██▒██░  ██▒▒ ▓██░ ▒░▒ ▓██░ ▒░▒██▒▓██  ▀█ ██▒▒██░▄▄▄░   ▒██░▄▄▄░▒███   ▓██  ▀█ ██▒
▒██░█▀  ▒██   ██░░ ▓██▓ ░ ░ ▓██▓ ░ ░██░▓██▒  ▐▌██▒░▓█  ██▓   ░▓█  ██▓▒▓█  ▄ ▓██▒  ▐▌██▒
░▓█  ▀█▓░ ████▓▒░  ▒██▒ ░   ▒██▒ ░ ░██░▒██░   ▓██░░▒▓███▀▒   ░▒▓███▀▒░▒████▒▒██░   ▓██░
░▒▓███▀▒░ ▒░▒░▒░   ▒ ░░     ▒ ░░   ░▓  ░ ▒░   ▒ ▒  ░▒   ▒     ░▒   ▒ ░░ ▒░ ░░ ▒░   ▒ ▒ 
▒░▒   ░   ░ ▒ ▒░     ░        ░     ▒ ░░ ░░   ░ ▒░  ░   ░      ░   ░  ░ ░  ░░ ░░   ░ ▒░
 ░    ░ ░ ░ ░ ▒    ░        ░       ▒ ░   ░   ░ ░ ░ ░   ░    ░ ░   ░    ░      ░   ░ ░ 
 ░          ░ ░                     ░           ░       ░          ░    ░  ░         ░ 
      ░                                                                                
""") 




# CONFIG #


def getProxy():
    return random.choice(proxies)

def rndstring(amount):
    return ''.join(choice(ascii_letters)for _ in range(amount))

def title():
    global genned, bypassed
    while True:
        os.system(f"title Generated: {genned} ^| Solved Captchas: {bypassed} ^| Invite: {invite} ^| Username: {username}")

thread = threading.Thread(target=title, args=(), daemon=True)
thread.start()

def createAccount(invite, username):
    global genned, bypassed
    bypassCaptcha = Bypass()
    bypassed += 1
    while True:
        try:
            with Client(transport=SyncProxyTransport.from_url(f'http://{getProxy()}')) as request:
                r = request.post("https://discord.com/api/v9/auth/register",
                                 headers = {"Accept": "*/*", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "en-US", "Content-Type": "application/json", "Origin": "https://discord.com/", "Host": "discord.com", "Authorization": "undefined", "Referer": "https://discord.com/register", "sec-ch-ua": "\"Google Chrome\";v=\"93\", \"Not; A Brand\";v=\"99\", \"Chromium\";v=\"93\"", "sec-ch-ua-mobile": "?1", "sec-ch-ua-platform": "\"Android\"", "sec-fetch-dest": "empty", "sec-fetch-mode": "cors", "sec-fetch-site": "same-origin", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36", "X-Debug-Options": "bugReporterEnabled", "X-Fingerprint": fingerprint, "X-Super-Properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6Iml0LUlUIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzkzLjAuNDU3Ny44MiBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiOTMuMC40NTc3LjgyIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjk5MDMxLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=="},
                                 json={"fingerprint": fingerprint,
                                       "username": random.choice(words),
                                       "email": f'{rndstring(6)}@gmail.com',
                                       "password": "f3ouhHDU3D.3S$A.3",
                                       "invite": "",
                                       "consent": True,
                                       "gift_code_sku_id": "",
                                       "captcha_key": bypassCaptcha}).json()
            tokens.write(f'{r["token"]}\n') 
            tokens.flush()
            genned += 1
            return r["token"]
        except Exception as e:
            try:
                proxies.remove(getProxy)
            except:
                pass
            pass
    
def start():
    print(f"{color}>{Fore.RESET} Created{color}:{Fore.RESET} {createAccount(invite, username)}")

for i in range(maxThreads):
    try:
        threading.Thread(target=start).start()
    except Exception as e:
        print(e)
        pass

    #pr
