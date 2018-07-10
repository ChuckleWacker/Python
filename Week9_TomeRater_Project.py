# TOME RATER PROJECT
# CLASSES:
class User:  # Methods Tested
    def __init__(self, name, email):
        self.name = name  # String
        self.email = email  # String
        self.books = {}  # Instance variable

    def get_email(self):  # Returns email associated with the user
        return self.email

    def change_email(self, address):  # Takes in a new email and changes the email associated with the user
        self.email = address
        print("This user's email has been updated")  # Should also print a message saying the users email was updated

    def read_book(self, book, rating):  # Page5 ###################################################################
        if rating == "":
            rating = "None"
        self.books[book] = rating

    def get_average_rating(self):
        # Iterates through all of the values in self.books, which are the ratings, and calculates the average rating.
        # It should return this average.
        total_ratings = 0
        for book in self.books:
            for rating in book.get(book):
                total_ratings += rating
        return total_ratings / len(self.books)  # Divide total_ratings by the number of books in dictionary


    def __repr__(self):  # Returns a string to print out this user object in a meaningful way.
        return "User: {},  Email: {},  Books Read: {}.".format(self.name, self.email, len(self.books))

    def __eq__(self, other_user):  # Returns True if name & email match, else False
        return self.name == other_user.name and self.email == other_user.email
# TESTS
alan = User("Alan Turing", "alan@turing.com")
dan = User("Daniel Boggs", "dan@email.com")
alan.change_email("new@email.com")
print(alan)
print(alan.__eq__(dan))  # Prints False
print(alan.__eq__(alan))  # Prints True


class Book:
    def __init__(self, title, isbn):
        self.title = title  # String
        self.isbn = isbn  # Number
        self.ratings = []  # Instance variable as empty list

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, isbn):
        self.isbn = isbn
        print("This book's ISBN has been updated")  # Should also print a message saying the book's ISBN was updated

    def add_rating(self, rating):  # Adds to Rating List if between 0-4, else prints invalid
        if rating >= 0 and rating <= 4:
            self.ratings.append(rating)
        else:
            print("Invalid Rating")

    def get_average_rating(self):
        total_ratings = 0
        for rating in self.ratings:
            total_ratings += rating
        return total_ratings / len(self.ratings)

    def __hash__(self):  # Allows the book to be hashable. https://docs.python.org/3/library/functions.html#hash
        return hash((self.title, self.isbn))

    def __eq__(self, other_book):  # Returns True if title & isbn match, else False
        return self.title == other_book.title and self.isbn == other_book.isbn


class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author  # String

    def get_author(self):
        return self.author

    def __repr__(self):
        return "{} by {}".format(self.title, self.author)
fict1 = Fiction("Alice In Wonderland", "Lewis Carroll", 12345)
fict2 = Fiction("Chthulu", "HP Lovecraft", 112233)
print(fict1)
print(fict1.get_author())


class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject  # String
        self.level = level  # String

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "{}, a {} manual on {}".format(self.title, self.level, self.subject)
non_fict1 = Non_Fiction("Automate the Boring Stuff", "Python", "beginner", 1929452)
non_fict2 = Non_Fiction("Computing Machinery and Intelligence", "AI", "advanced", 11111938)
print(non_fict1)
print(non_fict2)
non_fict2.add_rating(2)
print(non_fict2.ratings)  # Prints 2
print(non_fict1.__eq__(non_fict1))  # Returns True


class TomeRater:
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        book = Book(title, isbn)
        return book

    def create_novel(self, title, author, isbn):
        fiction = Fiction(title, author, isbn)
        return fiction

    def create_non_fiction(self, title, subject, level, isbn):
        non_fiction = Non_Fiction(title, subject, level, isbn)
        return non_fiction

    def add_book_to_user(self, book, email, rating):  # #########################################################
        if len(rating) == 0:
            rating = None
        if


    def add_user(self, name, email, books):
        user = User(name, email)
        if len(books) == 0:
            books = None
        else:
            for book in books:
                self.add_book_to_user(book, email, )



test_book = TomeRater()
print(test_book.create_book("Book", 1111))
test_novel = TomeRater()
print(test_novel.create_novel("Novel", "R.L. Stein", 2222))
test_nonfiction = TomeRater()
print(test_nonfiction.create_non_fiction("NonFiction", "Writing", "Hard", 3333))


print("End")
