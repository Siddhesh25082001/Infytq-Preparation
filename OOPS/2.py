# Book.py -> Displays all the Book Titles and their respective Authors

class Book:
    
    def __init__(self, name):
        self.name = name
        
    def get_title(self):
        title = self.name.split("-")[0]
        return ("Title -> " + title)
    
    def get_author(self):
        author = self.name.split("-")[1]
        return ("Author -> " + author)

PP = Book("Pride and Prejudice - Jane Austen")
H = Book("Hamlet - William Shakespeare")
WP = Book("War and Peace - Leo Tolstoy")

print("\n Solution to Question-2: ")
print("------------------------ \n")

print(PP.get_title())
print(PP.get_author())
print("----------------------------- \n")

print(H.get_title())
print(H.get_author())
print("----------------------------- \n")

print(WP.get_title())
print(WP.get_author())
print("----------------------------- \n")