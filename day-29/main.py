# defining a simple decorator

from typing import Callable

def example_decorator(func:Callable) -> Callable:
    def inner():
        print(f"Now calling {func.__name__}...")
        func()
        print(f"{func.__name__} has ended.")

    return inner

@example_decorator  #way-1
def greeter():
    print("Hello!")

# greeter = example_decorator(greeter) #way -2

greeter()


# Decorating function with arguments

from typing import Callable, Union

Real = Union[int, float]

def calculate(func: Callable) -> Callable:
    def inner (*args, **kwargs):
        print("Calculating..")

        func(*args, **kwargs)

    return inner

@calculate
def add(a: Real, b: Real):
    print(a+b)

add(1,5)




#  a real world example of run one time
from functools import wraps
from time import perf_counter
from typing import Callable, List, Set

def stopwatch(func: Callable) -> Callable:
    @wraps(func)
    def inner(*args, **kwargs):
        start_time = perf_counter()
        func(*args, **kwargs)
        stop_time = perf_counter()

        print(f"{func.__name__} ran in {stop_time - start_time:.5f}s")

    return inner

@stopwatch
def make_list(size: int) -> List:
    return list(range(size))

@stopwatch
def make_set(size: int) -> Set:
    return set(range(size))

make_list(100000)
make_set(100000)



#  a real world example of run several times and avg time
from functools import wraps
from time import perf_counter
from typing import Callable, List, Set
from math import fsum

def stopwatch(func: Callable) -> Callable:
    @wraps(func)
    def inner(*args, **kwargs):
        times = []
        for _ in range(10):
            start_time = perf_counter()
            func(*args, **kwargs)
            stop_time = perf_counter()

            elapsed = stop_time - start_time
            times.append(elapsed)
        avg_time = fsum(times) / len(times)

        print(f"{func.__name__} ran in {avg_time:.5f}s on average")

    return inner

@stopwatch
def make_list(size: int) -> List:
    return list(range(size))

@stopwatch
def make_set(size: int) -> Set:
    return set(range(size))

make_list(100000)
make_set(100000)