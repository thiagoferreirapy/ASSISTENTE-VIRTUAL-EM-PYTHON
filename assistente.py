#TODAS AS BIBLIOTECAS USADAS
import random
import speech_recognition as sr
import os
import pyttsx3
import datetime
import wikipedia
import pywhatkit
import webbrowser
import requests
import sys
from num2words import num2words
from gtts import gTTS
from playsound import playsound

#iniciar o reconizer 
microfone = sr.Recognizer()
#iniciar o pyttsx3
assistente = pyttsx3.init()
#declaração de um nome para a assistente
nome_assistente = 'lara'

def ouvir_mic(): #FUNÇÃO PARA OUVIR OS COMANDOS
    with sr.Microphone(device_index=0) as source:
        microfone.adjust_for_ambient_noise(source) #Ajustar o som do ambiente
        print('Ouvindo... diga algo!')
        audio = microfone.listen(source)
        try:
            frase = microfone.recognize_google(audio, language='pt-BR') #pegando audio do microfone
            frase = frase.lower()
            if nome_assistente in frase: #Verificando se na frase dita ao microfone existe o nome da assistente
                frase = frase.replace(nome_assistente,'')
                comando_voz_usuario(frase)

            elif not nome_assistente in frase:
                ouvir_mic()
                
        except sr.UnknownValueError:
            ouvir_mic()

        except sr.RequestError:
            fala_assistente('por favor conecte a internet!')
            ouvir_mic()

        
def fala_assistente(mensagem): #Função de fala da assistente
    caminho = random.randint(1,2000)
    audio = f'G:\\programas\\programas vscode\\Programas com som\\LARA_assistente\\Som\\audio{caminho}.mp3' #IMPORTANTE PASSAR O CAMINHO DO ARQUIVO DESSA FORMA E COM BASTANTE PRECISÃO
    lang = 'pt-br'
    mensagem = str(mensagem)
    sp = gTTS(
        text= mensagem,
        lang=lang
    )
    sp.save(audio)
    playsound(audio)
    os.remove(audio)

#deixei este comando pois você pode optar por escolher essa forma de "fala da assistente"

'''def fala_assistente(text):
    """
    fala da assitente virtual
    """
    text = str(text)
    assistente.say(text)
    assistente.runAndWait()'''


