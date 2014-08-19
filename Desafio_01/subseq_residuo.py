# Written by Mathieu Lienard--Mayor, UFRGS, 2014-2

import re;
re_A = re.compile('[ACGT]A[ACGT]A[ACGT]');
re_C = re.compile('[ACGT]C[ACGT]C[ACGT]');
re_G = re.compile('[ACGT]G[ACGT]G[ACGT]');
re_T = re.compile('[ACGT]T[ACGT]T[ACGT]');

file = open('Homosapiens_Chromosome7.fasta', 'r');
header = file.readline(); # first line is the header

# reading the file
seq = file.read().strip();
# matching the regular expressions
seq_A = re_A.findall(seq);
seq_C = re_C.findall(seq);
seq_G = re_G.findall(seq);
seq_T = re_T.findall(seq);

size = len(seq_A) + len(seq_C) + len(seq_G) + len(seq_T);

print('Number of subsequences : ' + str(size));

file.close();

# Written by Mathieu Lienard--Mayor, UFRGS, 2014-2
