import discord
import os
import requests
import json

client = discord.Client()
def get_quote():
  response = requests.get("http://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

@client.event
async def on_ready():
  print("we have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.starswith('$inspire'):
    await message.channel.send("Hello!")

client.run("TOKEN")


https://www.youtube.com/watch?v=SPTfmiYiuok
