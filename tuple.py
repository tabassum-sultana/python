record = ("John Doe", (85, 92, 88), "Grade 10")

name = record[0]
marks = record[1]

avg = round(sum(marks) / 3, 2)

print(name, avg) 