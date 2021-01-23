import requests
from bs4 import BeautifulSoup as bs

search = "https://news.google.com/rss/search?q=moto"
websites_list = []


def getWebsites():

    r = requests.get(search)
    soup = bs(r.content, features="xml")

    articles = soup.find_all("item")

    for article in articles:
        link = article.find("link").text
        websites_list.append(link)


print("Websites List: ", websites_list)
print("Executing scraping...")
getWebsites()
print("Websites List: ", websites_list)
