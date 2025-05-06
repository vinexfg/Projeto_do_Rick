import requests
import webbrowser


def personagem_digitado():
    print('Digite o nome do personagem: ')
    personagem = input('Nome: ')
    return personagem


def consulta_personagem(personagem):
    url = f'https://rickandmortyapi.com/api/character/?name={personagem}'
    resultado = requests.get(url)

    if resultado.status_code == 200:
        dados = resultado.json()

        if dados['results']:
            personagem = dados['results'][0]
            return personagem
        else:
            print('Personagem não encontrado')
            return None
    else:
        print('Erro ao buscar personagem')
        



             






