class Animal:
    def breath(self):
        print("can Breath")
    def no_eyes(self):
        print("2")

class Fish(Animal):#fish class is inheriting behavior from animal
    def __init__(self):
        super().__init__()
    def swim(self):
        print("can swim")
    def breath(self):
        super().breath()
        print("can Breath inside water.")
nemo = Fish()
nemo.breath()
nemo.no_eyes()
nemo.swim()