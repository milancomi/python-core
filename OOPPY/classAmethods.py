mylist = [1,2,3]

mylist.append(4)

print(mylist)


class Sample():
    pass



x = Sample()

print(type(x))



class Dog():

    species ="mammal"
    def __init__(self,name,breed): # konstruktor
        self.name = name
        self.breed = breed


kuce = Dog("pekinezer",'blabla')

print(kuce.name)


class Circle():

    pi = 3.14
    def __init__(self,radius=1):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * Circle.pi

    def set_radius(self,new_r):
        self.radius = new_r



myc = Circle(3)
myc.radius = 5
myc.set_radius(100)
print(myc.area()) 