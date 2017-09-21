
checks = lambda x,y:not(x==y)

def distance(dna,dna2):
	cont,hamming = 0,0
	if len(dna) != len(dna2):
		 raise ValueError("Invalid input")
	for i in dna:
		if checks(i,dna2[cont]):
			hamming += 1
		cont+=1 
	return hamming
    
