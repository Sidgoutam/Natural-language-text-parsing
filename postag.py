import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

trainText = state_union.raw("project.txt")
sampleText = state_union.raw("project.txt")

custom_sent_tokenizer = PunktSentenceTokenizer(trainText)

tokenized = custom_sent_tokenizer.tokenize(sampleText)

def process_content():
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)    
            print(tagged)

    except Exception as e:
        print(str(e))

process_content()
