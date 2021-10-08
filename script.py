import requests
from bs4 import BeautifulSoup

url = str(input("Digite a URL: "))
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

page0 = str(page.content)
page1 = page0.find("answer-box-text")
page2 = page0.find("next-answer-box")

resultado = page0[page1:page2]

print(resultado)
