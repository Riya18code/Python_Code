class marks:
    def __init__(self,total_marks):
        self.__total_marks=total_marks #private variable
    def show(self):
        print("Marks of student1 is:",self.__total_marks)
m1=marks(67)
m1.show()