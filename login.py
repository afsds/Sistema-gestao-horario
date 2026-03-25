from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)
CSV_FILE = 'usuarios.csv'



@app.route('/login', methods=['POST'])
def login():

    usuario_digitado = request.form.get('usuario')
    senha_digitada = request.form.get('senha')

  
    with open('usuarios.csv', 'r') as f:
        reader = csv.DictReader(f)
        for linha in reader:
            if linha['usuario'] == usuario_digitado and linha['senha'] == senha_digitada:
                
                return redirect('/grade')
    

    return "Usuário ou senha inválidos", 401