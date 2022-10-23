class ProgrammingLanguage():
  def __init__(self, name: str, version: int, has_objects: bool) -> None:
    self.name = name
    self.version = version
    self.has_objects = has_objects

python = ProgrammingLanguage("Python", 2, True)

def have_same_version(a: ProgrammingLanguage, b: ProgrammingLanguage):
  return a.version == b.version

python2 = ProgrammingLanguage("Fake Python", 2, False)
print(have_same_version(python, python2)) # must be True