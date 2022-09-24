#! /usr/bin/python

import pandas as pd

#Genes TPM comparison
print ("Genes TPM difference Report:")
print("-------------------------------")

print()
print ("The differences are:")
file1 = open("dnanexus_genes_tpm.txt",'r')
file2 = open("crom_genes_tpm.txt",'r')

file1_lines = file1.readlines()
file2_lines = file2.readlines()

for i in range(len(file1_lines)):
		
	if file1_lines[i] != file2_lines[i]:
		print("Line " + str(i+1) + " doesn't match.")
		print("------------------------")
		print("DNA_nexus_genes_TPM: " + file1_lines[i], end = ' ')
		print("Cromwell_genes_TPM: " + file2_lines[i])

print ("Note: ***If the results are empty it means no difference in TPM between DNA nexus and Cromwell***")
print()

file1.close()
file2.close()

print ()
#Isoforms TPM comparison
print ("Isoforms TPM difference Report:")
print("----------------------------------")

print()
print ("The differences are:")
file1 = open("dnanexus_isoforms_tpm.txt",'r')
file2 = open("crom_isoforms_tpm.txt",'r')

file1_lines = file1.readlines()
file2_lines = file2.readlines()

for i in range(len(file1_lines)):
		
	if file1_lines[i] != file2_lines[i]:
		print("Line " + str(i+1) + " doesn't match.")
		print("------------------------")
		print("DNA_nexus_isoforms_TPM: " + file1_lines[i], end = ' ')
		print("Cromwell_isoforms_TPM: " + file2_lines[i])

print ("Note: ***If the results are empty it means no difference in TPM between DNA nexus and Cromwell***")

file1.close()
file2.close()
print ("___________________________________________________________________________________________________")
print ()
#Genes expcount comparison
print ("Genes expected count difference Report:")
print("-----------------------------------------")

print()
print ("The differences are:")
file1 = open("dnanexus_genes_expcount.txt",'r')
file2 = open("crom_genes_expcount.txt",'r')

file1_lines = file1.readlines()
file2_lines = file2.readlines()

for i in range(len(file1_lines)):
		
	if file1_lines[i] != file2_lines[i]:
		print("Line " + str(i+1) + " doesn't match.")
		print("------------------------")
		print("DNA_nexus_genes_expcount: " + file1_lines[i], end = ' ')
		print("Cromwell_genes_expcount: " + file2_lines[i])

print ("Note: ***If the results are empty it means no difference in expcount between DNA nexus and Cromwell***")
print()

file1.close()
file2.close()

print ()
#Isoforms expected count comparison
print ("Isoforms expcount difference Report:")
print("-------------------------------------")

print()
print ("The differences are:")
file1 = open("dnanexus_isoforms_expcount.txt",'r')
file2 = open("crom_isoforms_expcount.txt",'r')

file1_lines = file1.readlines()
file2_lines = file2.readlines()

for i in range(len(file1_lines)):
		
	if file1_lines[i] != file2_lines[i]:
		print("Line " + str(i+1) + " doesn't match.")
		print("------------------------")
		print("DNA_nexus_isoforms_expcount: " + file1_lines[i], end = ' ')
		print("Cromwell_isoforms_expcount: " + file2_lines[i])

print ("Note: ***If the results are empty it means no difference in expcount between DNA nexus and Cromwell***")

file1.close()
file2.close()

print ("______________________________________________________________________________________________________________________________________")
print ("______________________________________________________________________________________________________________________________________")
print()
