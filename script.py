import requests
from bs4 import BeautifulSoup

url = str(input("Digite a URL: "))
print("\n")
page = requests.get(url)
page.encoding = 'utf-8'
soup = BeautifulSoup(page.text, 'html.parser')

posts = soup.find_all(class_="sg-text sg-text--break-words brn-rich-content js-answer-content")

list = []

for post in posts:
    list.append(post.text)

for each in list:
    print(each)
