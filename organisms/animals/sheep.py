from organisms.animals.animal import Animal


class Sheep(Animal):
    def __init__(self, world, strength=4, initiative=4, species="sheep"):
        super(Animal, self).__init__(world, strength, initiative, species)

