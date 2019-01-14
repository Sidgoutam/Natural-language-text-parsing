from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps= PorterStemmer()

example = ["hellllo","hast","kashmirs"]

for w in example:
    print(ps.stem(w))
