n = int(input())

print((str(n) + " ") * n)

for i in range(n - 2):
    print(n, " " * (2 * n - 3), n)

print((str(n) + " ") * n)