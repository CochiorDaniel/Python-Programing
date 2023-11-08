class LibraryItem:
    def __init__(self, title, author, publication_date):
        self.title = title
        self.author = author
        self.publication_date = publication_date
        self.checked_out = False

    def check_out(self):
        if not self.checked_out:
            self.checked_out = True
            return f"{self.title} has been checked out."
        else:
            return f"{self.title} is already checked out."

    def return_item(self):
        if self.checked_out:
            self.checked_out = False
            return f"{self.title} has been returned."
        else:
            return f"{self.title} was not checked out."

    def display_info(self):
        return f"Title: {self.title}, Author: {self.author}, Publication Date: {self.publication_date}"


class Book(LibraryItem):
    def __init__(self, title, author, publication_date, genre):
        super().__init__(title, author, publication_date)
        self.genre = genre

    def display_info(self):
        return super().display_info() + f", Genre: {self.genre}"


class DVD(LibraryItem):
    def __init__(self, title, director, publication_date, genre):
        super().__init__(title, director, publication_date)
        self.genre = genre

    def display_info(self):
        return super().display_info() + f", Genre: {self.genre}"


class Magazine(LibraryItem):
    def __init__(self, title, publisher, publication_date, edition):
        super().__init__(title, publisher, publication_date)
        self.edition = edition

    def display_info(self):
        return super().display_info() + f", Edition: {self.edition}"


book = Book('Capra cu trei iezi', 'Ion Creanga', '1875', 'Fiction')
print(book.display_info())
print(book.check_out())
print(book.return_item())
