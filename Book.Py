# Base class: Book
class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
    
    def read(self):
        print(f"📖 You are reading '{self.title}' by {self.author}.")
    
    def get_summary(self):
        return f"'{self.title}' has {self.pages} pages and costs ${self.price}."


# Subclass: EBook (inherits from Book)
class EBook(Book):
    def __init__(self, title, author, pages, price, file_size):
        super().__init__(title, author, pages, price)
        self.file_size = file_size
    
    # Polymorphism: Overriding method
    def read(self):
        print(f"💻 You are reading the eBook '{self.title}' on your device.")
    
    def download(self):
        print(f"⬇️ Downloading '{self.title}'... ({self.file_size}MB)")


# Example usage
book1 = Book("1984", "George Orwell", 328, 9.99)
ebook1 = EBook("Python Crash Course", "Jimmy Yoakin", 544, 19.99, 5)

book1.read()
print(book1.get_summary())

ebook1.read()
ebook1.download()
