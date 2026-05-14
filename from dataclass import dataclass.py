class Profile:
    clan = "Avengers"

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old."

    def show(self):
        print(f"Name: {self.name}, Age: {self.age}")

    def __eq__(self, other):
        return isinstance(other, Profile) and self.name == other.name and self.age == other.age


p1 = Profile("Vishal", 18)
p2 = Profile("Yash", 17)
p3 = Profile("Jami", 19)

print(Profile.clan)

# Output
print(p1)
print(p2)
print(p3)
