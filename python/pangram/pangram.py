def is_pangram(word):
	alphabet = list('abcdefghijklmnopqrstuvwxyz')
	rep = word.replace('.','').lower()
	for i in alphabet:
		if not(i in rep):
			return False
	return True


    