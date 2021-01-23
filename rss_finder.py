import requests
from bs4 import BeautifulSoup as bs
import feedparser
import urllib.parse
import validators
import random


A = ("Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
     )

Agent = A[random.randrange(len(A))]

headers = {'user-agent': Agent}


def init_finder(term):

    query = term
    query = query.replace(' ', '+')
    search = f"https://google.com/search?q={query}"
    websites_list = []
    result = []

    def getWebsites():

        r = requests.get(search, headers=headers)
        soup = bs(r.text, features="lxml")

        for info in soup.find_all('div', class_='yuRUbf'):
            link = info.find('a')
            websites_list.append(link.get('href'))

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
                    possible_feeds.append(base+href)
        for u in list(set(possible_feeds)):
            if validators.url(u):
                if u not in result:
                    result.append(u)

    print("Executing scraping...")
    print("Visiting ", search)
    getWebsites()

    for website in websites_list:
        find_rss(website)

    return result
