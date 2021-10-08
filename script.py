import requests
from bs4 import BeautifulSoup
import os

while True:
    url = str(input("Digite a URL: "))
    print()
    page = requests.get(url)
    page.encoding = 'utf-8'
    soup = BeautifulSoup(page.text, 'html.parser')

    posts = soup.find_all(class_="sg-text sg-text--break-words brn-rich-content js-answer-content")

    list = []

    for post in posts:
        list.append(post.text)

    i = 1
    for each in list:
        print("Resposta(%d): " % i, each)
        i += 1

    q = input(str("[1] Tentar de novo\n[2] Sair\n"))

    if q == "2":
        break
    else:
        os.system('cls') or None
