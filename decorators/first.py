s = "GLOBAL VARIABLE !"

def func(s): # ako ovde prazno uzima global S
    print(s);

func(s)



def func2():
    mylocal = 10
    print(locals())
    print(globals()['s'])




def hello(name="Jose"):
    return "hello "+name

print(hello())

mynewgreet = hello
print(mynewgreet())


def hello2(name="jose"):
    print("THE HELLO() FUNCTION HAS BEEN RUN!")

    def greet():
        return "This string is inside greet()"


    def welcome():
        return "This string is inside wlcodme!"


    if name =="jose":
        return greet
    else:
        return welcome
    print(greet())
    print(welcome())

x =hello2()

x()


# function as argument


def hello3():
    return "hi JOSE!"

def other(func):
    print("Hello")
    print(func)

other(hello3())


# decorator

def new_decorator(func):

    def wrap_func():
        print("CODE HERE BEFORE EXECUTING FUNCTION")
        func()
        print("Funct() has been called")

    return wrap_func

def func_needs_decorator():
    print("This function is in need of a decorator!")

func_needs_decorator = new_decorator(funct_need_decorator)

func_needs_decorator()

# case 2 

@new_decorator
def func_needs_decorator():
    print("This function is in need of a decorator!")


func_needs_decorator()