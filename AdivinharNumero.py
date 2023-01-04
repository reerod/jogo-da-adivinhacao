import tkinter
from tkinter import *
from tkinter import ttk

import random

janela = Tk()
janela.title('')
janela.geometry('350x300')
janela.configure(bg="#3b3b3b")

### Frames

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=2, ipadx=280)

frame_topo = Frame(janela, width=350, height=30, bg="#feffff", pady=0, relief="flat")
frame_topo.grid(row=1, column=0, sticky=NW)
frame_corpo = Frame(janela, width=350, height=280, bg="#3b3b3b", pady=0, relief="flat")
frame_corpo.grid(row=2, column=0, sticky=NW)

estilo = ttk.Style(janela)
estilo.theme_use("clam")

# CONFIGURANDO O frame topo
nome_jogo = Label(frame_topo, text="ADIVINHE O NÚMERO", anchor='center', font=('Monaco 16 bold'), bg="#feffff", fg="#38576b")
nome_jogo.place(x=55, y=0)

# CONFIGURANDO O frame corpo

# BARRA PARA DIVIDIR AS INFORMAÇÕES
exibe_acertos = Label(frame_corpo, text='Acertos: 0', anchor='center', font=('monaco 11 bold'), bg="#3b3b3b", fg='#feffff')
exibe_acertos.place(x=20, y=30)
exibe_tentativas = Label(frame_corpo, text='Tentativas: 5', anchor='center', font=('monaco 11 bold'), bg="#3b3b3b", fg='#feffff')
exibe_tentativas.place(x=205, y=30)

# REGRAS E BOAS VINDAS
msg_1 = Label(frame_corpo, text='Olá, jogador!', anchor='center', font=('monaco 10 bold'), bg="#3b3b3b", fg='#feffff')
msg_1.place(x=20, y=68)
regra_jogo = Label(frame_corpo, text='Tente adivinhar em que número estou pensando.\n'
            'Para isso, você terá o total de 5 tentativas.', anchor='center', font=('monaco 9 bold'), bg="#3b3b3b", fg='#feffff')
regra_jogo.place(x=20, y=90)
regra_jogo2 = Label(frame_corpo, text='Se acertar, você ganha +2 tentativas.', anchor='center', font=('monaco 9 bold'), bg="#3b3b3b", fg='#feffff')
regra_jogo2.place(x=20, y=122)

# FUNCAO PARA INICIAR O JOGO

chance = 5
acerto = 0

