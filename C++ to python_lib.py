import os
import datetime


class Date:
    def __init__(self, d, m, y):
        self.d = d
        self.m = m
        self.y = y


def get_date():
    while True:
        try:
            d = int(input("Enter day: "))
            m = int(input("Enter month: "))
            y = int(input("Enter year: "))
            datetime.datetime(y, m, d)  # Check if the date is valid
            return Date(d, m, y)
        except ValueError:
            print("Invalid date. Please try again.")


def day_in_month(m, y):
    if m in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif m in [4, 6, 9, 11]:
        return 30
    elif m == 2:
        if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0):
            return 29
        else:
            return 28


class Book:
    def __init__(self):
        self.bno = None
        self.bname = ""
        self.bauthor = ""
        self.bprice = 0.0
        self.status = "AVAILABLE"
        self.isno = 0

    def set_data(self):
        while True:
            try:
                self.bno = int(input("Enter book number: "))
                # Search if book with this number already exists
                if search_book(self.bno):
                    print("Book with this number already exists! Please try another number.")
                else:
                    break
            except ValueError:
                print("Invalid book number. Please try again.")

        self.bname = input("Enter book name: ")
        self.bauthor = input("Enter book author: ")
        while True:
            try:
                self.bprice = float(input("Enter price: "))
                break
            except ValueError:
                print("Invalid price. Please try again.")

    def show_data(self):
        print("\nBook Number: ", self.bno)
        print("Book Name: ", self.bname)
        print("Book Author: ", self.bauthor)
        print("Book Price: ", self.bprice)


class Member:
    def __init__(self):
        self.mno = None
        self.mname = ""
        self.maddress = ""
        self.pno = 0
        self.ino = 0
        self.dob = None

    def set_data(self):
        while True:
            try:
                self.mno = int(input("Enter member number: "))
                # Search if member with this number already exists
                if search_member(self.mno):
                    print("Member with this number already exists! Please try another number.")
                else:
                    break
            except ValueError:
                print("Invalid member number. Please try again.")

        self.mname = input("Enter member name: ")
        self.maddress = input("Enter member address: ")
        while True:
            try:
                self.pno = int(input("Enter phone number: "))
                break
            except ValueError:
                print("Invalid phone number. Please try again.")

        print("Enter date of birth:")
        self.dob = get_date()

    def show_data(self):
        print("\nMember Number: ", self.mno)
        print("Member Name: ", self.mname)
        print("Member Address: ", self.maddress)
        print("Phone Number: ", self.pno)
        print("Number of Books: ", self.ino)
        print("Date of Birth: ", self.dob.d, "/", self.dob.m, "/", self.dob.y)


def book_entry():
    book = Book()
    book.set_data()

    try:
        with open("book.dat", "ab") as file:
            file.write(str(book.bno).encode() + b"\n")
            file.write(book.bname.encode() + b"\n")
            file.write(book.bauthor.encode() + b"\n")
            file.write(str(book.bprice).encode() + b"\n")
            file.write(book.status.encode() + b"\n")
            file.write(str(book.isno).encode() + b"\n")
        print("\nBook record added successfully!")
    except IOError:
        print("Error occurred while adding book record.")


def book_delete():
    bno = int(input("Enter book number to delete: "))

    if not search_book(bno):
        print("Book not found!")
        return

    try:
        with open("book.dat", "rb") as file:
            lines = file.readlines()
        with open("book.dat", "wb") as file:
            for i in range(0, len(lines), 6):
                if int(lines[i].decode().strip()) != bno:
                    file.write(lines[i])
                    file.write(lines[i + 1])
                    file.write(lines[i + 2])
                    file.write(lines[i + 3])
                    file.write(lines[i + 4])
                    file.write(lines[i + 5])
        print("Book record deleted successfully!")
    except IOError:
        print("Error occurred while deleting book record.")


