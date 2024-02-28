from carro import MinhaLista
import requests

carro = MinhaLista()

url = 'https://parallelum.com.br/fipe/api/v1/carros/marcas'

response   = requests.get(url)
dados_json = response.json()

for item in dados_json:
    nome_carro = item['nome']
    carro.append(nome_carro)
    
    
def main():
    print(carro.listar_carros)
    
    
if __name__ == '__main__':
    main()