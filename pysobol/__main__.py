from . import Sobol
import sys


N, D = int(sys.argv[1]), int(sys.argv[2])
file = sys.argv[3] if len(sys.argv) > 3 else None
for P in Sobol(N, D, file):
    print(' '.join(map(str, P)))