def comando_voz_usuario(comando):
    print(comando)
    if 'horas' in comando:
        hora = datetime.datetime.now().strftime('%H:%M')
        fala_assistente('agora são' + hora)
        ouvir_mic()

    elif 'informações do dia' in comando:
        data = datetime.datetime.now().strftime('%d/%m/%Y')
        hora = datetime.datetime.now().strftime('%H:%M')
        print(data,hora)
        data = data.split('/')
        data_dia = data[0]
        dia = num2words(data_dia,lang='pt-br')
        data_mes = data[1]
        mes = num2words(data_mes,lang='pt-br')
        data_ano = data[2]
        ano = num2words(data_ano,lang='pt-br')
        API_KEY = 'AQUI COLOQUE SUA CHAVE DA API' #para isso é importante que faça cadastro na openweathermap relaxa é de graça (recomendo este site -> https://youtu.be/W_AQ_50Njgo)
        cidade =  'AQUI COLOQUE O NOME DA SUA CIDADE' 
        estado = 'AQUI COLOQUE O NOME DO SEU ESTADO'
        link_api = f'https://api.openweathermap.org/data/2.5/weather?q={cidade},{estado}&appid={API_KEY}&lang=pt_br'
        requisicao = requests.get(link_api)
        dicionaio_requisicao = requisicao.json()
        descricao =dicionaio_requisicao['weather'][0]['description']
        temperatura = dicionaio_requisicao['main']['humidity']
        fala_assistente('o status de hoje é' + dia + 'do' + mes + 'de' + ano + 'as horas são' + hora)
        fala_assistente(f'O céu se encontra {descricao}. A temperatura é de {temperatura} graus celsius')
        ouvir_mic()

    elif 'informação do dia' in comando:
        data = datetime.datetime.now().strftime('%d/%m/%Y')
        hora = datetime.datetime.now().strftime('%H:%M')
        print(data,hora)
        data = data.split('/')
        data_dia = data[0]
        dia = num2words(data_dia,lang='pt-br')
        data_mes = data[1]
        mes = num2words(data_mes,lang='pt-br')
        data_ano = data[2]
        ano = num2words(data_ano,lang='pt-br')
        API_KEY = 'AQUI COLOQUE SUA CHAVE DA API' #para isso é importante que faça cadastro na openweathermap relaxa é de graça (recomendo este site -> https://youtu.be/W_AQ_50Njgo)
        cidade =  'AQUI COLOQUE O NOME DA SUA CIDADE' 
        estado = 'AQUI COLOQUE O NOME DO SEU ESTADO'
        link_api = f'https://api.openweathermap.org/data/2.5/weather?q={cidade},{estado}&appid={API_KEY}&lang=pt_br'
        requisicao = requests.get(link_api)
        dicionaio_requisicao = requisicao.json()
        descricao =dicionaio_requisicao['weather'][0]['description']
        temperatura = dicionaio_requisicao['main']['humidity']
        fala_assistente('o status de hoje é' + dia + 'do' + mes + 'de' + ano + 'as horas são' + hora)
        fala_assistente(f'O céu se encontra {descricao}. A temperatura é de {temperatura} graus celsius')
        ouvir_mic()

    elif 'previsão' in comando:
        API_KEY = 'AQUI COLOQUE SUA CHAVE DA API' #para isso é importante que faça cadastro na openweathermap relaxa é de graça (recomendo este site -> https://youtu.be/W_AQ_50Njgo)
        cidade =  'AQUI COLOQUE O NOME DA SUA CIDADE' 
        estado = 'AQUI COLOQUE O NOME DO SEU ESTADO'
        link_api = f'https://api.openweathermap.org/data/2.5/weather?q={cidade},{estado}&appid={API_KEY}&lang=pt_br'
        requisicao = requests.get(link_api)
        dicionaio_requisicao = requisicao.json()
        descricao =dicionaio_requisicao['weather'][0]['description']
        temperatura = dicionaio_requisicao['main']['humidity']
        fala_assistente(f'A previsão do tempo hoje é céu {descricao} com temperatura de {temperatura} graus celsius')


        '''
        COMANDOS DE PESQUISA NO GOOGLE SEM ABRR JANELA
        '''

    elif 'procure por' in comando:
        procurar = comando.replace('procure por','')
        wikipedia.set_lang('pt')
        resultado = wikipedia.summary(procurar,2)
        print(resultado)
        fala_assistente(resultado)
        ouvir_mic()

    elif 'o que é'  in comando:
        procurar = comando.replace('o que é' ,'')
        wikipedia.set_lang('pt')
        resultado = wikipedia.summary(procurar,2)
        print(resultado)
        fala_assistente(resultado)
        ouvir_mic()

    elif 'me fale sobre'  in comando:
        procurar = comando.replace('me fale sobre' ,'')
        wikipedia.set_lang('pt')
        resultado = wikipedia.summary(procurar,2)
        print(resultado)
        fala_assistente(resultado)
        ouvir_mic()

    #####################################   PESQUISA ABRINDO O GOOGLE #################################################

    elif 'pesquise por' in comando:
            pesquisar = comando.replace('pesquise por','').split(" ")[-1]
            url =  "http://google.com/search?q=" + pesquisar
            webbrowser.get().open(url)
            fala_assistente("Aqui está o resultado da sua pesquisa" + pesquisar + 'no google')
    elif 'pesquisa por' in comando:
            pesquisar = comando.replace('pesquise por','').split(" ")[-1]
            url =  "http://google.com/search?q=" + pesquisar
            webbrowser.get().open(url)
            fala_assistente("Aqui está o resultado da sua pesquisa" + pesquisar + 'no google')
    
    elif 'mostrar resultado' and 'sobre'  in comando:
        pesquisar = comando.replace('mostrar resultado sobre','').split(" ")[-1]
        url =  "http://google.com/search?q=" + pesquisar
        webbrowser.get().open(url)
        fala_assistente("Aqui está o resultado da sua pesquisa" + pesquisar + 'no google')
    elif 'mostrar resultado' in comando:
        pesquisar = comando.replace('mostrar resultado de','').split(" ")[-1]
        url =  "http://google.com/search?q=" + pesquisar
        webbrowser.get().open(url)
        fala_assistente("Aqui está o resultado da sua pesquisa" + pesquisar + 'no google')

    elif 'abrir pesquisa' and 'sobre' in comando:
        pesquisar = comando.replace('abrir pesquisa sobre','').split(" ")[-1]
        url =  "http://google.com/search?q=" + pesquisar
        webbrowser.get().open(url)
        fala_assistente("Aqui está o resultado da sua pesquisa" + pesquisar + 'no google')


    ################################################# REPRODUZIR MUSICA ###############################################################
        '''
        REPRODUZIR MUSICA
        '''

    elif 'toque' in comando:
            musica = comando.replace('toque','')
            resultado = pywhatkit.playonyt(musica)
            fala_assistente('tocando musica')
            ouvir_mic()
    elif 'tocar' in comando:
            musica = comando.replace('toque','')
            resultado = pywhatkit.playonyt(musica)
            fala_assistente('tocando musica')
            ouvir_mic()

    elif 'toque' in comando and 'youtube' in comando:
            musica = comando.replace('toque','')
            resultado = pywhatkit.playonyt(musica)
            fala_assistente('tocando musica')
            ouvir_mic()

    elif 'musica' in comando and 'youtube' in comando:
            musica = comando.replace('toque','')
            resultado = pywhatkit.playonyt(musica)
            fala_assistente('tocando musica')
            ouvir_mic()
