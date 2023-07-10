from lib.animal import Animal

class Zoo:
    all = []
    def __init__(self, name="Name", location="Location"):
        self.name = name
        self.location = location
        Zoo.all.append(self)

    def animals(self):
        animals = [animal for animal in Animal.all if animal.zoo == self]
        return animals
    
    def animal_species(self):
        species = set(animal.species for animal in self.animals())
        return list(species)
    
    def find_by_species(self, search_species):
        animals = [animal for animal in self.animals() if animal.species == search_species]
        if animals:
            return animals
        else:
            print('Cannot find species')
    
    def animal_nicknames(self):
        nicknames = [animal.nickname for animal in self.animals()]
        return nicknames
    
    @classmethod
    def find_by_location(cls, search_location):
        return [zoo for zoo in cls.all if zoo.location == search_location]

    @property
    def location(self):
        return self._location 
    
    @location.setter
    def location(self, new_location):
        if isinstance(new_location, str):
            self._location = new_location

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str):
            self._name = new_name
        else:
            raise ValueError("Zoo name must be a string")

