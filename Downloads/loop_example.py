##for x in xrange(2,21):
	##for y in xrange(1,4):
		##print x**y

##print "you did it!"

print("Enter sequence below to check for ORFs:")
seq=input()

print("\nWhat should I name the text file?")
file_name=input()

for x in range(0,len(seq)): 		#This loop will examine every possible 3-base sequence for a possible ATG
	current_bases=seq[x:(x+3)] 		#The variable 'x' defines which 3 bases are being examined
	if current_bases.upper() in ('ATG'): 		#If the current slice of 3 bases is an ATG, investigate further
		start=x						#set the index of the start codon
		for y in range(1,len(seq)):		#begin reading the codons of the sequence
			first=start+(3*y) 		#set the index of the next codon to examine
			end=first+3 		#set the index of where the next codon ends
			codon=seq[first:end]		#slice the codon based on the above indexes
			if codon.upper() in ('TGA','TAA','TAG'):		#check if the current codon is a stop
				print('\n		There is an open reading frame starting at base {0} and ending at base {1}:\n{2}'.format(start+1,end,seq[start:end]))
				with open('{0}.txt'.format(file_name), "a") as myfile: 		#write the output to a text file
					myfile.write('		There is an open reading frame starting at base {0} and ending at base {1}:\n{2}\n\n'.format(start+1,end,seq[start:end]))
				break		#This breaks only the nested 'for'-loop so the program doesn't read through the stop and give you extra ORFs that don't exist

print("\nWant to Translate? Enter the number location of the first base in the sequence:")
start_input=int(input())

print("\nEnter the number location of the lase base in the sequence:")
end_input=int(input())

py_start=(start_input)-1

ORF=seq[py_start:end_input] #extract the ORF for reading below

translation=''
for x in range(0, int(len(ORF)/3)): #value of x indicates which codon is being read
	first=(3*x) #every iteration of the loop moves this index forward 3 places
	last=first+3
	codon=ORF[first:last] #define the current codon
	if codon.upper() in ('TTT','TTC'): #translate the current codon
		translation=translation+'F'
	elif codon.upper() in ('ATG'):
		translation=translation+'M'
	elif codon.upper() in ('TTA','TTG','CTT','CTC','CTA','CTG'):
		translation=translation+'L'
	elif codon.upper() in ('ATT','ATC','ATA'):
		translation=translation+'I'
	elif codon.upper() in ('GTT','GTC','GTA','GTG'):
		translation=translation+'V'
	elif codon.upper() in ('TCT','TCC','TCA','TCG'):
		translation=translation+'S'
	elif codon.upper() in ('CCT','CCC','CCA','CCG'):
		translation=translation+'P'
	elif codon.upper() in ('ACT','ACC','ACA','ACG'):
		translation=translation+'T'
	elif codon.upper() in ('GCT','GCC','GCA','GCG'):
		translation=translation+'A'
	elif codon.upper() in ('TAT','TAC'):
		translation=translation+'Y'
	elif codon.upper() in ('CAT','CAC'):
		translation=translation+'H'
	elif codon.upper() in ('CAA','CAG'):
		translation=translation+'Q'
	elif codon.upper() in ('AAT','AAC'):
		translation=translation+'N'
	elif codon.upper() in ('AAA','AAG'):
		translation=translation+'K'
	elif codon.upper() in ('GAT','GAC'):
		translation=translation+'D'
	elif codon.upper() in ('GAA','GAG'):
		translation=translation+'E'
	elif codon.upper() in ('TGT','TGC'):
		translation=translation+'C'
	elif codon.upper() in ('CGT','CGC','CGA','CGG','AGA','AGG'):
		translation=translation+'R'
	elif codon.upper() in ('AGT','AGC'):
		translation=translation+'S'
	elif codon.upper() in ('GGT','GGC','GGA','GGG'):
		translation=translation+'G'
	elif codon.upper() in ('TGG'):
		translation=translation+'W'
	elif codon.upper() in ('TAA','TAG','TGA'):
		translation=translation+'*'
		break
	else:
		print('ERROR: UNRECOGNIZED CODON {}'.format(codon))
		break

print(translation)
