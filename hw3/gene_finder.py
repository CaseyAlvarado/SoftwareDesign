# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 11:24:42 2014

@author: YOUR NAME HERE
"""

# you may find it useful to import these variables (although you are not required to use them)
#from amino_acids import aa, codons
from amino_acids import codons
from amino_acids import aa


def collapse(L):
    """ Converts a list of strings to a string by concatenating all elements of the list """
    output = ""
    for s in L:
        output = output + s
    return output


def coding_strand_to_AA(dna):
    """ Computes the Protein encoded by a sequence of DNA.  This function
        does not check for start and stop codons (it assumes that the input
        DNA sequence represents an protein coding region).
        
        dna: a DNA sequence represented as a string
        returns: a string containing the sequence of amino acids encoded by the
                 the input DNA fragment
    """
    Seq = ''
    for i in range(0,len(dna),3): 
        triple = dna[i:i+3]
        print triple
        for k in range(len(codons)):
            if triple in codons[k]: 
                print "Casey Rocks"
                print codons[k]
                amino = aa[k]
                Seq+=amino
    return Seq
                
def coding_strand_to_AA_unit_tests(dna, expected):
    """ Unit tests for the coding_strand_to_AA function 
    input: INPUT_HERE, expected output: EXPECTED_OUTPUT_HERE, actual output: ACTUAL_OUTPUT_HERE"""
    print coding_strand_to_AA("ATGCGA")
    print coding_strand_to_AA("ATGCCCGCTTT")
    print coding_strand_to_AA("GGTAAA")
    print "input: " + str(dna) + ", expected output: " + str(expected) + ", actual output: " + coding_strand_to_AA(dna)


def get_reverse_complement(dna):
    """ Computes the reverse complementary sequence of DNA for the specfied DNA
        sequence
    
        dna: a DNA sequence represented as a string
        returns: the reverse complementary DNA sequence represented as a string
    """
    reverseDNA = ''
    newDNA = ''
    for i in range(len(dna)): 
           reverseDNA+= dna[-1-i]
    for k in range(len(dna)): 
        if reverseDNA[k] == 'A': 
            newDNA+='T'
        elif reverseDNA[k] =='T':
            newDNA+= 'A' 
        elif reverseDNA[k] =='G':
            newDNA+= 'C'
        elif reverseDNA[k] =='C':
            newDNA+= 'G' 
    return newDNA

def get_reverse_complement_unit_tests():
    """ Unit tests for the get_complement function """
        
    print get_reverse_complement("ATGCCCGCTTT")
    print get_reverse_complement("CCGCGTTCA")
    print get_reverse_complement("ACCTTGGAAAATTT")

def rest_of_ORF(dna):
    """ Takes a DNA sequence that is assumed to begin with a start codon and returns
        the sequence up to but not including the first in frame stop codon.  If there
        is no in frame stop codon, returns the whole string.
        
        dna: a DNA sequence
        returns: the open reading frame represented as a string
    """
    readingFrame = ''
    endCodons = ["TAG", "TAA", "TGA"]
    for i in range(0,len(dna),3):
        triple = dna[i:i+3]
        if triple in endCodons:
            readingFrame = readingFrame
            break
        else: 
            readingFrame+=triple   
    return readingFrame                    


def rest_of_ORF_unit_tests(dna, expected):
    """ Unit tests for the rest_of_ORF function """
    print rest_of_ORF("ATGCCGTAG")   
    print "input: " + str(dna) + ", expected output: " + str(expected) + ", actual output: " + rest_of_ORF(dna)
        
def find_all_ORFs_oneframe(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence and returns
        them as a list.  This function should only find ORFs that are in the default
        frame of the sequence (i.e. they start on indices that are multiples of 3).
        By non-nested we mean that if an ORF occurs entirely within
        another ORF, it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    strand = []
    startCodon = ["ATG"]
    for i in range(0,len(dna),3):
        triple = dna[i:i+3]
        if triple in startCodon: 
            strand.append(rest_of_ORF(dna[i:]))
    print strand
    return strand 

    
def find_all_ORFs_oneframe_unit_tests(dna, expected):
    """ Unit tests for the find_all_ORFs_oneframe function """

    print find_all_ORFs_oneframe("ATGCATGAATGTAGATAGATGTGCCC")
    print "input: " + str(dna) + ", expected output: " + str(expected) + ", actual output: " + find_all_ORFs_oneframe(dna)
        

def find_all_ORFs(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence in all 3
        possible frames and returns them as a list.  By non-nested we mean that if an
        ORF occurs entirely within another ORF and they are both in the same frame,
        it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """

    readingFrame0 = ''
    readingFrame1 = ''
    readingFrame2 = ''
    output = ''
    for k in range(0,3): 
        if k ==0: 
            readingFrame0 = find_all_ORFs_oneframe(dna[k:])
        elif k ==1: 
            readingFrame1 = find_all_ORFs_oneframe(dna[k:])
        elif k ==2:
            readingFrame2 = find_all_ORFs_oneframe(dna[k:])
    print 'Reading Frame 1: ' + str(readingFrame0) + ', Reading Frame 2: ' + str(readingFrame1) + ', Reading Frame 3: ' + str(readingFrame2)
    output = readingFrame0 + readingFrame1 + readingFrame2
    return output 
                  

