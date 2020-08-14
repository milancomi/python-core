mylist = [1,2,3]

print(mylist)

class Book():
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self): # ako se printa objekat izbaci ovo dole
        return "HELLO"


    def __len__(self):
        return self.pages


b = Book("Python","jose",200)

del b #brisanje objekta
 
print(b)
