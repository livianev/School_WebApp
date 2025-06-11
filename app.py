from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, static_folder='static')

@app.route('/')
def mural():
    print
    return render_template('mural.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Aqui valida o login com o banco de dados
        return redirect(url_for('painel'))
    return render_template('login.html')

@app.route('/painel')
def painel():
    return "Área privada do aluno"

if __name__ == '__main__':
    app.run(debug=True)


