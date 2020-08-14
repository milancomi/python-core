def func():
    print("Func() in one.py")

print("TOP LEVEL ONE.PY")


if __name__ == '__main__': # name of current module
    print("one.py is being run directyly")

else:
    print("one.py has been imported")



