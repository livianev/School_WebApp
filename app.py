from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
import os

app = Flask(__name__, static_folder='static')
app.secret_key = 'sua_chave_secreta'  # Necessário para usar sessões

# Caminho absoluto para o banco de dados
basedir = os.path.abspath(os.path.dirname(__file__))
caminho_banco = os.path.join(basedir, 'database_ic', 'meu_banco.db')

# Função para verificar login
def verificar_login(email, senha):
    con = sqlite3.connect(caminho_banco)
    cur = con.cursor()
    cur.execute("SELECT * FROM alunos WHERE email = ? AND senha = ?", (email, senha))
    aluno = cur.fetchone()
    con.close()
    return aluno

@app.route('/')
def mural():
    return render_template('mural.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        aluno = verificar_login(email, senha)
        if aluno:
            session['aluno'] = email
            return redirect(url_for('painel'))
        else:
            return redirect(url_for('login_invalido'))
    return render_template('login.html')

@app.route('/login_invalido')
def login_invalido():
    return render_template('login_invalido.html')

@app.route('/home')
def painel():
    if 'aluno' in session:
        return render_template('aluno.html')  # Aqui renderiza o HTML corretamente
    else:
        return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
