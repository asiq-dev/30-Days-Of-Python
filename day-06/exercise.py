# Print how much each employee is due to be paid at the end of the week in a nice, readable format.
employees = [
    ("Rolf Smith", 35, 8.75),
    ("Anne Pun", 30, 12.50),
    ("Charlie Lee", 50, 15.50),
    ("Bob Smith", 20, 7.00)
]

for emp_details in employees:
    print(f"{emp_details[0]} has to be paid: {emp_details[1] * emp_details[2]}")

total_wage = 0
total_emp = 0
for emp in employees:
    total_wage += emp[2]
    total_emp += 1

avg_wage = total_wage / total_emp

for emp in employees:
    if emp[2] > avg_wage:
        print(f"{emp[0]} has earnd more than avg")