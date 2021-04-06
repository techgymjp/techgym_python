import requests
from bs4 import BeautifulSoup

url = 'https://techgym.jp/?cat=2'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

articles = soup.find_all('div', class_='vk_post')

print(articles)
