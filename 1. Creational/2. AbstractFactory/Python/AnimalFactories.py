from Animals import *

class AnimalFactory:
    def __init__(self, species):
        self.Species = species

    def CreateAnimal(self, type, species):
        pass

class DogFactory(AnimalFactory):
    def __init__(self):
        super().__init__("dog")

    def CreateAnimal(self, breed):
        return Dog(breed)
    

class CatFactory(AnimalFactory):
    def __init__(self):
        super().__init__("cat")

    def CreateAnimal(self, breed):
        return Cat(breed)

class FishFactory(AnimalFactory):
    def __init__(self):
        super().__init__("fish")
        
    def CreateAnimal(self, breed):
        return Fish(breed)