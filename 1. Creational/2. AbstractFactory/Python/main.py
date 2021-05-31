import AnimalFactories

animals = []

factory = AnimalFactories.DogFactory()
animals.append(factory.CreateAnimal("Husky"))
animals.append(factory.CreateAnimal("German Shepherd"))
animals.append(factory.CreateAnimal("Rottweiler"))

factory = AnimalFactories.CatFactory()
animals.append(factory.CreateAnimal("Persian"))
animals.append(factory.CreateAnimal("siamese"))

factory = AnimalFactories.FishFactory()
animals.append(factory.CreateAnimal("goldfish"))
animals.append(factory.CreateAnimal("shark"))


for animal in animals:
    animal.Speak()
    animal.Describe()