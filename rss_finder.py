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


def find_rss(site):
    raw = requests.get(site).text
    result = []
    possible_feeds = []
    html = bs(raw, features="html5lib")
    feed_urls = html.findAll("link", rel="alternate")
    if len(feed_urls) > 1:
        for f in feed_urls:
            t = f.get("type", None)
            if t:
                if "rss" in t or "xml" in t:
                    href = f.get("href", None)
                    if href:
                        possible_feeds.append(href)
                        print(href)


print("Executing scraping...")
getWebsites()

for website in websites_list:
    find_rss(website)
