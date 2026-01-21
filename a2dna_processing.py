def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    if dna1 > dna2:
        return True
    else:
        return False


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    num_nucleotides = 0
    for char in dna:
        if nucleotide == char:
            num_nucleotides += 1
    return num_nucleotides    


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    for char in dna1:
        if dna2 in dna1:
            return True
        else:
            return False

def is_valid_sequence(dna):
    """ (str) -> bool

    Return True if and only if the dna sequence is valid.

    >>> is_valid_sequence('UATCG')
    False
    >>> is_valid_sequence('atAcg')
    False
    >>> is_valid_sequence('AATCG')
    True
    """
    for char in dna:
        if char in 'ATCG':
            return True
        else:
            return False

def insert_sequence(dna1, dna2, index):
    """ (str, str, int) -> str
    
    Return the DNA sequence obtained by inserting the dna2
    into dna2 at the given index.

    >>> insert_sequence('ATCGA', 'GCA', 2)
    'ATGCACGA'
    >>> insert_sequence('AGC','TGA', 3)
    'AGCTGA'
    """
    return dna1[:index] + dna2 + dna1[index:]

def get_complement(nucleotide):
    """ (str) -> str

    Return the nucleotide's complement.

    >>> get_complement('A')
    'T'
    >>> get_complement('C')
    'G'
    >>> get_complement('G')
    'C'
    """
    if nucleotide == 'G':
        return 'C'
    if nucleotide == 'C':
        return 'G'
    if nucleotide == 'T':
        return 'A'
    if nucleotide == 'A':
        return 'T'

def get_complementary_sequence(dna):
    """ (str) -> str

    Return the DNA sequence that is complementary
    to dna.

    >>> get_complementary_sequence('ATCG')
    'TAGC'
    >>> get_complementary_sequence('CCGA')
    'GGCT'
    """
    comp_sequence = ''
    for char in dna:
        if char == 'G':
            comp_sequence += 'C'
        if char == 'C':
            comp_sequence += 'G'
        if char == 'T':
            comp_sequence += 'A'
        if char == 'A':
            comp_sequence += 'T'
        
    return comp_sequence    
       
     
    
