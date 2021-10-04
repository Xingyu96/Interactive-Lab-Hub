import codecs
from bs4 import BeautifulSoup

file = codecs.open("templates/index.html", 'r')
fileString = file.read()
fileHtmlSoup = BeautifulSoup(fileString, 'html.parser')

toDoItemsHtml = fileHtmlSoup.find_all("li", {"class": "to-do-list-item"})
toDoItemsText = [x.text for x in toDoItemsHtml]

print(toDoItemsText)
