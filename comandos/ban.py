@bot.command() #ban
async def ban(ctx, member : discord.Member=None, *, reason=None):
    if member is None:
        embed1 = discord.Embed(title="Mencione o Usuário Que Tomara Ban!", description="Ex.: !ban @user Motivo", timestamp=datetime.datetime.utcnow(), color=discord.Color.dark_blue())
        embed1.set_footer(text=f'Solicitado Por {ctx.author}')
        embed1.set_thumbnail(url="https://engenheirodecustos.com.br/wp-content/uploads/2019/02/Erro.jpeg")
        await ctx.send(embed=embed1)
        return
    if reason is None:
        reason = 'Não Informado'
    
    embed3 = discord.Embed(title=f"Você Tomou Ban do Servidor: {ctx.guild.name}", description=f"Motivo: {reason}", timestamp=datetime.datetime.utcnow(), color=discord.Color.dark_blue())
    embed3.set_footer(text=f'Banido Por {ctx.author}')
    embed3.set_thumbnail(url="https://cliqueuniao.com.br/wp-content/uploads/2018/11/arbitro-580x335.jpg")
    await member.send(embed=embed3)
    
    await member.ban(reason=reason)#Ação de Ban
    
    embed2 = discord.Embed(title=f"Usuário(a) {member} Tomou Ban", description=f"Motivo: {reason}", timestamp=datetime.datetime.utcnow(), color=discord.Color.dark_blue())
    embed2.set_footer(text=f'Banido Por {ctx.author}')
    embed2.set_thumbnail(url="https://cliqueuniao.com.br/wp-content/uploads/2018/11/arbitro-580x335.jpg")
    await ctx.send(embed=embed2)#Ação de Envio de Mensagem
    return
