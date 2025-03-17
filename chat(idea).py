import os

def limp():
    os.system('cls' if os.name == 'nt' else 'clear')

limp()

def chatbot(pergunta, nome):
    respostas = {
        "jarvis":f"Olá {nome} como posso ajudar-lo?", "oi": f"Oi, {nome}!",
    "ola": f"Olá, {nome}!",
    "eae": f"Eae, {nome}, como você está?",
    "tudo bem": f"Tudo bem, {nome}? Como posso te ajudar?",
    "oi tudo bem": f"Oi, {nome}, tudo bem com você?",
    "cumprimento": f"Oi, {nome}! Tudo certo por aí?",
    "ola jarvis": f"Oi, {nome}, eu sou o Jarvis! Como posso te ajudar hoje?",
    "como esta": f"Como você está, {nome}?",
    "tudo certo": f"Oi, {nome}, tudo certinho com você?",
    "bom dia": f"Oi, {nome}, bom dia! Como posso te ajudar?",
    "boa tarde": f"Oi, {nome}, boa tarde! O que você precisa?",
    "boa noite": f"Oi, {nome}, boa noite! O que posso fazer por você?",
    "quer ajuda": f"Oi, {nome}, em que posso te ajudar agora?",
    "piada": f"Quer ouvir uma piada, {nome}?",
    "filme": f"Oi, {nome}, você assistiu algum filme bom ultimamente?",
    "livro": f"Oi, {nome}, você leu algum livro interessante recentemente?",
    "musica": f"Oi, {nome}, qual é a sua música favorita?",
    "tempo": f"Oi, {nome}, você quer saber a previsão do tempo?",
    "relaxar": f"Oi, {nome}, como você costuma relaxar?",
    "hobbie": f"Oi, {nome}, qual é o seu maior hobby?",
    "desafio": f"Oi, {nome}, você gosta de desafios?",
    "viagem": f"Oi, {nome}, qual lugar você gostaria de visitar?",
    "comida": f"Oi, {nome}, qual é o seu prato favorito?",
    "esportes": f"Oi, {nome}, você gosta de praticar esportes?",
    "jogos": f"Oi, {nome}, qual é o seu jogo favorito?",
    "futuro": f"Oi, {nome}, o que você acha que o futuro nos reserva?",
    "animal": f"Oi, {nome}, se você fosse um animal, qual seria?",
    "medo": f"Oi, {nome}, você tem algum medo que gostaria de compartilhar?",
    "superheroi": f"Oi, {nome}, se você fosse um super-herói, qual seria seu poder?",
    "sonho": f"Oi, {nome}, qual é o seu maior sonho?",
    "passatempos": f"Oi, {nome}, o que você gosta de fazer para passar o tempo?"
    }

    pergunta = pergunta.lower()
    return respostas.get(pergunta,
        "Desculpa, não entendi")

nome = input('Digite seu nome: ')

os.system('cls')
print('Chatbot iniciado: digite "sair" para encerrar:')
while True:
    os.system('cls')
    pergunta = input('você: ')
    if pergunta.lower() == 'sair':
        print('chatbot: Até logo!')
        break
    respostas = chatbot(pergunta, nome)
    print(f'chatbot: {respostas}')
