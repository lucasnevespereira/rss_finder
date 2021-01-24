import requests
from bs4 import BeautifulSoup as bs
import feedparser
import urllib.parse
import validators
import os


# get the API KEY here: https://developers.google.com/custom-search/v1/overview
API_KEY = os.getenv("GOOGLE_API_KEY")
# get your Search Engine ID on your CSE control panel
SEARCH_ENGINE_ID = os.getenv("GOOGLE_SEARCH_ENGINE_ID")


websites_list = []


def init_finder(term, num_pages):

    query = term
    query = query.replace(" ", "+")
    # search = f"https://google.com/search?q={query}&num={n}"
    result = []

    def getWebsites(n):

        page = n
        start = (page - 1) * 10 + 1
        url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}"

        # make the API request
        data = requests.get(url).json()
        # get the result items
        search_items = data.get("items")

        for i, search_item in enumerate(search_items, start=1):
            # extract the page url
            link = search_item.get("link")
            # print the results
            print("=" * 10, f"Result #{i+start-1}", "=" * 10)
            print("URL:", link, "\n")
            websites_list.append(link)

        # r = requests.get(search)
        # soup = bs(r.text, features="lxml")

        # for info in soup.find_all('div', class_='yuRUbf'):
        #     link = info.find('a')
        #     websites_list.append(link.get('href'))

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
        for u in list(set(possible_feeds)):
            if validators.url(u):
                if u not in result:
                    result.append(u)

    print("Executing scraping...")

    for x in range(num_pages):
        getWebsites(x + 1)

    for website in websites_list:
        find_rss(website)

    return result
