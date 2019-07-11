#!/usr/bin/env python

import spacy

nlp = spacy.load('en')
doc = nlp('hello world! this is a test of spacy')

print([(token.text, token.tag_) for token in doc])
