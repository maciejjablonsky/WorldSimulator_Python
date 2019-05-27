from organisms.animals.animal import Animal


class Wolf(Animal):
    def __init__(self, world, strength=9, initiative=5, species="wolf"):
        super(Animal, self).__init__(world, strength, initiative, species)
