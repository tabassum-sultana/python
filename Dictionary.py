scores = {'Alice':78, 'Bob':42, 'Charlie':90, 'David':49, 'Eve':65}

p = []
f = []

for name in scores:
    if scores[name] >= 50:
        p.append(name)
    else:
        f.append(name)

print("Pass:", p)
print("Fail:", f)