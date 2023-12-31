# BioTools

 Repository for bioinformatic tools developed by me.
 It will contain package of tools for working with biological data such as
biological sequences, NGS data and so on.

## Contents (will be updated regularly):
 
 1. **fastq_filter.py**:
      This is a script for filtering NGS reads from FASTQ files. Filtering criteria:
      - read length (default: 0 - 2^32)
      - GC-content (default: 0, 100)
      - mean sequencing quality threshold by phred scale (default: 0)
      
      Input:
       1.  a `dictionary` where keys are sequnce IDs, values are tuples of two elements:
         sequence and quality of reading (by phred scale), both are str type
       2. `gc_bounds`: bounding interval of GC-content values (%); if only one value is present,
         it will be treated as a higher bound
       3.  `length_bounds`: bounding interval of read lengths; if only one value is present,
         it will be treated as a higher bound
       4. `quality_threshold`: minimal mean sequence quality of the read
      
      Output: _dictionary_ containing filtered sequnces; it has the same structure as input dictionary. 
