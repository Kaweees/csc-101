#
# Programmer: Miguel Villa Floran
# GitHub: Kaweees
# Date: 10/14/2022
# Course Name: CSC 101 - Fundamentals of Computer Science
# Section: Week 04 (Oct 10 - Oct 17)
# Purpose/Assignment: Assignment 2
#

import math

class Duration:
  """Represents a length of time in minutes and whole seconds."""
  def __init__(self, minutes: int, seconds: int):
    self.minutes = minutes
    self.seconds = seconds

  def __repr__(self):
    return f"Duration({self.minutes},{self.seconds})"

  def __eq__(self, other):
    return (other is self or
      type(other) == Duration and
      self.minutes == other.minutes and
      self.seconds == other.seconds)

class Point:
  """Represents an 2d cartesian coordinate point."""
  def __init__(self, x: float, y: float):
    self.x = x
    self.y = y

  def __repr__(self):
    return f"Point({self.x},{self.y})"

  def __eq__(self, other):
    return (other is self or
      type(other) == Point and
      math.isclose(self.x, other.x) and
      math.isclose(self.y, other.y))

class Rectangle:
  """Represents rectangle defined by top-left and bottom-right points."""
  def __init__(self, top_left: Point, bottom_right: Point):
    self.top_left = top_left
    self.bottom_right = bottom_right

  def __repr__(self):
    return f"Rectangle({self.top_left},{self.bottom_right})"

  def __eq__(self, other):
    return (other is self or
      type(other) == Rectangle and
      self.top_left == other.top_left and
      self.top_left == other.top_left)

class Triangle:
  """Represents Triangle defined by three points."""
  def __init__(self, a: Point, b: Point, c: Point):
    self.a = a
    self.b = b
    self.c = c

  def __repr__(self):
    return f"Triangle({self.a}, {self.b}, {self.c})"

  def __eq__(self, other):
    return (other is self or
      type(other) == Triangle and
      self.a == other.a and
      self.b == other.b and
      self.c == other.c)

def isShorterThan(d1: Duration, d2: Duration) -> bool:
  """Return True if d1 is shorter than d2, False otherwise."""
  return (d1.minutes + (d1.seconds * 60)) < (d2.minutes + (d2.seconds * 60))

def triangulateRectangle(r1: Rectangle) -> list[Triangle]:
  """Return a list containing two Triangle objects that represent splitting the Rectangle along its top-left and bottom-right points into two triangles."""
  return [Triangle(r1.top_left, Point(r1.bottom_right.x, r1.top_left.y), r1.bottom_right), Triangle(r1.bottom_right, Point(r1.top_left.x, r1.bottom_right.y), r1.top_left)]

def createRectangle(p1: Point, p2: Point) -> Rectangle:
  """Return a Rectangle object with the given points as its top-left and bottom-right points."""
  return Rectangle(Point(min(p1.x, p2.x), max(p1.y, p2.y)), Point(max(p1.x, p2.x), min(p1.y, p2.y)))

def addDurations(d1: Duration, d2: Duration) -> Duration:
  """Return a Durations object which is a sum of two given Durations objects."""
  return Duration((d1.minutes + d2.minutes + ((d1.seconds + d2.seconds) // 60)), ((d1.seconds + d2.seconds) % 60))

class Song:
  def __init__(self, name: str, artist: str, duration: Duration):
    """Represents a song."""
    self.name = name
    self.artist = artist
    self.duration = duration

  def __repr__(self):
    return f"Song({self.name}, {self.artist}, {self.duration})"

  def __eq__(self, other):
    return (other is self or
      type(other) == Song and
      self.name == other.name and
      self.artist == other.artist and
      self.duration == other.duration)

def getLengthsInSeconds(l1: list[Song]) -> list[int]:
  """Return a list of integers representing lengths of songs in seconds."""
  return [((song.duration.minutes * 60) + song.duration.seconds) for song in l1]

def getSongsByArtist(l1: list[Song], artist: str) -> list[Song]:
  """Return a list of songs by given artist name."""
  return [song for song in l1 if song.artist == artist]

def getPlaylistLengthInSeconds(l1: list[Song]) -> Duration:
  """Return the total length of all songs in the playlist in a Duration object."""
  sum_sec = sum([((song.duration.minutes * 60) + song.duration.seconds) for song in l1])
  return Duration(sum_sec // 60, sum_sec % 60)