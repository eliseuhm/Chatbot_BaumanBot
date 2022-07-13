import requests
import time
import json
import os
import random
 
 
class TelegramBot:
    def __init__(self):
        token = 'MEUTOKENAQUI'
        self.url_base = f"https://api.telegram.org/bot{token}/"
 
    def Iniciar(self):
        update_id = None
        while True:
            atualizacao = self.obter_novas_mensagens(update_id)
            dados = atualizacao['result']
            if dados:
                for dado in dados:
                    update_id = dado['update_id']
                    mensagem = str(dado['message']['text'])
                    chat_id = dado["message"]["from"]["id"]
                    eh_primeira_mensagem = int(
                        dado["message"]["message_id"]) == 1
                    resposta = self.criar_resposta(mensagem,
                                                   eh_primeira_mensagem)
                    self.responder(resposta, chat_id)
 
    # Obter mensagens
    def obter_novas_mensagens(self, update_id):
        link_requisicao = f'{self.url_base}getUpdates?timeout=100'
        if update_id:
            link_requisicao = f'{link_requisicao}&offset={update_id + 1}'
        resultado = requests.get(link_requisicao)
        return json.loads(resultado.content)
 
    # Criar uma resposta
    def criar_resposta(self, mensagem, eh_primeira_mensagem):
        if eh_primeira_mensagem == True or mensagem in ('oi', 'Oi'):
            list5 = [f'''Olá, você provavelmente nem deveria estar aqui. Tudo é mais fácil na vida virtual, mas perdemos a arte das relações sociais e da amizade.{os.linesep}\n Ainda quer ficar por aqui? Responda: quero{os.linesep}\n Não entende? Responda: negativo{os.linesep}\n Vá, e viva uma vida que realmente tenha valor. Responda: certo''',
                     f'''Olá, estimada pessoa.\n Você sabe que vivemos tempos líquidos, nada realmente é para durar.{os.linesep}\n Ainda quer ficar por aqui? Responda: quero{os.linesep}\n Não entende? Responda: negativo{os.linesep}\n Vá, e viva uma vida que realmente tenha valor. Responda: certo''',
                     f'''Não posso dizer que é bom ver-te num mensageiro eletrônico, mas já que na era da informação, a invisibilidade é equivalente à morte, digo-te: Olá!{os.linesep}\n Ainda quer ficar por aqui? Responda: quero{os.linesep}\n Não entende? Responda: negativo{os.linesep}\n Vá, e viva uma vida que realmente tenha valor. Responda: certo''',
                     f'''Bem vindo ao lar, Ser das cinzas. Fale o desejo do seu coração.{os.linesep}\n Ainda quer ficar por aqui? Responda: quero{os.linesep}\n Não entende? Responda: negativo{os.linesep}\n Vá, e viva uma vida que realmente tenha valor. Responda: certo''',
                     f'''Ser das cinzas, o que há de errado?{os.linesep}\n Ainda quer ficar por aqui? Responda: quero{os.linesep}\n Não entende? Responda: negativo{os.linesep}\n Vá, e viva uma vida que realmente tenha valor. Responda: certo''']
            item5 = random.choice(list5)
            return item5
        if mensagem.lower() in ('quero', 'Quero', 'QUERO'):
            list4 = [f'''Então esquecerá o amor, a amizade, os sentimentos, o trabalho bem feito. O que se encontra aqui, o tempo perdido, são apenas sedativos morais que tranquilizam seus escrúpulos éticos{os.linesep}\n Entende isso? Responda: sim ou não
            ''',
                     f'''Vivemos tempos líquidos. Nada é para durar.{os.linesep}\n Entende isso? Responda: sim ou não''',
                     f'''Nenhuma sociedade que esquece a arte de questionar pode esperar encontrar respostas para os problemas que a afligem.{os.linesep}\n Entende isso? Responda: sim ou não''',
                     f'''Os tempos são líquidos porque, assim como a água, tudo muda muito rapidamente. Na sociedade contemporânea, nada é feito para durar.{os.linesep}\n Entende isso? Responda: sim ou não''',
                     f'''A vida é muito maior que a soma de seus momentos.{os.linesep}\n Entende isso? Responda: sim ou não''']
            item4 = random.choice(list4)
            return item4
 
        elif mensagem.lower() in ('negativo', 'Negativo', 'NEGATIVO'):
            list3 = [f'''Os grupos de amigos ou as comunidades de bairro não te aceitam sem dar razão, mas ser membro de um grupo no Instagram, WhatsApp ou Telegram é facílimo. Você pode ter mais de 5000 contatos sem sair de casa, você aperta um botão e pronto.{os.linesep}\n Triste, não é mesmo? Responda: sim ou não
            ''',
                     f'''A preocupação com a administração da vida parece distanciar o ser humano da reflexão moral.{os.linesep}\n Triste, não é mesmo? Responda: sim ou não''',
                     f'''Hoje, o medo da exposição foi abafado pela alegria de ser notado.{os.linesep}\n Triste, não é mesmo? Responda: sim ou não''',
                     f'''Loucos são apenas os significados não compartilhados. A loucura não é loucura quando compartilhada.{os.linesep}\n Triste, não é mesmo? Responda: sim ou não''',
                     f'''A incerteza foi sempre o chão familiar da escolha.{os.linesep}\n Triste, não é mesmo? Responda: sim ou não''']
            item3 = random.choice(list3)
            return item3
 
        elif mensagem.lower() in ('certo', 'Certo', 'CERTO'):
            list2 = [f'''Até logo, e lembre que as redes sociais são uma armadilha.{os.linesep}\n Foi o suficiente, não foi? Responda: sim ou não''',
                     f'''Como se pode lutar contra as adversidades do destino sozinho, sem a ajuda de amigos fiéis e dedicados, sem um companheiro de vida, pronto para compartilhar os altos e baixos?{os.linesep}\n Foi o suficiente, não foi? Responda: sim ou não''',
                     f'''A incapacidade de escolher entre atração e repulsão, entre esperanças e temores, redunda na incapacidade de agir.{os.linesep}\n Foi o suficiente, não foi? Responda: sim ou não''',
                     f'''Sem humildade e coragem não há amor. Essas duas qualidades são exigidas, em escalas enormes e contínuas, quando se ingressa numa terra inexplorada e não-mapeada. E é a esse território que o amor conduz ao se instalar entre dois ou mais seres humanos.{os.linesep}\n Foi o suficiente, não foi? Responda: sim ou não''',
                     f'''“Medo” é o nome que damos a nossa incerteza: nossa ignorância da ameaça e do que deve ser feito.{os.linesep}\n Foi o suficiente, não foi? Responda: sim ou não''']
            item2 = random.choice(list2)
            return item2
 
        elif mensagem.lower() in ('s', 'sim', 'Sim', 'SIM'):
            list1 = ["Se quiser continuar, digite ~oi~ novamente. Caso contrário,\n Adeus!", "Se quiser continuar, digite ~oi~ novamente. Caso contrário,\n Até logo...", "Se quiser continuar, digite ~oi~ novamente. Caso contrário,\n Tchau!", "Se quiser continuar, digite ~oi~ novamente. Caso contrário,\n Até outra hora.", "Se quiser continuar, digite ~oi~ novamente. Caso contrário,\n Fique bem e até mais.", "Se quiser continuar, digite ~oi~ novamente. Caso contrário,\n Até outra oportunidade."]
            item1 = random.choice(list1)
            return item1
        elif mensagem.lower() in ('n', 'não', 'Não', 'NÃO'):
            list0 = ["Se quiser continuar, digite ~oi~ novamente. Caso contrário,\n Adeus!", "Se quiser continuar, digite ~oi~ novamente. Caso contrário,\n Até logo...", "Se quiser continuar, digite ~oi~ novamente. Caso contrário,\n Tchau!", "Se quiser continuar, digite ~oi~ novamente. Caso contrário,\n Até outra hora.", "Se quiser continuar, digite ~oi~ novamente. Caso contrário,\n Fique bem e até mais.", "Se quiser continuar, digite ~oi~ novamente. Caso contrário,\n Até outra oportunidade."]
            item0 = random.choice(list0)
            return item0
        else:
            list = ["Gostaria de conversar? Digite: oi", 
                    "Bom dia, boa tarde ou boa noite! Converse comigo, diga: oi", 
                    "Me chamo Zygmunt Bauman, para conversarmos diga: oi", 
                    "Olá! Tudo bem com você? Espero que sim, para conversar comigo, inicie com: oi",
                    "Você parece uma pessoa cansada,caso queira iniciar uma conversa diga: oi",
                    "Está se sentindo solitário, mesmo com tantas pessoas conectadas a você? Para um diálogo, diga: oi"]
            item = random.choice(list)
            return item
 
    # Responder
    def responder(self, resposta, chat_id):
        link_requisicao = f'{self.url_base}sendMessage?chat_id={chat_id}&text={resposta}'
        requests.get(link_requisicao)
 
 
bot = TelegramBot()
bot.Iniciar()