RAKE is an extremely effiecient keyword extraction algorithm and operates on individual documents. Its language and domain independent.

Literature is abundant with methods which uses Noun phrase chunks,POS tags, ngram statistics and similar others.

Given a document, stop word list and a list of phrase delimiters, RAKE extracts candidate phrases.
    
    phrases = []
    
    for line in sentences:
    	words = nltk.word_tokenize(line)
    	phrase = ''
    	for word in words:
    		if word not in stopwords.words('english') and word not in [',','.','?',':',';']:
    			phrase+=word + ' '
    		else:
    			if phrase != '':
    			phrases.append(phrase.strip())
    			phrase = ''

We takes the stop word list from nltk and use a list of special characters as word delimiters.Every sentence is split into chunks at stop words occurence and phrase delimiters occurence.

The next step is to find out the frequency of the individual words in these phrases. Frequency is the count of occurence of the word.

    word_freq = defaultdict(int)
    word_degree = defaultdict(int)
    word_score = defaultdict(float)
    
    for phrase in phrases:
    	words = phrase.split(' ')
    	phrase_length = len(words)
    	for word in words:
    		word_freq[word]+=1
    		word_degree[word]+=phrase_length

Degree of a word is sum of length of all the phrases where the word occurs. Finally scoring for each word is done by 
> score(word) = degree(word) / freq(word).
    
    for word,freq in word_freq.items():
    	degree = word_degree[word]
    	score = ( 1.0 * degree ) / (1.0 * freq )
    	word_score[word] = score


Phrase scores are calcuated by sum of individual word scores in that phrase. Phrase with very large scores are considered to be keyphrases for the document.

RAKE algorithm is explained in the book [http://www.amazon.com/Text-Mining-Applications-Michael-Berry/dp/0470749822](http://www.amazon.com/Text-Mining-Applications-Michael-Berry/dp/0470749822 "Text Mining:Application and Theory")

There are several python implementations available.
