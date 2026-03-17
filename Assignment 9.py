#1
# class Employee:
#     def __init__(self, name, age, salary, address):
#         self.name = name
#         self.age = age
#         self.salary = salary
#         self.address = address
#
#     def display(self):
#         print("Name:", self.name)
#         print("Age:", self.age)
#         print("Salary:", self.salary)
#         print("Address:", self.address)
#
#
# class Manager(Employee):
#     def __init__(self, name, age, salary, address, department):
#         super().__init__(name, age, salary, address)
#         self.department = department
#
#     def display_manager(self):
#         print("\nManager Information")
#         super().display()
#         print("Department:", self.department)
#
#
# managers = []
#
# for i in range(10):
#     print("\nEnter details of Manager", i+1)
#
#     name = input("Enter Name: ")
#     age = int(input("Enter Age: "))
#     salary = float(input("Enter Salary: "))
#     address = input("Enter Address: ")
#     department = input("Enter Department: ")
#
#     m = Manager(name, age, salary, address, department)
#     managers.append(m)
#
# print(" Managers Information ")
#
# for m in managers:
#     m.display_manager()


#2
class Book:
    def __init__(self, title):
        self.title = title
        self.available = True


class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title):
        book = Book(title)
        self.books.append(book)
        print("Book added successfully")

    def show_books(self):
        print("\nLibrary Books:")
        for book in self.books:
            status = "Available" if book.available else "Not Available"
            print(book.title, "-", status)

    def lend_book(self, title, member):
        for book in self.books:
            if book.title == title and book.available:
                book.available = False
                member.borrowed_books.append(title)
                print("Book issued successfully")
                return
        print("Book not available")

    def return_book(self, title, member):
        for book in self.books:
            if book.title == title:
                book.available = True
                member.borrowed_books.remove(title)
                print("Book returned successfully")
                return


library = Library()
member = Member("Student")

while True:
    print("\n1.Add Book")
    print("2.Show Books")
    print("3.Lend Book")
    print("4.Return Book")
    print("5.Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        title = input("Enter book title: ")
        library.add_book(title)

    elif choice == 2:
        library.show_books()

    elif choice == 3:
        title = input("Enter book title to lend: ")
        library.lend_book(title, member)

    elif choice == 4:
        title = input("Enter book title to return: ")
        library.return_book(title, member)

    elif choice == 5:
        print("Exiting program")
        break

    else:
        print("Invalid choice")