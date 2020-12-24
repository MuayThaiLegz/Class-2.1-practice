# Define a function `having_fun` that prints "Functions are FUN!".
# YOUR CODE HERE!
def having_fun():
    print("Functions are fun!!!")


# YOUR CODE HERE!
def thirty_seven():
    print(18 + 19)

# Call the two functions you've defined so far.
having_fun()
thirty_seven()

# Define a function `hello` that takes in a string parameter and prints the parameter variable.
# YOUR CODE HERE!
def hello(string_param):
    print(string_param)

# Call your `hello` function.
# YOUR CODE HERE!
hello("Top of the morning!")
# Define a function `average` that calculates the average between two parameters and returns the average.
# YOUR CODE HERE!
def average(num_1, num_2):
    av_cal = (num_1 + num_2) / 2
    return av_cal

# Call the `average` function and assign to a variable `calculated_average`.
# Print your `calculated_average`.
calculated_average = average(90, 10)
print(f'Calculated Average: {calculated_average}')
