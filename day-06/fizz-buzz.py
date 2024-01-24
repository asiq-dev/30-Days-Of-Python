# Today's project is actually a very common interview question, which revolves around a childhood counting game called Fizz Buzz.


for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("Fizz Buzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)