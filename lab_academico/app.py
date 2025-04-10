# app.py

from flask import Flask, render_template, request, redirect, url_for, flash
from config import verificar_login
from flask import session
import sqlite3
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.secret_key = 'chave_secreta_segura'  # usada para sessões e segurança

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        tipo = request.form['tipo']

        if verificar_login(email, senha, tipo):
            session['usuario'] = email
            session['tipo'] = tipo
            flash('Login realizado com sucesso!', 'success')
            return f'Bem-vindo, {tipo.capitalize()}!'
        else:
            flash('Credenciais inválidas. Tente novamente.', 'danger')
            return redirect(url_for('login'))

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)

app = Flask(__name__)
app.secret_key = "sua_chave_secreta"

# Rota da tela de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

# Rota de registro de aluno
@app.route('/registro', methods=['POST'])
def registro():
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']
    tipo = 'aluno'  # Apenas alunos podem se registrar sozinhos

    senha_hash = generate_password_hash(senha)

    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO usuarios (nome, email, senha, tipo) VALUES (?, ?, ?, ?)",
                       (nome, email, senha_hash, tipo))
        conn.commit()
        conn.close()
        flash('Cadastro realizado com sucesso!', 'success')
    except sqlite3.IntegrityError:
        flash('E-mail já cadastrado.', 'danger')

    return redirect(url_for('login'))
