#
# Programmer: Miguel Villa Floran
# GitHub: Kaweees
# Date: 10/10/2022
# Course Name: CSC 101 - Fundamentals of Computer Science
# Section: Week 04 (Oct 10 - Oct 17)
# Purpose/Assignment: Lab 4 (ListFunctions)
#

class Employee:
  def __init__(self, name: str, pay_rate: int, job_code: int) -> None:
    self.name = name
    self.pay_rate = pay_rate
    self.job_code = job_code
  def __repr__(self) -> str:
    return f"Employee({self.name},{self.pay_rate},{self.job_code})"
  def __eq__(self, other) -> bool:
    return (other is self or
      type(other) == Employee and
      self.name == other.name and
      self.pay_rate == other.pay_rate and
      self.job_code == other.job_code)