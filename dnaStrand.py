pairs = {'A':'T','T':'A','C':'G','G':'C'}
def DNA_strand(dna):
    #return ''.join([pairs[x] for x in dna])
    return dna.translate(str.maketrans("ATCG","TAGC"))

print(DNA_strand("ATCG"))