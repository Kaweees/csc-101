print([i for i in range(1, 5)])

def addToSome(ls: List[int]) -> List[int]:
  return [x + 1 for x in ls if x < 3]
    
def addAllTogether(ls: List[int]) -> int:
  return sum(ls)
    
def addToEach(ls: List[int]) -> List[int]:
  return [x + 1 for x in ls]