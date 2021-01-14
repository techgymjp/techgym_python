import requests

url = 'https://techgym.jp/?cat=2'

response = requests.get(url)
print(response.text)
