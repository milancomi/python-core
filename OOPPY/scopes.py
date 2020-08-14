x = 25

def my_funct():

    x = 50
    return x


print(x)

lambda x: x**2

name  = "This is a global name !"

def greet():
    name = "sammy"
    def hello():
        print("hello "+name)
    hello()

greet()



# built in level 

x  = 50

def function(x):
    print('x is:',x)
    x = 1000
    print('local x change to:',x)

function(x)
print(x) # vraca isto local 50


# global x change 

def function2():
    global x
    x = 1000


funcion2() 
print(x)
# promenjen global x na 1000


def function3():
    x  =1500
    return x
x = function3()
  