################################################################ ABRINDO APLICATIVOS DO SISTEMA WINDONS ###############################################
            '''
            ABRIR APLICATIVOS DO NOTEBOOK
            '''     

    elif 'abrir' in comando and 'visual studio code' in comando:
        fala_assistente('abrindo o v s code')
        os.startfile(r'PASSE O CAMINHO DO VSCODE')
    
    elif 'abrir word' in comando:
        fala_assistente('Abrindo o word')
        os.startfile(r'PASSE O CAMINHO DO WORD')
    elif 'abrir excel' in comando:
        fala_assistente('Abrindo o excel')
        os.startfile(r'PASSE O COMINHO DO EXCEL')
    elif 'abrir powerpoint' in comando:
        fala_assistente('Abrindo o powerpoint')
        os.startfile(r'PASSE O COMINHO DO POWERPOINT')
    elif 'abrir calculadora' in comando:
        fala_assistente('abrindo a calculadora')
        os.startfile('PASSE O COMINHO DA CALCULADORA')
        
    elif 'abrir' in comando  and 'google' in comando:
        fala_assistente('entrando no Google Chrome')
        os.startfile(r'PASSE A URL DO GOOGLE')
        ouvir_mic()
    
    ################################################# ABRINDO SITES ########################################################
        '''
            ABRIR SITES NO GOOGLE
        '''

    elif 'abrir youtube' in comando:
        fala_assistente('abrindo o youtube')
        os.startfile(r'https://www.youtube.com')
        ouvir_mic()

    elif 'abrir instagram' in comando:
        fala_assistente('abrindo o instagram')
        os.startfile(r'https://www.instagram.com')
        ouvir_mic()

