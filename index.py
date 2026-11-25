print("Welcome to Python!")

name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("\n--- Student Information ---")
print("Name:", name)
print("Age:", age)

if age >= 18:
    print("You are an adult.")
else:
    print("You are a student.")