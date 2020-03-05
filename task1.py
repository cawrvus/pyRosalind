from libs.io import from_file
from libs.io import to_file
from libs.trans import convert
from libs.rna import RNA
from libs.inst import dna

to_file(convert(dna(from_file("datasets/1")), RNA), "outputs/1")
