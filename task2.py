from libs.io import from_file
from libs.io import to_file
from libs.trans import rev_complement
from libs.inst import dna

to_file(rev_complement(dna(from_file("datasets/2"))), "outputs/2")
