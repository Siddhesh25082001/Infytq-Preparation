# User.py -> Counts the no of Users

class User:
    
    counter = 0
    def __init__(self, username):
        self.username = username
        User.counter = User.counter + 1
        
    def display_count(self):
        print("User.user_count -> ", self.counter)
        
print("\n Solution to Question-1: ")
print("----------------------------- \n")

u1 = User("johnsmith10")
u1.display_count()
print("u1.username -> ", u1.username)
print("----------------------------- \n")

u2 = User("marysue1989")
u2.display_count()
print("u2.username -> ", u2.username)
print("----------------------------- \n")

u3 = User("milan_rodrick")
u3.display_count()
print("u3.username -> ", u3.username)
print("----------------------------- \n")