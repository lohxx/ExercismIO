import re
from collections import Counter
def word_count(word):
	if '_' in word:
		word = word.replace('_',' ')
	regex = re.sub('\W',' ',word.lower())
	return Counter(regex.split())

