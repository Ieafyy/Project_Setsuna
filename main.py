import nacl
import discord
import youtube_dl
import ffmpeg
import random
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
from selenium import webdriver
import urllib
from selenium.webdriver.common.keys import Keys
import time
import os
import math
from pycotacao import get_exchange_rates, CurrencyCodes



bot = commands.Bot(command_prefix='#')
client = discord.Client()
comandos = [''] * 1000
respostas = [''] * 1000
i = 0
j = 0
comando = ''
text = ''
url = ''

navegador = webdriver.Firefox()

parametros ={
    'format': 'bestaudio/best',
    'outtmpl': '\musica.(ext)s',
    'postprocessors':[{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    
}

@client.event

async def on_message(bot):
    global i
    global j
    global comando
    global text
    global url
    if bot.author == client.user:
        return

    
    def check(message):
        try:
            int(message.content)
            return True
        except ValueError:
            return False

    
    if bot.content.startswith('#ola'):
        await bot.channel.send('Olá {}!'.format(client.get_user(bot.author.id)))
    
    
    if bot.content.startswith('#comando'): 
        await bot.channel.send('Como será chamado o comando?')
        comandos[i] = await client.wait_for('message')
        await bot.channel.send('Qual será minha resposta?')
        respostas[i] = await client.wait_for('message')
        await bot.channel.send('Ok!')
        i+=1
 
    elif bot.content.startswith('#sorteio'):
        await bot.channel.send('Escolha até que numero irá ser sorteado')
        esc1 = await client.wait_for('message')
        fim = int(esc1.content)
        num = random.randrange(1,fim)
        await bot.channel.send(num)

    elif bot.content.startswith('#trava'):
        await bot.channel.send('Digite um nome de um pokemon')
        poke = await client.wait_for('message')
        poke2 = ('{0.content}'.format(poke))
        pokelink = 'https://pokemondb.net/pokedex/'
        linkfinal = pokelink+poke2
        navegador.get(linkfinal) 
        if navegador.find_element_by_xpath("/html/body/div/div/div/p[2]/button") != 0:
            botao2 = navegador.find_element_by_xpath("/html/body/div/div/div/p[2]/button")
            botao2.click()
        with open ('pokemon.png','wb') as file:
            file.write(navegador.find_element_by_xpath('/html/body/main/div[3]/div[2]/div/div[1]/div[1]/p[1]/a/img').screenshot_as_png)
        await bot.channel.send(file=discord.File('pokemon.png'))


    elif bot.content.startswith('#musica '):
        pesq = str(bot.content)
        print(pesq)
        pesq = pesq[8:]
        navegador.get('https://www.youtube.com/results?search_query={}'.format(pesq))
        musica = navegador.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a/yt-formatted-string')
        musica.click()
        await bot.channel.send(navegador.current_url)
        await bot.channel.send('Download: https://www.snappea.com/pt/videoInfo?key={}'.format(navegador.current_url))   


    elif bot.content.startswith('#pokemon'):
        await bot.channel.send('Digite um nome de um pokemon')
        poke = await client.wait_for('message')
        poke2 = ('{0.content}'.format(poke))
        pokelink = 'https://pokemondb.net/pokedex/'
        linkfinal = pokelink+poke2
        navegador.get(linkfinal) 
        with open ('pokemon.png','wb') as file:
            file.write(navegador.find_element_by_xpath('/html/body/main/div[3]/div[2]/div/div[1]/div[1]/p[1]/a/img').screenshot_as_png)
        await bot.channel.send(file=discord.File('pokemon.png'))

    elif bot.content.startswith('mareep'):
         await bot.channel.send('🐑')
         
        
            
    elif bot.content.startswith('#pokedolar'):
        valorpd = str(get_exchange_rates(CurrencyCodes.USD))
        valorpd = valorpd[42:46]
        print(valorpd)
        linkpd = 'https://pokemondb.net/pokedex/'
        pokedexpd = valorpd[0] + valorpd[2] + valorpd[3]
        linkfpd = linkpd + pokedexpd
        navegador.get(linkfpd)
        with open ('pokedolar.png','wb') as file:
            file.write(navegador.find_element_by_xpath('/html/body/main/div[3]/div[2]/div/div[1]/div[1]/p[1]/a/img').screenshot_as_png)
        await bot.channel.send(file=discord.File('pokedolar.png'))
        namepd = navegador.find_element_by_xpath('/html/body/main/h1')
        namefpd = namepd.get_attribute('innerHTML')
        await bot.channel.send('O dolar está: {} referente ao pokemon: {}'.format(valorpd, namefpd))


    elif bot.content.startswith('#pokeeuro'):
        valorpe = str(get_exchange_rates(CurrencyCodes.EUR))
        valorpe = valorpe[42:46]
        linkpe = 'https://pokemondb.net/pokedex/'
        pokedexpe = valorpe[0] + valorpe[2] + valorpe[3]
        linkfpe = linkpe + pokedexpe
        navegador.get(linkfpe)
        with open ('pokeeuro.png','wb') as file:
            file.write(navegador.find_element_by_xpath('/html/body/main/div[3]/div[2]/div/div[1]/div[1]/p[1]/a/img').screenshot_as_png)
        await bot.channel.send(file=discord.File('pokeeuro.png'))
        namepe = navegador.find_element_by_xpath('/html/body/main/h1')
        namefpe = namepe.get_attribute('innerHTML')
        await bot.channel.send('O euro está: {} referente ao pokemon: {}'.format(valorpe, namefpe))

    elif bot.content.startswith('#pokelibra'):
        valorpl = str(get_exchange_rates(CurrencyCodes.GBP))
        linkpl = 'https://pokemondb.net/pokedex/'
        pokedexpl = valorpl[0] + valorpl[2] + valorpl[3]
        linkfpl = linkpl + pokedexpl
        navegador.get(linkfpl)
        with open ('pokelibra.png','wb') as file:
            file.write(navegador.find_element_by_xpath('/html/body/main/div[3]/div[2]/div/div[1]/div[1]/p[1]/a/img').screenshot_as_png)
        await bot.channel.send(file=discord.File('pokelibra.png'))
        namepl = navegador.find_element_by_xpath('/html/body/main/h1')
        namefpl = namepl.get_attribute('innerHTML')
        await bot.channel.send('A libra está: {} referente ao pokemon: {}'.format(valorpl, namefpl))
        

    elif bot.content.startswith('#segundograu'):
        await bot.channel.send('Digite o valor de A')
        a1 = await client.wait_for('message')
        a = float(a1.content)
        
        await bot.channel.send('Digite o valor de B')
        b1 = await client.wait_for('message')
        b = float(b1.content)
        
        await bot.channel.send('Digite o valor de C')
        c1 = await client.wait_for('message')
        c = float(c1.content)
        
        if a > 0:
            await bot.channel.send("Concavidade pra cima")

        if a < 0:
            await bot.channel.send("Concavidade pra baixo")


        xm = -b/(2*a)

        ym = a*xm*xm + xm*b + c

        await bot.channel.send("X máximo: {}".format(xm))
        await bot.channel.send("Y máximo: {}".format(ym)) 
        
        d = b*b - 4*a*c

        if d > 0:

            x1 = (-b + math.sqrt(d))/(2*a) 
            x2 = (-b - math.sqrt(d))/(2*a)

            await bot.channel.send("Delta = {}".format(d))
            await bot.channel.send("X1 = {}".format(x1))
            await bot.channel.send("X2 = {}".format(x2))
            
        if d < 0:

            await bot.channel.send("Delta = {}".format(d))
            await bot.channel.send("Não há raizes reais")

        if d == 0:

            await bot.channel.send("Delta = {}".format(d))
            x1 = (-b + math.sqrt(d))/(2*a)
            await bot.channel.send("X1 = {}".format(x1))


        await bot.channel.send("Corta o eixo Y em: {}".format(c))
        
        formula = "{}*x*x + {}*x + {}".format(a, b, c)

        
        navegador.get("https://www.mathe-fa.de/pt")
        barra = navegador.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/form/table/tbody/tr[3]/td/table/tbody/tr[2]/td/table/tbody/tr[1]/td[3]/input')
        barra.send_keys(formula)
        barra.send_keys(Keys.ENTER)
        
        time.sleep(2)
        
        with open ('graf.png','wb') as file:
            file.write(navegador.find_element_by_xpath('/html/body/p/img').screenshot_as_png)
           
        await bot.channel.send(file=discord.File('graf.png'))
        
        
        
    elif bot.content.startswith('#primeirograu'):
        await bot.channel.send('Digite o valor de A')
        a1 = await client.wait_for('message')
        a = float(a1.content)
        
        await bot.channel.send('Digite o valor de B')
        b1 = await client.wait_for('message')
        b = float(b1.content)
        
        if a > 0:
            await bot.channel.send("Função crescente")

        if a < 0:
            await bot.channel.send("Função decrescente")

        await bot.channel.send("Corta o eixo Y em: {}".format(b))
        
        x1 = -b/a
        
        await bot.channel.send("A raiz é: {}".format(x1))
        
        formula = "{}*x + {}".format(a, b)

        
        navegador.get("https://www.mathe-fa.de/pt")
        barra = navegador.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/form/table/tbody/tr[3]/td/table/tbody/tr[2]/td/table/tbody/tr[1]/td[3]/input')
        barra.send_keys(formula)
        barra.send_keys(Keys.ENTER)
        
        time.sleep(2)
        
        with open ('graf.png','wb') as file:
            file.write(navegador.find_element_by_xpath('/html/body/p/img').screenshot_as_png)
           
        await bot.channel.send(file=discord.File('graf.png'))
 

    else: 
        j = 0
        while j < i:
            if bot.content == ('{0.content}'.format(comandos[j])):
                await bot.channel.send('{0.content}'.format(respostas[j]))
                j = i
            else:
                j+=1



#bot.run('NzUxMzk4ODg1MTc1NTkwOTMy.X1Igvg.qT135tu0skSrjhHGkA-2inH2pgg')    
client.run('NzUxMzk4ODg1MTc1NTkwOTMy.X1Igvg.qT135tu0skSrjhHGkA-2inH2pgg')
#bot.content.startswith('*') 
