a = True
b = False
c = b or a and not b
print(c)

a = [0, 1, 2, 3, 4, 5]
b = ["apple", "orange", "apple", "orange", "apple", "orange", "apple", "orange"]

print(a[2:4])
print(a[a[2] + 1])
print(b[-1])
print(b[a[2]])


print([num for num in range(0, 9) if num <= 5])