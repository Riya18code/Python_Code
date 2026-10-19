class cal: #calculation of area pf rectangle
    def __init__(self,len,bre):
        self.len=len
        self.bre=bre
    def area(self):
        return self.len*self.bre
R=cal(5,8)
print("Area of rectangle is=",R.area())