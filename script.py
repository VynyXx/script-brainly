import requests
from bs4 import BeautifulSoup

url = str(input("Digite a URL: "))
page = requests.get(url)
page.encoding = 'utf-8'
soup = BeautifulSoup(page.text, 'html.parser')

posts = soup.find_all(class_="sg-text sg-text--break-words brn-rich-content js-answer-content")
text = str(posts)

print(text.replace("<div class=\"sg-text sg-text--break-words brn-rich-content js-answer-content\" data-test=\"answer-box-text\">", "")
.replace("<p>", " ")
.replace("</p>", " ")
.replace("<strong>", " ")
.replace("</strong>", " ")
.replace("<em>", " ")
.replace("</em>", " ")
.replace("</div>", " ")
.replace("<>", " ")
.replace("</>", " ")
.replace(",", " "))
