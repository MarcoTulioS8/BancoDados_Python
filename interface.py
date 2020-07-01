from sqlite3 import OperationalError
from tkinter import *
from tkinter import ttk, messagebox
import banco_dados as BD
# ------------------------------------

nomeBanco = 'irmaosDesignados.db'           # nome Banco criado
nomeTabela = 'irmaosDesignados'             # tabela dentro do Banco para receber dados

global entraId
global entraNome
global entraDesignado

global entraIdNova
global entraNomeNovo
global entraDesignadoNovo

global root
# ------------------------------------


def pega_dados():
    id = entraId.get()                      # .get() obtem o dado de input do usuário
    nome = entraNome.get()
    designado = entraDesignado.get()

    try:
        num = int(id)                               # verificar se é uma ID númerica inteira
        BD.adicionar_dados(num, nome, designado)    # chamada da função na aba banco_dados.py
        BD.atualizarBanco()                         # chamada da função na aba banco_dados.py
        root.destroy()                              # fechar janela principal para atualização do Banco
        criar_janela()                              # reabrir janela principal com Banco atualizado

    except (ValueError, TypeError):
        messagebox.showinfo('Erro no Cadastro', 'Insira um ID numérico, por favor!')    # (nome, mensagem)


def deleta_dados():
    id = entraId.get()

    try:
        BD.deletar_dados(id)
        BD.atualizarBanco()
        root.destroy()
        criar_janela()

    except (ValueError, TypeError, OperationalError):
        messagebox.showinfo('Erro ao Deletar', 'Insira um ID válido, por favor!')


def edita_dados():
    novo_id = entraIdNova.get()
    novo_nome = entraNomeNovo.get()
    novo_designado = entraDesignadoNovo.get()

    try:
        BD.editar_dados(novo_id, novo_id, novo_nome, novo_designado)
        BD.atualizarBanco()
        root.destroy()
        criar_janela()

    except (ValueError, TypeError, OperationalError):
        messagebox.showinfo('Erro ao Deletar', 'Insira um ID válido, por favor!')


def criar_janela():

    global entraId                  # criar variáveis globais para uma função interferir na outra
    global entraNome
    global entraDesignado

    global entraIdNova
    global entraNomeNovo
    global entraDesignadoNovo

    global root
    # ------------------------------------------------

    root = Tk()                 # criação da janela principal
    BD.criar_banco()            # chamada da função na aba banco_dados.py
    # ------------------------------------------------

    root.title('Designações Augusto SomSystem')
    largura_janela, altura_janela = root.winfo_screenwidth(), root.winfo_screenheight()       # gerar tela cheia
    root.geometry(f'{largura_janela}x{altura_janela}+0+0')
    # ------------------------------------------------

    cadastro = LabelFrame(root, text='  CADASTRAR  ', padx=10, pady=10)   # criando uma partição da tela
    cadastro.grid(row=0, column=0, padx=10, pady=10)

    labelId = Label(cadastro, text='ID do caboclo')
    labelId.grid(row=0, column=0, pady=5)

    entraId = Entry(cadastro)                   # input do usuário sobre a ID
    entraId.grid(row=0, column=1, pady=5)              # alocação do input na tela

    labelNome = Label(cadastro, text='Nome do caboclo')
    labelNome.grid(row=1, column=0, pady=5)

    entraNome = Entry(cadastro)
    entraNome.grid(row=1, column=1, pady=5)

    labelDesignado = Label(cadastro, text='Está Designado?')
    labelDesignado.grid(row=2, column=0, pady=5)

    entraDesignado = Entry(cadastro)
    entraDesignado.grid(row=2, column=1, pady=5)

    botao_add = Button(cadastro, text="Adicionar Dados", command=pega_dados, padx=100)
    botao_add.grid(row=5, column=1, pady=5)

    botao_del = Button(cadastro, text="Deletar Dados", command=deleta_dados, padx=107)
    botao_del.grid(row=6, column=1, pady=5)
    # ------------------------------------------------

    edicao = LabelFrame(root, text='  EDITAR CADASTRO  ', padx=55, pady=28)
    edicao.grid(row=0, column=1, padx=10, pady=10)

    labelIdNova = Label(edicao, text='ID do caboclo')
    labelIdNova.grid(row=0, column=0, pady=5)

    entraIdNova = Entry(edicao)                   # input do usuário sobre a ID
    entraIdNova.grid(row=0, column=1, pady=5)              # alocação do input na tela

    labelNomeNovo = Label(edicao, text='Novo Nome')
    labelNomeNovo.grid(row=1, column=0, pady=5)

    entraNomeNovo = Entry(edicao)
    entraNomeNovo.grid(row=1, column=1, pady=5)

    labelDesignadoNovo = Label(edicao, text='Está Designado?')
    labelDesignadoNovo.grid(row=2, column=0, pady=5)

    entraDesignadoNovo = Entry(edicao)
    entraDesignadoNovo.grid(row=2, column=1, pady=5)

    botao_edit = Button(edicao, text="Editar Dados", command=edita_dados, padx=50)
    botao_edit.grid(row=5, column=1, pady=5)
    # ------------------------------------------------

    ver_dado = LabelFrame(root)
    ver_dado.grid(row=1, column=0, columnspan=2)
    BD.criar_visualizador(ver_dado)
    # ------------------------------------------------


criar_janela()
root.mainloop()
# ------------------------------------------------
