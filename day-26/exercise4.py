# 4) Create a read function using a partial that opens a file in read ("r") mode.

from functools import partial

read = partial(open, mode="r")

# We can now use this read function just like the open function: it even works in context managers!