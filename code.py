import urllib.request
import json
import time
from discord_webhook import DiscordWebhook

id="UCFPyFfzaO3U0XRG_DgnIjsw"

key="AIzaSyBR6YZQFmm3Wj2QWch1-r1QIbWenZwoIms"

x=0

while(x<1):
    
   data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&id="+id+"&key="+key).read()
   subsa=json.loads(data)["items"][0]["statistics"]["subscriberCount"]


   time.sleep(60)

   data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&id="+id+"&key="+key).read()
   subsb=json.loads(data)["items"][0]["statistics"]["subscriberCount"]

   if subsb>subsa:
      webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1083812337816973424/QolP3zaEzE-f62uq0WjwiUh6l6m3hOPMYVIAFG6lP6gkfihyw-jdXlHAbklf51VGSxOL', content='Your Youtube subscriber count increased by 1!')
      response = webhook.execute()
      print("Your subscriber count increased by 1!")
