class employee:
    def __init__(self):
        self.name="amit"
        self._salary="80800000"
        self.__password="ABC"
e=employee()

print(e.name)
print(e._salary)
print(e.__password)
