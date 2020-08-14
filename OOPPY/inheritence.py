class Animal():

    def __init__(self):
        print("Animal created")

    def whoAmI(self):
        print("Animal")
    
    def eat(self):
        print('Eating')



class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Dog created")

    def bark(self):
        print("WOOF")

    def eat(self):
        print("DOG EATING")

mya = Animal()

mya.whoAmI()

mya.eat()


kuce2 = Dog()

kuce2.whoAmI()

kuce2.eat()