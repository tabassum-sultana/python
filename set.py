s1 = "python is fun and easy"
s2 = "python is powerful and fast"

a = set(s1.split())
b = set(s2.split())

print(a | b)
print(a - b)