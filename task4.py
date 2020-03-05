from libs.io import from_file
from libs.io import to_file
from libs.trans import evolve
from libs.inst import popul
from libs.seq import fib

to_file(evolve(popul(from_file("datasets/4", ' ', cast=int)), fib), "outputs/4")
