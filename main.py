class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age



    def display(self):
        print("I am a dog my name is", self.name, "and my age is", self.age)


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age



    def display(self):
        print("I am a cat my name is", self.name, "and my age is", self.age)


dog1 = Dog("Buddy", 3)
cat1 = Cat("herfy", 2)


pets = (dog1, cat1)

for pet in pets:
    pet.display()