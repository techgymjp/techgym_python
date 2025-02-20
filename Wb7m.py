import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

url = 'https://techgym.jp/?cat=2'

response = requests.get(url,headers=headers)
soup = BeautifulSoup(response.text, 'lxml')

articles = soup.find_all('div', class_='vk_post')

for article in articles:
  print(article.find('h5').getText())
