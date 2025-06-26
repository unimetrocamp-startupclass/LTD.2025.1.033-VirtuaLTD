import sqlite3
from datetime import datetime
import hashlib

# Conecta com o banco ou cria o arquivo se não existir
def conectar():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Criptografa a senha com SHA256
def criptografar_senha(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

# Cria as tabelas necessárias no banco
def criar_banco():
    conn = conectar()
    cursor = conn.cursor()

    # Tabela de usuários
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            senha TEXT NOT NULL,
            tipo TEXT NOT NULL CHECK(tipo IN ('aluno', 'professor', 'desenvolvedor', 'coordenador')),
            data_criacao TEXT NOT NULL
        )
    ''')

    # Tabela de projetos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS projetos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            resumo TEXT NOT NULL,
            status TEXT NOT NULL,
            data_inicio TEXT NOT NULL,
            data_fim TEXT
        )
    ''')

    # Tabela de pessoas
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pessoas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_pessoa TEXT NOT NULL,
            funcao TEXT NOT NULL
        )
    ''')

    # Tabela de ligação pessoas-projetos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pessoas_projetos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            projetos_id INTEGER NOT NULL,
            pessoas_id INTEGER NOT NULL,
            FOREIGN KEY (projetos_id) REFERENCES projetos(id),
            FOREIGN KEY (pessoas_id) REFERENCES pessoas(id)
        )
    ''')

    conn.commit()
    conn.close()
    print("Banco de dados e tabelas criadas com sucesso!")

# Cria uma nova conta de usuário
def criar_conta(nome, email, senha, tipo):
    conn = conectar()
    cursor = conn.cursor()

    senha_criptografada = criptografar_senha(senha)
    data_criacao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        cursor.execute('''
            INSERT INTO usuarios (nome, email, senha, tipo, data_criacao)
            VALUES (?, ?, ?, ?, ?)
        ''', (nome, email, senha_criptografada, tipo, data_criacao))
        conn.commit()
        print(f"Conta de {tipo} criada com sucesso!")
    except sqlite3.IntegrityError:
        print("Erro: email já cadastrado.")
    finally:
        conn.close()

# Verifica login pelo email, senha e opcionalmente tipo
def verificar_login(email, senha, tipo_esperado=None):
    conn = conectar()
    cursor = conn.cursor()

    senha_hash = criptografar_senha(senha)

    if tipo_esperado:
        cursor.execute('SELECT * FROM usuarios WHERE email=? AND senha=? AND tipo=?',
                       (email, senha_hash, tipo_esperado))
    else:
        cursor.execute('SELECT * FROM usuarios WHERE email=? AND senha=?',
                       (email, senha_hash))

    usuario = cursor.fetchone()
    conn.close()

    return usuario is not None

# Criação controlada de conta de professor ou desenvolvedor pelo coordenador
def criar_conta_admin(nome, email, senha, tipo, email_coord, senha_coord):
    if not verificar_login(email_coord, senha_coord, tipo_esperado='coordenador'):
        print("❌ Acesso negado. Apenas coordenadores podem criar professores e desenvolvedores.")
        return

    if tipo not in ['professor', 'desenvolvedor']:
        print("❌ Tipo inválido.")
        return

    criar_conta(nome, email, senha, tipo)

if __name__ == '__main__':
    criar_banco()
