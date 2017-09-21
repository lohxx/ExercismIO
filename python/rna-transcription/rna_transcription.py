def to_rna(dna):
	dictdna,rna = {'g':'c','c':'g','t':'a','a':'u'},''
	for i in dna.lower():
		for x in list(dictdna):
			if  i == x:
				rna += dictdna[i]
			else:
				rna += ''
	if len(rna) != len(dna):
		return ''
	return rna.upper()