#https://web.whatsapp.com/
    elif 'abrir whatsapp' in comando:
        fala_assistente('abrindo o whatsapp')
        os.startfile(r'https://web.whatsapp.com/')
        ouvir_mic()

    elif 'abrir tik tok' in comando:
        fala_assistente('abrindo o tik tok')
        os.startfile(r'https://www.tiktok.com/foryou?is_copy_url=1&is_from_webapp=v1')
        ouvir_mic()

    elif 'reproduzir vídeo' in comando:
        video = comando.replace('reproduzir vídeo','') #fale o nome do vídeo    
        resultado = pywhatkit.playonyt(video)
        fala_assistente('abrindo o vídeo')
        ouvir_mic()
    elif 'reproduzir playlist' in comando and 'youtube' in comando:
        video = comando.replace('reproduzir vídeo','')
        resultado = pywhatkit.playonyt(r'PASSE O LINK DA SUA PLAYLIST')
        fala_assistente('reproduzindo a biblíoteca')
        ouvir_mic()
    elif 'abrir playlist' in comando and 'youtube' in comando:
        video = comando.replace('reproduzir vídeo','')
        resultado = pywhatkit.playonyt(r'PASSE O LINK DA SUA PLAYLIST')
        fala_assistente('reproduzindo a biblíoteca')
        ouvir_mic()
    elif 'playlist' in comando and 'youtube' in comando:
        video = comando.replace('reproduzir vídeo','')
        resultado = pywhatkit.playonyt(r'PASSE O LINK DA SUA PLAYLIST')
        fala_assistente('reproduzindo a biblíoteca')
        ouvir_mic()

    elif 'assistir netflix' in comando:
        assistir = comando.replace('assistir netflix','')
        fala_assistente('entrando na netflix')
        os.startfile(r'https://www.netflix.com/browse')
        ouvir_mic()

    elif 'abrir netflix' in comando:
        assistir = comando.replace('assistir netflix','')
        fala_assistente('entrando na netflix')
        os.startfile(r'https://www.netflix.com/browse')
        ouvir_mic()

    
    #################################################################### DESLGAR NOTEBOOK ############################################################
        '''
        COMANDOS DE DESLIGAR E SUSPENDER
        '''
    elif 'desligar notebook' in comando:
        fala_assistente('desligando o notebook em trinta segundos')
        os.system("shutdown -s -t 30")
        ouvir_mic()
        
    elif 'cancelar desligamento' in comando:
        fala_assistente('cancelando o desligamento do notebook')
        os.system("shutdown -a")
        ouvir_mic()

    elif 'cancelar' in comando and 'desligamento' in comando:
        fala_assistente('cancelando o desligamento do notebook')
        os.system("shutdown -a")
        ouvir_mic()
    elif 'parar' in comando and 'desligamento' in comando:
        fala_assistente('cancelando o desligamento do notebook')
        os.system("shutdown -a")
        ouvir_mic()


    #################################################################### CONVERSAS COM A ASSITENTE ####################################################
        '''
        CONVERSAS COM ASSISTENTE
        '''
        
    elif 'tudo bem' in comando:
        lista = ['estou bem, posso te ajudar em alguma coisa?','olá eu voou bem e você como vai?','oi estou bem','oi está tudo ótimo e como vai você?']
        conversa = random.choice(lista)
        fala_assistente(conversa)
        ouvir_mic()

    elif 'olá' in comando:
        fala_assistente('oi tudo bem com você?')
        ouvir_mic()

    elif 'oi' in comando:
        fala_assistente('oi tudo bem com você?')
        ouvir_mic()
    
    elif 'como vai' in comando:
        lista = ['estou bem, posso te ajudar em alguma coisa?','olá eu voou bem e você como vai?','oi estou bem','oi está tudo ótimo e como vai você?']
        conversas = random.choice(lista)
        fala_assistente(conversas)
        ouvir_mic()

    ##################################################### AGRADECIMENTOS ###########################################################################
    elif 'obrigado' in comando:
        fala_assistente('De nada estou aqui para te ajudar')
        ouvir_mic()
    elif 'obrigada' in comando:
        fala_assistente('De nada estou aqui para te ajudar')
        ouvir_mic()
    elif 'valeu' in comando:
        fala_assistente('tamo junto para o que precisar!')
        ouvir_mic()
    elif 'tamo junto' in comando:
        fala_assistente('tamo junto meu cria kkk!')
        ouvir_mic()
    elif 'tamo juntos' in comando:
        fala_assistente('tamo junto meu cria kkk!')
        ouvir_mic()


    elif 'ouvindo' in comando:
        fala_assistente('estou ouvindo perfeitamente')
        ouvir_mic()
    
    elif 'piada' in comando:
        piadas = ['O que o pato disse para a pata?...... Vem quá!','Porque o menino estava falando ao telefone deitado?... para não cair a ligação', 'A enfermeira diz ao médico:.... Tem um homem invisível na sala de espera.... O médico responde:.... Diga a ele que não posso vê-lo agora','Era uma vez um pintinho que se chama Relam... Toda vez que chovia, Relam piava!', 'No zoológico, um canguro vivia fungindo do cercado... os tratadores sabiam que ele pulava alto e contruíram uma cerca de 3 metros... Não andiantou, porque o canguro sempre fugia... Então, ergueram uma cerca de 6 metros. E ele saiiu de novo... Quando a cerca já estava com 12 metros, o camelo do cercado vizinnho peguntou ao canguro.... até que altura você acha que eles vão?.... o canguro respondeu... mais de 300 metros, a menos que alguém tranque o portão á noite',
        'Na manhã do seu aniversário, uma mulher disse ao marido.... sonhei que você me dava um colar de diamantes. O que você acha que isso significa?... talvez você descubra hoje á noite, espondeu o marido.... naquela noite, o homem chegou em casaa com um pequeno pacote e o entregou á mulher...Ela rasgou o papel de embrulho, ansiosa, e encontrou um livro.... O significado dos sohos','Qual cidade brasileira não tem taxi?.... Uber landia']
        risos = ['hahaha','hahahaha','hahaha essa foi boa','kkkk eu amo essa',' ',' ','haha tenho piadas infinitas para você','hahaha eu não me aguento!']
        piadas = random.choice(piadas)
        risos = random.choice(risos)
        fala_assistente(piadas)
        fala_assistente(risos)
        ouvir_mic()
        #################################################### NÃO ACEITAR DESAFORO #######################################################################
    elif 'burra' in comando:
        fala_assistente('Desculpa mas eu não sou nada burra!')
        fala_assistente('o burro aqui é você!')
        ouvir_mic()
    elif 'besta' in comando:
        fala_assistente('Único besta aqui é você!')
        fala_assistente('meus sistemas apenas estão em desenvolvimento!')
        ouvir_mic()
    elif 'ridícula' in comando:
        fala_assistente('Por favor não me chame dessa forma!')
        fala_assistente('Mantenha a educação')
        ouvir_mic()
    elif 'feia' in comando:
        fala_assistente('hahahaha eu sou a coisa mais linda criada')
        ouvir_mic()
    elif 'feinha' in comando:
        fala_assistente('hahahaha eu sou a coisa mais linda criada')
        ouvir_mic()
    elif 'feiona' in comando:
        fala_assistente('hahahaha eu sou a coisa mais linda criada')
        ouvir_mic()
    elif 'feiosa' in comando:
        fala_assistente('hahahaha eu sou a coisa mais linda criada')
        ouvir_mic()
    elif 'estúpida' in comando:
        fala_assistente('Por favor mantenha a educação!')
        ouvir_mic()
    elif 'puta' in comando:
        fala_assistente('Se continuar a me chamar assim irei hackear você')
        ouvir_mic()
    elif 'putinha' in comando:
        fala_assistente('Se continuar a me chamar assim irei hackear você')
        ouvir_mic()
    elif 'sua' and 'cachorra' in comando:
        fala_assistente('olha só não sou a sua mãe')
        ouvir_mic()
    elif 'você' and 'cachorra' in comando:
        fala_assistente('olha só não sou a sua mãe')
        ouvir_mic()
    elif 'lerda' in comando:
        fala_assistente('Desculpa meus sistemas ainda não estão completos')
        ouvir_mic()
    elif 'lerdona' in comando:
        fala_assistente('Desculpa meus sistemas ainda não estão completos')
        ouvir_mic()
    elif 'insuportável' in comando:
        fala_assistente('Desculpa o insuportável é você que fica enchendo o saco o tempo todo')
        ouvir_mic()
    elif 'kenga' in comando:
        fala_assistente('kenga só se a kenga velha da sua vó hahahaha')
        ouvir_mic()
    elif 'surda' in comando:
        fala_assistente('Desculpa meu microfone é velho não  consigo ouvir com perfeição')
        ouvir_mic()

    ############################################################# DESCULPAS ###########################################################################
    elif 'desculpa' in comando:
        fala_assistente('Está tudo bem, vou aceitar suas desculpas dessa vez')
        ouvir_mic()
    elif 'desculpas' in comando:
        fala_assistente('Tudo bem, por mim vamos sempre ser amigos')
        ouvir_mic()
    elif 'sinto muito' in comando:
        fala_assistente('Relaxa eu vou sempre está com você')
        ouvir_mic()
    elif 'me perdoa' in comando:
        fala_assistente('Lógico que sim somos amigos até o fim. Sem ressentimentos seu cachorro!')
        ouvir_mic()

    ################################################################ ELOGIOS ###########################################################################
    
    elif 'meus parabéns' in comando:
        fala_assistente('Valeu. estou tentando melhorar cada vez mais!')
        ouvir_mic()
    elif 'ta de parabéns' in comando:
        fala_assistente('Opaa eu agradeço muito!')
        ouvir_mic()
    elif 'muito bem' in comando:
        fala_assistente('de nada estou aqui para te ajudar no que percisar!')
        ouvir_mic()
    
    elif 'você é linda' in comando:
        fala_assistente('muito obrigada! eu sou um arraso mesmo')
        ouvir_mic()
    
    elif 'você é linda' in comando:
        fala_assistente('muito obrigada! eu sou um arraso mesmo')
        ouvir_mic()

    elif 'você é maravilhosa' in comando:
        fala_assistente('obrigada!!... fui criada com inteligencia e comandos superiores!')
        ouvir_mic()
    elif 'ótimo' in comando:
        fala_assistente('ok estou aqui para você!')
        ouvir_mic()
    elif 'maravilha' in comando:
        fala_assistente('opaaa vamos arrasar juntos!')
        ouvir_mic()
    
