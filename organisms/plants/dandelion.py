from random import uniform

from organisms.plants.plant import Plant


class Dandelion(Plant):
    seed_attempts_number = 3

    def __init__(self, world, strength=0, species="dandelion"):
        super(Plant, self).__init__(world, strength, Plant.initiative, species)

    def action(self):
        for i in range(0, Dandelion.seed_attempts_number):
            if (uniform(0, 1) <= Plant.seed_probability):
                self.world.create_organism(plant_parent=self)
                break
