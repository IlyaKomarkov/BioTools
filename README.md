# BioTools

 Repository for bioinformatic tools developed by me.
 It will contain package of tools for working with biological data such as
biological sequences, NGS data and so on.

 Packages list (will be updated regularly):
 
 1. **fastq_filter.py**:
      This is a script for filtering NGS reads from FASTQ files. Filtering criteria:
      - read length bounds (default: 0 - 2^32)
      - GC-content bounds (default: 0, 100)
      - mean sequencing quality threshold using phred scale (default: 0)
      Script's input: a dictionary where keys are sequnce IDs, values are tuples
      of two elements: sequence and quality of reading (by phred scale), both are str type.
      Output: dictionary containing filtered sequnces; it has the same structure as input dict. 
