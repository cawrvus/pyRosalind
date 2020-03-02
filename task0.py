from cmd import *
from libs.utils import from_file
from libs.utils import to_file

to_file(count(dna(from_file("datasets/0"))), "outputs/0", ' ')
