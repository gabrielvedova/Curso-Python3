import random
import tkinter as ttk

animal = ['Macaco', 'Elefante', 'Rato', 'Urso', 'Timbu',
          'Lagartixa', 'Girafa', 'T-Rex', 'Pássaro', 'Tartaruga']

tema = ['Praia', 'Mecânico', 'Skat', 'Paris', 'Trabalhador', 'Nordestino',
        'Astrounata', 'Depressiva', 'Nerd', 'Medroso']


def aperte_sim():
    sorteio = random.choice(animal), '+', random.choice(tema)
    texto_tema["texto"] = sorteio


# Interface Gráfica
# Criando Janela 2
def abrir_janela2():
    janela2 = ttk.Toplevel()
    janela2.title("Regras")
    janela2.geometry("600x450+500+50")
    janela2.minsize(600, 450)
    janela2.maxsize(600, 450)
    janela2.configure(background="#ADD8E6")

    texto_introdução = ttk.Label(
        janela2,
        text="REGRAS",
        font="Arial 19",
        background="#ADD8E6",
        pady=20
    )
    texto_introdução.pack()
    regra1 = ttk.Label(
        janela2,
        text="1.Objetivo do jogo: criar uma arte ou texto com tema sorteado.",
        font="Arial 15",
        background="#ADD8E6")
    regra1.place(x=20, y=70)
    regra2 = ttk.Label(
        janela2,
        text="2.Jogadores devem fazer todos uma arte ou um texto.",
        font="Arial 15",
        background="#ADD8E6"
    )
    regra2.place(x=20, y=120)
    regra3 = ttk.Label(
        janela2,
        text="3.Cada partida tem uma duração máxima de 15 minutos.",
        font="Arial 15",
        background="#ADD8E6"
    )
    regra3.place(x=20, y=170)
    regra4 = ttk.Label(
        janela2,
        text="4.Jogadores ou pessoas fora do jogo avaliam qual é o melhor.",
        font="Arial 15",
        background="#ADD8E6"
    )
    regra4.place(x=20, y=220)
    regra5 = ttk.Label(
        janela2,
        text="5.É proibido o uso de internet ou fotos que ajudam o jogador.",
        font="Arial 15",
        background="#ADD8E6"
    )
    regra5.place(x=20, y=270)


# layout Geral
janela = ttk.Tk()
janela.title('Gerador de temas')
janela.geometry("420x420+350+150")
janela.minsize(420, 420)
janela.maxsize(550, 550)
janela.configure(background="#92CBEC")

# ESPAÇO
espaco1 = ttk.Label(text="", background="#92CBEC")
espaco1.grid(column=0, row=0)
espaco2 = ttk.Label(text="", background="#92CBEC")
espaco2.grid(column=0, row=1)

# Linha 1
texto_pergunta = ttk.Label(
    janela,
    text="O tema de hoje será:",
    background="#92CBEC",
    font="Arial 20",
    padx=20
)
texto_pergunta.place(x=60, y=30)

# linha 2
botao_sim = ttk.Button(janela,
                       text="MOSTRAR",
                       command=aperte_sim,
                       font="Arial 15"
                       )
botao_sim.place(x=80, y=100)

botao_janela2 = ttk.Button(janela,
                            text="REGRAS",
                            command=abrir_janela2,
                            font="Arial 15"
                           )
botao_janela2.place(x=260, y=100)

# linha 3
texto_tema = ttk.Label(
    janela,
    text="",
    font="Arial 25",
    background="#92CBEC",
)
texto_tema.grid(column=0, row=4, pady=150, padx=60)


janela.mainloop()
