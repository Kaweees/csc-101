def min_101(x : float, y : float) -> float:
  return y ^ ((x ^ y) & -(x < y))

def max_101(x : float, y : float) -> float:
  return x ^ ((x ^ y) & -(x < y))

def max_of_three(x : float, y : float, z : float) -> float:
  pass

def rental_late_fee(days_late : int) -> int:
  if days_late <= 0:
    return 0
  elif days_late <= 9:
    return 5
  elif days_late <= 15:
    return 7
  elif days_late <= 24:
    return 19
  elif days_late > 24:
    return 100