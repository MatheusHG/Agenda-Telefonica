agenda = []
def pede_nome():
    return(input('Nome: '))
def pede_telefone():
    return(input('Telefone: '))
def mostra_dados(nome,telefone):
    print(f'Nome: {nome} Telefone: {telefone}')
def pede_nome_arquivo():
    return(input('Nome do arquivo: '))
def pesquisa(nome):
    mnome = nome.lower()
    for p, e in enumerate(agenda):
        if e[0].lower() == mnome:
            return p
    return None
def novo():
    global agenda
    nome = pede_nome()
    telefone = pede_telefone()
    agenda.append([nome,telefone])

def apaga():
    global agenda
    nome = pede_nome()
    p = pesquisa(nome)
    if p!=None:
        del apaga[p]
    else:
        print('Nome não encontrado.')

def altera():
    p = pesquisa(pede_nome())
    if p!=None:
        nome = agenda[p][0]
        telefone = agenda[p][1]
        print('Encontrado:')
        mostra_dados(nome,telefone)
        nome = pede_nome()
        telefone = pede_telefone()
        agenda[p] = [nome, telefone]
    else:
        print('Nome não encontrado.')
def lista():
    print('\nAgenda\n\n----------------')
    for e in agenda:
        mostra_dados(e[0], e[1])
    print('------\n')
def le():
    global agenda
    nome_arquivo = pede_nome_arquivo()
    arquivo = open(nome_arquivo, "r", encoding='utf-8')
    agenda = []
    for l in arquivo.readlines():
        nome, telefone = l.strip().split('#')
        agenda.append([nome,telefone])
    arquivo.close()
def grava():#
 i   nome_arquivo = pede_nome_arquivo()
    arquivo = open(nome_arquivo, 'w', encoding='utf-8')
    for e in agenda:
        arquivo.write('%s#%s\n'%(e[0],e[1]))
    arquivo.close()
def valida_faixa_inteiro(pergunta,inicio,fim):
    while True:
        try:
            valor = int(input(pergunta))
            if inicio <= valor <= fim:
                return(valor)
        except ValueError:
            print('Valor inválido, favor digitar entre {} e {}'.format(inicio,fim))
def menu():
    print('''
    1- Novo...
    2- Altera...
    3- Apaga...
    4- Lista...
    5- Grava...
    6- Lê

    0- Sai
''')
    return valida_faixa_inteiro('Escolha uma opção: ',0,6)

while True:
    opcao = menu()
    if opcao == 0:
        break
    if opcao == 1:
        novo()
    elif opcao == 2: 
        altera()
    elif opcao == 3:
        apaga()
    elif opcao == 4:
        lista()
    elif opcao == 5:
        grava()
    elif opcao == 6:
        le()
