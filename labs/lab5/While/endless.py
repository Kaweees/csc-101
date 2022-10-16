#
# Programmer: Miguel Villa Floran
# GitHub: Kaweees
# Date: 10/16/2022
# Course Name: CSC 101 - Fundamentals of Computer Science
# Section: Week 05 (Oct 17 - Oct 21)
# Purpose/Assignment: Lab 5 (while Loops)
#

if __name__ == "__main__": # This is to enable a "play" button in PyCharm
  value_1 = 0
  value_2 = 0
  while value_1 >= value_2:
    print("Performing an iteration of the loop:")
    print(f"Currently, value_1 = {value_1} and value_2 = {value_2}")
    value_1 += 1
    value_2 += 1
    # Add code here