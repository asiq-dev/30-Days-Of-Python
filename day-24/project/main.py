# Project: Dice Roller
# The user is going to be able to specify a selection of dice using the following syntax, where the number before the d represents the number of dice, and the number after the d represents how many sides those dice have.
# python main.py 3d6



import parser
import random
import output


args = parser.args

quantity, die_size = parser.parse_roll(args)
repetitions = args.repeat
log_file = args.log

for _ in  range(repetitions):
    rolls = [random.randint(1, die_size)  for _ in  range(quantity)]
    total = sum(rolls)
    average = total / len(rolls)

    print(output.format_result(rolls, total, average))
    output.log_result(rolls, total, average, log_file)
