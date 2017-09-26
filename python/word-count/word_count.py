import string
from collections import Counter

exp = lambda stri : stri.split() if ' ' in stri else stri.replace(',','_').split('_')

def word_count(word):
	stri = ''
	if word.find(string.punctuation) and ',' not in word:
		for i,item in enumerate(word):
			if word[i] not in string.punctuation:
				stri += word[i]
		return Counter(exp(stri.lower()))
	else:
		return Counter(exp(word.lower().replace('.','')))