roll_template = """Rolls: {}
Total: {}
Average: {}
"""

def format_result(rolls, total, average):
    rolls = ", ".join(str(roll) for roll in rolls)
    return roll_template.format(rolls, total, average)

def log_result(rolls, total, average, log_file):
    with open(log_file, "a")  as log:
        log.write(format_result(rolls, total, average))
        log.write("-" * 30 + "\n")
        