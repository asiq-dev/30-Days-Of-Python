#1) Ask the user to enter their given name and surname in response to a single prompt. Use split to extract the names, 
#and then assign each name to a different variable. For this exercise, you can assume that the user has a single given name 
#and a single surname.

full_names = input("Enter the user given name and surname separated by comma: ")
split_name= full_names.split(',')
given_name = split_name[0]
surname = split_name[1]
print(given_name)
print(surname)

#2) Print the list, [1, 2, 3, 4, 5], in the format 1 | 2 | 3 | 4 | 5 using the join method. Remember that you can only join
#collections of strings, so you’re going to need to do some initial processing of the list of numbers.

numbers = [1, 2, 3, 4, 5]
str_numbers = []
for number in numbers:
    str_numbers.append(str(number))
print(f"the numbers are: {' | '.join(str_numbers)}")


#3) Each quote is a string, but each string actually contains quote characters at the start and end. Using slicing, 
#extract the text from each string, without these extra quote marks, and print each quote. You may also want to try a solution using strip.
quotes = [
    "'What a waste my life would be without all the beautiful mistakes I've made.'",
    "'A bend in the road is not the end of the road... Unless you fail to make the turn.'",
    "'The very essence of romance is uncertainty.'",
    "'We are not here to do what has already been done.'"
 ]

for qoute in quotes:
     print(qoute.strip("'"))


#4)Ask the user to enter a word, and then print out the length of the word. You should account for any excess whitespace 
# in the user’s input, so you’re going to have to process the string before you find its length.

words = input("Enter a words: ").strip()
total_character = len(words)
total_words = len(words.split())
print(total_character)
print(total_words)