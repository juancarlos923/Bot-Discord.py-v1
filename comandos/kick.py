@bot.command() #kick
async def kick(ctx, member : discord.Member=None, *, reason=None):
    if member is None:
        embed1 = discord.Embed(title="Mencione o Usuário Que Tomara Kick!", description="Ex.: !kick @user Motivo", timestamp=datetime.datetime.utcnow(), color=discord.Color.dark_blue())
        embed1.set_footer(text=f'Solicitado Por {ctx.author}')
        embed1.set_thumbnail(url="https://engenheirodecustos.com.br/wp-content/uploads/2019/02/Erro.jpeg")
        await ctx.send(embed=embed1)
        return
    if reason is None:
        reason = 'Não Informado'
    
    embed3 = discord.Embed(title=f"Você Tomou Kick do Servidor: {ctx.guild.name}", description=f"Motivo: {reason}", timestamp=datetime.datetime.utcnow(), color=discord.Color.dark_blue())
    embed3.set_footer(text=f'Kikado Por {ctx.author}')
    embed3.set_thumbnail(url="https://cliqueuniao.com.br/wp-content/uploads/2018/11/arbitro-580x335.jpg")
    await member.send(embed=embed3)
    
    await member.kick(reason=reason)#Ação de Kick
    
    embed2 = discord.Embed(title=f"Usuário(a) {member} Tomou Kick", description=f"Motivo: {reason}", timestamp=datetime.datetime.utcnow(), color=discord.Color.dark_blue())
    embed2.set_footer(text=f'Kikado Por {ctx.author}')
    embed2.set_thumbnail(url="https://cliqueuniao.com.br/wp-content/uploads/2018/11/arbitro-580x335.jpg")
    await ctx.send(embed=embed2)#Ação de Envio de Mensagem
    return
