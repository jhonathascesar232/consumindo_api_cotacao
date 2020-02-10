import requests

#
# Requisição das informações sobre o Euro
#
url_dolar = "https://economia.awesomeapi.com.br/all/USD-BRL" 
url_euro = "https://economia.awesomeapi.com.br/all/EUR-BRL"

urls = {'dolar':url_dolar, 'euro': url_euro}

lista_titulos_d = ['Nome:',
     'Código',
     'Alta do Dolar',
     'Baixa do Dolar',
     'Data de Atualização']

lista_titulos_e = ['Nome:',
     'Código',
     'Alta do Euro',
     'Baixa do Euro',
     'Data de Atualização']

titulos = [lista_titulos_d, lista_titulos_e]

nomes = ['USD', 'EUR']

#####################################################
#
# Requisição das informações sobre o Dolar
#
def reqs(url, n):  
    req = requests.get(url)
    file_json = req.json()

    dados = {} # armazenar os dados
    dados['nome'] = file_json[n]['name']
    dados['codigo'] = file_json[n]['code']
    dados['alta'] = file_json[n]['high']
    dados['baixa'] = file_json[n]['low']
    dados['criacao'] = file_json[n]['create_date']
    dados['preco'] = file_json[n]['bid']

    return dados


def line():
    print("*"*30)
    


def show_responses(lista, data):
    '''
Mostra os dados
    '''
    indice = 0
    
    line()
    for key in data:
        print(f"** {lista[indice]} --> {data[key]}")
        indice += 1
        line()

def main():
##    indice = 0
##    
##    for k in urls:
##        dados = reqs(urls[k], n = nomes[indice])
##        show_responses(lista = titulos[indice], data = dados)
##        indice += 1
    dados = reqs(url = urls['dolar'], n = nomes[0])
    show_responses(lista = titulos[0], data = dados)

    
if __name__ == '__main__':
    main()
