# -*- coding: utf-8 -*-
import nltk
from textblob import TextBlob
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tag import tnt
from nltk.corpus import indian
from nltk import word_tokenize, pos_tag, ne_chunk
from indic_transliteration import sanscript
from indic_transliteration.sanscript import SchemeMap, SCHEMES, transliterate
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

'''
#Language Detection

Sent = TextBlob(u"सुनील ग्रोवर जल्द सलमान खान की फिल्म में नजर आने वाले हैं.")
e = Sent.detect_language()
print(e)

#Language Conversion

LangConv = TextBlob(u"सुनील ग्रोवर जल्द सलमान खान की फिल्म में नजर आने वाले हैं.")
z = LangConv.translate(from_lang = 'hi', to = 'en')
print(z)

#Language Itransliteration

data = 'ladke ne paani piyaa'
print(transliterate(data, sanscript.ITRANS, sanscript.DEVANAGARI))

#Tokenizing

example_text = "सुनील ग्रोवर जल्द सलमान खान की फिल्म में नजर आने वाले हैं.'सुल्तान' और 'टाइगर जिंदा है' के बाद एक बार फिर सलमान सुपरहिट फिल्मों की हैट्रिक लगाने के लिए अली अब्बास जफर के साथ काम कर रहे हैं. सुनील ग्रोवर M.B.B.S जबरदस्त फैन फॉलोइंग एंजॉय करते हैं और उनके इस फिल्म में आने से फिल्म की सफलता के चांसेस बेहतर हो चुके हैं."

for i in word_tokenize(example_text):
    print(i)

print (sent_tokenize(example_text))

#POS Tagging

pos_text = " इराक के विदेश मंत्री ने अमरीका के उस प्रस्ताव का मजाक उड़ाया है , जिसमें अमरीका ने संयुक्त राष्ट्र के प्रतिबंधों को इराकी नागरिकों के लिए कम हानिकारक बनाने के लिए कहा है ।"
train_data = indian.tagged_sents('hindi.pos')
tnt_pos_tagger = tnt.TnT()
tnt_pos_tagger.train(train_data)
tagged_words = (tnt_pos_tagger.tag(nltk.word_tokenize(pos_text)))
print(tagged_words)

#Stemming

Stem_text = "इराक के विदेश मंत्री ने अमरीका के उस प्रस्ताव का मजाक उड़ाया है"
for i in word_tokenize(Stem_text):
    suffixes = {
    1: [u"ो",u"े",u"ू",u"ु",u"ी",u"ि",u"ा"],
    2: [u"कर",u"ाओ",u"िए",u"ाई",u"ाए",u"ने",u"नी",u"ना",u"ते",u"ीं",u"ती",u"ता",u"ाँ",u"ां",u"ों",u"ें"],
    3: [u"ाकर",u"ाइए",u"ाईं",u"ाया",u"ेगी",u"ेगा",u"ोगी",u"ोगे",u"ाने",u"ाना",u"ाते",u"ाती",u"ाता",u"तीं",u"ाओं",u"ाएं",u"ुओं",u"ुएं",u"ुआं"],
    4: [u"ाएगी",u"ाएगा",u"ाओगी",u"ाओगे",u"एंगी",u"ेंगी",u"एंगे",u"ेंगे",u"ूंगी",u"ूंगा",u"ातीं",u"नाओं",u"नाएं",u"ताओं",u"ताएं",u"ियाँ",u"ियों",u"ियां"],
    5: [u"ाएंगी",u"ाएंगे",u"ाऊंगी",u"ाऊंगा",u"ाइयाँ",u"ाइयों",u"ाइयां"],
}
    for L in 5, 4, 3, 2, 1:
        if len(i) > L + 1:
            for suf in suffixes[L]:
                if i.endswith(suf):
                    print (i[:-L])
    print (i)
    
#Named Entity Recognition
 
sentence = "राम भारत में काम कर रहे हैं"
train_data = indian.tagged_sents('hindi.pos')
tnt_pos_tagger = tnt.TnT()
tnt_pos_tagger.train(train_data)
print (ne_chunk(tnt_pos_tagger.tag(nltk.word_tokenize(sentence))))
'''

train_text = state_union.raw("train.txt")
sample_text = state_union.raw("sample.txt")

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
tokenized = custom_sent_tokenizer.tokenize(sample_text)

def process_content():
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP><NN>?}"""
            chunkParser = nltk.RegexParser(chunkGram)
            chunked = chunkParser.parse(tagged)
            print(chunked)

