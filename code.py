import urllib.request
import json
import time
from discord_webhook import DiscordWebhook
from discord import SyncWebhook

id="CHANNEL_ID"

key="YOUTUBE_API_KEY"

x=0

while(x<1):
    
   data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&id="+id+"&key="+key).read()
   subsa=json.loads(data)["items"][0]["statistics"]["subscriberCount"]
   print(subsa)
   
   time.sleep(60)

   data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&id="+id+"&key="+key).read()
   subsb=json.loads(data)["items"][0]["statistics"]["subscriberCount"]
   print(subsb)

   increase = int(subsb) - int(subsa)
   decrease = int(subsa) - int(subsb)
   
   if subsb>subsa:
      webhook = SyncWebhook.from_url("WEBHOOK_URL")
      webhook.send(f"Your Youtube subscriber count increased by {increase}")
      print("Your subscriber count increased by", increase)
   elif subsa>subsb:
     webhook = SyncWebhook.from_url("WEBHOOK_URL")
     webhook.send(f"Your Youtube subscriber count decreased by {decrease}")
     print("Your subscriber count decreased by", decrease)
