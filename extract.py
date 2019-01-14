from nltk.tokenize import sent_tokenize, word_tokenize

example_text=" राजस्थान विधानसभा चुनावः पीएम मोदी से नहीं देखी गई अपनी मां की यह तकलीफ, जानिए भाषण की 10 बातें पीएम मोदी बोले-धुंआ क्या होता है, लकड़ी का चूल्हा कैसे जलता है य नामदार की चार पीढ़ियों को कभी पता ही नहीं चला. मैने अपनी मां को लकड़ी के चूल्हे पर खाना पकाते देखा है, धुंए से आंखों से पानी कैसे निकलता है ये भी मैने देखा है, इसी से मुझे उज्ज्वला योजना शुरू करने की प्रेरणा मिली. "




print(sent_tokenize(example_text))

print(word_tokenize(example_text))

for i in word_tokenize(example_text):
     print (i)
