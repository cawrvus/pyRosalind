from cmd import *
from libs.gen import Allele
from libs.utils import from_file
from libs.utils import to_file

to_file(gen_combine(gen_create(from_file("datasets/3", ' ')), Allele.DOMINANT), "outputs/3")
