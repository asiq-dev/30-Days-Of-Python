# 1) Ask the user for an integer between 1 and 10 (inclusive). If the number they give is outside of the specified range, 
# raise a ValueError and inform them that their choice was invalid.

number = int(input("Enter a number between 1 to 10: "))

if number not in range(1, 11):
    raise ValueError(f"The number must be between 1 and 10. You entered {number}.")




# 2) Below you'll find a divide function. Write exception handling so that we catch ZeroDivisionError exceptions, TypeError exceptions, 
# and other kinds of ArithmeticError.

def divide(a, b):
    try:
        print(a / b)
    except ZeroDivisionError:
        print("Cannot divide by zero")
    except TypeError:
        print(f"Both values must be numbers. Cannot divide {a} and {b}")
    except ArithmeticError:
        print("Could not complete the division. The numbers were likely too large")

print(divide(15, 5))


# 3) Below you'll find an itemgetter function that takes in a collection, and either a key or index. Catch any instances of 
# KeyError or IndexError, and write the exception to a file called log.txt, along with the arguments that caused this issue. 
# Once you have written to the log file, reraise the original exception.
def log_exceptions(exception, fn, **kwargs):
    values = ",".join(f"{key} = {value!r}" for key, value in kwargs.items())
    with open("log.txt", "a") as log_file:
        log_file.write(f"Exception: {exception}, Function: {fn}, Values: {values}\n")

def itemgetter(collection, identifier):
    try:
        return collection[identifier]
    except (IndexError, KeyError, TypeError) as ex:
        log_exceptions(ex, "itemgetter", collection = collection, identifier = identifier)
        raise 