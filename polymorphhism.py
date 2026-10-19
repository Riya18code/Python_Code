#polymorphism means many forms
class dog:
    def sound(self):
        print("Dog Barks")
class cat:
    def sound(self):
        print("Cat Meows")
d=dog()
c=cat()
d.sound()
c.sound()

#the same method name can behave differntly for different objects.