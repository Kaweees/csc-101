#
# Programmer: Miguel Villa Floran
# GitHub: Kaweees
# Date: 10/22/2022
# Course Name: CSC 101 - Fundamentals of Computer Science
# Section: Week 06 (Oct 24 - Oct 31)
# Purpose/Assignment: Lab 6 (Command-Line Arguments)
#

import enum
import sys

def main():
  output = ""
  for num, name in enumerate(sys.argv, start = 0):
    output += f'"{num}": "{name}"{", " if (num + 1 < len(sys.argv)) else ""}'
  print(output)

if __name__ == "__main__":
  main()