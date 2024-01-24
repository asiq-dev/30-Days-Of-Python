#A Simple Earnings Calculator 

name = input("Enter Employee Name: ").strip().title()
hourly_wage = float(input("What is their hourly wage?: "))
hours_worked = float(input("How many hours have they worked this week?: "))

total_earned =hourly_wage * hours_worked

print(f"{name} earned ${total_earned:.2f} this week.")