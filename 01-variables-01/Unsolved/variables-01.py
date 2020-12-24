# Variables

# This is a comment - any code commented out is not run -
# meaning that any code or text commented out is ignored.

"""
This is a multi-line comment.
You can comment out many lines at once.
For the most part you will see single line comments
As in single line comments, any code contained within multi-line comments is not run -
meaning that any code commented out is ignored.
"""

# Topic: Strings

# Create a variable named `subject` with no value (None).
# YOUR CODE HERE!
subject = None
subject_two = None
# Assign a value of "Programmers to the variable `subject`.
# YOUR CODE HERE!
subject = "Programmers"
subject_two = 'Software dev'
# Create a variable, `first_name`, and assign it a value of an empty string.
# YOUR CODE HERE!
first_name = ""
first_name_two = ""
# Assign a value of "Ada" to the variable `first_name`.
# YOUR CODE HERE!
first_name = "Ada"
first_name_two = "Javier"
# Create a variable, `last_name`, and assign it a value of a string, "Lovelace".
# YOUR CODE HERE!
last_name = 'Lovelace'
last_name_two = "BarrNun"



# Topic: Integers

# Create a variable, `birth_year`, and assign it with an integer of 1815.
# YOUR CODE HERE!
birth_year = 1815
year_hired = 2021
# Create a variable, death_year, and assign it with an integer of 1852.
# YOUR CODE HERE!
death_year = 1852
year_of_merger = 2025
# Create a variable, age_at_passing, and assign it a value of death_year minus birth_year.
# YOUR CODE HERE!
age_at_passing = death_year - birth_year
year_of_sale = 2033
#Topic: Print

# Print: "First Name: " and `first_name`.
# YOUR CODE HERE!
print(f"First Name: {first_name}")
print(f"First Name: {first_name_two}")

# YOUR CODE HERE!
print(f"Last Name: {last_name}")
print(f"Last Name: {last_name_two}")

#Topic: Concat Values

# Create and print a variable, `statement_one`, by assigning it a value of a string:
# "Programmers: Ada Lovelace was born in 1815, and she lived to be 37 years old."
# YOUR CODE HERE!
statement_one = f"{subject}: {first_name} {last_name} was born in {birth_year}, and she lived to be {age_at_passing} years old."
print(statement_one)

statement_two = f"{subject_two}: {first_name_two} {last_name_two} was hired in {year_hired} he faciltated a merger with his company Familiar Families LLC {year_of_merger} and sold his majority share in {year_of_sale}."
print(statement_two)