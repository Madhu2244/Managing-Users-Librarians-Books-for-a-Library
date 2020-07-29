import rand as rand


class Person:
    def __init__(self,fname,lname,dob,id,password):
        self.fname = fname
        self.lname = lname
        self.dob = dob
        self.id = id
        self.password = password
    def __repr__(self):
        return "'{}' '{}' '{}' '{}' '{}'".format(self.fname,self.lname,self.dob,self.id,self.password)
    def checkId(self,idCheck):
        if self.id==idCheck:
            return True

class Book:
    def __init__(self,bookName,author,bookId,edition):
        self.bookName = bookName
        self.author = author
        self.bookId = bookId
        self.edition = edition
    def updateBookName(self, newBookName):
        self.bookName = newBookName
    def updateAuthor(self, newAuthor):
        self.author = newAuthor
    def updateBookId(self, newBookId):
        self.bookId = newBookId
    def updateEdition(self, newEdition):
        self.edition = newEdition
    def __repr__(self):
        return "'{}' '{}' '{}' '{}'".format(self.bookName,self.author,self.bookId,self.edition)
    def checkId(self,idCheck):
        if self.bookId == idCheck:
            return True
import random
print(str(random.randrange(1, 100)))
userList = []
librarianList = []
bookInfoList = []
bookList = {}
bookCheckOutList = {}
while(True):
    print("""Welcome to Davis Library""")
    personInput = input("""Continue as user or librarian
    Login Menu:
    a) Librarian
    b) User""")
    if (personInput == "a"):
        librarianInput = input("""Are you a:
        1) Existing Librarian
        2) New Librarian""")
        if (librarianInput == "2"):
            librarianFirstName = str(input("Enter First Name"))
            librarianLastName = str(input("Enter Last Name"))
            librarianDOB = str(input("Enter DOB in the format of MM-DD-YYYY"))
            librarianPassword = str(input("Enter in the password for your account"))
            librarianId = str(random.randrange(1, 100)) + librarianDOB
            librarian = Person(librarianFirstName, librarianLastName, librarianDOB, librarianId, librarianPassword)
            librarianList.append(librarian)
            print("Thank you for registering, your u_id is: " , librarianId)
            print(librarianList)

        if (librarianInput == "1"):
            librarianIdInput = input("Enter Librarian Id")
            foundId = False
            for people in librarianList:
                if people.checkId(librarianIdInput):
                    foundId = True
            if foundId:
                choice = input("""1) List of Books available
                2) List of Books issued to users
                3) Add Book
                4) Delete Book
                5) Update Book""")
                if choice == "1":
                    print(bookList)
                if choice == "3":
                    bookName = str(input("Enter Book Name"))
                    bookAuthor = str(input("Enter Author Full Name"))
                    bookEdition = str(input("Enter Book Edition"))
                    bookId = str(random.randrange(1, 100)) + bookName
                    print(bookId)
                    book = Book(bookName, bookAuthor, bookId, bookEdition)
                    if (bookName in bookList):
                        x = bookList[bookName] + 1
                        bookList[bookName] = x
                    else:
                        bookList[bookName] = 1
                    bookInfoList.append(book)
                    print("Book Id is: ", bookId)
                    print(librarianList)
                if choice == "2":
                    print(bookCheckOutList)
                if choice == "4":
                    bookIdDelete = input("Type in the bookId to Delete")
                    for book in bookList.keys():
                        if bookIdDelete in bookList:
                            x = bookList[bookName] - 1
                            bookList[bookName] = x
                    print(bookList)
                if choice == "5":
                    bookIdUpdate = input("Type in the bookId to Update")
                    foundId = False
                    bookNameUpdate = ""
                    for people in bookInfoList:
                        if people.checkId(bookIdUpdate):
                            bookNameUpdate = people.__getattribute__(bookName)
                            foundId = True
                    if foundId:
                        newbookName = str(input("Enter Book Name"))
                        newbookAuthor = str(input("Enter Author Full Name"))
                        newbookEdition = str(input("Enter Book Edition"))
                        newbook = Person(newbookName, newbookAuthor, bookIdUpdate, newbookEdition)
                        bookList[bookNameUpdate] = newbookName



    if (personInput == "b"):
        userInput = input("""1)Existing User
        2) New User""")
        if userInput == "2":
            personFirstName = str(input("Enter First Name"))
            personLastName = str(input("Enter Last Name"))
            personDOB = str(input("Enter DOB in the format of MM-DD-YYYY"))
            personPassword = str(input("Enter in the password for your account"))
            personId = str(random.randrange(1, 100)) + personDOB
            person = Person(personFirstName, personLastName, personDOB, personId, personPassword)
            userList.append(person)
            print("Thank you for registering, your u_id is: ", personId)
            print(userList)
        if userInput == "1":
            userIdInput = input("Enter User Id")
            foundId = False
            for people in userList:
                if people.checkId(userIdInput):
                    foundId = True
            if foundId:
                userControl = input("""1) Issue a Book
                            2) Books Issued
                            3) Return a Book""")
                if userControl == "1":
                    bookIdCheckout = input("Type in the book id you want to check out")
                    for book in bookList.keys():
                        if bookIdCheckout in bookList:
                            x = bookList[bookName]
                            if x >= 1:
                                x -=1
                                bookList[bookName] = x
                                bookCheckOutList[bookIdCheckout] = userIdInput
                            else:
                                print("there are no books under that id")
                if userControl == "2":
                    print(bookCheckOutList)
                if userControl == "3":
                    bookIdCheckIn = input("Type in the book id you want to return")
                    for book in bookList.keys():
                        if bookIdCheckIn in bookList:
                            x = bookList[bookName]
                            x += 1
                            bookList[bookName] = x
                            #bookCheckOutList[bookIdCheckout] = userIdInput #smth not right here
                        else:
                            print("there are no books under that id")
