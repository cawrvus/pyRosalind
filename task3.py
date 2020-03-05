from libs.gen import Allele
from libs.io import from_file
from libs.io import to_file
from libs.trans import combine
from libs.gen import Genotypes
from libs.inst import gens

to_file(combine(Genotypes, gens(from_file("datasets/3", ' ')), Allele.DOMINANT), "outputs/3")
