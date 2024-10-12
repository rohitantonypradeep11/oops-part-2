class Library:
    def __init__(self, list_of_books, name):
        self.booklist = list_of_books
        self.name = name
        self.lendDict = {}

    def displaybooks(self):
        print(f"We have the following books in our library: {self.name}")
        for book in self.booklist:
            print(book)

    def lendbook(self, user, book):
        if book not in self.booklist:
            print("Sorry, we don't have that book.")
        elif book in self.lendDict:
            print(f"The book is already in use by {self.lendDict[book]}.")
        else:
            self.lendDict[book] = user
            print("Book database has been updated.")

    def addbook(self, book):
        self.booklist.append(book)
        print(f"{book} has been added to the book list.")

    def returnbook(self, book):
        if book in self.lendDict:
            del self.lendDict[book]
            print("Book has been returned.")
        else:
            print("The book wasn't borrowed.")

if __name__ == '__main__':
    library = Library(['Python', 'Rich Dad Poor Dad', 'Harry Potter', 'Algorithms'], "Let's Upscale")
    user = input("Welcome to our library, please enter your name: ")
    
    while True:
        print(f"\nHello {user}, welcome to the {library.name} library. Please select an option:")
        print("1. Display books\n2. Lend a book\n3. Add a book\n4. Return a book\n5. Quit")
        choice = input("Enter a choice: ")
        
        if choice not in ['1', '2', '3', '4', '5']:
            print("Please enter a valid option.")
            continue
        
        if choice == '1':
            library.displaybooks()
        elif choice == '2':
            book_name = input("Enter the name of the book: ")
            library.lendbook(user, book_name)
        elif choice == '3':
            book_name = input("Enter the name of the book: ")
            library.addbook(book_name)
        elif choice == '4':
            book_name = input("Enter the name of the book: ")
            library.returnbook(book_name)
        elif choice == '5':
            print("Goodbye!")
            break

            