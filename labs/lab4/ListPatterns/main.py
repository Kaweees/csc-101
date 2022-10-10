#
# Programmer: Miguel Villa Floran
# GitHub: Kaweees
# Date: 10/10/2022
# Course Name: CSC 101 - Fundamentals of Computer Science
# Section: Week 04 (Oct 10 - Oct 17)
# Purpose/Assignment: Lab 4 (ListPatterns)
#

from collections.abc import Callable

import pattern01
import pattern02
import pattern03
import pattern04

def applyPatternFunction(input: list[object], f: Callable[[int, object], object]) -> list[object]:
    """Given an input list, applys the function f to each element, then returns the result of each as a list"""
    return [f(i, value) for i, value in enumerate(input)]

if __name__ == "__main__":
    inputs    = [pattern01.input, pattern02.input, pattern03.input, pattern04.input]
    goals     = [pattern01.goal, pattern02.goal, pattern03.goal, pattern04.goal]
    functions = [pattern01.patternFunction, pattern02.patternFunction, pattern03.patternFunction, pattern04.patternFunction]

    for i in range(len(inputs)):
        print(f"Testing Pattern {i + 1}:")
        print("Input:  ", inputs[i])
        print("Goal:   ", goals[i])

        output = applyPatternFunction(inputs[i], functions[i])
        print("Output: ", output)

        if (output == goals[i]):
            print("Equal!")
        else:
            print("Not Equal!")

        print()
