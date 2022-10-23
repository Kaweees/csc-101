#
# Programmer: Miguel Villa Floran
# GitHub: Kaweees
# Date: 10/10/2022
# Course Name: CSC 101 - Fundamentals of Computer Science
# Section: Week 04 (Oct 10 - Oct 17)
# Purpose/Assignment: Lab 4 (Story)
#

class Item:
  """Represents a powerful item to be used by a hero"""
  def __init__(self, type: str, power: int) -> None:
    self.type  = type
    self.power = power

class Hero:
  """Represents a hero in our story"""
  def __init__(self, name: str, skill: str, item: Item) -> None:
    self.name  = name
    self.skill = skill
    self.item  = item

class Monster:
  """Represents a terrifying monster"""
  def __init__(self, type: str, appearance: str, power: int) -> None:
    self.type     = type
    self.appearance = appearance
    self.power    = power

class World:
  """Represents the world that a story may take place in"""
  def __init__(self, setting: str, name: str, year: int) -> None:
    self.setting = setting
    self.name  = name
    self.year  = year
