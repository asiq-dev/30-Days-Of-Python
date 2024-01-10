# 3) Use the mul function in the operator module to create a partial called double that always provides 2 as the first argument.

from operator import mul
from functools import partial

double = partial(mul, 2)

print(double(5))