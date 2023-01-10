# practicing class in python 23/01/04
# this is my library progam
class Book:
    def __init__(self, name, auth, id):
        self.name = name
        self.auth = auth
        self.id = id

class Menu:
    booklist = []
    def __init__(self):
        pass
    def addBook(self):
        name, auth, id = input("type the book name, auth, id : ").split()
        self.booklist.append(Book(name, auth, id))
        print("\nAdded!")
    def deleteBook(self):
        searchbookname = input("type in the book name : ")
        for cnt, i in enumerate(self.booklist):
            if i.name == searchbookname:
                del (self.booklist[cnt])
                print("\ndleated")
    def searchBook(self):
        searchname = input("type the name of the book : ")
        for i in range(len(self.booklist)):
            if self.booklist[i].name == searchname:
                print("the book info is name : %s   author : %s   id : %s  " % (self.booklist[i].name, self.booklist[i].auth, self.booklist[i].id))

    def printAll(self):
        for i in range(len(self.booklist)):
            print("there are total %s books"%(len(self.booklist)))
            print("name : %s   author : %s   id : %s  " % (self.booklist[i].name, self.booklist[i].auth, self.booklist[i].id))

#Main
menu = Menu()
while (1):
    print(
        "@@@@@@@@@\n\nwellcome, if you want to Add press a, if you want to search press s if you want to delete press d, if you want to list all press 'l' if you want to quit, press q : \n\n@@@@@@@@")
    menukey = input()
    if menukey == 'a':
        menu.addBook()
    elif menukey == 'd':
        menu.deleteBook()
    elif menukey == 's':
        menu.searchBook()
    elif menukey == 'l':
        menu.printAll()
    elif menukey == 'q':
        break
    else:
        print("cant read the menu, please check if the key you pressed is upcapp and only one letter")