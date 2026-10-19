class student:
    #constructor
    def __init__(self,name,age): #self keyword refers to the current object.
        self.name=name #attribute: variables belonging to an object.
        self.age=age #here name and age are the attributes.
#object creation
s1= student("Riya",20)
print(s1.name)
print(s1.age)   
     