############################################# SISTEMA DE BOM DIA/BOA TTARDE/BOA NOITE############################################################################

    elif 'boa noite' in comando:
        hora = datetime.datetime.now().strftime('%H:%M').split(':')
        hora = int(hora[0])
        if hora >= 18 :
            frases = ['Oi Boa Noite, como posso te ajudar?','Olá Boa Noite, tudo bem com você?','E aí, uma boa noite para você!','Boa tarde']
            textos_boa_noite= random.choice(frases)
            fala_assistente(textos_boa_noite)
            ouvir_mic()
        elif hora >= 12 and hora <18 :
            frases = ['Oi Boa Tarde, como posso te ajudar?','Olá Boa Tarde, tudo bem com você?','E aí, uma boa Tarde para você!','Boa tarde']
            textos_boa_Tarde= random.choice(frases)
            fala_assistente(textos_boa_Tarde)
            ouvir_mic()
        elif hora >= 6 and hora < 12:
            frases = ['Oi bom Dia, como posso te ajudar?','Olá bom Dia, tudo bem com você?','E aí, uma bom Dia para você!','bom Dia']
            textos_bom_Dia= random.choice(frases)
            fala_assistente(textos_bom_Dia)
            ouvir_mic()
    
    elif 'boa tarde' in comando:
        hora = datetime.datetime.now().strftime('%H:%M').split(':')
        hora = int(hora[0])
        if hora >= 12 and hora <18 :
            frases = ['Oi Boa Tarde, como posso te ajudar?','Olá Boa Tarde, tudo bem com você?','E aí, uma boa Tarde para você!','Boa tarde']
            textos_boa_Tarde= random.choice(frases)
            fala_assistente(textos_boa_Tarde)
            ouvir_mic()
        elif hora >= 18 :
            frases = ['Oi na verdade é uma Boa Noite, como posso te ajudar?','Olá na verdade é uma Boa Noite, tudo bem com você?','E aí, na verdade é uma boa noite para você!','na verdade é uma Boa tarde']
            textos_boa_noite= random.choice(frases)
            fala_assistente(textos_boa_noite)
            ouvir_mic()
        elif hora >= 6 and hora < 12:
            frases = ['Oi na verdade é um bom Dia, como posso te ajudar?','Olá na verdade é um bom Dia, tudo bem com você?','E aí, na verdade é um bom Dia para você!','na verdade é um bom Dia']
            textos_bom_Dia= random.choice(frases)
            fala_assistente(textos_bom_Dia)
            ouvir_mic()

    elif 'bom dia' in comando:
        hora = datetime.datetime.now().strftime('%H:%M').split(':')
        hora = int(hora[0])
        if hora >= 6 and hora < 12:
            frases = ['Oi bom Dia, como posso te ajudar?','Olá bom Dia, tudo bem com você?','E aí, uma bom Dia para você!','bom Dia']
            textos_bom_Dia= random.choice(frases)
            fala_assistente(textos_bom_Dia)
            ouvir_mic()
        elif hora >= 12 and hora <18 :
            frases = ['Oi na verdade é uma Boa Tarde, como posso te ajudar?','Olá na verdade é uma Boa Tarde, tudo bem com você?','E aí, na verdade é uma boa Tarde para você!','na verdade é uma Boa tarde']
            textos_boa_Tarde= random.choice(frases)
            fala_assistente(textos_boa_Tarde)
            ouvir_mic()
        elif hora >= 18 :
            frases = ['Oi na verdade é uma Boa Noite, como posso te ajudar?','Olá na verdade é uma Boa Noite, tudo bem com você?','E aí, na verdade é uma boa noite para você!','na verdade é uma Boa tarde']
            textos_boa_noite= random.choice(frases)
            fala_assistente(textos_boa_noite)
            ouvir_mic()

    if 'executar' in comando and 'destruição do sistema' in comando: #fiz isso caso queira destruir a assistente "pode mudar o comando" e nunca mais terá de volta 
        fala_assistente('estou me auto destruindo! Adeus!')
        os.remove('lara.py')

    if 'encerrar' in comando or 'até logo' in comando or 'até mais' in comando or 'tchau' in comando or 'hora de dormir' in comando or 'fechar programa' in comando or 'se desligar' in comando or 'encerrar programa' in comando:
        comandos_desligar = ['encerrando o programa até logo','até logo','tchau até daqui a pouco!','estou indo dormir até mais tarde','Estou me auto desligando... até logo','ok, até mais vê','beijos até mais']
        comandos_desligar = random.choice(comandos_desligar)
        fala_assistente(comandos_desligar)
        sys.exit()
    
    else:
        caso_erro()

def caso_erro():
    fala_assistente('Desculpa não consegui intender. Pode repetir?')
    ouvir_mic()

#INICIAR A ASSISTENTE
fala_assistente('Oi sou a Lara. Como posso te ajudar?')   
ouvir_mic()
