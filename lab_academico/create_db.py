# Importa o SQLite
import sqlite3 as lite

# Cria a conexão com o banco de dados
conn = lite.connect('virtualtd.db')

# -----------CRIANDO TABELAS------------
with conn:
    # Cria o cursor
    cursor = conn.cursor()

    # Cria a tabela lista de projetos
    cursor.execute('''CREATE TABLE IF NOT EXISTS projetos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        resumo TEXT NOT NULL,
        status TEXT NOT NULL,
        data_inicio DATE NOT NULL,
        data_fim DATE
    )''')                

    # Cria a tabela de pessoas associadas ao projeto
    cursor.execute('''CREATE TABLE IF NOT EXISTS pessoas(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_pessoa TEXT NOT NULL,
        funcao TEXT NOT NULL
    )''')

    # Cria a tabela de relação entre as duas
    cursor.execute('''CREATE TABLE IF NOT EXISTS pessoas_projetos(
        projetos_id INTEGER, 
        pessoas_id INTEGER,
        PRIMARY KEY (projetos_id, pessoas_id),
        FOREIGN KEY (projetos_id) REFERENCES projetos(id),
        FOREIGN KEY (pessoas_id) REFERENCES pessoas(id)
    )''')

    conn.commit()
