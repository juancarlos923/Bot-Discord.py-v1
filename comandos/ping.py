@bot.command() #ping
async def ping(ctx):
  embed = discord.Embed(title="Meu Tempo de Resposta!", description=f"{round(bot.latency*1000)} ms", timestamp=datetime.datetime.utcnow(), color=discord.Color.dark_blue())
  embed.set_footer(text=f'Solicitado Por {ctx.author}')
  embed.set_thumbnail(url="https://media.tenor.com/images/b1c98908e2b1f6b2cdbad3ab98d60248/tenor.gif")
  await ctx.send(embed=embed)
