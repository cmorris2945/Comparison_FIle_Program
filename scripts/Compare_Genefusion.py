#! /usr/bin/python

import pandas as pd

#Star Gene fusion comparison
print ("Star Genes fusion differences Report:")
print("---------------------------------------")

print()
print ("The differences are:")
print ("           #FusionName   JunctionReadCount  SpanningFragCount  LeftBreakpoint  RightBreakpoint")
file1 = open("dnanexus_star_genefusion_subset.txt",'r')
file2 = open("crom_genes_star_genefusion_subset.txt",'r')

file1_lines = file1.readlines()
file2_lines = file2.readlines()

for i in range(len(file1_lines)):
		
	if file1_lines[i] != file2_lines[i]:
		print("Line " + str(i+1) + " doesn't match.")
		print("------------------------")
		print("DNA_nexus: " + file1_lines[i], end = ' ')
		print(" Cromwell: " + file2_lines[i])

print ("Note: ***If the results are empty it means no difference in Gene fusion results from star between DNA nexus and Cromwell***")
print()

file1.close()
file2.close()

#Arriba Gene fusion comparison
print ("Arriba Genes fusion differences Report:")
print("-----------------------------------------")

print()
print ("The differences are:")
print ("           #gene1 gene2 breakpoint1, breakpoint2, split_reads1, split_reads2, discordant_mates")
file1 = open("dnanexus_arriba_genefusion_subset.txt",'r')
file2 = open("crom_genes_arriba_genefusion_subset.txt",'r')

file1_lines = file1.readlines()
file2_lines = file2.readlines()

for i in range(len(file1_lines)):
		
	if file1_lines[i] != file2_lines[i]:
		print("Line " + str(i+1) + " doesn't match.")
		print("------------------------")
		print("DNA_nexus: " + file1_lines[i], end = ' ')
		print(" Cromwell: " + file2_lines[i])

print ("Note: ***If the results are empty it means no difference in Gene fusion results from arriba  between DNA nexus and Cromwell***")
print()

file1.close()
file2.close()

print ("______________________________________________________________________________________________________________________________________")
print ("______________________________________________________________________________________________________________________________________")
print()
