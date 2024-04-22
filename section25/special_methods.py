from copy import copy

class Human:
    def __init__(self, first, last, age) -> None:
        self.first = first
        self.last = last
        self.age = age
    
    def __repr__(self):
        return f"Human named {self.first} {self.last}"
    
    def __len__(self):
        return self.age
    
    def __add__(self, other):
        if isinstance(other, Human):
            return Human(first='Newborn', last=self.last, age=0)
        raise TypeError("You need to add two humans together")

    def __mul__(self, other):
        if isinstance(other, int):
            return [copy(self) for i in range(other)]
        raise TypeError("You need to provide an int!")

h = Human("Jan", "Klen", 45)
h2 = Human("aba", "qwdqw", 23)

print(h)
print(h2)

new_h = h + h2

print(new_h)

print(new_h*2)
