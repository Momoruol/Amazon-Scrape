import requests
from bs4 import BeautifulSoup

url = 'Your URL'
headers = {
    'YOUR': 'HEADERS'
}

response = requests.get(url, headers=headers)
html = response.text


soup = BeautifulSoup(html, "html.parser")
valor_inteiro = soup.find('span', class_='a-price-whole')
valor_int = [valor.get_text() for valor in valor_inteiro]

valor = valor_int[0]

print(valor)