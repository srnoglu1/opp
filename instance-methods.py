class person:
    def __init__(self,name,surname,year):
        self.name = name
        self.surname = surname
        self.year = year

    def intro(self):
        return f"My name is {self.name} and my surname is {self.surname}"

    def calculate_age (self):
        return f"my age {2021-self.year}"


p1 = person("Emirhan","Şirinoğlu",1998)

print(p1.intro())
print(p1.calculate_age())