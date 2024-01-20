# 1) Make a decorator which calls a given function twice. You can assume the functions don't return anything important, but they may take arguments.

from functools import wraps

def double(func):
    @wraps(func)
    def inner(*args , **kwargs):
        func(*args, *kwargs)
        func(*args, *kwargs)
    
    return inner

#2) Imagine you have a list called books, which several functions in your application interact with. Write a decorator which causes your functions to run only if books is not empty.

from functools import wraps

books = []

def required_content(func):
    @wraps(func)
    def inner(*args , **kwargs):
        if books:
            func(*args, *kwargs)
    
    return inner

#3) Write a decorator called printer which causes any decorated function to print their return values. If the return value of a given function is None, printer should do nothing.

def printer(func):
    @wraps(func)
    def inner(*args, **kwargs):
        return_value = func(*args, **kwargs)
        if return_value is not None:
            print(return_value)
            
    return inner

