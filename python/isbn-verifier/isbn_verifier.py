import re
import string


def Validations(text):
	alpha  = string.ascii_uppercase.replace('X','')
	letter = re.findall(r'[a-zA-Z]',text)[0] if len(re.findall(r'[a-zA-Z]',text)) >= 1 else ''
	if text == '' or text.count('X') > 1 or letter in list(alpha) or ('X' == letter and 'X' != text[len(text)-1]):
		return False

def verify(isbn):
    total,digits = 0,[x for x in range(10,-1,-1)]
    if Validations(isbn) == False:
    	return False
    for index,item in enumerate(re.findall(r'\w', isbn)):
    	total +=  digits[index] * int(item) if item != 'X' else digits[index] * 10
    return True if total % 11 == 0 else False







