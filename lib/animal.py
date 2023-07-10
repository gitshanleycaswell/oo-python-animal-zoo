class Animal:
    all =[]
    def __init__(self, species, weight, nickname, zoo):
        self.species = species
        self.weight = weight
        self.nickname = nickname
        self.zoo = zoo
        Animal.all.append(self)

    @classmethod
    def find_by_species(cls, search_species):
            return [animal for animal in cls.all if animal.species == search_species]
    
    @property
    def weight(self):
        return self._weight
    
    @weight.setter
    def weight(self, new_weight):
        if isinstance(new_weight, int):
            self._weight = new_weight
        else:
            print('Weight must be of type int')
    