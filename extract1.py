from nltk.tokenize import sent_tokenize, word_tokenize

example_text= "Rajasthan vidhansabha soochna: P.M Modi se nahi dekhi gayi apni maa ki yahan taklif. janiye bhasan ki 10 baatein bole dhuan kya hota he "




print(sent_tokenize(example_text))

print(word_tokenize(example_text))

for i in word_tokenize(example_text):
     print (i)
