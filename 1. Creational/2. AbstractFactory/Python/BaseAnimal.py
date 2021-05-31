class BaseAnimal:
    def __init__(self, nAppendages, type, breed):
        self.Appendages = nAppendages
        self.Type = type
        self.Breed = breed
        
    
    def Describe(self):
        print(f"I'm a {self.Breed} {self.Type} with {self.Appendages} appendages!")

    def Speak(self):
        pass