def book_list():
    try:
        with open("book.dat", "rb") as file:
            lines = file.readlines()

        if len(lines) == 0:
            print("No books found!")
        else:
            print("\nBOOK LIST\n")
            for i in range(0, len(lines), 6):
                book = Book()
                book.bno = int(lines[i].decode().strip())
                book.bname = lines[i + 1].decode().strip()
                book.bauthor = lines[i + 2].decode().strip()
                book.bprice = float(lines[i + 3].decode().strip())
                book.status = lines[i + 4].decode().strip()
                book.isno = int(lines[i + 5].decode().strip())
                book.show_data()
                print("----------------------------------")
    except IOError:
        print("Error occurred while accessing book records.")


def member_entry():
    member = Member()
    member.set_data()

    try:
        with open("member.dat", "ab") as file:
            file.write(str(member.mno).encode() + b"\n")
            file.write(member.mname.encode() + b"\n")
            file.write(member.maddress.encode() + b"\n")
            file.write(str(member.pno).encode() + b"\n")
            file.write(str(member.ino).encode() + b"\n")
            file.write(str(member.dob.d).encode() + b"\n")
            file.write(str(member.dob.m).encode() + b"\n")
            file.write(str(member.dob.y).encode() + b"\n")
        print("\nMember record added successfully!")
    except IOError:
        print("Error occurred while adding member record.")


def member_delete():
    mno = int(input("Enter member number to delete: "))

    if not search_member(mno):
        print("Member not found!")
        return

    try:
        with open("member.dat", "rb") as file:
            lines = file.readlines()
        with open("member.dat", "wb") as file:
            for i in range(0, len(lines), 8):
                if int(lines[i].decode().strip()) != mno:
                    file.write(lines[i])
                    file.write(lines[i + 1])
                    file.write(lines[i + 2])
                    file.write(lines[i + 3])
                    file.write(lines[i + 4])
                    file.write(lines[i + 5])
                    file.write(lines[i + 6])
                    file.write(lines[i + 7])
        print("Member record deleted successfully!")
    except IOError:
        print("Error occurred while deleting member record.")


def member_list():
    try:
        with open("member.dat", "rb") as file:
            lines = file.readlines()

        if len(lines) == 0:
            print("No members found!")
        else:
            print("\nMEMBER LIST\n")
            for i in range(0, len(lines), 8):
                member = Member()
                member.mno = int(lines[i].decode().strip())
                member.mname = lines[i + 1].decode().strip()
                member.maddress = lines[i + 2].decode().strip()
                member.pno = int(lines[i + 3].decode().strip())
                member.ino = int(lines[i + 4].decode().strip())
                member.dob = Date(
                    int(lines[i + 5].decode().strip()),
                    int(lines[i + 6].decode().strip()),
                    int(lines[i + 7].decode().strip())
                )
                member.show_data()
                print("----------------------------------")
    except IOError:
        print("Error occurred while accessing member records.")


