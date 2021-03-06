class User:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
    # always need self

    def full_name(self):
        return f"{self.first} {self.last}"

    def initials(self):
        return f"{self.first[0]}.{self.last[0]}."

    def likes(self, thing):
        return f"{self.first} likes {thing.lower()}."

    def is_senior(self):
        return self.age > 65

    def birthday(self):
        self.age += 1
        end = ""
        if str(self.age)[-1] == "1":
            end = "st"
        elif str(self.age)[-1] == "2":
            end = "nd"
        elif str(self.age)[-1] == "3":
            end = "rd"
        else:
            end = "th"
        return f"Happy {self.age}{end} Birthday, {self.first}!"


user1 = User("Joe", "Smith", 68)
user2 = User("Blanca", "Lopez", 41)
print(user2.full_name())
print(user2.initials())
print(user1.likes("Ice Cream"))
print(user2.likes("Chips"))
print(user2.is_senior())
print(user1.birthday())
print(user1.age)
