def fastq_filter(seqs: dict, gc_bounds: tuple = (0, 100), length_bounds: tuple = (0, 2**32), quality_threshold: float =
                 0) -> dict:
    """
    Filters reads form FASTQ files by read length, GC-content and sequence quality
    :param seqs: dict
    :param gc_bounds: tuple or float or int
    :param length_bounds: tuple or float or int
    :param quality_threshold: float
    :rtype: dict
    """

    filtered_seqs: dict = {}
    min_gc: float = 0
    max_gc: float = 0
    min_len: int = 0
    max_len: int = 0

    if isinstance(gc_bounds, int | float):
        min_gc = 0
        max_gc = gc_bounds
    elif isinstance(gc_bounds, tuple):
        min_gc = gc_bounds[0]
        max_gc = gc_bounds[1]
    if isinstance(length_bounds, int | float):
        min_len = 0
        max_len = length_bounds
    elif isinstance(length_bounds, tuple):
        min_len = length_bounds[0]
        max_len = length_bounds[1]

    def mean_quality(sequence: str):
        """
        * Counts mean quality (phred units) for read sequence
        * read: string of ASCII symbols encoding quality of sequence
        for each nucleotide
        """
        qual = 0
        for letter in sequence:
            qual += ord(letter) - 33
        mean_q = qual/len(sequence)
        return mean_q

    for key in seqs.keys():
        seq = seqs[key]
        read = seq[0]
        read_length = len(read)
        gc_content = ((read.count('G') + read.count('C'))/len(read)) * 100
        read_mean_qual = mean_quality(seq[1])
        if min_gc <= gc_content <= max_gc and min_len <= read_length <= max_len and read_mean_qual >= quality_threshold:
            filtered_seqs.update({key: seq})

    return filtered_seqs
