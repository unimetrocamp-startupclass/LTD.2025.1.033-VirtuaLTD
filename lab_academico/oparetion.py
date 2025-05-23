import sqlite3 as lite

#Criando conexão com o banco de dados
conn = lite.connect('virtualtd.db')

#Tabela projetos
titulo = input("Digite o título do projeto: ")
resumo = input("Digite o resumo do projeto: ")
data_inicio = input("Data de início do projeto (DD-MM-AAAA): ")

while True:
    status = int(input("Digite o status do projeto. [1] Em andamento / [2] Concluído: "))
    
    if status == 1: 
        print("Em andamento")
        data_fim = None
        break
    elif status == 2:
        print("Concluído")
        data_fim = input("Digite a data de término do projeto (DD-MM-AAAA): ")
        print(f"Data de término: {data_fim}")
        break
    else:
        print("Opção inválida. Digite [1] ou [2]")

values = [titulo, resumo, status, data_inicio, data_fim]
with conn:
    cursor = conn.cursor()
    query = "INSERT INTO projetos (titulo, resumo, status, data_inicio, data_fim) VALUES (?, ?, ?, ?, ?)"
    cursor.execute(query, values)
    

id_projeto = cursor.lastrowid
codigo = f'P{id_projeto:03}'
conn.commit()


#Tabela pessoas
tem_desenvolvedor = False
tem_cliente = False

while not (tem_desenvolvedor and tem_cliente):
    nome_pessoa = input("\nDigite o nome da pessoa: ")

    while True:
        funcao_input = int(input("Escolha a função dessa pessoa. [1] Desenvolvedor / [2] Cliente: "))
        if funcao_input == 1:
            funcao = "Desenvolvedor"
            tem_desenvolvedor = True
            break
        elif funcao_input == 2:
            funcao = "Cliente"
            tem_cliente = True
            break
        else:
            print("Opção inválida. Digite [1] ou [2].")

values = [nome_pessoa, funcao]  

with conn:
    cursor = conn.cursor()
    query = "INSERT INTO pessoas (nome_pessoa, funcao) VALUES (?, ?)"
    cursor.execute(query, values)
    id_pessoa = cursor.lastrowid
    conn.commit()

    cursor.execute('''
        INSERT INTO pessoas_projetos (projetos_id, pessoas_id)
        VALUES (?, ?)
    ''', (id_projeto, id_pessoa))

    conn.commit()
