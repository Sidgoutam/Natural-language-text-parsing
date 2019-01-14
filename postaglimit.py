import nltk
from nltk.corpus import gutenberg
from nltk.tokenize import sent_tokenize

sample = gutenberg.raw("project.txt")

tok = sent_tokenize(sample)

print(tok[0:3])

def process_content():
    try:
        for i in tok:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)    
            print(tagged)

    except Exception as e:
        print(str(e))

process_content()

