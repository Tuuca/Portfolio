from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/home')

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/projetos')
def projetos():
    return render_template('projetos.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')