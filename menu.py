from capAudio import reconhecer_fala
import pyttsx3 as vc
import time

msg =''
frases = ['Seu veiculo acaba de ser ligado','O sistema de ar-condicionado acaba de ser iniciado','Prontinho faróis ligados','Massa, hoje o dia está lindo']

voice = vc.init()
voice.say('Seja Bem - Vindo ao carro inteligente, o que vamos fazer hoje?')
voice.runAndWait()

while True:

    x = reconhecer_fala()
    time.sleep(5)

    if 'desligar' in x:
        msg = 'Sistema desligado com sucesso'
        voice.say(msg)
        voice.runAndWait()
        break
    elif 'condicionado' in x:
        msg = frases[1]
        print(msg)
    elif 'faróis' in x:
        msg = frases[2]
        print(msg)
    elif 'carro' in x:
        msg = 'Seu carro está prontinho para acelerar!'
     
    voice.say(msg)
    voice.runAndWait()

