#!/usr/bin/env python

import sys
import gzip
import pyfastx
import pysam

#(usage: ./dnanexus_cromwell_compare.py > dnanexus_cromwell_comparison_results.txt)

myvars = {}

for line in open('inputfiles.txt').readlines():
    if not '=' in line: continue

    left, right = line.split('=', 1)

    myvars[left.strip()] = right.strip()

#Comparison of trimming step 
print ("\u0332".join ("Comparison of read trimming process:"))

dnanexus = pyfastx.Fastq (myvars['dnanexusr1']) #provide dnanexus trimmed file
print ("The total number of reads in dnanexus R1 are:", len (dnanexus))
print ("The total number of bases in dnanexus R1 are:", dnanexus.size)
cromwell = pyfastx.Fastq (myvars['dnanexusr1']) #provide cromwell trimmed file
print ("The total number of reads in cromwell R1 are:", len (cromwell))
print ("The total number of bases in cromwell R1 are:", cromwell.size)

print('\n')

print ("\u0332".join("Trimming comparison results:"))

a= len(dnanexus)
b= len(cromwell)
if a == b:
	print ("There are no difference in the total number of trimmed reads from DNAnexus and Cromwell")
else:
	print ("The total number of trimmed reads from DNAnexus and Cromwell are not same, the difference is:", len (dnanexus)-len (cromwell))
	


c= dnanexus.size
d= cromwell.size
if c == d:
	print ("There are no difference in the total number of bases from DNAnexus and Cromwell")
else:
	print ("The total number of bases from DNAnexus and Cromwell are not same, the difference is: ", dnanexus.size-cromwell.size)

print ("______________________________________________________________________________________________________________________________________")
print ("______________________________________________________________________________________________________________________________________")
print()
