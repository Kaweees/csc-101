#
# Programmer: Miguel Villa Floran
# GitHub: Kaweees
# Date: 10/16/2022
# Course Name: CSC 101 - Fundamentals of Computer Science
# Section: Week 05 (Oct 17 - Oct 21)
# Purpose/Assignment: Lab 5 (while Loops)
#

if __name__ == "__main__": # This is to enable a "play" button in PyCharm
  strings = ["Hello", "this", "code", "prints", "each", "list", "element"]

  n = 0
  while n < len(strings):
    print(strings[n])
    n += 1
