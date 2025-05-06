import requests
import webbrowser
import os


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


def obter_episodios(episodio_urls):
    episodios = []
    for url in episodio_urls:
        resultado = requests.get(url)
        if resultado.status_code == 200:
            dados = resultado.json()
            episodios.append(dados)
    return episodios

def gerar_html(personagem, episodios):
    episodios_lista = ''
    for ep in episodios:
        episodios_lista += f"<li>{ep['episode']} - {ep['name']}</li>\n"

    return f"""
    <!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{personagem['name']}</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background-color: #f5f5f5;
            color: #333;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }}
        h1 {{
            text-align: center;
        }}
        img {{
            display: block;
            margin: 0 auto;
            border-radius: 8px;
            max-width: 250px;
        }}
        p {{
            font-size: 18px;
        }}
        ul {{
            list-style-type: square;
            padding-left: 20px;
        }}
        li {{
            margin-bottom: 5px;
        }}
    </style>
</head>
<body>
    <h1>{personagem['name']}</h1>
    <img src="{personagem['image']}" alt="{personagem['name']}">
    <p><strong>Origem:</strong> {personagem['origin']['name']}</p>
    <p><strong>Localização:</strong> {personagem['location']['name']}</p>
    <p><strong>Episódios:</strong></p>
    <ul>
        {episodios_lista}
    </ul>
</body>
</html>
"""


personagem = personagem_digitado()
personagem_encontrado = consulta_personagem(personagem)

if personagem_encontrado:
    episodios = obter_episodios(personagem_encontrado['episode'])
    html_inserido = gerar_html(personagem_encontrado, episodios)

    with open('personagem.html', 'w', encoding= 'utf-8') as arquivo:
        arquivo.write(html_inserido)
        
    webbrowser.open('personagem.html')






