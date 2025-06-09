import datetime

late_fee_per_day = 10


class Books:
    def __init__(self):
        self.collections = {}

    def add_books(self, book_name):
        if book_name in self.collections:
            return f"{book_name} book is already present"
        self.collections[book_name] = {'name': '', 'borrow_date': '', 'return_date': ''}
        return f"{book_name} book is successfully added to the collection"

    def remove_books(self, book_name):
        if book_name in self.collections:
            del self.collections[book_name]
            return f"{book_name} book is successfully removed to the collection"
        return f"{book_name} book is not found in the collection"


class Student:
    def __init__(self, name):
        self.name = name
        self.books_taken = {}

    def borrow_book(self, book, book_name, date, days):
        if book_name in book.collections:
            date_obj = datetime.datetime.strptime(date, "%d/%m/%Y")
            if book.collections[book_name]['return_date'] == '' or book.collections[book_name]['return_date'] <= date_obj:
                book.collections[book_name]['name'] = self.name
                book.collections[book_name]['borrow_date'] = date_obj
                book.collections[book_name]['return_date'] = date_obj + datetime.timedelta(days=days)
                self.books_taken[book_name] = date_obj + datetime.timedelta(days=days)
                return f"{book_name} book has been borrowed by {self.name}"
            else:
                return f"{book_name} book will be available by {book.collections[book_name]['return_date'].strftime("%d/%m/%Y")}"
        return f"{book_name} book is not found in the collection"

    def return_book(self, book, book_name, date):
        date_obj = datetime.datetime.strptime(date, "%d/%m/%Y")
        if book_name in self.books_taken:
            original_return_date = book.collections[book_name]['return_date']
            if original_return_date < date_obj:
                penalty = late_fee_per_day * (date_obj - original_return_date).days
                print(f"Please pay a fine of {penalty} rupees for late return")
            book.collections[book_name]['return_date'] = date_obj
            book.collections[book_name]['name'] = ''
            del self.books_taken[book_name]
            return f"{book_name} is successfully returned by {self.name}"
        return f"{book_name} was never taken by {self.name}"


if __name__ == "__main__":
    book = Books()
    student1 = Student("John Doe")
    student2 = Student("Anna")
    print(book.add_books("Python Programming"))
    print(book.add_books("Data Structures"))
    print(book.add_books("Machine Learning"))
    print(student1.borrow_book(book, "Python Programming", "01/01/2023", 10))
    print(student1.return_book(book, "Python Programming", "15/01/2023"))
    print(student1.borrow_book(book, "Data Structures", "05/01/2023", 5))
    print(student1.return_book(book, "Data Structures", "10/01/2023"))
    print(student1.return_book(book, "Python Programming", "20/01/2023"))
    print(student2.borrow_book(book, "Python Programming", "15/01/2023", 2))
    print(student2.return_book(book, "Python Programming", "18/01/2023"))
    print(book.remove_books("Python Programming"))






