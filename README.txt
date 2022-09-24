****Instruction to perform comparsion of files between DNAnexus and Cromwell for RNAseq*****

Make sure you have the following file in the folder: inputfiles.txt, README.txt, scripts folder, RNAseq_compare.py

Step1: Provide the exact path for all the required files in 'inputfiles.txt'

...................................................................................................................................
Example:
#path to trimmed fastq files
dnanexusr1=/media/CCR1.R1.fastq.gz
cromwellr1=/media/CCR2.R1.fastq.gz

#path to BAM files
dnanexus_genome_bam=/media/CCR1.bam
cromwell_genome_bam=/media/CCR2.bam
dnanexus_transcriptome_BAM=/media/CPR1.bam
cromwell_transcriptome_BAM=/media/CPR2.bam

#path to genes.results file
dnanexus_genesresults=/media/DNA_NEXUS_SL477618.genes.results
cromwell_genesresults=/media/CROMWELL_SL477618_2.genes.results
dnanexus_isoformresults=/media/DNA_NEXUS_SL477618.isoforms.results
cromwell_isoformresults=/media/CROMWELL_SL477618.isoforms.results

#path to gene fusion files
dnanexus_starfusion=/media/DNA_NEXUS_SL477618.star-fusion.fusion_predictions.tsv
cromwell_starfusion=/media/CROMWELL_star-fusion.fusion_predictions.tsv
dnanexus_arribafusion=/media/ARRIBA_DNA_NEXUS_FUSION_SL430702.arriba.fusion_predictions.tsv
cromwell_arribafusion=/media/CROMWELL_SL430702.arriba.fusion_predictions.tsv

#path to metrics files
dnanexus_metrics=/media/DNA_NEXUS_SL477618.metrics.tsv
cromwell_metrics=/media/CROMWELL_SL477618.metrics.tsv
..........................................................................................................................................

Step2: 

Convert the python files to executable files: 

chmod 777 /scripts/*.py
chmod 777 RNAseq_compare.py

Step3: Run the command in the same folder:  python3 RNAseq_compare.py > Samplename_RNAseqcompare_report.txt

Step4: View the results in the output file: Samplename_RNAseqcompare_report.txt

Note: The speed of the process may vary based on the available computational resources. 
