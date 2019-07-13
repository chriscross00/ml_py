#!/usr/bin/env python3

from bs4 import BeautifulSoup
from collections import Counter

import logging
import re
import requests
import spacy


# globals
NLP = spacy.load('en')


def main():
    logging.basicConfig(level=logging.DEBUG)
    ny_bb = url_to_string('https://www.nytimes.com/2018/08/13/us/politics/peter-strzok-fired-fbi.html?hp&action=click&pgtype=Homepage&clickSource=story-heading&module=first-column-region&region=top-news&WT.nav=top-news')
    article = NLP(ny_bb)

    print(tokenize(article))


def url_to_string(url):

    res = requests.get(url)
    html = res.text
    soup = BeautifulSoup(html, 'html.parser')

    for script in soup(['script', 'style', 'aside']):
        script.extract()

    return ' '.join(re.split(r'[\n\t]+', soup.get_text()))


def tokenize(text):

    labels = [x.label_ for x in text.ents]
    terms = [x.text for x in text.ents]

    return Counter(labels), Counter(terms).most_common(5)


if __name__ == '__main__':
    main()
