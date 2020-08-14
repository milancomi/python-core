if 1<2:
    print("FIRST BLOCK")
    if 2<3:
        print("Second block !")


if 1>2:
    print("hello")
elif 3==3:
    print('elif ran')
else:
    print('last')


# Looops
# For

seq = [1,2,3,4,5,6]

for item in seq:
    #codee here
    print(item)


d = {"Sam":1,"Frank":2,"Dan":3}

for k in d:
    print(k)
    print(d[k])



for k in d.keys:
    print(k)
    print(d[k])

for k in d.values:
    print(k)
    print(d[k])
    

mypairs =[(1,2),(3,4),(5,6)]

for item in mypairs:
    print(item)

for item1,item2 in mypairs:
    print(item1)
    print(item2)


i = 1

while i<5:
    print("i is:[]".format(i))
    i= i+1

 
list(range(0,5)) # od nula do 6

list(range(0,20,2)) # svaki drugi broj


for itm in range(10):
    print(item)



x = [1,2,3,4,5]

out = []

for num in x:
    out.append(num**2)

print(out)

out = [num**2 for num in x]
