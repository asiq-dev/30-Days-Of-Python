# For this project users should be able to:

# Create a scatter plot where the x axis is the species and the y axis is one of the other columns.
# Via a user menu, tell us the column they would like to plot in the y axis.
# Also via the menu, tell us the name of the file they would like to create to contain the final plot image.
# I would recommend tackling this project this way:

# Use the file [main.py](<http://main.py>) to contain the user menu.
# Create a file, such as data_storage.py, that contains functions to read the iris.csv data file.
# Create a third file, graphing.py, that contains a function that creates the scatter plot given the x and y values.


from charts import create_chart
from data_storage import read_column


user_menu = """Please choose from the following options:

- Enter 'c' to chart a new graph.
- Enter 'q' to quit.

Your selection: """

charting_menu = "Enter the column you'd like to chart: "
filename_prompt = "Enter your desired file name: "

def handle_chart():
    column = int(input(charting_menu))
    x = read_column(-1)
    y = [float(n) for n in read_column(column)]
    filename = input(filename_prompt).strip()
    create_chart(x, y, filename)

while True:
    user_selection = input(user_menu)
    if user_selection == 'q':
        break
    elif user_selection == 'c':
        handle_chart()
    else:
        print("Sorry!, '{user_selection}' is not valid option. ")
