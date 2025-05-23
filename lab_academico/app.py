from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from config import verificar_login, conectar

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

if __name__ == '__main__':
    app.run(debug=True)
