#
# Programmer: Miguel Villa Floran
# GitHub: Kaweees
# Date: 10/16/2022
# Course Name: CSC 101 - Fundamentals of Computer Science
# Section: Week 05 (Oct 17 - Oct 21)
# Purpose/Assignment: Lab 5 (while Loops)
#

if __name__ == "__main__": # This is to enable a "play" button in PyCharm
  # You will calculate the average of this list
  values = [3.33, 45.0, 12.5, 80.0, 45.0, 16.0]

  # Write your code here
  i = 0
  total = 0
  while i < len(values):
    total += values[i]
    i += 1
  print(total / i)