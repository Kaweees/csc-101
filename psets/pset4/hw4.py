#
# Programmer: Miguel Villa Floran
# GitHub: Kaweees
# Date: 11/03/2022
# Course Name: CSC 101 - Fundamentals of Computer Science
# Section: Week 08 (Nov 07 - Nov 14)
# Purpose/Assignment: Assignment 4
#

from typing import List, Dict
import build_data
data = build_data.getData()

def populationTotal(counties_data: List[build_data.CountyDemographics]) -> int:
  """Returns the total 2014 population across the set of counties in the provided list"""
  return sum([county.population["2014 Population"] for county in counties_data])

def filterByState(counties_data: List[build_data.CountyDemographics], state: str) -> List[build_data.CountyDemographics]:
  """Returns a List of CountyDemographics objects with the specified state"""
  return [county for county in counties_data if county.state == state]

def populationByEducation(counties_data: List[build_data.CountyDemographics], education_key: str) -> float:
  """Returns the total 2014 sub-population across the set of counties in the provided list with the specified education level"""
  return sum([county.education[education_key] * county.population["2014 Population"] for county in counties_data])

def populationByEthnicity(counties_data: List[build_data.CountyDemographics], ethnicity_key: str) -> float:
  """Returns the total 2014 sub-population across the set of counties in the provided list with the specified poverty level"""
  return sum([county.ethnicities[ethnicity_key] * county.population["2014 Population"] for county in counties_data])

def populationBelowPovertyLevel(counties_data: List[build_data.CountyDemographics], income_key: str) -> float:
  """Returns the total 2014 sub-population across the set of counties in the provided list with the specified poverty level"""
  return sum([county.income[income_key] * county.population["2014 Population"] for county in counties_data])

def percentByEducation(counties_data: List[build_data.CountyDemographics], education_key: str) -> float:
  """Returns the total 2014 sub-population for the specified education key of interest as a percentage of the total population across the set of counties in the provided list"""
  return (populationByEducation(counties_data, education_key) / populationTotal(counties_data))

def percentByEthnicity(counties_data: List[build_data.CountyDemographics], ethnicity_key: str) -> float:
  """Returns the total 2014 sub-population for the specified ethnicity key of interest as a percentage of the total population across the set of counties in the provided list"""
  return (populationByEthnicity(counties_data, ethnicity_key) / populationTotal(counties_data))

def percentBelowPovertyLevel(counties_data: List[build_data.CountyDemographics], income_key: str) -> float:
  """Returns the total 2014 sub-population for the specified income key of interest as a percentage of the total population across the set of counties in the provided list"""
  return (populationBelowPovertyLevel(counties_data, income_key) / populationTotal(counties_data))

def educationGreaterThan(counties_data: List[build_data.CountyDemographics], education_key: str, threshold : float) -> List[build_data.CountyDemographics]:
  """Returns a list of all county demographics objects for which the value for the specified education key is greater than the specified threshold value"""
  return [county for county in counties_data if county.education[education_key] > threshold]

def educationLessThan(counties_data: List[build_data.CountyDemographics], education_key: str, threshold : float) -> List[build_data.CountyDemographics]:
  """Returns a list of all county demographics objects for which the value for the specified education key is less than the specified threshold value"""
  return [county for county in counties_data if county.education[education_key] < threshold]

def ethnicityGreaterThan(counties_data: List[build_data.CountyDemographics], ethnicity_key: str, threshold : float) -> List[build_data.CountyDemographics]:
  """Returns a list of all county demographics objects for which the value for the specified ethnicity key is less than the specified threshold value"""
  return [county for county in counties_data if county.ethnicities[ethnicity_key] > threshold]

def ethnicityLessThan(counties_data: List[build_data.CountyDemographics], ethnicity_key: str, threshold : float) -> List[build_data.CountyDemographics]:
  """Returns a list of all county demographics objects for which the value for the specified ethnicity key is less than the specified threshold value"""
  return [county for county in counties_data if county.ethnicities[ethnicity_key] < threshold]

def belowPovertyLevelGreaterThan(counties_data: List[build_data.CountyDemographics], threshold : float) -> List[build_data.CountyDemographics]:
  """Returns a list of all county demographics objects for which the value for the poverty value of the level key "Persons Below Poverty Level" is less than the specified threshold value"""
  return [county for county in counties_data if county.income["Persons Below Poverty Level"] > threshold]

def belowPovertyLevelLessThan(counties_data: List[build_data.CountyDemographics], threshold : float) -> List[build_data.CountyDemographics]:
  """Returns a list of all county demographics objects for which the value for the poverty value of the level key "Persons Below Poverty Level" is less than the specified threshold value"""
  return [county for county in counties_data if county.income["Persons Below Poverty Level"] < threshold]