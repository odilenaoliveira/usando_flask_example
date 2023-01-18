from app import app
from flask import render_template

@app.route('/') # rota do link
@app.route('/index') # rota do link
def index():
    nome = 'Oliver'
    dados = {'profissao':'cientista', 'funcao':'digitar','nome':'Oliver'}
    return render_template('index.html', nome=nome, dados=dados)

@app.route('/contato')
def contato():
    return render_template('contato.html')