# 1
numbers = [1, 2, 3, 4, 5]

try:
    print(numbers[100])  # <- Out of range index
except IndexError:
    print("The requested index is out of range")
except LookupError:
    print("Could not retrieve that value.")




# 2
person = {
    "name": "Phil",
    "city": "Budapest"
}

try:
    print(person["age"])  # <- Referencing an undefined key
except IndexError:
    print("The requested index is out of range")
except LookupError:
    print("Could not retrieve that value.")


# 3
    
numbers = [1, 2, 3, 4, 5]

try:
    print(numbers[100])
except LookupError as ex:
    print(f"Error: {ex}")


# 4
raise ValueError ("I raised this ValueError for no reason!")



# 5
def intify(number):
    try:
        return int(number)
    except ValueError:
        try:
            f_number = float(number)
        except ValueError:
            raise ValueError(f"could not convert string to an integer: {number}") from None
        else:
            return round(f_number)

with open("numbers.txt", "r") as numbers_file:
    numbers = [intify(number) for number in numbers_file]
