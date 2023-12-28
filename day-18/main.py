#import module
import math
print(math.pi * 5**2)


# difference between sum and fsum
numbers = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
print(sum(numbers))
print(math.fsum(numbers))



#Importing specific things from modules
from math import pi, tau


# Modules and namespaces
print(globals())

import numpy as np

print(globals())