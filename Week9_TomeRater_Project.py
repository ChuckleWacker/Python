# TOME RATER PROJECT
# CLASSES:
class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):  # Returns email associated with the user
        return email

    def change_email(self, address):  # Takes in a new email and changes the email associated with the user
        self.email = address
        print("This user's email has been updated")  # Should also print a message saying the users email was updated

    def __repr__(self):  # Returns a string to print out this user object in a meaningful way.
        return "User: {},  Email: {},  Books Read: {}.".format(self.name, self.email, self.len(books))

    def __eq__(self, other_user):
        # method to define comparison between users. A User object should be equal to another User object if they
        # both have the same name and email.
        pass

# PAGE 3 "Create a Book"