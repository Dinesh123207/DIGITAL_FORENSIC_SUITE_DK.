import datetime

class Date:
    def __init__(self):
        self.d = 0
        self.m = 0
        self.y = 0

def timer():
    now = datetime.datetime.now()
    print(now.strftime("%d/%m/%Y %H:%M:%S"))

def get_date():
    date = Date()
    try:
        date.d = int(input("Enter day: "))
        date.m = int(input("Enter month: "))
        date.y = int(input("Enter year: "))
    except ValueError:
        print("Invalid date format.")
        return get_date()
    
    if not correct_date(date.d, date.m, date.y):
        print("Invalid date.")
        return get_date()
    
    return date

def correct_date(d, m, y):
    try:
        datetime.datetime(y, m, d)
        return True
    except ValueError:
        return False

def day_in_month(m, y):
    if m == 2:
        if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0):
            return 29
        else:
            return 28
    elif m in [4, 6, 9, 11]:
        return 30
    else:
        return 31

class Book:
    def __init__(self):
        self.bno = 0
        self.bname = ""
        self.bauthor = ""
        self.bprice = 0.0
        self.status = "AVAILABLE"
        self.isno = 0

    def set_data(self):
        while True:
            try:
                self.bno = int(input("Enter book number: "))
                # Check if the book number already exists
                # Implement the searchbook() function to check the existence of the book number
                # if searchbook(self.bno) is True:
                #     print("Book with this number already exists! Try another number.")
                #     continue
                break
            except ValueError:
                print("Invalid book number.")
        
        self.bname = input("Enter book name: ")
        self.bauthor = input("Enter book author: ")
        
        while True:
            try:
                self.bprice = float(input("Enter book price: "))
                break
            except ValueError:
                print("Invalid price format.")

    def show_data(self):
        print("Book Number:", self.bno)
        print("Book Name:", self.bname)
        print("Book Author:", self.bauthor)
        print("Book Price:", self.bprice)

class Member:
    def __init__(self):
        self.mno = 0
        self.mname = ""
        self.maddress = ""
        self.pno = 0
        self.ino = 0
        self.dob = Date()

    def set_data(self):
        while True:
            try:
                self.mno = int(input("Enter member number: "))
                # Check if the member number already exists
                # Implement the searchmember() function to check the existence of the member number
                # if searchmember(self.mno) is True:
                #     print("Member with this number already exists! Try another number.")
                #     continue
                break
            except ValueError:
                print("Invalid member number.")
        
        self.mname = input("Enter member name: ")
        self.maddress = input("Enter member address: ")
        
        while True:
            try:
                self.pno = int(input("Enter phone number: "))
                break
            except ValueError:
                print("Invalid phone number format.")
        
        self.dob = get_date()

    def show_data(self):
        print("Member Number:", self.mno)
        print("Member Name:", self.mname)
        print("Member Address:", self.maddress)
        print("Phone Number:", self.pno)
        print("Date of Birth:", self.dob.d, self.dob.m, self.dob.y)

def add_book(books):
    book = Book()
    book.set_data()
    books.append(book)
    print("Book added successfully.")

def delete_book(books, bno):
    for book in books:
        if book.bno == bno:
            books.remove(book)
            print("Book deleted successfully.")
            return
    print("Book not found.")

def add_member(members):
    member = Member()
    member.set_data()
    members.append(member)
    print("Member added successfully.")

def delete_member(members, mno):
    for member in members:
        if member.mno == mno:
            members.remove(member)
            print("Member deleted successfully.")
            return
    print("Member not found.")

def display_books(books):
    for book in books:
        book.show_data()
        print()

def display_members(members):
    for member in members:
        member.show_data()
        print()

def search_book(books, bno):
    for book in books:
        if book.bno == bno:
            print("Book found:")
            book.show_data()
            return
    print("Book not found.")

def search_member(members, mno):
    for member in members:
        if member.mno == mno:
            print("Member found:")
            member.show_data()
            return
    print("Member not found.")

def issue_book(books, members, bno, mno):
    book_found = False
    member_found = False
    
    for book in books:
        if book.bno == bno:
            book_found = True
            if book.status == "AVAILABLE":
                for member in members:
                    if member.mno == mno:
                        member_found = True
                        book.status = "ISSUED"
                        book.isno += 1
                        print("Book issued successfully.")
                        return
                print("Member not found.")
                return
            print("Book already issued.")
            return
    
    if not book_found:
        print("Book not found.")

def return_book(books, bno):
    for book in books:
        if book.bno == bno:
            if book.status == "ISSUED":
                book.status = "AVAILABLE"
                book.isno -= 1
                print("Book returned successfully.")
                return
            print("Book is not issued.")
            return
    print("Book not found.")

def main():
    books = []
    members = []
    
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Delete Book")
        print("3. Add Member")
        print("4. Delete Member")
        print("5. Display Books")
        print("6. Display Members")
        print("7. Search Book")
        print("8. Search Member")
        print("9. Issue Book")
        print("10. Return Book")
        print("11. Display Date and Time")
        print("12. Exit")
        
        choice = input("Enter your choice (1-12): ")
        
        if choice == "1":
            add_book(books)
        elif choice == "2":
            bno = int(input("Enter book number to delete: "))
            delete_book(books, bno)
        elif choice == "3":
            add_member(members)
        elif choice == "4":
            mno = int(input("Enter member number to delete: "))
            delete_member(members, mno)
        elif choice == "5":
            display_books(books)
        elif choice == "6":
            display_members(members)
        elif choice == "7":
            bno = int(input("Enter book number to search: "))
            search_book(books, bno)
        elif choice == "8":
            mno = int(input("Enter member number to search: "))
            search_member(members, mno)
        elif choice == "9":
            bno = int(input("Enter book number to issue: "))
            mno = int(input("Enter member number: "))
            issue_book(books, members, bno, mno)
        elif choice == "10":
            bno = int(input("Enter book number to return: "))
            return_book(books, bno)
        elif choice == "11":
            timer()
        elif choice == "12":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
