#! /usr/bin/python

import pandas as pd
import sys

myvars = {}

for line in open('inputfiles.txt').readlines():
    if not '=' in line: continue

    left, right = line.split('=', 1)

    myvars[left.strip()] = right.strip()

#Genes.results files to genes TPM file conversion
nexus_tpm = pd.read_csv(myvars['dnanexus_genesresults'], sep='\t', usecols=['gene_symbol', 'TPM'])
crom_tpm=pd.read_csv(myvars['cromwell_genesresults'], sep='\t', usecols=['gene_symbol', 'TPM'])

nexus_tpm_string= nexus_tpm.to_csv(index=False, sep='\t')
sys.stdout = open('dnanexus_genes_tpm.txt','wt')
print(nexus_tpm_string)

crom_tpm_string= crom_tpm.to_csv(index=False, sep='\t')
sys.stdout = open('crom_genes_tpm.txt','wt')
print(crom_tpm_string)

#isoform.results files isoform TPM file conversion
nexus_tpm = pd.read_csv(myvars['dnanexus_isoformresults'], sep='\t', usecols=['transcript_id', 'TPM'])
crom_tpm=pd.read_csv(myvars['cromwell_isoformresults'], sep='\t', usecols=['transcript_id', 'TPM'])


nexus_tpm_string= nexus_tpm.to_csv(index=False, sep='\t')
sys.stdout = open('dnanexus_isoforms_tpm.txt','wt')
print(nexus_tpm_string)

crom_tpm_string= crom_tpm.to_csv(index=False, sep='\t')
sys.stdout = open('crom_isoforms_tpm.txt','wt')
print(crom_tpm_string)


#Genes.results files to genes expected count file conversion
nexus_tpm = pd.read_csv(myvars['dnanexus_genesresults'], sep='\t', usecols=['gene_symbol', 'expected_count'])
crom_tpm=pd.read_csv(myvars['cromwell_genesresults'], sep='\t', usecols=['gene_symbol', 'expected_count'])

nexus_tpm_string= nexus_tpm.to_csv(index=False, sep='\t')
sys.stdout = open('dnanexus_genes_expcount.txt','wt')
print(nexus_tpm_string)

crom_tpm_string= crom_tpm.to_csv(index=False, sep='\t')
sys.stdout = open('crom_genes_expcount.txt','wt')
print(crom_tpm_string)

#isoform.results files isoform expected count file conversion
nexus_tpm = pd.read_csv(myvars['dnanexus_isoformresults'], sep='\t', usecols=['transcript_id', 'expected_count'])
crom_tpm=pd.read_csv(myvars['cromwell_isoformresults'], sep='\t', usecols=['transcript_id', 'expected_count'])


nexus_tpm_string= nexus_tpm.to_csv(index=False, sep='\t')
sys.stdout = open('dnanexus_isoforms_expcount.txt','wt')
print(nexus_tpm_string)

crom_tpm_string= crom_tpm.to_csv(index=False, sep='\t')
sys.stdout = open('crom_isoforms_expcount.txt','wt')
print(crom_tpm_string)
