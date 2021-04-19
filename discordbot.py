from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='(')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
@bot.command(name="こんにちは")
async def hello(ctx):
    await ctx.send(f"どうも、{ctx.message.author.name}さん！")

@bot.command(name="さようなら")
async def goodbye(ctx):
    await ctx.send(f"じゃあね、{ctx.message.author.name}さん！")
   
@bot.command(name="エリア")
async def ping(ctx):
    await ctx.send('https://cdn.discordapp.com/attachments/794486155214979104/806409875578945576/image0.png')

@bot.command(name="ポイント")
async def ping(ctx):
    await ctx.send('https://i.imgur.com/mqn2Z1C.jpg')

bot.run(token)
