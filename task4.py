from cmd import *
from libs.utils import from_file
from libs.utils import to_file

to_file(evolve(popul(from_file("datasets/4", ' ', cast=int))), "outputs/4")
