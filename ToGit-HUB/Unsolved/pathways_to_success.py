"""Pathways to Success."""
# @TODO: Import the Path tool from the pathlib library
# YOUR CODE HERE!
import csv
from pathlib import Path
# @TODO: Create a path to the `quarterly_data.csv` file
New_path = Path('quarterly_data.csv')
# YOUR CODE HERE
# Print the relative path (the relative location of the file)
print(f"The relative CSV path is {New_path}")

# Print the absolute path (The absolute location of the file on the computer)
print(f"The absolute CSV path is {New_path.absolute()}")
