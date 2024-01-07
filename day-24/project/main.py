# Project: Dice Roller

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