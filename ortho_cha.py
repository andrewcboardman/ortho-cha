import sys
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna


def split_seqs():
	pass

def combine_seqs():
	pass

def generate_domain():
	pass

def Fitness(domains):
	pass
# read in catalyst sequence
C1 = [Seq(line) for line in sys.argv[1:]]

# reverse domains 
CatDomains = [seq.reverse_complement() for seq in C1]

for N in range(10):
	for n in range(100):
		# Design first hairpin (based on catalyst sequence)
		Domains[3] = generate_domain()
		
		H1 = combine_seqs((*CatDomains,d4_,d3_,d2_,d5_,d6_))
		H2 = combine_seqs((d4_,d2_,d3_,d4,d3))

		if CheckHairpin(H1) and CheckHairpin(H2):
			if CheckDomains(all_domains):
				break

CheckDomains(all_domains)
