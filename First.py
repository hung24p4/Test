class Vampire:
    num = 1
    def __init__(self, Name, Age, Gender, Power):
        self.name = Name
        self.age = Age
        self.gender = Gender
        self.power = Power
        self.number = Vampire.num
        Vampire.num += 1
        self.gg = 500
    def intro(self):
        line = 'My name is ' + self.name
        return line

A = "A"
B = "B"
C = "C"

Vampire_1 = Vampire(A,A,A,A)
Vampire_2 = Vampire(B,B,B,B)
Vampire_3 = Vampire(C,C,C,C)

print(Vampire_1.number)
print(Vampire_2.number)
print(Vampire_3.number)


