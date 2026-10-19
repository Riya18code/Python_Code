class insects:
    def like(self):  #same funcn name
        print("i like to see butterfly")
class ant(insects):
    def like(self):  #same funcn name
        print("i like watching ants")
OBJ=ant()
OBJ.like()

#if both classes have same method name then the child method is executed instead of parent one.
