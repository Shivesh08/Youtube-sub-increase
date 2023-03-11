import urllib.request
import json
import time
from discord_webhook import DiscordWebhook

id="CHANNEL_ID"

key="YOUTUBE_API_KEY"

x=0

while(x<1):
    
   data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&id="+id+"&key="+key).read()
   subsa=json.loads(data)["items"][0]["statistics"]["subscriberCount"]


   time.sleep(60)

   data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&id="+id+"&key="+key).read()
   subsb=json.loads(data)["items"][0]["statistics"]["subscriberCount"]

   if subsb>subsa:
      webhook = DiscordWebhook(url='WEBHOOK_URL', content='Your Youtube subscriber count increased by 1!')
      response = webhook.execute()
      print("Your subscriber count increased by 1!")
