def branchPath(x: int):
  x = x + 10
  y = 3 * x
  if y < 45:
    print("east")
  elif y == 45:
    print("west")
  else:
    print("north")

print(branchPath(5))