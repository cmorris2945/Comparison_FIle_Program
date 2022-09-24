#! /usr/bin/python

import subprocess

subprocess.run("python3 ./scripts/Compare_Trimfiles.py && python3 ./scripts/Compare_BAMfiles.py && python3 ./scripts/Convert_resultsfile_to_TPM_expectedcount_file.py && python3 ./scripts/Compare_TPM_ECfiles.py && python3 ./scripts/Convert_fusionfiles_to_breakpoints_reads_file.py && python3 ./scripts/Compare_Genefusion.py && python3 ./scripts/Compare_metricsfiles.py ", shell=True)
