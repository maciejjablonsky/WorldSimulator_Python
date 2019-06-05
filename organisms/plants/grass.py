from organisms.plants.plant import Plant


class Grass(Plant):
    def __init__(self, world, strength=0, species="grass"):
        super(Plant, self).__init__(world, strength, Plant.initiative, species)
