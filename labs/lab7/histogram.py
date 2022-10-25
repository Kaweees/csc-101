#
# Programmer: Miguel Villa Floran
# GitHub: Kaweees
# Date: 10/25/2022
# Course Name: CSC 101 - Fundamentals of Computer Science
# Section: Week 07 (Oct 31 - Oct Nov 7)
# Purpose/Assignment: Lab 7
#

def getHistogram(input: str) -> dict[str, int]:
  histogram = {}
  for word in input.split(" "):
    if word in histogram:
      histogram[word] += 1
    else:
      histogram[word] = 1
  return histogram