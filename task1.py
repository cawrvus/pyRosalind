from cmd import *
from libs.utils import from_file
from libs.utils import to_file

to_file(dna2rna(dna(from_file("datasets/0"))), "outputs/1")
