def is_isogram(string):
	stri = [characters.lower() for characters in string if characters.isalpha()]
	print(stri)
	return len(set(stri)) == len(stri)	

