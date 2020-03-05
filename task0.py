from libs.io import from_file
from libs.io import to_file
from libs.trans import matches
from libs.inst import dna
from libs.const import DNA_NUCLEOTIDES

to_file(matches(dna(from_file("datasets/0")), DNA_NUCLEOTIDES), "outputs/0", ' ')
