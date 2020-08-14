def my_funct(param1='defailt'):
    """
    THIS IS THE DOCSTRING
    DESCRIPTION OF FUNCTION
    """
    print("my first python function {} !".format(param1))

my_funct()

def hello():
    return "hello"

result = hello()

print(result)


def addNum(num1,num2):
    if(type(num1)==type(num2)==type(10)):
        return num1+num2
    else:
        return "Sorry, i need integers"

result = addNum(2,3)
result2 = addNum("2","3")

print(type(result))

# lambda expression

mylist= [1,2,3,4,5,6,7,8]

def event_bool(num):
    return num%2 ==0


evens = filter(event_bool,mylist)
print(list(evens))

# lambda case

evens = filter(lambda num:num%2==0,mylist)
print(evens)


# general helpers

st = "hello"

st.lower()
st.upper()
st.split()

# example
tweet = "Go Sports! #Sports"

result = tweet.split('#')

print(result)

print('x' in[1,2,3])
print('x' in[1,2,'x'])