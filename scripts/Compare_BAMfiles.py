#!/usr/bin/env python

import sys
import gzip
import pyfastx
import pysam

myvars = {}

for line in open('inputfiles.txt').readlines():
    if not '=' in line: continue

    left, right = line.split('=', 1)

    myvars[left.strip()] = right.strip()

#Input files
dnanexus_genome=(myvars['dnanexus_genome_bam'])
cromwell_genome=(myvars['cromwell_genome_bam'])
dnanexus_transcriptome=(myvars['dnanexus_transcriptome_BAM'])
cromwell_transcriptome=(myvars['cromwell_transcriptome_BAM'])

#****Comparison of genome alignment step***** 

print ("\u0332".join("Genome Alignment:"))

print ("\u0332".join("Genome alignment Summary:"))

#Total number of mapped reads
mapped_nexus=pysam.view("-c", "-F", "4", dnanexus_genome) 
print ("Mapped reads from DNA Nexus:", mapped_nexus)
mapped_cromwell=pysam.view("-c", "-F", "4", cromwell_genome) 
print ("Mapped reads from Cromwell:", mapped_cromwell)
#Total number of unmapped reads
unmapped_nexus=pysam.view("-c", "-f", "4", dnanexus_genome)
print ("Unmapped reads from DNA Nexus:", unmapped_nexus)
unmapped_cromwell=pysam.view("-c", "-f", "4", cromwell_genome) 
print ("Unmapped reads from Cromwell:", unmapped_cromwell)
#Total number of uniquely unmapped reads
uniquemapped_nexus=pysam.view("-bh", "-f", "3", "-F" "2316", "-c", dnanexus_genome) 
print ("Uniquely mapped reads from DNA Nexus:", uniquemapped_nexus)
uniquemapped_cromwell=pysam.view("-bh", "-f", "3", "-F" "2316", "-c", cromwell_genome)
print ("Uniquely mapped reads from Cromwell:", uniquemapped_cromwell)
print ("\u0332".join("Genome Alignment Comparison Summary:"))


if int(mapped_nexus) == int(mapped_cromwell):
	print ("Mapped Reads: No differences for genome alignment between DNAnexus and Cromwell")
else:
	print ("Mapped reads: Differences are observed from genome alignment between DNAnexus and Cromwell, the difference is:", int(mapped_nexus) - int(mapped_cromwell))
	
if int(unmapped_nexus) == int(unmapped_cromwell):

	print ("Unmapped Reads: No differences for genome alignment between DNAnexus and Cromwell")
else:
	print ("Unmpapped Reads: Differences are observed from genome alignment between DNAnexus and Cromwell, the difference is:", int(unmapped_nexus)-int(unmapped_cromwell))
	
if int(uniquemapped_nexus) == int(uniquemapped_cromwell):
	print ("Uniquely mapped reads: No differences for genome alignment between DNAnexus and Cromwell")
else:
	print ("Uniquely mapped reads: Differences are observed from genome alignment between DNAnexus and Cromwell, the difference is:", int(uniquemapped_nexus)-int(uniquemapped_cromwell))

print ("Note: **Difference value: Negative number means Cromwell had more reads and positive number means DNAnexus had more reads**")


#**Comparison of transcriptome alignment step************************************************************************************************************
print ('\n')
print ("\u0332".join("Transcriptome Alignment:"))

print ("\u0332".join("Transcriptome alignment Summary:"))

#Total number of mapped reads
trans_mapped_nexus=pysam.view("-c", "-F", "4", dnanexus_transcriptome) 
print ("Mapped reads from DNA Nexus:", trans_mapped_nexus)
trans_mapped_cromwell=pysam.view("-c", "-F", "4", cromwell_transcriptome) 
print ("Mapped reads from Cromwell:", trans_mapped_cromwell)
#Total number of unmapped reads
trans_unmapped_nexus=pysam.view("-c", "-f", "4", dnanexus_transcriptome) 
print ("Unmapped reads from DNA Nexus:", trans_unmapped_nexus)
trans_unmapped_cromwell=pysam.view("-c", "-f", "4", cromwell_transcriptome) 
print ("Unmapped reads from Cromwell:", trans_unmapped_cromwell)
#Total number of uniquely unmapped reads
trans_uniquemapped_nexus=pysam.view("-bh", "-f", "3", "-F" "2316", "-c", dnanexus_transcriptome) 
print ("Uniquely mapped reads from DNA Nexus:", trans_uniquemapped_nexus)
trans_uniquemapped_cromwell=pysam.view("-bh", "-f", "3", "-F" "2316", "-c", cromwell_transcriptome) 
print ("Uniquely mapped reads from Cromwell:", trans_uniquemapped_cromwell)
print ("\u0332".join("Transcritome alignment Comparison Summary:"))


if int(trans_mapped_nexus) == int(trans_mapped_cromwell):
	print ("Mapped Reads: No differences for transcriptome alignment between DNAnexus and Cromwell")
else:
	print ("Mapped reads: Differences are observed from transcriptome alignment between DNAnexus and Cromwell, the difference is:", int(trans_mapped_nexus) - int(trans_mapped_cromwell))
	
if int(trans_unmapped_nexus) == int(trans_unmapped_cromwell):

	print ("Unmapped Reads: No differences for transcriptome alignment between DNAnexus and Cromwell")
else:
	print ("Unmpapped Reads: Differences are observed from transcriptome alignment between DNAnexus and Cromwell, the difference is:", int(trans_unmapped_nexus)-int(trans_unmapped_cromwell))
	
if int(trans_uniquemapped_nexus) == int(trans_uniquemapped_cromwell):
	print ("Uniquely mapped reads: No differences for transcriptome alignment between DNAnexus and Cromwell")
else:
	print ("Uniquely mapped reads: Differences are observed from transcriptome alignment between DNAnexus and Cromwell, the difference is:", int(trans_uniquemapped_nexus)-int(trans_uniquemapped_cromwell))

print ("Note: **Difference value: Negative number means Cromwell had more reads and positive number means DNAnexus had more reads**")

print ("______________________________________________________________________________________________________________________________________")
print ("______________________________________________________________________________________________________________________________________")
print()

