#! /usr/bin/python

import pandas as pd

#Genes TPM comparison
print ("RNAseq Metrics differences Report:")
print("-------------------------------")

print()
print ("The differences are:")

myvars = {}

for line in open('inputfiles.txt').readlines():
    if not '=' in line: continue

    left, right = line.split('=', 1)

    myvars[left.strip()] = right.strip()

file1 = open(myvars['dnanexus_metrics'],'r')
file2 = open(myvars['cromwell_metrics'],'r')

file1_lines = file1.readlines()
file2_lines = file2.readlines()

for i in range(len(file1_lines)):
		
	if file1_lines[i] != file2_lines[i]:
		print("Line " + str(i+1) + " doesn't match.")
		print("------------------------")
		print("DNA_nexus: " + file1_lines[i], end = ' ')
		print(" Cromwell: " + file2_lines[i])

print ("Note: ***If the results are empty it means no difference in Metrics between DNA nexus and Cromwell***")
print()

file1.close()
file2.close()

print ("______________________________________________________________________________________________________________________________________")
print ("______________________________________________________________________________________________________________________________________")
print()
