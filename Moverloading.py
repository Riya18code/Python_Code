class calculator:
    def add(self,*number):
        return sum(number)
c=calculator()
print(c.add(7,6))
print(c.add(80,50,45))
print(c.add(2,4,5,6,2,1))
