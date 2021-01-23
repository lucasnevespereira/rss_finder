import requests
from bs4 import BeautifulSoup as bs
import feedparser
import urllib.parse
import validators


def init_finder(term):
    search = "https://news.google.com/rss/search?q="+term+""
    keyword = term
    websites_list = []
    result = []

    def getWebsites():

        r = requests.get(search)
        soup = bs(r.content, features="xml")

        articles = soup.find_all("item")

        for article in articles:
            link = article.find("link").text
            websites_list.append(link)

    def find_rss(site):
        raw = requests.get(site).text
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
        parsed_url = urllib.parse.urlparse(site)
        base = parsed_url.scheme + "://" + parsed_url.hostname
        atags = html.find_all("a")
        for a in atags:
            href = a.get("href", None)
            if href:
                if "xml" in href or "rss" in href or "feed" in href:
                    possible_feeds.append(base + href)
        for url in list(set(possible_feeds)):
            if len(url) > 0:
                if url not in result:
                    if keyword in url and validators.url(url):
                        result.append(url)

    print("Executing scraping...")
    getWebsites()

    for website in websites_list:
        find_rss(website)

    return result


print(init_finder())
