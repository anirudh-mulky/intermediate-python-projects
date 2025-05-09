from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

articles = soup.find_all(name="span",class_="titleline")
article_texts = []
article_links = []
for article in articles:
    article_text  = article.getText()
    article_texts.append(article_text)
    article_link = article.get("href")
    article_links.append(article_link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span",class_= "score")]

largest_num = max(article_upvotes)
largest_index = article_upvotes.index(largest_num)

print(article_texts[largest_index])
# print(largest_num)
# print(article_texts)
# print(article_links)
# print(article_upvotes)















# import lxml 
# with open("website.html") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, "html.parser")

# #print(soup.title)

# #print(soup.prettify())

# anchortags = soup.find_all(name="a")#will get all the anchor tags in a list

# for tag in anchortags:
#     #print(tag.getText)#
#     print(tag.get("href"))

# heading = soup.find(name="h1",id="name")
# print(heading)

# section_heading = soup.find(name="h3", class_= "heading")
# print(section_heading)