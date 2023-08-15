from threading import Thread
from colorama import Fore
import requests
import json

with open('config.json') as config_file:
	config = json.load(config_file)


token = config ["token"]
webhook = config ["webhook_url"]
vanity_url = input ('Vanity URL : ')
guild_id = input ('Guild ID : ')

headers = {"authorization": token,
               "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}


def start():
	print(f"Hoşgeldin Yiğit. | Program Başlatılıyor ")


def change_vanity():
   payload = {"code": vanity_url}
   response = requests.patch(f"https://canary.discord.com/api/v9/guilds/{guild_id}/vanity-url", headers=headers, json=payload)
   if response.status_code == 200:
      print(f"succesfully sniped https://discord.gg/{vanity_url}")
      data = {"content" : f"succesfully sniped https://discord.gg/{vanity_url} @everyone"}
      requests.post(webhook, json=data)
   else:
      print(f"URL Alınamadı https://discord.gg/{vanity_url}")


def check_vanity():
   response = requests.get(f"https://canary.discord.com/api/v10/invites/{vanity_url}?with_counts=true&with_expiration=true", headers=headers)
   if response.status_code == 404:
      change_vanity()
      exit()
   else:
      print(f'Sniper Çalışıyor | Aktif URL : {vanity_url}')

start()

while True:
   check_vanity()



