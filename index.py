from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def index():
    url = 'https://kworb.net/youtube/archive.html'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Localizar a tabela de artistas
    table = soup.find('table')
    rows = table.find_all('tr')[1:6]  # Pegar os 5 primeiros (ignorando o cabeçalho)

    artists_data = []

    for row in rows:
        cols = row.find_all('td')
        rank = cols[0].text.strip()
        artist = cols[1].text.strip()
        views = cols[2].text.strip()
        artists_data.append({'rank': rank, 'artist': artist, 'views': views})

    return render_template('index.html', artists=artists_data)

if __name__ == '__main__':
    app.run(debug=True)


