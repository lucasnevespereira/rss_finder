# rss_finder

Flask Application with a python script that crawls for google results and returns rss feeds from keyword.

## Scripts

[Google_Finder](scripts/google_finder.py)

Params:

- Keywords: keywords you want to look for (ex: "moto voiture")
- Number of page results: Is the number of results pages you want to analyse(ex: 5)

[RSS_Finder](scripts/rss_finder.py)

Params:

- Keywords: keywords you want to look for (ex: "moto voiture")
- Number of results: Is the number of results you want to analyse(ex: 50)

### Additional info

By default Google displays 10 result by page.
So in <b>RSS Finder script</b> 50 results equals to 5 pages.

For <b>Google Script</b> 5 pages equals to 50 results.

### How to switch between rss_finder and google_finder scripts

In [app.py](app.py) change the import statement

```
from scripts import google_finder as finder
```

or

```
from scripts import rss_finder as finder
```

### Setup Google Credentials

Create a .env file

```
touch .env
```

Enter you API KEYS

```
GOOGLE_API_KEY=YOUR_API_KEY_HERE
GOOGLE_SEARCH_ENGINE_ID=YOUR_SEARCH_ENGINE_ID_HERE
```

<hr>

## Usage

```
git clone https://github.com/lucasnevespereira/rss_finder.git
```

```
pip install -r requirements.txt
```

```
python app.py
```

Visit [localhost:5000](http://127.0.0.1:5000/)
