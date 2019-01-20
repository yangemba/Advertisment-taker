import requests
import bs4


response = requests.get('https://premier.ua/prodam-2kv-saltovka-603-m-n-12005774.html')

soup = bs4.BeautifulSoup(response.text, "html.parser")

tag = soup.select('tbody')

print(tag)