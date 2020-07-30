import rand as rand


class Person:
    def __init__(self, fname, lname, dob, id, password):
        self.fname = fname
        self.lname = lname
        self.dob = dob
        self.id = id
        self.password = password

    def __repr__(self):
        return "'{}' '{}' '{}' '{}' '{}'".format(self.fname, self.lname, self.dob, self.id, self.password)

    def checkId(self, idCheck):
        if self.id == idCheck:
            return True

    def checkPassword(self, passwordCheck):
        if self.password == passwordCheck:
            return True
        else:
            return False


class Book:
    def __init__(self, bookName, author, bookId, edition):
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
        return "'{}' '{}' '{}' '{}'".format(self.bookName, self.author, self.bookId, self.edition)

    def checkId(self, idCheck):
        if self.bookId == idCheck:
            return True


import random
'''
i made 6 lists
the userList is a list of all the users information
the librarian list is a list of all the librarian information
the bookInfoList is a list of all the different types of books (not count)
the bookList is a dictionary of the book name and the count of each book
the bookCheckOutList is a dictionary of the bookID and which userID its checked out to


when making an account i take infomration from the user and i then create a person object
out of it and i append it to the end of the userlist or librarian list depending on which we
are making

to check the username i go through the list of librarian information and i check if the id matches
any of the ids in the list. if it does then i prompt for the pass word and the password and id
must be both in the same librarian

once the information has been given, the librarian/user has a few options of what they want to to
'''
print(str(random.randrange(1, 100)))
userList = []
librarianList = []
bookInfoList = []
bookList = {}
bookCheckOutList = {}
while True:
    print(userList)
    print(librarianList)
    print(bookInfoList)
    print(bookList)
    print(bookCheckOutList)
    print("""Welcome to Davis Library""")
    personInput = input("Continue as user or librarian \n Login Menu: \n a) Librarian \n b) User \n c) Save to File")
    if personInput == "a":
        librarianInput = input("""Are you a: \n 1) Existing Librarian \n 2) New Librarian""")
        if librarianInput == "2":
            librarianFirstName = str(input("Enter First Name"))
            librarianLastName = str(input("Enter Last Name"))
            librarianDOB = str(input("Enter DOB in the format of MM-DD-YYYY"))
            librarianPassword = str(input("Enter in the password for your account"))
            librarianId = str(random.randrange(1, 100)) + librarianDOB
            librarian = Person(librarianFirstName, librarianLastName, librarianDOB, librarianId, librarianPassword)
            librarianList.append(librarian)
            print("Thank you for registering, your u_id is: ", librarianId)
            print(librarianList)

        if librarianInput == "1":
            librarianIdInput = input("Enter Librarian Id")
            foundId = False
            foundId1 = False
            for people in librarianList:
                if people.checkId(librarianIdInput):
                    foundId = True
            if foundId:
                librarianPassInput = input("Enter Librarian Password")
                for people in librarianList:
                    if people.checkId(librarianIdInput):
                        if people.checkPassword(librarianPassInput):
                            foundId1 = True
            if foundId1:
                choice = input("1) List of Books available \n 2) List of Books issued to users \n 3) Add Book \n " +
                               "4) Delete Book \n 5) Update Book")
                if choice == "1":
                    print(bookList)
                if choice == "3":
                    bookName = str(input("Enter Book Name"))
                    bookAuthor = str(input("Enter Author Full Name"))
                    bookEdition = str(input("Enter Book Edition"))
                    bookId = str(random.randrange(1, 100)) + bookName
                    print(bookId)
                    book = Book(bookName, bookAuthor, bookId, bookEdition)
                    if bookName in bookList:
                        x = bookList[bookName] + 1
                        bookList[bookName] = x
                    else:
                        bookList[bookName] = 1
                    bookInfoList.append(book)
                    print("Book Id is: ", bookId)
                if choice == "2":
                    print(bookCheckOutList)
                if choice == "4":
                    bookIdDelete = input("Type in the bookId to Delete")
                    for people in bookInfoList:
                        if people.checkId(bookIdDelete):
                            bookNameDelete = people.bookName
                            foundId = True
                            x = bookList[bookNameDelete] - 1
                            bookList[bookNameDelete] = x
                    print(bookList)
                if choice == "5":
                    bookIdUpdate = input("Type in the bookId to Update")
                    foundId = False
                    for people in bookInfoList:
                        if people.checkId(bookIdUpdate):
                            bookNameDelete = people.bookName
                            x = bookList[bookNameDelete]
                            if x >= 1:
                                foundId = True
                                x -= 1
                                bookList[bookNameDelete] = x
                            else:
                                print("There are no copies of that book")

                    if foundId:
                        newBookName = str(input("Enter Book Name"))
                        newBookAuthor = str(input("Enter Author Full Name"))
                        newBookEdition = str(input("Enter Book Edition"))
                        newBook = Book(newBookName, newBookAuthor, bookIdUpdate, newBookEdition)
                        print(newBook)
                        if newBookName in bookList:
                            x = bookList[newBookName] + 1
                            bookList[newBookName] = x
                        else:
                            bookList[newBookName] = 1
                        bookInfoList.append(newBook)

    if personInput == "b":
        userInput = input("""1)Existing User \n 2) New User""")
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
            foundId1 = False
            for people in userList:
                if people.checkId(userIdInput):
                    foundId = True
            if foundId:
                userPassInput = input("Enter User Password")
                for people in userList:
                    if people.checkId(userPassInput):
                        if people.checkPassword(userPassInput):
                            foundId1 = True
            if foundId1:
                userControl = input("""1) Issue a Book \n 2) Books Issued \n 3) Return a Book""")
                if userControl == "1":
                    bookIdCheckout = input("Type in the book id you want to check out")
                    for people in bookInfoList:
                        if people.checkId(bookIdCheckout):
                            bookNameDelete = people.bookName
                            bookIdUserGive = people.bookId
                            x = bookList[bookNameDelete]
                            if x >= 1:
                                x -= 1
                                bookList[bookNameDelete] = x
                                bookCheckOutList[bookIdUserGive] = userIdInput
                            else:
                                print("There are no books under that ID")
                if userControl == "2":
                    for key, value in bookCheckOutList.items():
                        if userIdInput == value:
                            print(key, ",", value)
                if userControl == "3":
                    bookIdCheckIn = input("Type in the book id you want to return")
                    for people in bookInfoList:
                        if people.checkId(bookIdCheckIn):
                            bookIdUserReturn = people.bookId
                            bookCheckOutList.pop(bookIdUserReturn)
                            bookNameAdd = people.bookName
                            if bookNameAdd in bookList:
                                x = bookList[bookNameAdd] + 1
                                bookList[bookNameAdd] = x
                            else:
                                bookList[bookNameAdd] = 1
