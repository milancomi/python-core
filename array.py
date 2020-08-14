mylist = [1,2,3]

mylist2 = ['wqewqeqwe',1,2,3,23.2,True,'asd',[1,2,3]]

print(len(mylist))

mylist3=['a','b','c']

print(mylist[1])

print(mylist[1:])

mylist3[0] = 'NEW ITEM'

mylist3.append('New item at end')
mylist3.append(["wdqw",'wqdqw','qwdqw']) # ubaci listu kao element
mylist3.extend(["wdqw",'wqdqw','qwdqw']) # dodaj drugu listu

item = mylist3.pop() # poslednji item je uzet i smesten u variablu

mylist3.pop(3)

mylist3.reverse()

mylist3.sort()

mylist4 = [1,2,['x','y','z']]
print(mylist3[2][1])



# list comprehension
matrix = [[1,2,3,],[4,5,6],[7,8,9]]

first_col = [row[0] for row in matrix]

# each 0 for each element in

# 1 ,4 ,7
print(first_col)