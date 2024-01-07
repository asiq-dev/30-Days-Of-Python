# 1) Write a generator that generates prime numbers in a specified range.

def gen_primes(limit):
    for number in range(2, limit):
        for divisor in range(2, number):
            if number % divisor == 0:
                break
        else:
            yield number

limit = int(input("Enter limit number for check prime number: "))
prime = gen_primes(limit)

print(*prime, sep=",")


# 2) Below we have an example where map is being used to process names in a list. Rewrite this code using a generator expression.
# names = [" rick", " MORTY  ", "beth ", "Summer", "jerRy    "]
# names = map(lambda name: name.strip().title(), names)

names = [" rick", " MORTY  ", "beth ", "Summer", "jerRy    "]
names = (name.strip().title() for name in names )
print(*names, sep=",")