import requests
from bs4 import BeautifulSoup

url = 'https://techgym.jp/?cat=2'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

articles = soup.find_all('article', class_='media')

for article in articles:
  print(article.find('h1').getText())
