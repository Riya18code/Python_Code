class student:
    def __init__(self,name,age,total_marks):
        self.name=name
        self.age=age
        self.total_marks=total_marks
    def display(self): #method:function inside the class
        print("name is:",self.name)
        print("age is:",self.age)
        print("marks got:",self.total_marks)
#object
s=student("Riya Kumari",19,98)
#call method: object.function_name

s.display()    