def iniciar_jogo():
    msg_1['text'] = ''
    regra_jogo['text'] = ''
    regra_jogo2['text'] = ''

    # GERANDO LISTA DE NUMEROS ALEATORIOS
    numeros = random.sample(range(0, 11), 8)
    resposta = random.choice(numeros)

    def modificando_valor(p):

        numeros = random.sample(range(0, 101), 8)
        resposta = [random.choice(numeros)]

        global chance
        global acerto

        for i in resposta:
            if p == i:
                acerto += 1
                chance += 2
                exibe_tentativas['text'] = 'Tentativas: ' + str(chance)
                exibe_acertos['text'] = 'Acertos: ' + str(acerto)

            else:
                chance -= 1
                exibe_tentativas['text'] = 'Tentativas: ' + str(chance)

                # DESABILITANDO OS BOTÕES APOS TENTATIVAS IGUAIS A 0
                if chance == 0:
                    botao_1['state'] = 'disable'
                    botao_2['state'] = 'disable'
                    botao_3['state'] = 'disable'
                    botao_4['state'] = 'disable'
                    botao_5['state'] = 'disable'
                    botao_6['state'] = 'disable'
                    botao_7['state'] = 'disable'
                    botao_8['state'] = 'disable'

                    # REMOVENDO NUMERAÇÃO DOS BOTÕES
                    botao_1['text'] = ''
                    botao_2['text'] = ''
                    botao_3['text'] = ''
                    botao_4['text'] = ''
                    botao_5['text'] = ''
                    botao_6['text'] = ''
                    botao_7['text'] = ''
                    botao_8['text'] = ''

                    # FUNÇAO DE FIM DE JOGO
                    fim_jogo()

                else:
                    pass




    # BOTAO DE ESCOLHA DE NUMEROS
    botao_1 = Button(frame_corpo, command=lambda:modificando_valor(numeros[0]), width=5, height=2, text=numeros[0], anchor='center', font=('ivy 12 bold'),
                     bg="#fcfbf7", fg="#444466", relief=RAISED, overrelief=RIDGE)
    botao_1.place(x=60, y=70)
    botao_2 = Button(frame_corpo, command=lambda:modificando_valor(numeros[1]), width=5, height=2, text=numeros[1], anchor='center', font=('ivy 12 bold'),
                     bg="#fcfbf7", fg="#444466", relief=RAISED, overrelief=RIDGE)
    botao_2.place(x=120, y=70)
    botao_3 = Button(frame_corpo, command=lambda:modificando_valor(numeros[2]), width=5, height=2, text=numeros[2], anchor='center', font=('ivy 12 bold'),
                     bg="#fcfbf7", fg="#444466", relief=RAISED, overrelief=RIDGE)
    botao_3.place(x=180, y=70)
    botao_4 = Button(frame_corpo, command=lambda:modificando_valor(numeros[3]), width=5, height=2, text=numeros[3], anchor='center', font=('ivy 12 bold'),
                     bg="#fcfbf7", fg="#444466", relief=RAISED, overrelief=RIDGE)
    botao_4.place(x=240, y=70)
    botao_5 = Button(frame_corpo, command=lambda:modificando_valor(numeros[4]), width=5, height=2, text=numeros[4], anchor='center', font=('ivy 12 bold'),
                     bg="#fcfbf7", fg="#444466", relief=RAISED, overrelief=RIDGE)
    botao_5.place(x=60, y=122)
    botao_6 = Button(frame_corpo, command=lambda:modificando_valor(numeros[5]), width=5, height=2, text=numeros[5], anchor='center', font=('ivy 12 bold'),
                     bg="#fcfbf7", fg="#444466", relief=RAISED, overrelief=RIDGE)
    botao_6.place(x=120, y=122)
    botao_7 = Button(frame_corpo, command=lambda:modificando_valor(numeros[6]), width=5, height=2, text=numeros[6], anchor='center', font=('ivy 12 bold'),
                     bg="#fcfbf7", fg="#444466", relief=RAISED, overrelief=RIDGE)
    botao_7.place(x=180, y=122)
    botao_8 = Button(frame_corpo, command=lambda:modificando_valor(numeros[7]), width=5, height=2, text=numeros[7], anchor='center', font=('ivy 12 bold'),
                     bg="#fcfbf7", fg="#444466", relief=RAISED, overrelief=RIDGE)
    botao_8.place(x=240, y=122)


# CRIANDO FUNÇAO DE FIM DE JOGO
def fim_jogo():
    global chance
    global acerto

    acertos = Label(frame_corpo, text='Total de acertos: ' + str(acerto), relief='raised', anchor='center', font=('ivy 12 bold'), bg="#444466",
                          fg="#feffff")
    acertos.place(x=105, y=78)

    chance = 5
    acerto = 0

    exibe_tentativas['text'] = 'Tentativas: ' + str(chance)
    exibe_acertos['text'] = 'Acertos: ' + str(acerto)

    msg_fim_jogo = Label(frame_corpo, text='FIM DE JOGO', relief='raised', anchor='center', font=('ivy 12 bold'), bg="#444466", fg="#feffff")
    msg_fim_jogo.place(x=125, y=108)

    # BOTAO DE JOGAR NOVAMENTE
    l_botao_reiniciar = Button(frame_corpo, command=iniciar_jogo, width=18, text='Jogar novamente', font=('ivy 12 bold'),
                     bg="#444466", fg="#feffff", relief=RAISED, overrelief=RIDGE)
    l_botao_reiniciar.place(x=86, y=138)

# BOTAO PARA JOGAR
l_botao = Button(frame_corpo, command=iniciar_jogo, width=18, text='JOGAR', anchor='center', font=('ivy 8 bold'), bg="#444466", fg="#feffff", relief=RAISED, overrelief=RIDGE)
l_botao.place(x=100, y=149)


janela.mainloop()
