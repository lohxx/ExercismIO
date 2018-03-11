from string import ascii_letters as alphabet


def rotate(text, key):
    msg,cipher = '',''
    for letter in list(text):
    	if letter in alphabet:
    		indexOf  =  alphabet.index(letter) + key
    		if indexOf > len(alphabet):
    			indexOf = indexOf -  alphabet.index(alphabet[-1])-1
    		msg += letter
    		cipher += alphabet[indexOf].upper() if letter.isupper() else alphabet[indexOf].lower()
    return text.translate(str.maketrans(msg,cipher))




