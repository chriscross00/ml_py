import spacy

nlp = spacy.load('en')
doc = nlp('hello world!')

for token in doc:
    print('"' + token.text + '"')
