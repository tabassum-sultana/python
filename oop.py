class Student:
    def __init__(self, sub, sub_code):
        self.sub = sub
        self.sub_code = sub_code

class Teacher:
    def __init__(self, sub, sub_code):
        self.sub = sub
        self.sub_code = sub_code

s1 = Student("Python", "101")
t1 = Teacher("OOP", "102")

print(s1.sub, s1.sub_code)
print(t1.sub, t1.sub_code)