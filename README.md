### API de Vendas
Esta API permite acessar os dados de vendas de uma base de dados fictícia.

## Requisitos

Python 3.x
Flask

Pandas

Instalação

Clone este repositório:

bash
Copy code
git clone https://github.com/davifernandodias/api-consumption-one-metodh.git

Para fazer uma requisição de dados de vendas, utilize o endpoint /get_sales. Você pode passar parâmetros opcionais na URL para filtrar os resultados. 


### Exemplo
python
Copy code
import requests

url = 'http://localhost:5000/get_sales'
params = {'date': '2024-02-14'}
response = requests.get(url, params=params)

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.
