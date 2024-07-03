class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.books_borrowed = 0

class Book:
    def __init__(self, book_id, title, author, year_published, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year_published = year_published
        self.copies = copies
class Library:
    def __init__(self):
        self.students = {}
        self.books = {}