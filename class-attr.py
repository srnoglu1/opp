class User:

    active_users = 0

    def __init__(self,first,last,age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1

    def full_name(self):
        return f"{self.first} {self.last}"

    def logout(self):
        User.active_users -= 1
        return f"{self.full_name()} exited the application."


userA = User("Sadık","KARTAL",12)
userB = User("Osman","AKTAN",15)
userC = User("Hasan","SARAL",24)

print(User.active_users)
print(userA.logout())
print(User.active_users)

print(userA.full_name())
print(userB.full_name())
print(userC.full_name())