#
# Programmer: Miguel Villa Floran
# GitHub: Kaweees
# Date: 11/03/2022
# Course Name: CSC 101 - Fundamentals of Computer Science
# Section: Week 08 (Nov 07 - Nov 14)
# Purpose/Assignment: Assignment 4
#

import build_data
import unittest
import hw4

full_data = build_data.getData()

reduced_data = [
  build_data.CountyDemographics(
    {
      'Percent 65 and Older': 13.8,
      'Percent Under 18 Years': 25.2,
      'Percent Under 5 Years': 6.0
    },
    'Autauga County',
    {
      "Bachelor's Degree or Higher": 20.9,
      'High School or Higher': 85.6
    },
    {
      'American Indian and Alaska Native Alone': 0.5,
      'Asian Alone': 1.1,
      'Black Alone': 18.7,
      'Hispanic or Latino': 2.7,
      'Native Hawaiian and Other Pacific Islander Alone': 0.1,
      'Two or More Races': 1.8,
      'White Alone': 77.9,
      'White Alone, not Hispanic or Latino': 75.6
    },
    {
      'Per Capita Income': 24571,
      'Persons Below Poverty Level': 12.1,
      'Median Household Income': 53682
      },
    {
      '2010 Population': 54571,
      '2014 Population': 55395,
      'Population Percent Change': 1.5,
      'Population per Square Mile': 91.8
    },
  'AL'),
  build_data.CountyDemographics(
    {
      'Percent 65 and Older': 15.3,
      'Percent Under 18 Years': 25.1,
      'Percent Under 5 Years': 6.0
    },
    'Crawford County',
    {
      "Bachelor's Degree or Higher": 14.3,
      'High School or Higher': 82.2
    },
    {
      'American Indian and Alaska Native Alone': 2.5,
      'Asian Alone': 1.6,
      'Black Alone': 1.6,
      'Hispanic or Latino': 6.7,
      'Native Hawaiian and Other Pacific Islander Alone': 0.1,
      'Two or More Races': 2.8,
      'White Alone': 91.5,
      'White Alone, not Hispanic or Latino': 85.6
    },
    {
      'Per Capita Income': 19477,
      'Persons Below Poverty Level': 20.2,
      'Median Household Income': 39479
    },
    {
      '2010 Population': 61948,
      '2014 Population': 61697,
      'Population Percent Change': -0.4,
      'Population per Square Mile': 104.4
    },
  'AR'),
  build_data.CountyDemographics(
    {
      'Percent 65 and Older': 17.5,
      'Percent Under 18 Years': 18.1,
      'Percent Under 5 Years': 4.8
    },
    'San Luis Obispo County',
    {
      "Bachelor's Degree or Higher": 31.5,
      'High School or Higher': 89.6
    },
    {
      'American Indian and Alaska Native Alone': 1.4,
      'Asian Alone': 3.8,
      'Black Alone': 2.2,
      'Hispanic or Latino': 22.0,
      'Native Hawaiian and Other Pacific Islander Alone': 0.2,
      'Two or More Races': 3.4,
      'White Alone': 89.0,
      'White Alone, not Hispanic or Latino': 69.5
    },
    {
      'Per Capita Income': 29954,
      'Persons Below Poverty Level': 14.3,
      'Median Household Income': 58697
    },
    {
      '2010 Population': 269637,
      '2014 Population': 279083,
      'Population Percent Change': 3.5,
      'Population per Square Mile': 81.7
    },
  'CA'),
  build_data.CountyDemographics(
    {
      'Percent 65 and Older': 11.5,
      'Percent Under 18 Years': 21.7,
      'Percent Under 5 Years': 5.8
    },
    'Yolo County',
    {
      "Bachelor's Degree or Higher": 37.9,
      'High School or Higher': 84.3
    },
    {
      'American Indian and Alaska Native Alone': 1.8,
      'Asian Alone': 13.8,
      'Black Alone': 3.0,
      'Hispanic or Latino': 31.5,
      'Native Hawaiian and Other Pacific Islander Alone': 0.6,
      'Two or More Races': 5.0,
      'White Alone': 75.9,
      'White Alone, not Hispanic or Latino': 48.3
    },
    {
      'Per Capita Income': 27730,
      'Persons Below Poverty Level': 19.1,
      'Median Household Income': 55918
    },
    {
      '2010 Population': 200849,
      '2014 Population': 207590,
      'Population Percent Change': 3.4,
      'Population per Square Mile': 197.9
    },
  'CA'),
  build_data.CountyDemographics(
    {
      'Percent 65 and Older': 19.6,
      'Percent Under 18 Years': 25.6,
      'Percent Under 5 Years': 4.9
    },
    'Butte County',
    {
      "Bachelor's Degree or Higher": 17.9,
      'High School or Higher': 89.2
    },
    {
      'American Indian and Alaska Native Alone': 1.0,
      'Asian Alone': 0.3,
      'Black Alone': 0.2,
      'Hispanic or Latino': 5.8,
      'Native Hawaiian and Other Pacific Islander Alone': 0.2,
      'Two or More Races': 2.3,
      'White Alone': 96.1,
      'White Alone, not Hispanic or Latino': 90.6
    },
    {
      'Per Capita Income': 20995,
      'Persons Below Poverty Level': 15.7,
      'Median Household Income': 41131
    },
    {
      '2010 Population': 2891,
      '2014 Population': 2622,
      'Population Percent Change': -9.4,
      'Population per Square Mile': 1.3
    },
  'ID'),
  build_data.CountyDemographics(
    {
      'Percent 65 and Older': 15.3,
      'Percent Under 18 Years': 25.1,
      'Percent Under 5 Years': 6.9
    },
    'Pettis County',
    {
      "Bachelor's Degree or Higher": 15.2,
      'High School or Higher': 81.8
    },
    {
      'American Indian and Alaska Native Alone': 0.7,
      'Asian Alone': 0.7,
      'Black Alone': 3.4,
      'Hispanic or Latino': 8.3,
      'Native Hawaiian and Other Pacific Islander Alone': 0.3,
      'Two or More Races': 1.9,
      'White Alone': 92.9,
      'White Alone, not Hispanic or Latino': 85.5
    },
    {
      'Per Capita Income': 19709,
      'Persons Below Poverty Level': 18.4,
      'Median Household Income': 38580
    },
    {
      '2010 Population': 42201,
      '2014 Population': 42225,
      'Population Percent Change': 0.1,
      'Population per Square Mile': 61.9
    },
  'MO'),
  build_data.CountyDemographics(
    {
      'Percent 65 and Older': 18.1,
      'Percent Under 18 Years': 21.6,
      'Percent Under 5 Years': 6.5
    },
    'Weston County',
    {
      "Bachelor's Degree or Higher": 17.2,
      'High School or Higher': 90.2
    },
    {
      'American Indian and Alaska Native Alone': 1.7,
      'Asian Alone': 0.4,
      'Black Alone': 0.7,
      'Hispanic or Latino': 4.2,
      'Native Hawaiian and Other Pacific Islander Alone': 0.0,
      'Two or More Races': 2.2,
      'White Alone': 95.0,
      'White Alone, not Hispanic or Latino': 91.5
    },
    {
      'Per Capita Income': 28764,
      'Persons Below Poverty Level': 11.2,
      'Median Household Income': 55461
    },
    {
      '2010 Population': 7208,
      '2014 Population': 7201,
      'Population Percent Change': -0.1,
      'Population per Square Mile': 3.0
    },
  'WY')
]

