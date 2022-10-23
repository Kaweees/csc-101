#
# Programmer: Miguel Villa Floran
# GitHub: Kaweees
# Date: 10/22/2022
# Course Name: CSC 101 - Fundamentals of Computer Science
# Section: Week 06 (Oct 24 - Oct 31)
# Purpose/Assignment: Lab 6 (String Operations)
#

def swapCase(input_str: str) -> str:
  "Return a string which swaps the cases of the input string."
  output = []
  for char in input_str:
    if char.isupper():
      char = char.lower()
    else:
      char = char.upper()
    output.append(char)
  return ''.join(output)

def replaceChar(input_str: str, old_char: str, new_char: str) -> str:
  "Return a string in which the occurrences of old_char in input_str are replaced with new_char"
  if len(old_char) > 1 or len(new_char) > 1:
    return input_str
  output = []
  for char in input_str:
    if char == old_char:
      char = new_char
    output.append(char)
  return ''.join(output)