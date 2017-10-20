import re

def hey(string):
	regex = {'Sure.':string.rfind('?'),'Fine. Be that way!':string.isspace() or string == '','Whoa, chill out!':string.isupper() or string.endswith('!')}
	expressions = list(regex.values())	
	for index,exp in enumerate(regex):
		if not expressions[index] < 1 :
			return exp
	else:
		return 'Whatever.'