def find_all_ORFs_unit_tests(dna, expected):
    """ Unit tests for the find_all_ORFs function """
        
    print find_all_ORFs("ATGCATGAATGTAG")
    print "input: " + str(dna) + ", expected output: " + str(expected) + ", actual output: " + find_all_ORFs(dna)

def find_all_ORFs_both_strands(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence on both
        strands.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
     
    #reverse first 
    #then take compliment 
    #then find ORF 
    reverseStrand = [] 
    original = [] 
    new = []
    reverseStrand.append(get_reverse_complement(dna)) 
    original.append(find_all_ORFs(dna))
    new.append(find_all_ORFs(reverseStrand))
    return original + new 
   
    

def find_all_ORFs_both_strands_unit_tests(dna, expected):
    """ Unit tests for the find_all_ORFs_both_strands function """

    print find_all_ORFs_both_strands("ATGCGAATGTAGCATCAAA")
    print "input: " + str(dna) + ", expected output: " + str(expected) + ", actual output: " + find_all_ORFs_both_strands(dna)
    

def longest_ORF(dna):
    """ Finds the longest ORF on both strands of the specified DNA and returns it
        as a string"""

    reverseComp = get_reverse_complement(dna)
    openFramesfromReverse = find_all_ORFs(reverseComp)
    openFramesfromNormal = find_all_ORFs(dna)
    all_ORFs = openFramesfromNormal + openFramesfromReverse
    longest = max(all_ORFs, key=len)
    return longest

def longest_ORF_unit_tests(dna, expected):
    """ Unit tests for the longest_ORF function """
    print longest_ORF("ATGCGAATGTAGCATCAAA")
    print "input: " + str(dna) + ", expected output: " + str(expected) + ", actual output: " + longest_ORF(dna)

def longest_ORF_noncoding(dna, num_trials):
    """ Computes the maximum length of the longest ORF over num_trials shuffles
        of the specfied DNA sequence
        
        dna: a DNA sequence
        num_trials: the number of random shuffles
        returns: the maximum length longest ORF """
    from random import shuffle
    listdna = list(dna)
    
    for k in range(0,num_trials):
        shuffle(listdna)
        collapse(listdna)
    return len(collapse(listdna))
    
        
        
def gene_finder(dna, threshold):
    """ Returns the amino acid sequences coded by all genes that have an ORF
        larger than the specified threshold.
        
        dna: a DNA sequence
        threshold: the minimum length of the ORF for it to be considered a valid
                   gene.
        returns: a list of all amino acid sequences whose ORFs meet the minimum
                 length specified.
    """
    finder = []
    twoStrands = find_all_ORFs_both_strands(dna) #this calls the function that finds the compliment of dna and finds all ORFs 
    print twoStrands    
    for k in range(len(twoStrands)): #go through the list "twoStrands"
        if twoStrands[k]>threshold:  #if the length of 
            print twoStrands[k]
            print len(twoStrands[k])
            finder.append(twoStrands[k])
    return finder 
            
        