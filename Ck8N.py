import requests
from bs4 import BeautifulSoup

url = 'https://news.yahoo.co.jp/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

titles = soup.find_all('li', class_='topicsListItem')

print(titles)