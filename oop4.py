class Student:
    def __init__(self):
        self.__marks = 0

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        if marks >= 0:
            self.__marks = marks
        else:
            print("Invalid Marks")

s1 = Student()
s1.set_marks(85)
print("Marks:", s1.get_marks())