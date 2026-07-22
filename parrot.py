class Parrot: 
    species = "bird"
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Parrot("billy", 9)
p2 = Parrot("bob", 13)
print(Parrot.species)
print(p1.name)
print(p1.age)
print(p2.name)
print(p2.age)
