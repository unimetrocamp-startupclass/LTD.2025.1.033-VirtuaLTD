from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from config import verificar_login, conectar
import sqlite3

app = Flask(__name__)
app.secret_key = 'chave_super_secreta'

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    senha = request.form['senha']

    if verificar_login(email, senha):
        session['usuario'] = email
        flash("Login realizado com sucesso!", "success")
        return redirect(url_for('pagina_inicial')) 
    else:
        flash("Email ou senha inválido!", "error")
        return redirect(url_for('index'))

# Verifica login com hash
def verificar_login(email, senha):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute('SELECT senha FROM usuarios WHERE email=?', (email,))
    resultado = cursor.fetchone()
    conn.close()

    if resultado:
        senha_armazenada = resultado[0]
        return check_password_hash(senha_armazenada, senha)
    else:
        return False

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    email = request.form['email']
    ra = request.form['ra']
    password = request.form['password']
    confirm_password = request.form['confirm_password']

    if password != confirm_password:
        flash("As senhas não coincidem.", "error")
        return redirect(url_for('index'))

    hashed_password = generate_password_hash(password)

    conn = conectar()

    try:
        conn.execute(
            'INSERT INTO usuarios (nome, email, senha, tipo, data_criacao) VALUES (?, ?, ?, ?, datetime("now"))',
            (username, email, hashed_password, 'aluno')  # Tipo padrão 'aluno'
        )
        conn.commit()
        flash("Usuário registrado com sucesso!", "success")
    except:
        flash("Erro: Nome de usuário ou email já registrado.", "error")
    finally:
        conn.close()

    return redirect(url_for('index'))

@app.route('/dashboard')
def dashboard():
    if 'usuario' not in session:
        flash('Faça login para acessar o dashboard.', 'error')
        return redirect(url_for('index'))

    return f"Bem-vindo ao dashboard, {session['usuario']}!"

@app.route('/logout')
def logout():
    session.pop('usuario', None)
    flash('Logout realizado com sucesso.', 'success')
    return redirect(url_for('index'))

@app.route('/pagina_inicial')
def pagina_inicial():
    if 'usuario' not in session:
        flash('Faça login primeiro.', 'error')
        return redirect(url_for('index'))
    return render_template('pginicial.html', usuario=session['usuario'])

@app.route('/calendario')
def calendario():
    if 'usuario' not in session:
        flash('Faça login primeiro.', 'error')
        return redirect(url_for('index'))
    return render_template('calendario.html', usuario=session['usuario'])

@app.route('/cadproj')
def pagina_cadastro():
    return render_template('cadproj.html')

# Rota para salvar projeto
@app.route('/salvar', methods=['POST'])
def salvar():
    print("Recebido POST /salvar com dados:", request.form.to_dict(flat=False))
    titulo = request.form.get('project_title')
    resumo = request.form.get('project_description')
    data_inicio = request.form.get('project_start_date')
    status = request.form.get('project_status')
    data_fim = request.form.get('project_end_date')

    if status == 'andamento':
        data_fim = None

    projeto_id = insert_projeto(titulo, resumo, status, data_inicio, data_fim)

    # Desenvolvedor
    dev_nome = request.form.get('developer_name')
    dev_id = insert_pessoa(dev_nome, 'Desenvolvedor')
    link_pessoa_projeto(projeto_id, dev_id)

    # Cliente
    cliente_nome = request.form.get('client_name')
    cliente_id = insert_pessoa(cliente_nome, 'Cliente')
    link_pessoa_projeto(projeto_id, cliente_id)

    # Participantes extras
    participantes_nomes = request.form.getlist('participant_name[]')
    participantes_funcoes = request.form.getlist('participant_role[]')

    for nome, funcao in zip(participantes_nomes, participantes_funcoes):
        if nome.strip():
            pessoa_id = insert_pessoa(nome, funcao)
            link_pessoa_projeto(projeto_id, pessoa_id)

    return redirect(url_for('projetos'))

# Funções auxiliares
def insert_projeto(titulo, resumo, status, data_inicio, data_fim):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO projetos (titulo, resumo, status, data_inicio, data_fim)
        VALUES (?, ?, ?, ?, ?)
    ''', (titulo, resumo, status, data_inicio, data_fim))
    conn.commit()
    projeto_id = cursor.lastrowid
    conn.close()
    return projeto_id

def insert_pessoa(nome, funcao):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO pessoas (nome_pessoa, funcao)
        VALUES (?, ?)
    ''', (nome, funcao))
    conn.commit()
    pessoa_id = cursor.lastrowid
    conn.close()
    return pessoa_id

def link_pessoa_projeto(projeto_id, pessoa_id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO pessoas_projetos (projetos_id, pessoas_id)
        VALUES (?, ?)
    ''', (projeto_id, pessoa_id))
    conn.commit()
    conn.close()
    
@app.route('/projetos')
def projetos():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, titulo, status, data_inicio, data_fim FROM projetos')
    projetos = cursor.fetchall()
    conn.close()
    return render_template('projinicial.html', projetos=projetos)

# Inicialização da aplicação
if __name__ == '__main__':
    app.run(debug=True)
