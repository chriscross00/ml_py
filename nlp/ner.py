#!/usr/bin/env python3

from bs4 import BeautifulSoup
from collections import Counter

import datetime
import logging
import re
import requests
import spacy


# globals
NLP = spacy.load('en')


def main():
    logging.basicConfig(filename='ner.log', level=logging.DEBUG)

    logging.info(f'{datetime.datetime.now()} Running main')

    ny_bb = url_to_string('https://www.nytimes.com/2018/08/13/us/politics/peter-strzok-fired-fbi.html?hp&action=click&pgtype=Homepage&clickSource=story-heading&module=first-column-region&region=top-news&WT.nav=top-news')
    article = NLP(ny_bb)

    print(tokenize(article))

    logging.info(f'{datetime.datetime.now()} End main')


def url_to_string(url):

    logging.info('Begin requests')

    res = requests.get(url)
    html = res.text
    soup = BeautifulSoup(html, 'html.parser')

    for script in soup(['script', 'style', 'aside']):
        script.extract()

    logging.info('End requests')

    return ' '.join(re.split(r'[\n\t]+', soup.get_text()))


def tokenize(text):

    labels = [x.label_ for x in text.ents]
    terms = [x.text for x in text.ents]

    logging.info(f'Tokenizing to {labels} and {terms}')

    return Counter(labels), Counter(terms).most_common(5)


if __name__ == '__main__':
    main()
