from BaseAnimal import BaseAnimal

class Dog(BaseAnimal):
    def __init__(self, species) -> None:
        super().__init__(4, "dog", species)
    
    def Speak(self):
        print(f"I'm a {self.Breed} dog! Woof woof!")

class Cat(BaseAnimal):
    def __init__(self, species) -> None:
        super().__init__(4, "cat", species)

    def Speak(self):
        print(f"I'm a {self.Breed} cat! Meow meow!")

class Fish(BaseAnimal):
    def __init__(self, species) -> None:
        super().__init__(3, "fish", species)

    def Speak(self):
        print(f"I'm a {self.Breed} fish! *Bubbles*")