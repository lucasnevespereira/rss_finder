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

<hr>

### Additional info

By default Google displays 10 result by page.
So in <b>RSS Finder script</b> 50 results equals to 5 pages.

For <b>Google Script</b> 5 pages equals to 50 results.