def issue_book():
    mno = int(input("Enter member number: "))
    if not search_member(mno):
        print("Member not found!")
        return

    bno = int(input("Enter book number: "))
    if not search_book(bno):
        print("Book not found!")
        return

    try:
        with open("member.dat", "rb") as file:
            lines = file.readlines()
        with open("member.dat", "wb") as file:
            for i in range(0, len(lines), 8):
                if int(lines[i].decode().strip()) == mno:
                    member = Member()
                    member.mno = int(lines[i].decode().strip())
                    member.mname = lines[i + 1].decode().strip()
                    member.maddress = lines[i + 2].decode().strip()
                    member.pno = int(lines[i + 3].decode().strip())
                    member.ino = int(lines[i + 4].decode().strip())
                    member.dob = Date(
                        int(lines[i + 5].decode().strip()),
                        int(lines[i + 6].decode().strip()),
                        int(lines[i + 7].decode().strip())
                    )
                    member.ino += 1
                    file.write(str(member.mno).encode() + b"\n")
                    file.write(member.mname.encode() + b"\n")
                    file.write(member.maddress.encode() + b"\n")
                    file.write(str(member.pno).encode() + b"\n")
                    file.write(str(member.ino).encode() + b"\n")
                    file.write(str(member.dob.d).encode() + b"\n")
                    file.write(str(member.dob.m).encode() + b"\n")
                    file.write(str(member.dob.y).encode() + b"\n")
                else:
                    file.write(lines[i])
                    file.write(lines[i + 1])
                    file.write(lines[i + 2])
                    file.write(lines[i + 3])
                    file.write(lines[i + 4])
                    file.write(lines[i + 5])
                    file.write(lines[i + 6])
                    file.write(lines[i + 7])
    except IOError:
        print("Error occurred while updating member record.")

    try:
        with open("book.dat", "rb") as file:
            lines = file.readlines()
        with open("book.dat", "wb") as file:
            for i in range(0, len(lines), 6):
                if int(lines[i].decode().strip()) == bno:
                    book = Book()
                    book.bno = int(lines[i].decode().strip())
                    book.bname = lines[i + 1].decode().strip()
                    book.bauthor = lines[i + 2].decode().strip()
                    book.bprice = float(lines[i + 3].decode().strip())
                    book.status = "ISSUED"
                    book.isno = mno
                    file.write(str(book.bno).encode() + b"\n")
                    file.write(book.bname.encode() + b"\n")
                    file.write(book.bauthor.encode() + b"\n")
                    file.write(str(book.bprice).encode() + b"\n")
                    file.write(book.status.encode() + b"\n")
                    file.write(str(book.isno).encode() + b"\n")
                else:
                    file.write(lines[i])
                    file.write(lines[i + 1])
                    file.write(lines[i + 2])
                    file.write(lines[i + 3])
                    file.write(lines[i + 4])
                    file.write(lines[i + 5])
    except IOError:
        print("Error occurred while updating book record.")

    print("Book issued successfully!")


def return_book():
    bno = int(input("Enter book number: "))
    if not search_book(bno):
        print("Book not found!")
        return

    try:
        with open("book.dat", "rb") as file:
            lines = file.readlines()
        with open("book.dat", "wb") as file:
            for i in range(0, len(lines), 6):
                if int(lines[i].decode().strip()) == bno:
                    book = Book()
                    book.bno = int(lines[i].decode().strip())
                    book.bname = lines[i + 1].decode().strip()
                    book.bauthor = lines[i + 2].decode().strip()
                    book.bprice = float(lines[i + 3].decode().strip())
                    book.status = "AVAILABLE"
                    book.isno = 0
                    file.write(str(book.bno).encode() + b"\n")
                    file.write(book.bname.encode() + b"\n")
                    file.write(book.bauthor.encode() + b"\n")
                    file.write(str(book.bprice).encode() + b"\n")
                    file.write(book.status.encode() + b"\n")
                    file.write(str(book.isno).encode() + b"\n")
                else:
                    file.write(lines[i])
                    file.write(lines[i + 1])
                    file.write(lines[i + 2])
                    file.write(lines[i + 3])
                    file.write(lines[i + 4])
                    file.write(lines[i + 5])
    except IOError:
        print("Error occurred while updating book record.")

    print("Book returned successfully!")


def search_book(bno):
    try:
        with open("book.dat", "rb") as file:
            lines = file.readlines()

        for i in range(0, len(lines), 6):
            if int(lines[i].decode().strip()) == bno:
                return True

        return False
    except IOError:
        return False


def search_member(mno):
    try:
        with open("member.dat", "rb") as file:
            lines = file.readlines()

        for i in range(0, len(lines), 8):
            if int(lines[i].decode().strip()) == mno:
                return True

        return False
    except IOError:
        return False


def main():
    while True:
        print("\nLIBRARY MANAGEMENT SYSTEM")
        print("1. Add book")
        print("2. Delete book")
        print("3. List all books")
        print("4. Add member")
        print("5. Delete member")
        print("6. List all members")
        print("7. Issue book")
        print("8. Return book")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            book_entry()
        elif choice == "2":
            book_delete()
        elif choice == "3":
            book_list()
        elif choice == "4":
            member_entry()
        elif choice == "5":
            member_delete()
        elif choice == "6":
            member_list()
        elif choice == "7":
            issue_book()
        elif choice == "8":
            return_book()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
