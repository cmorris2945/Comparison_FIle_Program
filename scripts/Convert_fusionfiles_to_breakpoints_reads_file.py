#! /usr/bin/python

import pandas as pd
import sys

myvars = {}

for line in open('inputfiles.txt').readlines():
    if not '=' in line: continue

    left, right = line.split('=', 1)

    myvars[left.strip()] = right.strip()
      
#Star Genes fusion files to subset file with fusiongene name, breakpoints, junction and spanning reads
nexus_genefusion = pd.read_csv(myvars['dnanexus_starfusion'], sep='\t', usecols=['#FusionName', 'JunctionReadCount', 'SpanningFragCount', 'LeftBreakpoint','RightBreakpoint'])
crom_genefusion = pd.read_csv(myvars['cromwell_starfusion'], sep='\t', usecols=['#FusionName', 'JunctionReadCount', 'SpanningFragCount', 'LeftBreakpoint','RightBreakpoint'])

nexus_gf_string= nexus_genefusion.to_csv(index=False, sep='\t')
sys.stdout = open('dnanexus_star_genefusion_subset.txt','wt')
print(nexus_gf_string)

crom_gf_string= crom_genefusion.to_csv(index=False, sep='\t')
sys.stdout = open('crom_genes_star_genefusion_subset.txt','wt')
print(crom_gf_string)

#Arriba Genes fusion files to subset file with fusiongene name, breakpoints, junction and spanning reads
nexus_genefusion_arriba = pd.read_csv(myvars['dnanexus_arribafusion'], sep='\t', usecols=['#gene1', 'gene2', 'breakpoint1', 'breakpoint2', 'split_reads1', 'split_reads2', 'discordant_mates'])
crom_genefusion_arriba = pd.read_csv(myvars['cromwell_arribafusion'], sep='\t', usecols=['#gene1', 'gene2', 'breakpoint1', 'breakpoint2', 'split_reads1', 'split_reads2', 'discordant_mates'])

nexus_gf_string_arriba= nexus_genefusion_arriba.to_csv(index=False, sep='\t')
sys.stdout = open('dnanexus_arriba_genefusion_subset.txt','wt')
print(nexus_gf_string_arriba)

crom_gf_string_arriba= crom_genefusion_arriba.to_csv(index=False, sep='\t')
sys.stdout = open('crom_genes_arriba_genefusion_subset.txt','wt')
print(crom_gf_string_arriba)