class TestCases(unittest.TestCase):
  def test_case_one(self):
    self.assertEqual(hw4.populationTotal(reduced_data), 655813)
  def test_case_two(self):
    self.assertEqual(hw4.filterByState(reduced_data, 'WY'), [reduced_data[6]])
  def test_case_three(self):
    self.assertAlmostEqual(hw4.populationByEducation(reduced_data, "Bachelor's Degree or Higher"), 19511409.1)
    self.assertAlmostEqual(hw4.populationByEthnicity(reduced_data, "Two or More Races"), 2361395.1)
    self.assertAlmostEqual(hw4.populationBelowPovertyLevel(reduced_data, "Persons Below Poverty Level"), 10771171.4)
  def test_case_four(self):
    self.assertAlmostEqual(round(hw4.percentByEducation(reduced_data, "Bachelor's Degree or Higher"), 2), 29.75)
    self.assertAlmostEqual(round(hw4.percentByEthnicity(reduced_data, "Two or More Races"), 2), 3.6)
    self.assertAlmostEqual(round(hw4.percentBelowPovertyLevel(reduced_data, "Persons Below Poverty Level"), 2), 16.42)
  def test_case_five(self):
    self.assertEqual(hw4.educationGreaterThan(reduced_data, "Bachelor's Degree or Higher", 60), [])
    self.assertEqual(hw4.educationLessThan(reduced_data, "Bachelor's Degree or Higher", 60), [reduced_data[0], reduced_data[1], reduced_data[2], reduced_data[3], reduced_data[4], reduced_data[5], reduced_data[6]])
    self.assertEqual(hw4.ethnicityGreaterThan(reduced_data, "Hispanic or Latino", 30), [reduced_data[3]])
    self.assertEqual(hw4.ethnicityLessThan(reduced_data, "Hispanic or Latino", 30), [reduced_data[0], reduced_data[1], reduced_data[2], reduced_data[4], reduced_data[5], reduced_data[6]])
    self.assertEqual(hw4.belowPovertyLevelGreaterThan(reduced_data, 30), [])
    self.assertEqual(hw4.belowPovertyLevelLessThan(reduced_data, 30), [reduced_data[0], reduced_data[1], reduced_data[2], reduced_data[3], reduced_data[4], reduced_data[5], reduced_data[6]])

if __name__ == '__main__':
  unittest.main()