@bot.command() #unban
async def unban(ctx, *, member=None):
    if member is None:
        embed1 = discord.Embed(title="Mencione o Usuário Que Tomara Unban!", description="Ex.: !unban @user", timestamp=datetime.datetime.utcnow(), color=discord.Color.dark_blue())
        embed1.set_footer(text=f'Solicitado Por {ctx.author}')
        embed1.set_thumbnail(url="https://engenheirodecustos.com.br/wp-content/uploads/2019/02/Erro.jpeg")
        await ctx.send(embed=embed1)
        return

    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            embed2 = discord.Embed(title=f"Usuário(a) {member} Tomou Unban", description=f"Desbanido Por {ctx.author}", timestamp=datetime.datetime.utcnow(), color=discord.Color.dark_blue())
            embed2.set_thumbnail(url="https://media1.giphy.com/media/21Q0iTg8c1tabEcIBe/giphy.gif")
            await ctx.send(embed=embed2)#Ação de Envio de Mensagem
            return
