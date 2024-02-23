import pandas as pd  # import pandas
from flask import Flask, jsonify # import flash  and jsonify

app = Flask(__name__)   # init service

# Build function's

@app.route('/') # app rout run site - stable on
def homepage():
    return 'API ON'

@app.route('/get_sales')  # get sales - stable on

def get_sales():  # metodh get
    tabela = pd.read_csv('advertising.csv')
    total_vendas = tabela['Vendas'].sum()
    resposta = {'total_vendas' : total_vendas}
    return jsonify(resposta)

app.run() # run service