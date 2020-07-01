import sqlite3                                  # importar Sqlite (gerenciador banco dados)
from os import getcwd, chdir, path, makedirs    # importar OS (gerenciador de diretórios)
from tkinter import ttk, Scrollbar, W, E             # importar ttk (criar visualizador Banco)
# ---------------------------------------------

diretorio_prog = getcwd()                   # diretório principal do programa

nomePasta = '#bancoDados'                   # nome Pasta Banco
nomeBanco = 'irmaosDesignados.db'           # nome Banco criado
nomeTabela = 'irmaosDesignados'             # tabela dentro do Banco para receber dados

# ---------------------------------------------


def criar_pasta(nomePasta):
    try:                                    # testa se:
        if not path.exists(nomePasta):      # se a pasta não existir, criar
            makedirs(nomePasta)
    except OSError:                         # caso ocorra um erro na criação, informe
        print('Error: Creating directory. ' + nomePasta)

    chdir(f'{diretorio_prog}\\{nomePasta}')  # diretório pasta Banco Dados


def criar_banco():

    criar_pasta(nomePasta)                  # criar pasta do Banco

    conexao = sqlite3.connect(nomeBanco)    # conectar com o Banco de Dados
    c = conexao.cursor()                    # cursor move dentro do Banco

    c.execute(f"""CREATE TABLE IF NOT EXISTS {nomeTabela}(  
                ID text,
                Nome text,
                Designado text
            )
    """)

    conexao.commit()        # salvar dados no Banbco de Dados
    conexao.close()         # encerrar conexão com o Banco
    chdir(diretorio_prog)   # retornar para diretório principal do Programa


def adicionar_dados(id, nome, designado):
    chdir(f'{diretorio_prog}\\{nomePasta}')

    conexao = sqlite3.connect(nomeBanco)    # conectar com o Banco de Dados
    c = conexao.cursor()                    # cursor move dentro do Banco

    c.execute(f"INSERT INTO {nomeTabela} VALUES(:id, :nome, :designado)",
              {
                  'id': id,
                  'nome': nome,
                  'designado': designado
              })

    conexao.commit()
    conexao.close()

    chdir(diretorio_prog)               # sempre é necessário retornar para a pasta principal. Fica mais fácil.


def editar_dados(escolha, novo_id, novo_nome, novo_designado):
    chdir(f'{diretorio_prog}\\{nomePasta}')

    conexao = sqlite3.connect(nomeBanco)    # conectar com o Banco de Dados
    c = conexao.cursor()                    # cursor move dentro do Banco

    c.execute("""UPDATE irmaosDesignados SET
                id = ?,
                nome = ?,
                designado = ?
                WHERE id = """ + escolha, (novo_id, novo_nome, novo_designado))

    conexao.commit()
    conexao.close()
    chdir(diretorio_prog)   # retornar para diretório principal do Programa


def deletar_dados(escolha):
    chdir(f'{diretorio_prog}\\{nomePasta}')

    conexao = sqlite3.connect(nomeBanco)    # conectar com o Banco de Dados
    c = conexao.cursor()                    # cursor move dentro do Banco

    c.execute(f"""DELETE from {nomeTabela} WHERE id = """ + escolha)

    conexao.commit()
    conexao.close()
    chdir(diretorio_prog)   # retornar para diretório principal do Programa


def criar_visualizador(janela):

    listaID = []                    # criar uma lista para impressão
    listaNOME = []                  # criar uma lista para impressão
    listaDESIGNADO = []             # criar uma lista para impressão

    visualizador = ttk.Treeview(janela, height=10, columns=('ID', 'Nome', 'Designado'))
    visualizador.grid(row=0, column=0)

    deslizarX = Scrollbar(janela, orient='horizontal', command=visualizador.xview)
    deslizarX.grid(row=1, column=0, columnspan=3, sticky=W + E)

    deslizarY = Scrollbar(janela, orient='vertical', command=visualizador.yview)
    deslizarY.grid(row=0, column=1, sticky="NSE")

    visualizador.configure(yscrollcommand=deslizarY.set)
    visualizador.configure(xscrollcommand=deslizarX.set)

    visualizador.heading('#0', text='ID')           # nome da coluna 0
    visualizador.heading('#1', text='Nome')         # nome da coluna 1
    visualizador.heading('#2', text='Designado')    # nome da coluna 2

    chdir(f'{diretorio_prog}\\{nomePasta}')         # importante ir para a Pasta do Banco

    conexao = sqlite3.connect(nomeBanco)            # conectar com o Banco de Dados
    c = conexao.cursor()                            # cursor move dentro do Banco
    c.execute(f"SELECT *,oid FROM {nomeTabela}")    # selecionar todos dados da tabela
    gravar = c.fetchall()                           # necessário para gravar os dados selecionados

    # Aquisição dos Dados do Banco de Dados:

    for dados in gravar:                            # agora usamos o FOR para imprimir os dados no visualizador
        listaID.append(str(dados[0]))               # add dado[i] na lista desejada

    for dados in gravar:
        listaNOME.append(str(dados[1]))

    for dados in gravar:
        listaDESIGNADO.append(str(dados[2]))

    listaID = listaID                               # atualização da lista
    listaNOME = listaNOME
    listaDESIGNADO = listaDESIGNADO

    conexao.commit()
    conexao.close()

    chdir(diretorio_prog)                           # retornar para diretório principal do Programa

    for i in range(len(listaID)):                   # imprimir dados coletados nas respectivas colunas

        visualizador.insert('', i, text=listaID[int(i)],
                            values=(listaNOME[int(i)], listaDESIGNADO[int(i)]))

    return listaID, listaNOME, listaDESIGNADO       # retornar para poder ser lido pelo programa


def atualizarBanco():                               # mesmo princípio de criar, mas agr atualizando

    listaID = []
    listaNOME = []
    listaDESIGNADO = []

    chdir(f'{diretorio_prog}\\{nomePasta}')

    conexao = sqlite3.connect(nomeBanco)
    c = conexao.cursor()
    c.execute(f"SELECT *,oid FROM {nomeTabela}")
    gravar = c.fetchall()

    for dados in gravar:
        listaID.append(str(dados[1]))

    for dados in gravar:
        listaNOME.append(str(dados[2]))

    for dados in gravar:
        listaDESIGNADO.append(str(dados[3]))

    listaID = listaID
    listaNOME = listaNOME
    listaDESIGNADO = listaDESIGNADO

    conexao.commit()
    conexao.close()

    chdir(diretorio_prog)  # retornar para diretório principal do Programa

    return listaID, listaNOME, listaDESIGNADO

#   ----------------------------------------
