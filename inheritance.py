#child class acuires the property and behavior of the parent class is known as inheritance
class father:
    def eye(self):
        print("FATHER EYE'S IS GREEN")
class child(father):
    def hair(self):
        print("MY HAIR IS BROWN") 
C=child()
C.eye()
C.hair()
