#
# Programmer: Miguel Villa Floran
# GitHub: Kaweees
# Date: 10/16/2022
# Course Name: CSC 101 - Fundamentals of Computer Science
# Section: Week 05 (Oct 17 - Oct 21)
# Purpose/Assignment: Lab 5 (while Loops)
#

if __name__ == "__main__": # This is to enable a "play" button in PyCharm
  value = 0
  while True:
    if value == 8:
      break
    value += 1
    print("Stuck in an endless loop...")

  # This should output a value of 8
  print(f"Ended with value = {value}")
