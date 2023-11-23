import requests

from bs4 import BeautifulSoup

url = input()

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

paragraphs = soup.find_all('h1')
for p in paragraphs:
    print(p.text)
