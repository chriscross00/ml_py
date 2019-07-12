#!/usr/bin/env python3

from bs4 import BeautifulSoup

import re
import requests
import spacy


def main():
    nlp = spacy.load('en')
    ny_bb = url_to_string('https://www.nytimes.com/2018/08/13/us/politics/peter-strzok-fired-fbi.html?hp&action=click&pgtype=Homepage&clickSource=story-heading&module=first-column-region&region=top-news&WT.nav=top-news')
    article = nlp(ny_bb)

    print(len(article.ents))


def url_to_string(url):

    res = requests.get(url)
    html = res.text
    soup = BeautifulSoup(html, 'html5lib')

    for script in soup(['script', 'style', 'aside']):
        script.extract()

    return ' '.join(re.split(r'[\n\t]+', soup.get_text()))


if __name__ == 'main':
    main()
